# 📋 AWS DCO 교육용 장애/인시던트 요약 보고서 (Incident Summary)
**보고서 생성 일시:** `2026-07-20 12:27:26`

## 1. 데이터 수집 요약 (Data Overview)
- **분석 대상 파일:** `sample_dco_log.txt`
- **전체 수집 로그 수:** `140` 줄

## 2. 심각도별 로그 통계 (Severity Statistics)
- **ERROR**: `2`건 (1.4%)
- **INFO**: `135`건 (96.4%)
- **WARNING**: `3`건 (2.1%)

## 3. 이벤트별 통계 (Event Type Statistics)
- `Normal heartbeat`: `125`건
- `Ticket opened`: `3`건
- `Ticket escalated`: `3`건
- `Maintenance completed`: `3`건
- `Fan Alert`: `1`건
- `Temperature warning`: `1`건
- `SSD failure warning`: `1`건
- `CRC error 증가`: `1`건
- `Link Down`: `1`건
- `Link Up`: `1`건

## 4. 경고 및 위험 로그 목록 (WARNING & CRITICAL Logs)
| 일시 (Timestamp) | 장비명 (Device) | 심각도 | 이벤트 | 상세 메시지 |
|---|---|---|---|---|
| 2026-07-03 01:05:00 | DEMO_CORE_SW_02 | ⚠️ WARNING | `Fan Alert` | Fan module 2 RPM dropped to 15% (Below threshold 20%). IP: 198.51.100.2 |
| 2026-07-03 02:05:00 | EDU_SRV_R04_N12 | ⚠️ WARNING | `Temperature warning` | Chassis temperature reached 42C (Threshold: 40C). IP: 192.0.2.12 |
| 2026-07-03 03:05:00 | SAMPLE_TOR_SW_01 | ⚠️ WARNING | `CRC error 증가` | Interface Gi0/1 CRC error counter increased to 154 within 5 minutes. IP: 192.0.2.1 |

## 5. DCO 주요 관심 장애 이벤트 분석 (CRC_ERROR, LINK_DOWN, TICKET_ESCALATED)
> DCO(Data Center Operations) 직무에서는 물리적 케이블 상태(CRC 에러, 링크 다운) 및 서비스 티켓 이관 상태를 가장 민감하게 모니터링합니다.

*주요 장애 이벤트(CRC_ERROR, LINK_DOWN, TICKET_ESCALATED)가 기록되지 않았습니다.*