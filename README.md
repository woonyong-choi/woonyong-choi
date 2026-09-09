# 최우녕

코드 예제를 노트 안에서 실행하고, 기록을 날짜와 링크로 다시 찾는 도구를 만듭니다. 실행 결과가 불명확할 때의 재시도와 외부 시스템에 변경을 전달하는 경계를 중요하게 다룹니다.

현재는 **Kotlin으로 백엔드 기반을 다지며**, 직접 사용하는 Obsidian 도구를 만들고 유지하고 있습니다.

[공개 기술 문서](https://docs.woonyong.com/) · [코드 실행 도구 체험](https://docs.woonyong.com/obsidian-runnable-code-blocks/) · [이메일](mailto:woonyong.kr@gmail.com)

## 지금 사용해 볼 수 있는 도구

개인 도구 프로젝트입니다. 각 저장소의 설치 안내와 공개 릴리스로 직접 확인할 수 있습니다.

### Runnable Code Blocks — 읽는 자리에서 코드를 실행하기

코드를 읽을 때마다 별도 실행 환경으로 옮겨야 하는 불편을 줄이는 도구입니다. Markdown 원문과 실행 중의 임시 편집을 분리하고, 코드가 **어디에서 실행되는지**와 출력·오류를 함께 보여 줍니다. 결과가 불명확한 실행은 다른 환경에서 자동으로 반복하지 않습니다. 같은 실행 UI를 Obsidian과 정적 웹사이트에서 사용하며, 브라우저 데모는 설치 없이 열어 볼 수 있습니다.

[브라우저 데모](https://docs.woonyong.com/obsidian-runnable-code-blocks/) · [설치 안내](https://github.com/woonyong-kr/obsidian-runnable-code-blocks#installation-and-compatibility) · [최신 릴리스 다운로드](https://github.com/woonyong-kr/obsidian-runnable-code-blocks/releases/latest) · [소스](https://github.com/woonyong-kr/obsidian-runnable-code-blocks)

현재 GitHub 릴리스로 수동 설치합니다. 언어별 실행 환경과 선택적 로컬 companion은 설치 안내에서 확인할 수 있습니다.

### Link Calendar Navigator — 날짜에서 노트와 일정으로

날짜별 기록을 달력에서 찾아 노트로 이어 주는 도구입니다. 로컬 노트 탐색과 외부 일정 동기화를 분리하고, Google Calendar 연동은 **선택한 전용 캘린더의 수동 양방향 동기화**로 범위를 제한했습니다. 충돌은 확인할 수 있게 남기며, Google 연동 없이도 로컬 노트를 탐색할 수 있습니다.

[소개·미리보기](https://community.obsidian.md/plugins/link-calendar) · [설치 안내](https://github.com/woonyong-kr/obsidian-link-calendar-navigator#installation-and-compatibility) · [최신 릴리스 다운로드](https://github.com/woonyong-kr/obsidian-link-calendar-navigator/releases/latest) · [소스](https://github.com/woonyong-kr/obsidian-link-calendar-navigator)

### Linked Graph Navigator — 전체 그래프보다 지금 읽는 문서의 맥락

링크가 많아질수록 전체 그래프만으로 다음에 읽을 문서를 고르기 어려워집니다. 이 도구는 현재 노트의 **직접 연결된 링크와 작성 순서**를 기준으로 Outline과 1-hop 그래프를 구성합니다. 노트에 없는 관계를 추측해 추가하지 않고, 실제로 해석된 링크를 따라 탐색하도록 범위를 좁혔습니다.

[소개·미리보기](https://community.obsidian.md/plugins/linked-graph) · [설치 안내](https://github.com/woonyong-kr/obsidian-linked-graph-navigator#installation-and-compatibility) · [최신 릴리스 다운로드](https://github.com/woonyong-kr/obsidian-linked-graph-navigator/releases/latest) · [소스](https://github.com/woonyong-kr/obsidian-linked-graph-navigator)

## 팀 프로젝트에서 다룬 문제

### Clue — 장애 증거에서 안전한 변경 제안까지

Kubernetes 장애의 관측, 원인 판정, 변경 제안, 사후 검증이 서로 끊어지는 문제를 다룬 **크래프톤 정글 5인 팀 프로젝트**입니다. 팀장으로 전체 아키텍처, 장애 처리 파이프라인과 서비스 간 인터페이스 설계를 맡았습니다.

핵심 판단은 자동화에 클러스터 수정 권한을 직접 주지 않는 것이었습니다. 같은 사건의 증거를 연결하고, 규칙과 허용된 변경 범위로 제안을 제한한 뒤 **사람이 검토하는 GitHub Draft PR**로 넘깁니다.

프로젝트 후 개인 작업으로 ImagePullBackOff 한 경로에 집중해 안전 계약과 로컬 재현 경로를 정리했습니다. Python Reference에서 대표 흐름의 코드와 로컬 데모를 확인할 수 있습니다. 후속 Clue 저장소는 새 구현을 위한 설계 단계입니다.

[Python Reference·재현 방법](https://github.com/woonyong-kr/k8s-clue-python-reference) · [안전 계약과 대표 흐름](https://github.com/woonyong-kr/k8s-clue-python-reference/blob/main/docs/GOLDEN-PATH.md) · [후속 Clue 설계](https://github.com/woonyong-kr/clue)

## 기반을 다지는 학습

정글 팀 학습 프로젝트의 코드를 개인 미러로 보존하고, 코드를 따라 설명하며 보완하는 학습 저장소입니다.

- [lrn-pintos](https://github.com/woonyong-kr/lrn-pintos): 교육용 OS에서 스케줄링·프로세스·가상메모리의 흐름을 다룹니다. COW fork와 익명 페이지 swap을 함께 읽으며 자원의 공유·회수 경계를 살펴봅니다.
- [lrn-sql](https://github.com/woonyong-kr/lrn-sql): C로 SQL 파싱부터 실행, B+ Tree와 디스크 저장까지 연결한 단일 테이블·ID 인덱스 중심의 학습용 DB입니다.

개발 개념과 예제는 [WN Docs](https://docs.woonyong.com/)에서 이어 읽을 수 있습니다.
