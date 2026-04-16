import pandas as pd
from .detectors.suspicious_patterns import detect_user_enumeration, detect_directory_traversal

def generate_report(df, log_type, output_file):
    with open(output_file, 'w') as f:
        f.write(f"LOGHUNTER REPORT - {log_type.upper()}\n")
        f.write("="*50 + "\n\n")
        
        if 'source_ip' in df.columns:
            top_ips = df['source_ip'].value_counts().head(10)
            f.write("Top 10 Source IPs by Activity:\n")
            for ip, count in top_ips.items():
                f.write(f"  {ip} : {count} events\n")
            f.write("\n")
        
        if 'timestamp' in df.columns and not df['timestamp'].isnull().all():
            df['hour'] = df['timestamp'].dt.hour
            hour_counts = df['hour'].value_counts().sort_index()
            f.write("Activity by Hour (UTC):\n")
            for hour, count in hour_counts.items():
                f.write(f"  {hour:02d}:00 - {count} events\n")
            f.write("\n")
        
        if log_type == 'apache':
            traversal_ips = detect_directory_traversal(df)
            if traversal_ips:
                f.write("Directory Traversal Attempts from IPs:\n")
                for ip in traversal_ips:
                    f.write(f"  {ip}\n")
        elif log_type in ['ssh', 'windows']:
            enum_ips = detect_user_enumeration(df)
            if enum_ips:
                f.write("Potential User Enumeration from IPs (3+ different usernames):\n")
                for ip in enum_ips:
                    f.write(f"  {ip}\n")
        
        f.write("\n[+] End of report.\n")
