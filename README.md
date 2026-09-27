<div align="center">

<img src="assets/brand/woonyong-caricature.png" width="96" height="96" alt="최우녕의 흑백 캐리커처">

# 최우녕

쓰면서 생긴 불편을 직접 구현해서 해결합니다.

[이력서 · 포트폴리오](https://docs.woonyong.com/resume/) · [개발 위키](https://docs.woonyong.com/)

</div>

C# 프레임워크와 3D 콘텐츠를 개발했고, 이후 PD로 제품 개발을 이끌었습니다. 서버와 인프라까지 직접 이해하고 싶어 크래프톤 정글에서 운영체제와 SQL 엔진을 구현하고 Kubernetes 장애 진단 도구를 설계했습니다.

공부하고 개발하면서 필요한 도구도 직접 만듭니다. 노트에서 코드를 실행하려고 Obsidian 플러그인을 만들었고, 쌓인 기록을 다시 찾고 정리하려고 위키 시스템을 만들었습니다. 지금은 코딩 에이전트와 함께 일할 때 생기는 불편을 Saturn으로 풀고 있습니다.

## 지금 만들고 있는 Saturn

에이전트마다 대화와 터미널이 나뉘고, 작업을 옮길 때마다 맥락을 다시 챙겨야 했습니다. 어떤 일을 맡겼고 어디까지 끝났는지 한곳에서 보고 싶어 macOS 작업 공간을 만들고 있습니다.

현재는 로컬 폴더에서 Codex·Claude CLI를 실행하고, 터미널·Markdown·작업 기록을 나란히 볼 수 있습니다. 응답이 끝났다고 작업까지 끝난 것은 아니어서, 요청에 적은 완료 조건과 검사 결과도 함께 남깁니다.

개인 프로젝트이며 개발 중입니다. 여러 계정 전환과 CLI/API 사이의 대화 연결은 아직 설계 단계입니다.

**[Saturn 저장소](https://github.com/woonyong-choi/saturn)** · [현재 사용법](https://github.com/woonyong-choi/saturn/blob/main/docs/guide.md) · [개발 설계](https://github.com/woonyong-choi/saturn/blob/main/docs/saturn-design.md)

## 직접 쓰려고 만든 도구

### Obsidian 플러그인 · Manta

기록을 읽고 예제를 실행하는 동안 다른 창으로 옮겨 다니는 일을 줄이고 싶었습니다.

| 도구 | 해결하려는 불편 |
| --- | --- |
| [Manta Code Blocks](https://github.com/woonyong-choi/manta-code-blocks) | 노트의 코드를 실행하려고 에디터에 다시 붙여 넣는 일 |
| [Manta Calendar](https://github.com/woonyong-choi/manta-calendar) | 날짜가 적힌 노트를 하나씩 찾아다니는 일 |
| [Manta Graph](https://github.com/woonyong-choi/manta-graph) | 여러 노트에 걸친 링크를 오가며 읽을 순서를 놓치는 일 |
| [Manta Diagrams](https://github.com/woonyong-choi/manta-diagrams) | 노트 속 다이어그램의 긴 글자와 복잡한 연결을 읽기 어려운 점 |

Code Blocks·Calendar·Graph는 Obsidian Community에서 설치할 수 있습니다. Diagrams는 출시 후보 버전을 검증하고 있습니다.

### 개발 위키

대화와 메모가 쌓이면서 이미 정리한 내용을 다시 찾기 어려워졌고, 어떤 자료에서 나온 설명인지도 놓치곤 했습니다. 원자료와 문장의 출처를 연결해 두고, 필요한 부분을 검색할 수 있도록 만들었습니다. 공개 위키에는 직접 검토한 문서만 올립니다.

[개발 위키 읽기](https://docs.woonyong.com/) · [구현 코드 · woon-core](https://github.com/woonyong-choi/woon-core)

## 프로젝트

### [PintOS](https://github.com/woonyong-choi/lrn-pintos)

C로 스케줄링과 가상 메모리를 구현한 정글 팀 과제입니다. 스케줄링·프로세스 생명주기·가상 메모리를 분담했고, 과제 이후에도 MLFQS와 선점·우선순위 기부 문제를 보완했습니다.

### [SQL 엔진](https://github.com/woonyong-choi/lrn-sql)

정글 팀 과제에서 C 기반 엔진 구현을 주도했습니다. B+Tree·페이지 저장 구조·버퍼 풀을 연결했고, 이후 100만 행 삽입에서 드러난 반복 탐색과 잠금 누적을 gdb로 추적해 고쳤습니다. [설계와 선택 이유](https://github.com/woonyong-choi/lrn-sql/blob/main/docs/design.md)를 함께 기록했습니다.

### [Kubernetes 장애 진단 · K8s Clue](https://github.com/woonyong-choi/k8s-clue)

5인 팀의 팀장으로 장애 진단 파이프라인과 서비스 간 인터페이스를 설계했습니다. 증거는 읽기 전용으로 수집하고, 수정안은 사람이 검토할 Draft PR로 제안합니다. 공개 정리본은 ImagePullBackOff 경로의 계약 테스트를 중심으로 검증했으며, 실제 클러스터·GitHub 연동 E2E는 남아 있습니다.

### [다누리 C# 프레임워크](https://github.com/woonyong-choi/dx_framework)

C++ 엔진 위에서 콘텐츠를 개발할 수 있도록 실무에서 직접 만든 C# 계층입니다. 액터 생명주기·코루틴·이벤트 API를 구현했습니다. 엔진 DLL은 비공개이며, 공개 저장소에서는 코루틴 계층을 별도로 실행해 볼 수 있습니다.
