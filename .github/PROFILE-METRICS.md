# 프로필 콘텐츠 관리

## 정본과 자동화

`README.md`가 면접관에게 보여 줄 소개와 프로젝트 선택의 정본이다. 문구·대표 프로젝트·링크는 근거를 검토한 뒤 직접 고친다. GitHub bio, 기여 수, 테스트 파일 수, 자동 점수로 소개를 생성하지 않는다.

이름을 유지한 `scripts/update_profile.py --check`는 읽기 전용 검증기다. 외부 API를 호출하거나 README·활동 원장·SVG를 쓰지 않는다. `metrics.yml`도 변경 시 구조를 검사하는 read-only workflow로 전환했다. 정기 갱신·자동 commit·push는 없다.

```bash
python3 -B scripts/update_profile.py --check
python3 -B -m unittest discover -s scripts -p 'test_*.py'
```

이 검사는 문서 구조·링크 문법·폐기된 경로의 재등장을 확인할 뿐, 실무 숙련도나 현재 서비스 가용성을 증명하지 않는다. 링크 변경은 실제 공개 페이지·릴리스 파일·브라우저 동작을 따로 확인한다.

기존 `.github/activity-history.json`, `assets/generated/`, `github-metrics.svg`는 이번 변경에서 삭제하지 않는다. 현재 README와 workflow는 이를 사용하거나 자동 갱신하지 않는다. 과거 `#/blog` 경로를 WN Docs로 바꾸려던 변경의 의도는 `https://docs.woonyong.com/` 링크로 유지한다.

## 공개 문장 근거

2026-09-10 검토 기준이다. 공개 범위는 이 프로필과 아래 공개 저장소·서비스 링크에 한정하며, 다른 이력서·Wiki의 공개 권한을 바꾸지 않는다.

| Claim ID | 공개하는 최소 사실 | 소유권·검증 범위 | 공개 근거 |
|---|---|---|---|
| profile-runnable | 원문과 임시 편집을 분리하고 실행 위치·결과를 노출하는 코드 실행 도구 | 개인 도구 유지보수; 공개 코드·릴리스, 개인 Obsidian 실행 확인 결과를 대조. 외부 제공자의 상시 가용성은 주장하지 않음 | [코드·설계](https://github.com/woonyong-kr/obsidian-runnable-code-blocks), [0.7.3](https://github.com/woonyong-kr/obsidian-runnable-code-blocks/releases/tag/0.7.3) |
| profile-calendar | 날짜 기반 탐색과 선택한 전용 Calendar의 수동 동기화 | 개인 도구 유지보수; 공개 기능·릴리스 및 담당자의 계정 검증 범위. 계정 정보는 공개하지 않음 | [공개 기능](https://github.com/woonyong-kr/obsidian-link-calendar-navigator), [3.6.2](https://github.com/woonyong-kr/obsidian-link-calendar-navigator/releases/tag/3.6.2) |
| profile-graph | 현재 노트의 실제 outgoing 링크·작성 순서로 Outline/1-hop 탐색 | 개인 도구 유지보수; 공개 코드·릴리스 범위 | [공개 기능](https://github.com/woonyong-kr/obsidian-linked-graph-navigator), [1.6.10](https://github.com/woonyong-kr/obsidian-linked-graph-navigator/releases/tag/1.6.10) |
| profile-clue-role | 5인 팀의 아키텍처·파이프라인·인터페이스 설계와 종료 후 대표 경로·안전 계약 정리 | 팀 결과 / 개인 설계 / 종료 후 개인 정리를 분리. 전체 코드의 단독 작성이나 운영 성과로 표현하지 않음 | [Reference 역할·한계](https://github.com/woonyong-kr/k8s-clue-python-reference/tree/778e1e864a91179776d258f40083d24b358a7503), [Golden Path](https://github.com/woonyong-kr/k8s-clue-python-reference/blob/778e1e864a91179776d258f40083d24b358a7503/docs/GOLDEN-PATH.md) |
| profile-clue-next | 후속 Clue는 새 구현을 위한 설계 저장소 | 현재 공개 README 확인; 배포 완료가 아님 | [Clue](https://github.com/woonyong-kr/clue) |
| profile-learning | OS·DB 팀 학습 코드의 개인 보존 미러 | 팀 학습; 직접 기여는 개별 author/diff로 확인. Kotlin 학습 사실만 소개하고 비공개 저장소 링크는 제외 | [lrn-pintos](https://github.com/woonyong-kr/lrn-pintos), [lrn-sql](https://github.com/woonyong-kr/lrn-sql) |
| profile-docs | 개발 개념과 예제를 정리하는 공개 문서 | 공개 첫 화면·탐색 확인; 작성 중 항목 포함, 완독·실무 숙련 주장 아님 | [WN Docs](https://docs.woonyong.com/) |

위 항목은 기존 공개 코드·릴리스와 사용자 지정 소개 범위에서 선별한 public-approved portfolio 문장이다. 정량 성능·사용자 규모·만족도·운영 안정성 수치는 사용하지 않는다. 생성 이력서, 커밋 개수와 테스트 파일 개수는 신규 경력 근거로 쓰지 않는다. 원본·개인·팀 기여를 AI 사용 여부로 대신 판정하지 않는다.

## 보류와 갱신

- Clue 컨테이너 배포는 후속 작업이다. 정리된 실행 경로와 설치 계약을 확인한 뒤 Docker Hub 등의 계정·저장소·공개 이미지 배포 범위를 별도로 확정한다. 현재 이미지 push나 다운로드 가능 문구를 추가하지 않는다.
- 플러그인 소개·설치·미디어는 해당 저장소 담당이 유지한다. 프로필은 원고나 private 화면을 복제하지 않고 공식 소개와 릴리스로 연결한다.
- 학습 저장소의 README는 학습 담당이 유지한다. 프로젝트 채팅의 정리·삭제·신규 추출 보류는 그대로다.
- 최신 릴리스 링크는 버전 자동 선정을 위해서만 사용한다. 기능·검증 범위가 바뀌면 공개 문장과 이 근거 표를 함께 검토한다.
