<div align="center">

<img src="assets/brand/woonyong-caricature.png" width="96" height="96" alt="최우녕의 흑백 캐리커처">

# 최우녕

필요한 도구를 직접 구현합니다.

[이력서 · 포트폴리오](https://docs.woonyong.com/resume/) · [개발 위키](https://docs.woonyong.com/)

</div>

C# 프레임워크와 3D 콘텐츠를 개발한 뒤, PD로 제품 개발을 이끌었습니다. 시스템의 동작을 더 깊이 이해하기 위해 크래프톤 정글에서 PintOS와 SQL 엔진을 구현하고 Kubernetes 장애 진단 도구를 설계했습니다.

현재는 Saturn과 Obsidian 플러그인, 출처를 보존하는 개발 위키를 만들고 있습니다.

## Saturn

코딩 에이전트의 대화, 터미널, 작업 기록을 한곳에서 다루는 macOS 작업 공간입니다. 로컬 폴더에서 Codex·Claude CLI를 실행하고, 요청의 완료 조건과 검사 결과를 응답 기록과 함께 남깁니다.

개인 프로젝트로 개발 중입니다. 여러 계정 전환과 CLI/API 대화 연결은 설계 단계입니다.

**[Saturn 저장소](https://github.com/woonyong-choi/saturn)** · [현재 사용법](https://github.com/woonyong-choi/saturn/blob/main/docs/guide.md) · [개발 설계](https://github.com/woonyong-choi/saturn/blob/main/docs/saturn-design.md)

## 개인 도구

### Manta

| 도구 | 기능 |
| --- | --- |
| [Manta Code Blocks](https://github.com/woonyong-choi/manta-code-blocks) | 노트 안에서 코드 편집·실행·결과 확인 |
| [Manta Calendar](https://github.com/woonyong-choi/manta-calendar) | 날짜가 적힌 노트를 달력에서 탐색 |
| [Manta Graph](https://github.com/woonyong-choi/manta-graph) | 현재 노트의 연결을 목차와 그래프로 탐색 |
| [Manta Diagrams](https://github.com/woonyong-choi/manta-diagrams) | 긴 라벨과 복잡한 연결을 읽기 쉽게 렌더링 |

Code Blocks·Calendar·Graph는 Obsidian Community에서 설치할 수 있습니다. Diagrams는 출시 후보 버전을 검증하고 있습니다.

### 개발 위키

원자료·주장·페이지 명세를 분리하고, 승인 기록과 해시를 검사한 뒤 문서를 조립합니다. 검색은 필요한 절만 반환하고, 공개 사이트에는 검토를 마친 문서만 내보냅니다.

[개발 위키 읽기](https://docs.woonyong.com/) · [구현 코드 · woon-core](https://github.com/woonyong-choi/woon-core)

## 프로젝트

### [PintOS](https://github.com/woonyong-choi/lrn-pintos)

정글 팀 과제로 스케줄링·프로세스 생명주기·가상 메모리를 구현했습니다. 과제 이후에는 MLFQS와 선점·우선순위 기부 문제를 보완했습니다.

### [SQL 엔진](https://github.com/woonyong-choi/lrn-sql)

정글 팀 과제에서 C 기반 엔진 구현을 주도했습니다. B+Tree·페이지 저장 구조·버퍼 풀을 연결했고, 100만 행 삽입에서 드러난 반복 탐색과 잠금 누적을 gdb로 추적해 고쳤습니다. [설계와 선택 이유](https://github.com/woonyong-choi/lrn-sql/blob/main/docs/design.md)를 기록했습니다.

### [Kubernetes 장애 진단 · K8s Clue](https://github.com/woonyong-choi/k8s-clue)

5인 팀의 팀장으로 장애 진단 파이프라인과 서비스 간 인터페이스를 설계했습니다. 증거 수집은 읽기 전용으로, 수정안은 사람이 검토하는 Draft PR로 제한했습니다. 공개 정리본은 ImagePullBackOff 경로의 계약 테스트를 통과했지만 실제 클러스터·GitHub 연동 E2E는 남아 있습니다.

### [다누리 C# 프레임워크](https://github.com/woonyong-choi/dx_framework)

실무에서 C++ 엔진 위에 액터 생명주기·코루틴·이벤트 API를 제공하는 C# 계층을 구현했습니다. 엔진 DLL은 비공개이며, 공개 저장소에서는 코루틴 계층만 실행할 수 있습니다.
