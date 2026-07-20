import glob
import os

def analyze_logs():
    # Find all server*.log files in the current directory
    log_files = sorted(glob.glob("server*.log"))
    
    if not log_files:
        print("No server*.log files found in the current directory.")
        return
        
    print(f"{'Server':<12} | {'CRC Error':<10} | {'Link Down':<10}")
    print("-" * 40)
    
    total_crc = 0
    total_link_down = 0
    
    for file_path in log_files:
        server_name = os.path.splitext(os.path.basename(file_path))[0]
        
        crc_count = 0
        link_down_count = 0
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    lower_line = line.lower()
                    if 'crc error' in lower_line:
                        crc_count += 1
                    if 'link down' in lower_line:
                        link_down_count += 1
                        
            print(f"{server_name:<12} | {crc_count:<10} | {link_down_count:<10}")
            total_crc += crc_count
            total_link_down += link_down_count
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            
    print("-" * 40)
    print(f"{'Total':<12} | {total_crc:<10} | {total_link_down:<10}")

if __name__ == "__main__":
    analyze_logs()
