<div align="center">

<img src="assets/brand/woonyong-caricature.png" width="96" height="96" alt="최우녕의 흑백 캐리커처">

# 최우녕

**Backend Engineer · 개발 도구와 지식 시스템**

데이터의 저장 구조부터 작업의 검증 과정까지, 직접 만들고 원인을 추적합니다.

[이력서 · 포트폴리오](https://docs.woonyong.com/resume/) · [기술 기록](https://docs.woonyong.com/)

</div>

C# 콘텐츠 프레임워크를 개발하고, PD로 제품의 요구사항과 출시를 조율했습니다. 이후 서버와 인프라의 동작 원리를 직접 이해하기 위해 크래프톤 정글에서 SQL 엔진과 운영체제를 구현하고 Kubernetes 장애 진단 도구를 설계했습니다.

지금은 직접 사용하는 지식 시스템과 개발 도구를 만들고 있습니다. **문제가 생긴 실행 경로를 좁혀 원인을 찾고, 자동화의 권한과 완료 조건을 코드로 명확히 하는 일**에 관심이 있습니다.

## 대표 프로젝트

### [SQL 엔진](https://github.com/woonyong-choi/lrn-sql) — 저장 구조와 성능 병목

`C11` · 정글 팀 과제에서 엔진 구현 주도, 종료 후 개인 확장

Slotted Page·B+Tree·Buffer Pool을 연결한 디스크 기반 SQL 엔진입니다. 100만 행 삽입에서 드러난 힙 체인 재탐색과 잠금 누적을 gdb로 추적해 수정했습니다. 단일 성능 배수보다 데이터 규모에 따른 실행 시간의 변화를 재현해 비교합니다.

[설계와 선택한 자료구조](https://github.com/woonyong-choi/lrn-sql/blob/main/docs/design.md) · [규모별 측정과 재현 명령](https://github.com/woonyong-choi/lrn-sql#증거는-배수가-아니라-기울기로-남깁니다)

### [K8s Clue](https://github.com/woonyong-choi/k8s-clue) — 장애 진단과 변경 제안

`Python` `Kubernetes` `PostgreSQL` · 5인 팀장, 아키텍처·파이프라인·인터페이스 설계

장애 증거 수집 → 규칙 기반 원인 판정 → 제한된 변경 제안 → 복구 확인을 연결했습니다. 수집은 읽기 전용으로, 변경은 사람이 승인할 Draft PR로 제한했습니다. 팀 과제 종료 후에는 ImagePullBackOff 경로와 base SHA·허용 필드·Draft PR 조건을 계약 테스트로 정리했습니다.

[설계와 자동화의 경계](https://github.com/woonyong-choi/k8s-clue/blob/main/docs/design.md) · [팀 기여와 개인 확장](https://github.com/woonyong-choi/k8s-clue#담당)

현재 공개 참조 구현의 대표 검증은 계약 테스트이며, 실제 클러스터·GitHub 연동 E2E는 후속 과제입니다.

### [Saturn](https://github.com/woonyong-choi/saturn) — 코딩 에이전트를 위한 작업 공간

`Electron` `JavaScript` `Kotlin/JS` · 개인 프로젝트 · 개발 중

Codex·Claude CLI 실행, 터미널, Markdown 맥락과 작업 기록을 한곳에서 다루는 macOS 앱입니다. 에이전트의 응답 종료와 작업 완료를 구분하고, 요청별 수락 기준과 검사 결과를 함께 확인하도록 만들고 있습니다.

로컬 폴더·분할 패널·CLI 실행·실제 계정 사용량 조회를 구현했습니다. 여러 계정 전환, CLI/API 공통 대화와 그래프 편집은 설계 단계입니다.

[현재 사용법](https://github.com/woonyong-choi/saturn/blob/main/docs/guide.md) · [설계와 수락 기준](https://github.com/woonyong-choi/saturn/blob/main/docs/saturn-design.md)

### [LLM Wiki · woon-core](https://github.com/woonyong-choi/woon-core) — 출처를 보존하는 지식 시스템

`Python` `SQLite FTS5` `MCP` · 개인 프로젝트

대화와 문서가 쌓일수록 출처를 잃고 같은 내용을 다시 정리하는 문제를 다룹니다. 원자료·주장·페이지 명세를 분리하고, 승인 기록과 해시를 검사한 뒤 프로그램이 문서를 조립합니다. 검색은 필요한 절만 반환하고, 공개 사이트에는 승인된 문서만 내보냅니다.

[컴파일·검색·공개 구조](https://github.com/woonyong-choi/woon-core/blob/main/docs/architecture.md) · [공개 기술 위키](https://docs.woonyong.com/)

## 직접 사용하는 Obsidian 도구 · Manta

노트 안에서 코드를 실행하고, 날짜와 링크를 따라 기록을 다시 찾는 플러그인입니다.

| 프로젝트 | 하는 일 | 사용해 보기 |
| --- | --- | --- |
| [Manta Code Blocks](https://github.com/woonyong-choi/manta-code-blocks) | 노트 안에서 코드 편집·실행·결과 확인 | [설치](https://community.obsidian.md/plugins/runnable-code-blocks) |
| [Manta Calendar](https://github.com/woonyong-choi/manta-calendar) | 노트의 날짜를 달력으로 모아 원문 열기 | [설치](https://community.obsidian.md/plugins/link-calendar) |
| [Manta Graph](https://github.com/woonyong-choi/manta-graph) | 현재 노트의 링크를 목차·그래프로 탐색 | [설치](https://community.obsidian.md/plugins/linked-graph) |

## 실무 경험과 시스템 기초

- **[Danuri C# Framework](https://github.com/woonyong-choi/dx_framework)** — C++ 엔진 위의 콘텐츠용 C# 계층을 직접 구현했습니다. 액터 생명주기·코루틴·이벤트 API를 제공하며, 공개 저장소에서 엔진 DLL 없이 코루틴 계약을 실행할 수 있습니다.
- **[PintOS](https://github.com/woonyong-choi/lrn-pintos)** — 정글 팀 과제에서 스케줄링·프로세스 생명주기·가상 메모리를 분담했습니다. 종료 후 MLFQS와 선점·우선순위 기부 문제를 보완하고, QEMU에서 회귀 테스트를 실행하는 CI를 정리했습니다.

각 저장소에서 구현 범위, 설계 이유, 재현 방법과 남은 한계를 확인할 수 있습니다.
