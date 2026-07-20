import glob
import os

def analyze_logs():
    # 현재 디렉토리에서 server*.log 파일들을 검색
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
        
        # 로그 엔트리 파싱 (여러 줄에 걸친 로그를 하나의 엔트리로 병합)
        entries = []
        current_entry = []
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    stripped = line.strip()
                    if not stripped:
                        continue
                    
                    # 공백이나 탭으로 시작하는 하위 라인은 이전 로그 엔트리에 병합
                    if line.startswith(' ') or line.startswith('\t'):
                        if current_entry:
                            current_entry.append(stripped)
                    else:
                        # 새로운 로그 엔트리 시작
                        if current_entry:
                            entries.append("\n".join(current_entry))
                        current_entry = [stripped]
                
                # 마지막 엔트리 추가
                if current_entry:
                    entries.append("\n".join(current_entry))
            
            # 각 엔트리를 분석하여 ERROR 레벨의 실제 오류만 카운트
            for entry in entries:
                lines = entry.split('\n')
                first_line = lines[0]
                
                # 로그 레벨이 ERROR인 로그 엔트리만 검사
                # (INFO 레벨의 'no CRC error found', 'CRC error recovered' 등의 오탐 방지)
                if ' ERROR ' in first_line:
                    entry_lower = entry.lower()
                    if 'crc error' in entry_lower:
                        crc_count += 1
                    if 'link down' in entry_lower:
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
