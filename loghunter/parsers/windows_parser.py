import pandas as pd

def parse_windows(csv_path):
    df = pd.read_csv(csv_path)
    if 'IpAddress' not in df.columns:
        return pd.DataFrame(columns=['source_ip', 'timestamp', 'username', 'event_type'])
    df = df.rename(columns={'TimeCreated': 'timestamp', 'IpAddress': 'source_ip', 'TargetUserName': 'username'})
    df['event_type'] = df['EventID'].apply(lambda x: 'FAILED_LOGON' if x == 4625 else 'OTHER')
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    return df[['source_ip', 'timestamp', 'username', 'event_type']]
