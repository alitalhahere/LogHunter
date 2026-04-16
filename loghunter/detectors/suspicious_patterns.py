def detect_user_enumeration(df):
    if 'username' not in df.columns or 'source_ip' not in df.columns:
        return []
    grouped = df[df['event_type'].str.contains('FAIL', case=False)].groupby('source_ip')['username'].nunique()
    suspicious = grouped[grouped >= 3].index.tolist()
    return suspicious

def detect_directory_traversal(df):
    if 'request' not in df.columns:
        return []
    traversal = df[df['request'].str.contains(r'\.\./', na=False)]
    return traversal['source_ip'].unique().tolist()
