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

- 현재 로컬 폴더와 CLI 세션을 연결하는 기능을 개발하고 있습니다.
- 여러 계정 전환과 CLI/API 대화 연결은 설계 단계입니다.

**[Saturn 저장소](https://github.com/woonyong-choi/saturn)** · [현재 사용법](https://github.com/woonyong-choi/saturn/blob/main/docs/guide.md) · [개발 설계](https://github.com/woonyong-choi/saturn/blob/main/docs/saturn-design.md)

## 개인 도구

### Manta

Obsidian에서 코드 실행, 일정, 노트 관계, 다이어그램 작업을 확장하는 플러그인입니다.

<table width="100%">
  <thead>
    <tr>
      <th width="28%">도구</th>
      <th>무엇을 하는가</th>
      <th width="22%">현재 상태</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="https://github.com/woonyong-choi/manta-code-blocks">Manta Code Blocks</a></td>
      <td>노트 안에서 코드를 편집하고 실행 결과를 확인합니다. 브라우저·로컬·원격 실행기는 같은 어댑터 계약으로 연결합니다.</td>
      <td>Community 배포</td>
    </tr>
    <tr>
      <td><a href="https://github.com/woonyong-choi/manta-calendar">Manta Calendar</a></td>
      <td>Markdown의 날짜를 달력으로 모읍니다. Google 동기화는 선택 사항입니다.</td>
      <td>Community 배포</td>
    </tr>
    <tr>
      <td><a href="https://github.com/woonyong-choi/manta-graph">Manta Graph</a></td>
      <td>현재 노트와 직접 링크를 목차와 그래프로 읽기 전용으로 보여줍니다.</td>
      <td>Community 배포</td>
    </tr>
    <tr>
      <td><a href="https://github.com/woonyong-choi/manta-diagrams">Manta Diagrams</a></td>
      <td>Mermaid 원문을 바꾸지 않고 긴 라벨과 복잡한 연결을 전용 뷰어와 SVG로 렌더링합니다.</td>
      <td>출시 후보 검증</td>
    </tr>
  </tbody>
</table>

### 개발 위키

원자료에서 공개 문서까지의 출처를 보존하는 개발 위키입니다.

- 원자료·주장·페이지 명세를 분리하고, 승인 기록과 해시를 검사한 뒤 문서를 조립합니다.
- 검색은 필요한 절만 반환하고, 공개 사이트에는 검토를 마친 문서만 내보냅니다.

[개발 위키 읽기](https://docs.woonyong.com/) · [구현 코드 · woon-core](https://github.com/woonyong-choi/woon-core)

## 프로젝트

### [PintOS](https://github.com/woonyong-choi/lrn-pintos)

교육용 운영체제 PintOS에 스레드 스케줄링, 사용자 프로세스, 가상 메모리를 구현한 팀 학습 프로젝트입니다.

- 과제 이후 MLFQS와 선점·우선순위 기부 문제를 다시 추적해 보완했습니다.
- 제공된 테스트로 단계별 동작을 검증한 범위와 남은 실패를 저장소에 기록했습니다.

### [SQL 엔진](https://github.com/woonyong-choi/lrn-sql)

C로 SQL을 입력받아 페이지에 저장하고 B+Tree 인덱스로 조회하는 학습용 데이터베이스 엔진입니다.

- 팀 과제에서 페이지 저장 구조와 버퍼 풀, B+Tree를 연결하는 구현을 주도했습니다.
- 100만 행 삽입에서 드러난 반복 탐색과 잠금 누적을 gdb로 추적해 수정했습니다. 자세한 선택은 [설계 문서](https://github.com/woonyong-choi/lrn-sql/blob/main/docs/design.md)에 기록했습니다.

### [Kubernetes 장애 진단 · K8s Clue](https://github.com/woonyong-choi/k8s-clue)

Kubernetes 장애 증거를 수집하고 수정안을 Draft PR로 제안하는 5인 팀 프로젝트입니다.

- 팀장으로 진단 파이프라인과 서비스 간 인터페이스를 설계하고, 증거 수집을 읽기 전용으로 제한했습니다.
- 공개 정리본은 ImagePullBackOff 경로의 계약 테스트를 통과했으며, 실제 클러스터·GitHub 연동 E2E는 아직 검증하지 않았습니다.

### [다누리 C# 프레임워크](https://github.com/woonyong-choi/dx_framework)

C++ 엔진 위에서 액터 생명주기, 코루틴, 이벤트를 다루는 C# 실무 프레임워크입니다.

- C# 계층의 API와 실행 흐름을 구현하고 3D 콘텐츠 개발에 사용했습니다.
- 원본 엔진 DLL은 비공개이며, 공개 저장소에서는 코루틴 계층만 실행할 수 있습니다.
