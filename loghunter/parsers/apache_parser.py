import re
import pandas as pd
from datetime import datetime

def parse_apache(log_path):
    pattern = r'^(\S+) \S+ \S+ \[(.*?)\] "(.*?)" (\d{3}) \S+'
    data = []
    with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            match = re.search(pattern, line)
            if match:
                ip = match.group(1)
                timestamp_str = match.group(2)
                request = match.group(3)
                status = int(match.group(4))
                try:
                    timestamp = datetime.strptime(timestamp_str, '%d/%b/%Y:%H:%M:%S %z')
                except:
                    timestamp = None
                data.append([ip, timestamp, request, status])
    df = pd.DataFrame(data, columns=['source_ip', 'timestamp', 'request', 'status'])
    return df
