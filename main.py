import json
import re
from datetime import datetime
from dateutil import parser
from pytz import timezone

SSH_LOG_LINE_REGEX = re.compile(r'^\[(.*?)\] (\S+) (\S+) (\S+)')
SHANGHAI_TZ = timezone('Asia/Shanghai')


def parse_log_file(_path: str) -> str:
    result: list = []
    with open(_path, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            line = line.strip().encode().decode('utf-8')
            '跳过蜜罐启动行'
            if 'ssh-honeypot' in line or 'started' in line:
                continue
            '跳过无效行'
            if not line.startswith('['):
                continue

            try:
                match = SSH_LOG_LINE_REGEX.search(line)
                if match:
                    timestamp_str, address, username, password = match.groups()
                    timestamp: datetime = parser.parse(timestamp_str)
                    '时区转换'
                    timestamp = SHANGHAI_TZ.localize(timestamp)
                    formatted_timestamp = timestamp.strftime('%Y/%m/%d %H:%M:%S')

                    hassh: str = ''
                    next_line = file.readline().strip()
                    if next_line.startswith('['):
                        hassh_match = re.search(r'HASSH: \S+ (\S+)', next_line)
                        if hassh_match:
                            hassh = hassh_match.group(1)

                    data = {
                        "Time": formatted_timestamp,
                        "Username": username,
                        "Password": password,
                        "Address": address,
                        "HASSH": hassh
                    }
                    result.append(data)
            except Exception as e:
                del e
                continue

    return json.dumps(result, indent=4)

if __name__ == '__main__':
    path: str = '/data/fake-ssh.log'
    print(parse_log_file(path))