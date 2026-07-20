🎫 EDU-TICKET-2026-001
발생 시간 (Timestamp): 2026-07-07 15:20:00 KST (SAMPLE_TIME)

샘플 장비명: SAMPLE_TOR_SW_01

이벤트: CRC Error Count Critical Increase & Subsequent Link Down

심각도 (Severity): High (SAMPLE_CRITICAL)

📝 관찰 내용 (Observation)
인터페이스 에러 감지:

샘플 장비 SAMPLE_TOR_SW_01의 특정 인터페이스에서 CRC(Cyclic Redundancy Check) 에러 수치가 급격히 증가하는 현상이 감지되었습니다.

링크 다운 발생:

CRC 에러 누적 직후, 해당 포트의 연결이 끊어지는 Link Down 이벤트가 연속적으로 관찰되었습니다.

영향도:

교육용 시뮬레이션 환경 내 일부 샘플 트래픽의 경로 우회(Rerouting)가 발생했습니다.

⚠️ Escalation 필요 여부
필요 여부: Yes (SAMPLE_ESCALATION)

이유: 물리적 케이블 불량 또는 샘플 광모듈(SFP) 장애 가능성이 있으므로, 가상의 현장 엔지니어(SAMPLE_FTE) 배정 및 가상 장비 점검 순서에 따른 확인이 필요합니다.

🔒 보안 주의사항 (Security Notice)
중요 (EDU_SECURITY_GUARD):
본 문서는 학습 및 자동화 실습을 위한 샘플 문서입니다. 절대 실제 인프라의 IP 주소, 장비 시리얼 넘버, 실제 계정 정보 및 인증 토큰 등을 이 문서나 GitHub 저장소에 기입하지 마십시오. 모든 데이터는 가상의 접두어(SAMPLE_, EDU_)를 유지해야 합니다.