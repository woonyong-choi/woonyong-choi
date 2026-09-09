# 최우녕

설명 가능한 상태 변화와 안전한 자동화에 관심이 있는 개발자입니다. 현재는 **Kotlin으로 백엔드 기반을 다지며**, 직접 사용하는 Obsidian 도구를 만들고 유지하고 있습니다.

실행 환경이 바뀌어도 같은 입력을 어떻게 다룰지, 실패했을 때 무엇을 남길지, 자동화가 어디에서 멈춰야 할지를 중요하게 봅니다. 아래에서 사용 가능한 도구와 팀 학습 프로젝트를 구분해 소개합니다.

[공개 기술 문서](https://docs.woonyong.com/) · [코드 실행 도구 체험](https://docs.woonyong.com/obsidian-runnable-code-blocks/) · [이메일](mailto:woonyong.kr@gmail.com)

## 지금 사용해 볼 수 있는 도구

개인 도구 프로젝트입니다. 각 저장소의 설치 안내와 공개 릴리스로 직접 확인할 수 있습니다.

### Runnable Code Blocks — 읽는 자리에서 코드를 실행하기

코드 예제를 읽을 때마다 별도 실행 환경으로 옮겨야 하는 불편을 줄이는 Obsidian 플러그인입니다. Markdown 원문과 실행 중의 임시 편집을 분리하고, 코드가 **어디에서 실행되는지**와 출력·오류를 함께 보여 줍니다. 결과가 불명확한 실행을 다른 환경에서 자동으로 반복하지 않도록 실행 전 실패와 실행 후 실패도 구분합니다.

노트 안에서 예제를 편집·실행할 수 있고, 같은 실행 UI를 정적 웹사이트에서도 사용합니다. 브라우저 데모는 설치 없이 열어 볼 수 있습니다. 언어에 따라 외부 실행 제공자나 별도 로컬 companion이 필요하므로 지원 범위는 설치 안내에서 확인해 주세요.

[브라우저 데모](https://docs.woonyong.com/obsidian-runnable-code-blocks/) · [설치 안내](https://github.com/woonyong-kr/obsidian-runnable-code-blocks#installation-and-compatibility) · [최신 릴리스 다운로드](https://github.com/woonyong-kr/obsidian-runnable-code-blocks/releases/latest) · [소스](https://github.com/woonyong-kr/obsidian-runnable-code-blocks)

### Link Calendar Navigator — 날짜에서 노트와 일정으로

날짜별 기록을 달력에서 찾아 노트로 이어 주는 Obsidian 플러그인입니다. 로컬 노트 탐색과 외부 일정 동기화를 분리하고, Google Calendar 연동은 **선택한 전용 캘린더와 사용자가 실행한 동기화**로 범위를 제한했습니다. 충돌은 조용히 덮어쓰지 않고 확인할 수 있게 남깁니다.

날짜 기반 노트 탐색과 선택적 수동 양방향 동기화를 제공합니다. Google 연동 없이도 로컬 노트 탐색을 사용할 수 있습니다.

[소개·미리보기](https://community.obsidian.md/plugins/link-calendar) · [설치 안내](https://github.com/woonyong-kr/obsidian-link-calendar-navigator#installation-and-compatibility) · [최신 릴리스 다운로드](https://github.com/woonyong-kr/obsidian-link-calendar-navigator/releases/latest) · [소스](https://github.com/woonyong-kr/obsidian-link-calendar-navigator)

### Linked Graph Navigator — 전체 그래프보다 지금 읽는 문서의 맥락

링크가 많아질수록 전체 그래프만으로 다음에 읽을 문서를 고르기 어려워집니다. 이 도구는 현재 노트의 **직접 연결된 링크와 작성 순서**를 기준으로 Outline과 1-hop 그래프를 구성합니다. 노트에 없는 관계를 추측해 추가하지 않고, 실제로 해석된 링크를 따라 탐색하도록 범위를 좁혔습니다.

문서 중심으로 읽기 순서와 인접한 노트를 확인할 수 있는 Obsidian 탐색 도구입니다.

[소개·미리보기](https://community.obsidian.md/plugins/linked-graph) · [설치 안내](https://github.com/woonyong-kr/obsidian-linked-graph-navigator#installation-and-compatibility) · [최신 릴리스 다운로드](https://github.com/woonyong-kr/obsidian-linked-graph-navigator/releases/latest) · [소스](https://github.com/woonyong-kr/obsidian-linked-graph-navigator)

설치는 각 GitHub 릴리스의 안내를 기준으로 합니다. Community 소개 페이지가 있다는 사실을 Obsidian 공식 목록 등록 완료와 같은 뜻으로 쓰지 않습니다.

## 팀 프로젝트에서 다룬 문제

### Clue — 장애 증거에서 안전한 변경 제안까지

Kubernetes 장애의 관측, 원인 판정, 변경 제안, 사후 검증이 서로 끊어지는 문제를 다룬 **크래프톤 정글 5인 팀 프로젝트**입니다. 팀장으로 전체 아키텍처, 장애 처리 파이프라인과 서비스 간 인터페이스 설계를 맡았습니다. 팀의 전체 코드를 혼자 구현한 것으로 설명하지 않습니다.

핵심 판단은 자동화에 클러스터 수정 권한을 직접 주지 않는 것이었습니다. 같은 사건의 증거를 연결하고, 규칙과 허용된 변경 범위로 제안을 제한한 뒤 **사람이 검토하는 GitHub Draft PR**로 넘깁니다.

프로젝트 종료 후 개인 작업에서는 대표 흐름을 ImagePullBackOff 한 경로로 좁히고 안전 계약을 다시 점검했습니다. Python Reference에는 해당 흐름의 코드·로컬 재현 방법·검증 범위가 공개돼 있습니다. 실사용 트래픽이나 외부 클러스터 E2E를 검증한 운영 서비스는 아니며, 후속 Clue 저장소는 새 구현을 위한 설계 단계입니다.

[Python Reference·재현 방법](https://github.com/woonyong-kr/k8s-clue-python-reference) · [안전 계약과 대표 흐름](https://github.com/woonyong-kr/k8s-clue-python-reference/blob/main/docs/GOLDEN-PATH.md) · [후속 Clue 설계](https://github.com/woonyong-kr/clue)

## 기반을 다지는 학습

다음 두 저장소는 정글 팀 학습 프로젝트의 개인 보존 미러입니다. 제품 운영 경험이나 모든 기능의 단독 구현으로 내세우지 않고, 코드를 따라 설명하고 보완하는 기반으로 삼고 있습니다.

- [lrn-pintos](https://github.com/woonyong-kr/lrn-pintos): 교육용 OS에서 스케줄링·프로세스·가상메모리의 흐름을 다룹니다. COW fork와 익명 페이지 swap을 함께 읽으며 자원의 공유·회수 경계를 살펴봅니다.
- [lrn-sql](https://github.com/woonyong-kr/lrn-sql): C로 SQL 파싱부터 실행, B+ Tree와 디스크 저장까지 연결한 학습 DB입니다. 단일 테이블·ID 인덱스 중심이며, WAL·crash recovery나 일반적인 트랜잭션 격리를 갖춘 DBMS는 아닙니다.

[WN Docs](https://docs.woonyong.com/)에는 개발 개념과 예제를 정리하고 있습니다. 작성 중인 항목을 포함하며, 공개 문서가 있다는 사실을 해당 기술의 실무 숙련 증거로 대신하지 않습니다.
