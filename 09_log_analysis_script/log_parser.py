# -*- coding: utf-8 -*-
"""
AWS DCO 인턴십 직무 이해를 위한 교육용 로그 분석 파이썬 스크립트
작성 목적: 초보자/비전공자 학생도 한 줄씩 이해할 수 있도록 설계된 파이썬 분석 도구입니다.
외부 라이브러리(패키지) 없이 파이썬 내장 기능(표준 라이브러리)만 사용합니다.
"""

import os
from datetime import datetime

# 1. 설정값 정의
# 입력으로 사용할 교육용 샘플 로그 파일 경로와 출력할 결과 보고서 경로를 지정합니다.
LOG_FILE_PATH = "sample_dco_log.txt"
OUTPUT_FILE_PATH = "incident_summary.md"


def analyze_dco_logs():
    print("=" * 60)
    print("▶ DCO 교육용 로그 분석을 시작합니다...")
    print("=" * 60)

    # 파일이 존재하는지 검사합니다 (에러 방지용 안전 장치)
    if not os.path.exists(LOG_FILE_PATH):
        print(f"❌ 에러: {LOG_FILE_PATH} 파일이 존재하지 않습니다!")
        print("먼저 로그 파일을 작성한 후 분석을 실행해 주세요.")
        return

    # 2. 분석에 필요한 변수(데이터를 담을 그릇)들을 초기화합니다.
    total_lines = 0               # 1) 전체 로그 줄 수를 셀 카운터
    severity_counts = {}          # 2) 심각도별 개수를 담을 딕셔너리 (예: {'INFO': 5, 'WARNING': 3})
    event_counts = {}             # 3) 이벤트별 개수를 담을 딕셔너리 (예: {'LINK_DOWN': 2, 'CRC_ERROR': 2})
    
    warning_critical_logs = []    # 4) WARNING 이나 CRITICAL 상태의 로그들을 따로 모아둘 리스트
    major_event_summary = []      # 5) 주요 이벤트(CRC_ERROR, LINK_DOWN, TICKET_ESCALATED) 로그만 모아둘 리스트

    # 3. 로그 파일을 열고 한 줄씩 읽어 분석을 진행합니다.
    # 'with open'을 사용하면 파일을 다 읽은 후 자동으로 닫아줍니다 (메모리 관리 안전 장치)
    with open(LOG_FILE_PATH, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()  # 줄 끝의 개행문자(\n)나 공백을 제거합니다.
            
            # 빈 줄이나 공백만 있는 줄은 무시하고 넘어갑니다.
            if not line:
                continue

            total_lines += 1  # 로그 줄 수 1 증가

            # 로그 형식 분해: YYYY-MM-DD HH:MM:SS | DEVICE | SEVERITY | EVENT | MESSAGE
            # ' | ' 문자를 기준으로 각 열의 데이터를 쪼갭니다.
            parts = [part.strip() for part in line.split("|")]
            
            # 로그 형식이 올바르게 5개 항목으로 구분되었는지 확인합니다.
            if len(parts) < 5:
                # 형식이 맞지 않는 라인은 에러를 내지 않고 기록해 둡니다.
                print(f"⚠️ 경고: 형식이 맞지 않는 줄을 건너뜁니다: {line}")
                continue

            # 쪼갠 데이터에 알맞은 이름을 붙여줍니다.
            timestamp_str = parts[0]
            device = parts[1]
            severity = parts[2]
            event = parts[3]
            message = parts[4]

            # ----------------------------------------------------------------
            # [분석 1] 심각도별 개수 카운팅
            # severity_counts 딕셔너리에 해당 심각도가 없으면 0으로 시작해서 1을 더합니다.
            if severity not in severity_counts:
                severity_counts[severity] = 0
            severity_counts[severity] += 1

            # ----------------------------------------------------------------
            # [분석 2] 이벤트 종류별 개수 카운팅
            if event not in event_counts:
                event_counts[event] = 0
            event_counts[event] += 1

            # ----------------------------------------------------------------
            # [분석 3] WARNING 또는 CRITICAL 로그 필터링 (리스트에 저장)
            if severity in ["WARNING", "CRITICAL"]:
                warning_critical_logs.append({
                    "timestamp": timestamp_str,
                    "device": device,
                    "severity": severity,
                    "event": event,
                    "message": message
                })

            # ----------------------------------------------------------------
            # [분석 4] 주요 이벤트 필터링 (CRC_ERROR, LINK_DOWN, TICKET_ESCALATED)
            if event in ["CRC_ERROR", "LINK_DOWN", "TICKET_ESCALATED"]:
                major_event_summary.append({
                    "timestamp": timestamp_str,
                    "device": device,
                    "severity": severity,
                    "event": event,
                    "message": message
                })

    # 4. 분석 결과 출력용 텍스트를 마크다운(Markdown) 형식으로 작성합니다.
    # 이 내용은 incident_summary.md 파일에 기록되고 콘솔에도 보기 좋게 출력됩니다.
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    markdown_content = []
    markdown_content.append("# 📋 AWS DCO 교육용 장애/인시던트 요약 보고서 (Incident Summary)")
    markdown_content.append(f"**보고서 생성 일시:** `{current_time}`\n")
    
    markdown_content.append("## 1. 데이터 수집 요약 (Data Overview)")
    markdown_content.append(f"- **분석 대상 파일:** `{LOG_FILE_PATH}`")
    markdown_content.append(f"- **전체 수집 로그 수:** `{total_lines}` 줄\n")
    
    markdown_content.append("## 2. 심각도별 로그 통계 (Severity Statistics)")
    for sev, count in sorted(severity_counts.items()):
        percentage = (count / total_lines) * 100 if total_lines > 0 else 0
        markdown_content.append(f"- **{sev}**: `{count}`건 ({percentage:.1f}%)")
    markdown_content.append("")
    
    markdown_content.append("## 3. 이벤트별 통계 (Event Type Statistics)")
    for ev, count in sorted(event_counts.items(), key=lambda x: x[1], reverse=True):
        markdown_content.append(f"- `{ev}`: `{count}`건")
    markdown_content.append("")
    
    markdown_content.append("## 4. 경고 및 위험 로그 목록 (WARNING & CRITICAL Logs)")
    if warning_critical_logs:
        markdown_content.append("| 일시 (Timestamp) | 장비명 (Device) | 심각도 | 이벤트 | 상세 메시지 |")
        markdown_content.append("|---|---|---|---|---|")
        for log in warning_critical_logs:
            # CRITICAL인 경우 강조 표시
            sev_display = f"🚨 **{log['severity']}**" if log['severity'] == 'CRITICAL' else f"⚠️ {log['severity']}"
            markdown_content.append(f"| {log['timestamp']} | {log['device']} | {sev_display} | `{log['event']}` | {log['message']} |")
    else:
        markdown_content.append("*해당하는 WARNING 또는 CRITICAL 등급의 로그가 없습니다.*")
    markdown_content.append("")
    
    markdown_content.append("## 5. DCO 주요 관심 장애 이벤트 분석 (CRC_ERROR, LINK_DOWN, TICKET_ESCALATED)")
    markdown_content.append("> DCO(Data Center Operations) 직무에서는 물리적 케이블 상태(CRC 에러, 링크 다운) 및 서비스 티켓 이관 상태를 가장 민감하게 모니터링합니다.")
    markdown_content.append("")
    
    if major_event_summary:
        for idx, log in enumerate(major_event_summary, 1):
            markdown_content.append(f"### [이슈 #{idx}] {log['event']} 감지 (장비: {log['device']})")
            markdown_content.append(f"- **발생 시각:** {log['timestamp']}")
            markdown_content.append(f"- **심각도:** `{log['severity']}`")
            markdown_content.append(f"- **장애 내역:** {log['message']}")
            
            # 이벤트별 조치 가이드라인 (학습용)
            guideline = ""
            if log['event'] == "LINK_DOWN":
                guideline = "💡 **[학습 가이드]** 물리적 광케이블 분리, 트랜시버 고장 혹은 상위 포트 셧다운 가능성이 큽니다. 광 파이버 청소 및 포트 플래핑 여부를 우선 점검해야 합니다."
            elif log['event'] == "CRC_ERROR":
                guideline = "💡 **[학습 가이드]** 이더넷 전송 중 패킷 오염이 발생하고 있습니다. 커넥터 접촉 불량이나 감쇠(Attenuation) 현상일 수 있어 패치 케이블 교체나 포트 교체가 필요합니다."
            elif log['event'] == "TICKET_ESCALATED":
                guideline = "💡 **[학습 가이드]** 상위 인프라 장애나 전력 문제 등으로 장애 티켓이 DCO 엔지니어에게 배정되었습니다. 교대 근무 조와 상황실(NOC) 간의 즉각적인 소통이 요구됩니다."
            
            markdown_content.append(f"{guideline}\n")
    else:
        markdown_content.append("*주요 장애 이벤트(CRC_ERROR, LINK_DOWN, TICKET_ESCALATED)가 기록되지 않았습니다.*")
        
    # 5. 결과를 Markdown 파일로 기록합니다.
    full_markdown_text = "\n".join(markdown_content)
    
    with open(OUTPUT_FILE_PATH, "w", encoding="utf-8") as out_file:
        out_file.write(full_markdown_text)
        
    print(f"✅ 분석 완료! 결과가 {OUTPUT_FILE_PATH} 파일로 성공적으로 저장되었습니다.")
    print("=" * 60)
    print(full_markdown_text[:400] + "\n...(이하 생략 - 파일 확인 요망)...\n")
    print("=" * 60)


if __name__ == "__main__":
    analyze_dco_logs()
