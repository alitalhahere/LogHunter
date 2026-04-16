import re
import pandas as pd
from datetime import datetime

def parse_ssh(log_path):
    fail_pattern = r'Failed password for (invalid user )?(\S+) from (\S+) port'
    accept_pattern = r'Accepted password for (\S+) from (\S+) port'
    
    data = []
    with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            ts_match = re.search(r'(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})', line)
            if not ts_match:
                continue
            timestamp_str = ts_match.group(1)
            try:
                timestamp = datetime.strptime(timestamp_str + f" {datetime.now().year}", '%b %d %H:%M:%S %Y')
            except:
                timestamp = None
            
            fail = re.search(fail_pattern, line)
            if fail:
                username = fail.group(2)
                ip = fail.group(3)
                data.append([ip, timestamp, username, 'FAILED'])
                continue
            
            accept = re.search(accept_pattern, line)
            if accept:
                username = accept.group(1)
                ip = accept.group(2)
                data.append([ip, timestamp, username, 'ACCEPTED'])
    
    df = pd.DataFrame(data, columns=['source_ip', 'timestamp', 'username', 'event_type'])
    return df
