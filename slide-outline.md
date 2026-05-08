# 느좋 바이브코딩 포스트모텀

## Meta
- **Topic**: 게임기획자가 AI 도구(Codex / ClaudeCode / GPT / Gemini / Suno / Figma 등)로 8주간 게임을 바이브코딩한 회고록 — 실패·발견·인사이트 중심
- **Target Audience**: 포트폴리오 리뷰어(채용·협업), 발표 청중(게임업계 동료·AI 도구에 관심 있는 기획자/개발자)
- **Tone/Mood**: 솔직한 1인칭 회고, 매거진 연재 일지 톤, 과장 없는 자기관찰, 임팩트 있는 인용구
- **Slide Count**: 약 46 slides
- **Aspect Ratio**: 16:9
- **Style**: modern-dark (변경 — editorial-magazine에서 전환, 모노크롬·악센트 제거)

## Design Principles (재설계 v2)
1. **한 슬라이드 = 한 메시지**. 보조 카드·풋노트·메타블록 모두 제거. 챕터 오픈은 "Week N + 한 줄 제목 + 한 줄 부제"만, 인용·인사이트는 "큰 한 문장"만.
2. **이미지가 메시지 자체**. 이미지 있는 슬라이드는 이미지가 캔버스 60%+ 차지. 텍스트는 좁은 컬럼 또는 캡션 한 줄.
3. **이미지 자산 재배치** (아래 슬라이드별 이미지 항목 참고). 모든 자산이 적재적소에 단 1회씩 사용되도록 매핑.

## Slide Composition (v3 — superseded by section below)

> 이 섹션은 v1 historical record. **실제 작업 기준**은 아래 "Slide Composition v3" 참고.

## Slide Composition v3 — Comic-Paneled, Layout C primary

### Layout System
- **Layout C (기본·다수)**: 좌 텍스트 / 우 패널 (1:1 또는 3:2). 패널 비율은 `aspect-ratio` 자동 매칭, `object-fit:contain`으로 절대 잘리지 않음.
- **Layout B (페어)**: 같은 슬라이드에 2개 관련 패널 가로 배치. 4컷 만화의 절반(panel 1+2 또는 3+4)을 한 슬라이드에 묶을 때 사용.
- **Layout D (간혹)**: 4컷 또는 6컷 통째로 큰 이미지로. 캡션은 미니멀. 챕터 종합·정리 슬라이드에 사용.

### Volume Budget
- **B 옵션 (~60장)**: 핵심 만화 3개 풀 분할(C) + 나머지 만화는 페어(B) + 6컷은 페어(B) × 3 + 단일 일러스트 풀-블리드(D)

### 핵심 풀 분할 만화 (3개)
- `1-5-1` Week 1 종합 회고 — 4 panels
- `6-4-1` Week 6 토큰 병목 깨달음 — 4 panels
- `7-4-1` Week 7 AI 시대 기획자 — 4 panels

### Slide-by-Slide

**[Cover · Intro · PART 1 Divider]**

| # | Title | Layout | Asset | Message |
|---|---|---|---|---|
| 1 | Cover | Cover | `ProjectH_Structure.png` BG | "느좋 바이브코딩 포스트모텀" + author |
| 2 | Contents | List | — | 6 챕터 |
| 3 | 화자 소개 | Text | — | "프론트·백엔드 전무한 게임 디자이너가 코드를 만진다" |
| 4 | 왜 바이브코딩 | Text | — | "벼르고 있던 바이브코딩. CLI도 처음, 코덱스도 처음." |
| 5 | PART 1 Divider | Divider | — | "8주의 항해" |
| 6 | 8주 타임라인 | List | — | 8행 W01~W08 |

**[Week 1 — 첫 코덱스] (7 slides)**

| # | Title | Layout | Asset | Message |
|---|---|---|---|---|
| 7 | Week 1 인트로 | C-1:1 | `1-1.jpg` | "첫 코덱스. 모든 게 처음." |
| 8 | 시스템 갈아엎기 | B-1:1 | `1-2.jpg` + `1-3.jpg` | "채팅→자동전투. 3~4번 갈아엎다" |
| 9 | skill.sh + 애니메이션 발견 | C-1:1 | `0311.gif` | "한 줄의 스킬 추가가 UI를 통째로 바꿨다" |
| 10 | 티케팅 프로세스 | C-1:1 | `1-4.jpg` | "GPT 티켓 → Codex 결과물. 검증까지 한 번에" |
| 11 | Week 1 회고 ① | C-1:1 | `1-5-1_p1` | "의식의 흐름으로 시작한 바이브코딩" |
| 12 | Week 1 회고 ② | C-1:1 | `1-5-1_p2` | "어떻게 만들지 알면 빨리 만들 수 있다" |
| 13 | Week 1 회고 ③ | C-1:1 | `1-5-1_p3` | "구조를 아는 내가 AI를 잘 다룬다" |
| 14 | Week 1 회고 ④ | C-1:1 | `1-5-1_p4` | "AI와 협업, 효율적인 프로세스" |

**[Week 2 — 중간 소회] (3 slides)**

| # | Title | Layout | Asset | Message |
|---|---|---|---|---|
| 15 | Week 2 — 환경 정리 | C-1:1 | `2-1.jpg` | "유니티 전환, 두 AI 병행. 토큰 압박 시작" |
| 16 | Week 2 깨달음 | D | `2-2-1.png` (단일) | "문서가 컨텍스트다. 기획서를 잘 써야 한다" |

**[Week 3 — 디벨롭하는 중] (3 slides)**

| # | Title | Layout | Asset | Message |
|---|---|---|---|---|
| 17 | Week 3 인트로 | C | 영상 카드 `3번 영상_0311.mp4` | "길드마스터 영감. ClaudeCode + Codex 병행" |
| 18 | 아트와 사운드 | Text | — | "GPT/Gemini/Grok 아트 + Suno BGM" |
| 19 | Week 3 회고 — 도메인 | D | `3-1-1.png` (단일) | "도메인 지식·인사이트·철학·기획력이 더 중요하다" |

**[Week 4 — 비교할 수 있는 빌드] (5 slides)**

| # | Title | Layout | Asset | Message |
|---|---|---|---|---|
| 20 | Week 4 — 비교 빌드 영상 | C | 영상 카드 `4번 영상_0405.mp4` | "저번 빌드 대비 비교 영상" |
| 21 | 4-1-1 ① + ② (UI · 재미) | B-3:2 | `4-1-1_p1` + `_p2` | "캐릭터 모집/정보/제작 UI · 핵심 재미 연출" |
| 22 | 4-1-1 ③ + ④ (토큰 100%) | B-3:2 | `4-1-1_p3` + `_p4` | "토큰 100% 소진 → 세상이 멈췄다" |
| 23 | 4-2-1 ① + ② (AI는 일을 줄일까) | B-3:2 | `4-2-1_p1` + `_p2` | "AI 쓰면 일 줄겠지? · 프로토타입 완성" |
| 24 | 4-2-1 ③ + ④ ('다음만 있었다') | B-3:2 | `4-2-1_p3` + `_p4` | "새 아이디어 폭발 · '멈춤은 없었고 다음만 있었다'" |

**[Week 5 — 어셋 작업 환경에 올인] (8 slides)**

| # | Title | Layout | Asset | Message |
|---|---|---|---|---|
| 25 | Week 5 — Pro→Max | C-3:2 | `5-6-1_p1` | "Pro→Max. 더 많은 다음을 위해" |
| 26 | Week 5 — Claude→Figma 환경 | B-3:2 | `5-6-1_p2` + `_p3` | "Claude→Figma 환경 구축, 진짜 그려준다" |
| 27 | Week 5 — Figma 워크플로 | B-3:2 | `5-6-1_p4` + `_p5` | "시안→유니티 스크립트→프리팹. 노하우 정착" |
| 28 | Week 5 — Pro→Max 결정 | C-3:2 | `5-6-1_p6` | "결국 더 많은 다음을 만들기 위한 선택" |
| 29 | Week 5 — UI 리뉴얼 | B-1:1 | `5-7-1_p1` + `_p2` | "퀄리티 UI 리뉴얼 · 좌표 X, 수학적 분할" |
| 30 | Week 5 — 유지보수 함정 | B-1:1 | `5-7-1_p3` + `_p4` | "offset 수정 불가능 → 규격화·규격화·규격화" |
| 31 | Week 5 — 자체 Tool | B-1:1 | `5-8-1_p1` + `_p2` | "Tool 제작. 만들고 폐기하고 개선" |
| 32 | Week 5 — 효율 강박 | B-1:1 | `5-8-1_p3` + `_p4` | "AI는 AI대로, 나는 다른 일 — 아직 무리" |

**[Week 6 — 멀티에이전트 오케스트라] (11 slides)**

| # | Title | Layout | Asset | Message |
|---|---|---|---|---|
| 33 | Week 6 — 오케스트라 | B-3:2 | `6-1-1_p1` + `_p2` | "4명 에이전트 — 디렉터/아이템/전투/내러티브" |
| 34 | Week 6 — 아트풍 충돌 | B-3:2 | `6-1-1_p3` + `_p4` | "GPT vs Gemini 아트풍 차이" |
| 35 | Week 6 — Codex 시뮬레이터 | B-3:2 | `6-1-1_p5` + `_p6` | "Claude 병렬 + Codex 밸런스 시뮬" |
| 36 | Week 6 영상 | C | 영상 카드 `6번 영상.mp4` | Week 6 빌드 영상 |
| 37 | Week 6 — Claude는 다 한다 | B-1:1 | `6-2-1_p1` + `_p2` | "영상·디자인·문서까지. 단, 편집 비효율" |
| 38 | Week 6 — 자동화·규격화 | B-1:1 | `6-2-1_p3` + `_p4` | "찍어낼 때 효율 나오는 프로세스" |
| 39 | Week 6 — 70/80 곡선 | B-3:2 | `6-3-1_p1` + `_p2` | "AI 결과 한계 · 70→85점은 가파르다" |
| 40 | Week 6 — 멀티태스킹 필요 | B-3:2 | `6-3-1_p3` + `_p4` | "여러 업무 동시 컨펌 = 도메인+멀티태스킹" |
| 41 | Week 6 회고 ① — 토큰 효율화 | C-3:2 | `6-4-1_p1` | "처음엔 토큰 효율 작업, 그러나 한계" |
| 42 | Week 6 회고 ② — 한계 | C-3:2 | `6-4-1_p2` | "더 이상 퍼포먼스 안 올라간다" |
| 43 | Week 6 회고 ③ — 정체 | C-3:2 | `6-4-1_p3` | "구조를 다듬어도 퀄리티 정체" |
| 44 | Week 6 회고 ④ — 본질 | C-3:2 | `6-4-1_p4` | "사람이! 비루한 토큰이! 병목이구나!" |

**[Week 7 — 레이드와 콘텐츠 루프 완성] (10 slides)**

| # | Title | Layout | Asset | Message |
|---|---|---|---|---|
| 45 | Week 7 — 레이드 | B-3:2 | `7-1-1_p1` + `_p2` | "12인 캐릭터 단일 보스 도전 · 시뮬레이터" |
| 46 | Week 7 — 컨디션·캐릭터 정보창 | B-3:2 | `7-1-1_p3` + `_p4` | "입장 가능 처리 + 정보창 리뉴얼" |
| 47 | Week 7 — 액션 3요소 | B-3:2 | `7-2-1_p1` + `_p2` | "Animation·Effect·Sound 시스템 적용" |
| 48 | Week 7 — 3요소 + 태그 시스템 | B-3:2 | `7-2-1_p3` + `_p4` | "3요소 구색 갖춤 · 태그 이전 시스템" |
| 49 | Week 7 — 콘텐츠 루프 완성 | B-3:2 | `7-3-1_p1` + `_p2` | "재료→재능→상위→레이드→다시" |
| 50 | Week 7 — 끝없는 개선 | B-3:2 | `7-3-1_p3` + `_p4` | "이후 다듬고 다듬고 — 끝이 없긴 하지" |
| 51 | Week 7 영상 | C | 영상 카드 `7번 영상.mp4` | Week 7 빌드 영상 |
| 52 | Week 7 회고 ① — Claude 아쉬움 | C-3:2 | `7-4-1_p1` | "Claude 사용경험이 점점 아쉽다" |
| 53 | Week 7 회고 ② — Claude vs Codex | C-3:2 | `7-4-1_p2` | "두 회사 완주 잘 했으면 좋겠다" |
| 54 | Week 7 회고 ③ — 게임으로 말한다 | C-3:2 | `7-4-1_p3` | "꼰대정신: 게임쟁이는 게임으로 말한다" |
| 55 | Week 7 회고 ④ — AI 시대 | C-3:2 | `7-4-1_p4` | "결과로 증명하던 기획자의 역량을, AI로 보여줄 수 있는 시대" |

**[Week 8 — 정리의 한 주] (4 slides)**

| # | Title | Layout | Asset | Message |
|---|---|---|---|---|
| 56 | Week 8 — 리팩 + 밸런스 | B-3:2 | `8-3-1_p1` + `_p2` | "리팩토링 Codex가 잘함 · 밸런스 시행착오" |
| 57 | Week 8 — "넌 시키는대로만 해" | B-3:2 | `8-3-1_p3` + `_p4` | "판단은 인간, 처리는 AI" |
| 58 | Week 8 — 라이브 그림자 ①② | B-3:2 | `8-4-1_p1` + `_p2` | "라이브 복잡 · AI 의존 자각" |
| 59 | Week 8 — 라이브 그림자 ③④ | B-3:2 | `8-4-1_p3` + `_p4` | "테이블 작업 · 'AI는 도구, 나는 설계자'" |

**[PART 2 — 5 Insights] (6 slides)**

| # | Title | Layout | Asset | Message |
|---|---|---|---|---|
| 60 | PART 2 Divider | Divider | — | "도구 너머의 발견" |
| 61 | Insight 1 — 도메인 | Text | — | "도메인 지식이 우위다" |
| 62 | Insight 2 — 70/80 | C | `토큰 소비-1.png` (단일) | "70점은 빠르고, 80점은 가파르다" |
| 63 | Insight 3 — 판단 vs 처리 | Text | — | "판단은 인간, 처리는 AI" |
| 64 | Insight 4 — 병목 | Text | — | "사람과 토큰이 병목이다" |
| 65 | Insight 5 — 다음만 있다 | Text | — | "AI는 일을 줄이지 않는다" |

**[PART 3 — 결과물] (5 slides)**

| # | Title | Layout | Asset | Message |
|---|---|---|---|---|
| 66 | PART 3 Divider | Divider | — | "8주가 남긴 것" |
| 67 | Project H 구조도 | D-Map | `ProjectH_Architecture_Poster.png` | 풀-블리드 구조도 |
| 68 | 빌드 영상 갤러리 | Gallery | 5개 영상 카드 | 발전 과정 |
| 69 | AI 스택 | Catalog | — | 8주간 동원한 도구 |
| 70 | 다음 항해 + Closing | Closing | — | "도메인 위에 AI 얹기" |

### Total: 70 slides

**조정 가능 옵션** (60장으로 더 줄이려면):
- Week 5: 5-6-1 6컷을 페어 3장 → 풀-블리드 1장으로 압축 (-3)
- Week 6: 6-1-1 6컷 페어 3장 → 풀-블리드 1장 (-2)
- Week 6: 6-3-1 페어 2장 → 1장 압축 (-1)
- Week 8: 8-4-1 페어 2장 → 1장 (-1)
- Closing 합치기 (-1)
= -8 slides → 62 slides

또는 70장 그대로 가도 호흡은 적절

---

### Slide 1 — Cover
- **Type**: Cover
- **Title**: 느좋 코딩(바이브코딩) 포스트모텀
- **Subtitle**: 게임 기획자가 AI로 8주간 게임을 만든 기록
- **Author**: 유병휘
- **Visual**: `ProjectH_Structure.png`을 풀-블리드 배경(어둡게·그레이스케일 처리) + 그라디언트 비네트 위에 타이틀 + author 한 줄

### Slide 2 — Table of Contents
- **Type**: Contents
- **Items**:
  1. 시작하며 — 왜 바이브코딩
  2. 8주의 항해 (Week 1 → Week 8)
  3. 5가지 인사이트
  4. 결과물
  5. 사용한 AI 스택
  6. 다음 항해

### Slide 3 — 들어가며: 화자 소개
- **Type**: Intro
- **Key Message**: 프론트·백엔드 지식 전무
- **Details**:
  - 15년차 PD & 시니어 게임 디자이너 
  - 코딩 경험 거의 없음
  - "0과 1, 수학으로 이루어지는 리소스는 AI가 빠르고 쉽게 채워준다"

### Slide 4 — 들어가며: 왜 바이브코딩인가
- **Type**: Quote / Intro
- **Key Message**: 시간이 생겨서 벼르고 있던 바이브코딩, 일단 해보자
- **Details**:
  - GPT 구독 → Codex로 시작
  - "CLI도 처음, 코덱스도 처음"
  - 목표: 게임 프로토타입을 실제로 동작하게 만들기

### Slide 5 — Section Divider: PART 1. 8주의 항해
- **Type**: Section Divider
- **Title**: PART 1. 8주의 항해
- **Subtitle**: 매주 한 챕터씩, 시행착오와 발견의 기록

### Slide 6 — 8주 타임라인 한눈에
- **Type**: Timeline
- **Key Message**: 웹 → 유니티를 통해 8주간 개발
- **Details**:
  - W1 첫 코덱스, 채팅→자동전투
  - W2 유니티 전환, 두 AI 병행
  - W3 길드마스터 영감, BGM·아트 본격
  - W4 UI 리뉴얼, 핵심재미 연출
  - W5 Claude→Figma, 자체 Tool 제작
  - W6 멀티에이전트 오케스트라
  - W7 레이드·엔드콘텐츠 완성
  - W8 리팩토링·밸런스·회귀

---

### Slide 7 — Week 1 (1/4): 시작
- **Type**: Chapter Open
- **Title**: Week 1 — 첫 코덱스
- **Key Message**: CLI도, 코덱스도, 모든 게 처음
- **Details**:
  - GPT 구독 중 → Codex 3일 사용
  - 초기 계획: 유니티 MCP 연동
  - "더 작고 빠르게 MVP 만들어보자" 
  - 결정: 웹 게임으로 선회

### Slide 8 — Week 1 (2/4): 게임 시스템 갈아엎기
- **Type**: Process / Iteration
- **Key Message**: 채팅 전투 → 자동 전투 → 스킬 다양화. 시스템을 3~4번 갈아엎음
- **Details**:
  - 채팅 기반 전투: 3시간만에 완성, 재미없음 → 폐기
  - 자동전투로 전환: 처음보다 좋음, 특색 부족
  - 확률 발동 / 자원 소모 / 횟수 트리거 스킬 — 다채로운 전투 구성
  - 텍스트 기반 진행인데도 그럴듯하고 재미있음
- **Image**: 1-1.jpg / 1-2.jpg / 1-3.jpg / 1-4.jpg

### Slide 9 — Week 1 (3/4): 결정적 도구의 발견
- **Type**: Discovery
- **Key Message**: skill.sh의 web-design-guidelines 스킬로 UI/UX가 눈에 띄게 좋아짐
- **Details**:
  - 처음 웹 페이지 UI/UX는 별로였음
  - 스킬 추가 후 즉각적인 개선
  - vercel-react-best-practices, frontend-design 병용
  - 애니메이션·연출(흔들림·페이드아웃)도 자연스럽게 구현됨

### Slide 10 — Week 1 (4/4): 티케팅 프로세스의 발견
- **Type**: Insight
- **Key Message**: GPT가 티켓을 만들고 Codex가 실행 → 검증·해결까지 한 번에
- **Details**:
  - "GPT한테 어떻게 시키면 돼?"라고 자주 물음
  - GPT의 티켓을 Codex로 던짐 → 코드 작성 → 구현 → 검증 → 해결 → 결과물
  - 회원가입·로그인·인벤토리·스킬·아이템·스탯 모두 알아서 동작
  - **인용**: "검증해서 문제 있으면 문제까지 해결해서 결과물을 가져온다고?!"

---

### Slide 11 — Week 2 (1/3): 중간 소회
- **Type**: Chapter Open
- **Title**: Week 2 — 중간 소회
- **Key Message**: "포스트모텀까진 아니고 중간 소회 정도"
- **Details**:
  - Codex 단독 → ClaudeCode 병행 시작
  - 웹 게임 → 유니티 엔진 기반 새 프로젝트로 전환
  - 이유: 게임의 복잡성은 게임 상용화 엔진 & 좀 더 고도화된 게임을 만들고 싶어서

### Slide 12 — Week 2 (2/3): 환경 정리와 한계
- **Type**: Decision Log
- **Key Message**: 유니티 MCP 포기, ComfyUI 포기, 결국 토큰 사용 유료 AI로 회귀
- **Details**:
  - 유니티 MCP 포기 — 토큰 너무 많이 먹음
  - 아트 리소스: GPT + Gemini로 컨셉·스프라이트 제작
  - ComfyUI 도전했으나 그래픽카드 한계로 포기
  - PC 업그레이드 견적 충격
  - 토큰 압박: "이거까지하면 터질까? 이거까진 괜찮겠지?"
- **Image**: 2-1.jpg

### Slide 13 — Week 2 (3/3): 핵심 깨달음
- **Type**: Insight
- **Key Message**: 두 AI 병행의 핵심은 "문서 기반 컨텍스트 관리"
- **Details**:
  - Codex와 ClaudeCode를 병행하려면 문서 최신화가 필수
  - 기준점을 문서로 두니 두 AI가 잘 따라옴
  - 깨달음: **"기획서를 잘 써야 한다"**
  - 버티컬 슬라이스 목표 얼추 달성

---

### Slide 14 — Week 3 (1/3): 디벨롭 시작
- **Type**: Chapter Open
- **Title**: Week 3 — 디벨롭하는 중
- **Key Message**: 게임 컨셉은 [길드마스터]에서 영감
- **Details**:
  - 코드: ClaudeCode + Codex 병행
  - "Opus는 토큰을 너무 많이 먹어서 많이 못 쓴다"
  - 빌드를 폰(Z플립) / LD플레이어에 넣어 테스트
  - LD플레이어로 녹화

### Slide 15 — Week 3 (2/3): 아트와 사운드
- **Type**: Tools Showcase
- **Key Message**: 아트는 GPT/Gemini/Grok, BGM은 Suno
- **Details**:
  - 일관된 리소스 위해 ComfyUI 환경 다시 갈증
  - Suno: "곡 왤케 잘 뽑음...?" 보컬은 구독 유도
  - AI가 짜준 UI를 다 덜어내고 프리팹 기반으로 재구성하는 게 어려웠음
  - 다음 빌드는 텍스트·이미지·UX 폴리싱

### Slide 16 — Week 3 (3/3): 작업하다 보니 느낀 것
- **Type**: Pull Quote
- **Quote**: "부족한 지식을 성장시키려는 것보다, 업의 근본인 도메인 지식·인사이트·철학·기획력이 더 중요하다"
- **Footnote**: 바이브코딩을 하면 할수록 느끼는 것

---

### Slide 17 — Week 4 (1/3): 비교 빌드
- **Type**: Chapter Open
- **Title**: Week 4 — 비교할 수 있는 빌드
- **Key Message**: 저번 빌드 대비 비교 영상 제작, 다음은 3D 액션 게임 예정
- **Details**:
  - Varco / Meshy / Tripo 모델링 도구 탐색 시작
  - "모델링까진 잘하는데 애니메이션이..."
  - 가장 큰 변경점 2가지: UI / 게임 핵심 재미 연출

### Slide 18 — Week 4 (2/3): 핵심 재미의 발견
- **Type**: Design Story
- **Key Message**: 개발 중 떠오른 새로운 재미 요소를 기존 기획에 녹여내기
- **Details**:
  - 캐릭터 모집 / 정보창 / 사무실 / 인벤토리 / 제작 UI 작업
  - 프리팹과 하드코딩 사이에서 진땀
  - 던전 파견 중: **실시간 직관·개입·결과의 경험**
  - "저번 빌드보단 재미있는 듯"
- **Video Thumbnail**: 4번 영상_0405.mp4 (링크 부착)

### Slide 19 — Week 4 (3/3): 토큰 100%
- **Type**: Pull Quote
- **Quote**: "AI는 일을 줄여주진 않고, 오히려 더 많은 일을 하게 한다"
- **Details**:
  - 이번주 Claude 토큰 100% 소진 → "세상이 멈췄다"
  - Codex는 23% 남았는데 초기화가 너무 멀다
  - "'멈춤'은 없었고 '다음'만 있었다"

---

### Slide 20 — Week 5 (1/4): Pro → Max
- **Type**: Chapter Open
- **Title**: Week 5 — 어셋 작업 환경에 올인
- **Key Message**: 결국 Claude Pro에서 Max로 업그레이드
- **Details**:
  - "더 많은 다음을 하기 위해" 구독 업그레이드
  - 이번주는 개발 진도보다 어셋 작업 환경 위주

### Slide 21 — Week 5 (2/4): Claude → Figma
- **Type**: Workflow
- **Key Message**: ClaudeCode가 시안 작성 → 유니티 에디터 스크립트 작성 → 버튼 한 번으로 UI 프리팹 완성
- **Details**:
  - claude-to-figma 환경 구축 — "진짜...힘들었다"
  - 퀄리티는 아쉽지만 직접 하는 것보단 빠르고 편함
  - 워크플로 정착: 아스키 시안 → 택1 → 피그마 작업
- **Image**: 5-1.jpg / 5-2.jpg / 5-3.jpg

### Slide 22 — Week 5 (3/4): 유지보수의 함정
- **Type**: Caveat
- **Key Message**: AI가 만든 UI 프리팹은 좌표 기반이 아닌 수학적 분할 → offset 수정 불가
- **Details**:
  - 코드뿐 아니라 UI도 AI 작업 결과의 유지보수가 어렵다
  - 해결책 가설: **규격화 · 규격화 · 규격화**
- **Image**: 5-4.jpg / 5-5.jpg

### Slide 23 — Week 5 (4/4): 자체 Tool
- **Type**: Insight
- **Key Message**: 콘텐츠 개발 효율을 위한 Tool을 직접 만들기 시작
- **Details**:
  - 만들고 폐기하고 개선하기를 혼자서 가능 — AI의 진짜 강점
  - 효율 강박: "AI는 AI대로 돌리고 나는 다른 일 하고 싶은데 아직 무리"

---

### Slide 24 — Week 6 (1/4): 오케스트라
- **Type**: Chapter Open
- **Title**: Week 6 — 멀티에이전트 오케스트라
- **Key Message**: 4명의 에이전트 — 디렉터 / 아이템 / 전투 / 내러티브
- **Details**:
  - "너희들 서로 싸워라. 디렉터, 잘 중재해줘"
  - Claude 병렬 에이전트로 빠르게 토큰 소모 → 리필까지 다른 일
  - Codex로 코드 리팩토링 + 로그 기반 밸런스 시뮬레이터 구축

### Slide 25 — Week 6 (2/4): 아트풍의 일관성 한계
- **Type**: Caveat
- **Key Message**: 동일 프롬프트·레퍼런스에도 GPT/Gemini 아트풍 차이가 큼
- **Details**:
  - 아이콘은 Gemini가 의도에 가까움
  - 캐릭터는 GPT가 잘했지만 아이콘에선 어긋남
  - 일관성 유지 어려움 → 도구 분업화의 비용

### Slide 26 — Week 6 (3/4): Claude는 다 한다
- **Type**: Tools Showcase
- **Key Message**: 영상·디자인·문서까지 — 단, 편집 단가가 비싸다
- **Details**:
  - Claude로 영상도 만들고 디자인도 한다
  - 편집할 때마다 자연어 입력 → 토큰 소모 → 비효율
  - 자동화·규격화 후 찍어낼 때 효율 나오는 프로세스

### Slide 27 — Week 6 (4/4): 본질
- **Type**: Pull Quote
- **Quote**: "사람이! 비루한 토큰이! 병목이구나!"
- **Details**:
  - 70점까진 빠르지만 75·80·85점은 매우 힘들다
  - 결국 막대한 토큰을 쏟아부어야 아웃풋이 나온다
  - "젠슨 황이시여… 이제야 깨닫습니다"
  - 여러 업무를 동시에 파악·피드백·컨펌하는 역량 = 도메인 지식 + 멀티태스킹

---

### Slide 28 — Week 7 (1/4): 엔드콘텐츠
- **Type**: Chapter Open
- **Title**: Week 7 — 레이드와 콘텐츠 루프 완성
- **Key Message**: 12인 캐릭터로 단일 보스 도전, 도달 wave까지 보상
- **Details**:
  - 파티별 롤 분담 형태 지향
  - 컨디션·입장 가능 처리 (계정 레벨 등)
  - 캐릭터 정보창 리뉴얼

### Slide 29 — Week 7 (2/4): 액션의 3요소
- **Type**: Concept
- **Key Message**: Animation · Effect · Sound — 구색을 갖췄다
- **Details**:
  - 이펙트 시스템·리소스 적용 → 타격감
  - 사운드 시스템 적용
  - 태그 시스템 리디자인 (캐릭터 획득 목표 제공)

### Slide 30 — Week 7 (3/4): 콘텐츠 루프
- **Type**: Loop Diagram
- **Key Message**: 재료 파밍 → 재능 파밍 → 레이드 도전 → 다시 재료 파밍
- **Details**:
  - "이제야 게임이 돌아가는 모습이 된 것 같다"
  - 이후는 연출·UI/UX·데이터 폴리싱
  - "끝이 없긴 하지"
- **Video Thumbnail**: 6번 영상.mp4 / 7번 영상.mp4 (링크 부착)

### Slide 31 — Week 7 (4/4): AI 시대 기획자의 증명
- **Type**: Pull Quote
- **Quote**: "결과로만 증명할 수 있었던 기획자의 역량을, AI로 보여줄 수 있는 시대가 왔다"
- **Details**:
  - 평소 "게임쟁이는 게임으로 말한다"는 꼰대정신
  - 규모 있는 게임은 오래 걸린다, 그러나 AI가 그걸 쉽게 해준다
  - Claude·Codex의 라이브 업데이트에 사용 경험이 좌우됨 — 두 회사가 완주하길

---

### Slide 32 — Week 8 (1/3): 리팩 · 밸런스 · 버그
- **Type**: Chapter Open
- **Title**: Week 8 — 정리의 한 주
- **Key Message**: 이번주는 3가지 — 리팩토링 / 밸런스 / 버그 수정
- **Details**:
  - 리팩토링: Codex가 잘해줌
  - 시행착오 많았던 영역: 밸런스

### Slide 33 — Week 8 (2/3): 회귀
- **Type**: Insight
- **Quote**: "넌 시키는대로만 해!"
- **Key Message**: 판단을 AI에 맡기니 값이 안 맞음 → 바이브코딩 초심으로 회귀
- **Details**:
  - 밸런스에는 기준·방향성이 필요한데 통째로 던지니 안됨
  - **판단은 인간, 데이터 입출력·정리는 AI**
  - 그제서야 값이 맞기 시작

### Slide 34 — Week 8 (3/3): 라이브 서비스의 그림자
- **Type**: Caveat / Reflection
- **Key Message**: AI 의존은 도메인 지식 없으면 끌려간다
- **Details**:
  - "테이블 입력·변경마저 토큰으로 시켜버린다"
  - 수백·수천 라인 엑셀/CSV는 최적화된 입출력 방식 필요
  - 모든 요소를 점수화하고 AI를 갈구는 것이 다음 단계
  - 하이퍼캐주얼 선두주자들이 먼저 가고 있을 듯
- **Image**: 8-1.jpg / 8-2.jpg

---

### Slide 35 — Section Divider: PART 2. 5가지 인사이트
- **Type**: Section Divider
- **Title**: PART 2. 8주가 남긴 5가지 인사이트
- **Subtitle**: 도구 너머의 발견

### Slide 36 — 인사이트 1: 도메인 지식이 우위다
- **Type**: Insight
- **Key Message**: AI 시대일수록 업의 근본(도메인·인사이트·철학·기획력)이 중요하다
- **Details**:
  - 게임 구조를 알기에 구조를 잡고 AI에 지시하는 게 어렵지 않았다
  - 부족한 지식을 메우는 것보다 본업의 깊이가 핵심
  - 기획을 잘 치는 능력 = 결과물 퀄리티

### Slide 37 — 인사이트 2: 70점은 빠르고, 80점은 가파르다
- **Type**: Insight / Curve
- **Key Message**: AI는 70점까지는 시간 대비 압도적, 80점부터는 가파른 토큰 곡선
- **Details**:
  - 빠른 프로토타이핑에는 대체 불가
  - 폴리싱 단계는 토큰을 쏟아붓는 게임
  - 의식의 흐름 수정이 잦으면 코드가 누더기될 우려

### Slide 38 — 인사이트 3: 판단은 인간, 처리는 AI
- **Type**: Insight
- **Key Message**: 판단을 AI에 위임하면 값이 안 맞는다
- **Details**:
  - 밸런스 작업에서 직접 체험
  - "넌 시키는대로만 해" 원칙
  - AI는 일단 진행시키므로 도메인 없으면 끌려간다

### Slide 39 — 인사이트 4: 사람과 토큰이 병목이다
- **Type**: Insight / Pull Quote
- **Key Message**: 효율보다 결국 토큰량과 사람의 멀티태스킹 역량이 한계선
- **Details**:
  - 토큰 효율로는 한계가 있다
  - 막대한 토큰을 쏟아부어야 아웃풋이 나오는 영역
  - 여러 업무 동시 컨펌하는 멀티태스킹 능력 필요
  - **인용**: "사람이! 비루한 토큰이! 병목이구나!"

### Slide 40 — 인사이트 5: AI는 일을 줄이지 않는다
- **Type**: Pull Quote
- **Quote**: "'멈춤'은 없었고 '다음'만 있었다"
- **Details**:
  - 결과물을 만들수록 다음 작업이 따라온다
  - 효율 강박과의 싸움
  - 검증 비용은 줄어들지만 결정 비용은 늘어난다

---

### Slide 41 — Section Divider: PART 3. 결과물
- **Type**: Section Divider
- **Title**: PART 3. 8주가 남긴 것
- **Subtitle**: 결과물 · 스택 · 다음 항해

### Slide 42 — Project H 구조도
- **Type**: System Map
- **Key Message**: Project H 전체 구조 — 코드·데이터·UI·문서 허브의 4축
- **Image**: ProjectH_Architecture_Poster.png 또는 ProjectH_Structure_Interactive.png
- **Details**:
  - 4축: 코드(Scripts) / 데이터(Tables) / UI(Prefabs) / 문서(Doc)
  - 주의 지점: CSV 헤더 기준 / SerializeField 변경 / Resources.Load 경로

### Slide 43 — 빌드 영상 모음
- **Type**: Video Gallery
- **Key Message**: 빌드 발전 과정 — 4편의 영상 (썸네일 + 링크)
- **Details**:
  - 3번 영상_0311.mp4 — 초기 프로토타입
  - 4번 영상_0405.mp4 — UI 리뉴얼 + 핵심재미 연출
  - 6번 영상.mp4 — 멀티에이전트 빌드
  - 7번 영상.mp4 — 레이드 엔드콘텐츠
  - project-h-final.mp4 — 최종 빌드
- **Note**: 발표 시 클릭→재생, 포트폴리오는 링크로

### Slide 44 — 사용한 AI 스택
- **Type**: Stack Catalog
- **Key Message**: 8주간 동원한 AI 도구 카탈로그
- **Details**:
  - **코드**: Codex (CLI) / ClaudeCode (Pro→Max) / Opus
  - **티케팅·기획**: GPT
  - **아트**: GPT / Gemini / Grok / Varco / Meshy / Tripo
  - **사운드**: Suno
  - **UI 디자인**: Claude → Figma 파이프라인
  - **세팅 보조**: Claude 스킬(web-design-guidelines / vercel-react-best-practices / frontend-design)
  - **포기한 도구**: 유니티 MCP / ComfyUI(GPU 한계)

### Slide 45 — 다음 항해
- **Type**: Next Up
- **Key Message**: 폴리싱과 3D 액션 게임 예고
- **Details**:
  - 현재 빌드: 연출 다듬기 / UI·UX 개선 / 데이터 폴리싱
  - 다음: 3D 액션 게임 도전 (모델링·애니메이션 파이프라인 탐색 중)
  - 콘텐츠 점수화·자동 밸런스 실험

### Slide 46 — Closing
- **Type**: Closing
- **Message**: 결과로 증명하던 기획자의 역량을, AI로 보여줄 수 있는 시대.
- **Details**:
  - 한 줄 요약: 도메인 위에 AI를 얹을 때 가장 빠르게 멀리 간다
  - 연락처 / 포트폴리오 링크 자리

---

## Notes for Design Stage (v2)

### Style
- **modern-dark** 모노크롬 (`#0F0F0F` BG / `#1A1A1A` card / `#FFFFFF` text / `#B0B0B0`·`#707070` secondary). 악센트 컬러 없음.
- 폰트: Pretendard Bold (display) + Pretendard (body) + JetBrains Mono (라벨)
- 위계는 사이즈·웨이트·여백·보더로만

### Slide-Type Layout Rules (v2)
| Type | 구성 (단순화) |
|---|---|
| Cover | 풀-블리드 이미지 배경 + 타이틀 + author 1줄. 마스트헤드/byline 박스 제거 |
| Chapter Open | 좌측 큰 이미지 60% (있으면) / 우측 텍스트 (WEEK NN 라벨 + 한 줄 제목 + 한 줄 부제). 챕터카드·세부 카드 제거 |
| Process / Iteration | 큰 이미지 1~2장 + 캡션 한 줄. 다단 리스트 제거 |
| Discovery / Insight | 풀-블리드 이미지(또는 단색) + 큰 한 문장. Before/After 카드 제거 |
| Pull Quote | 큰 인용 한 문장만. eyebrow + 풋터 카드 제거 |
| Tools Showcase | 큰 도구명 그리드 (3개 max). 본문 박스 최소화 |
| Caveat | 큰 경고 메시지 + 보조 한 줄. 이미지 있으면 절반 |
| Stat | 큰 숫자 1개 + 한 줄. 다단 셀 제거 |
| Section Divider | "PART N" + 큰 제목 + 한 줄. 거대 데코 숫자 매우 옅게 |
| Section Map | 풀-블리드 이미지(ProjectH 구조도). 본문 텍스트 최소화 |

### Image / Video Asset Map (재배치)
모든 자산이 단 1회 사용되도록 매핑.

| 슬라이드 | 자산 | 활용 |
|---|---|---|
| 1 | `ProjectH_Structure.png` | 풀-블리드 배경 (어둡게 처리) |
| 7 (W1 챕터) | `1-1-1.jpg` | 좌측 60% 풀 이미지 |
| 8 (W1 시스템 변천) | `1-2-1.jpg` + `1-3-1.jpg` | 큰 2장 그리드 + 캡션 한 줄씩 |
| 9 (W1 스킬 발견) | `0311.gif` | 풀-블리드 (좌측 비네트) |
| 10 (W1 인용) | — | 텍스트 only |
| 11 (W2 챕터) | `2-1-1.jpg` | 좌측 60% 풀 이미지 |
| 12 (W2 환경) | — | 텍스트 only (간소화: ✕✕✓ 라인 정도) |
| 13 (W2 깨달음) | — | 텍스트 only 인용 |
| 14 (W3 챕터) | `3번 영상_0311.mp4` | 비디오 카드 (썸네일 추출 전 placeholder) |
| 15 (W3 아트·사운드) | — | 도구명 큰 그리드만 |
| 16 (W3 도메인 인용) | — | 텍스트 only |
| 17 (W4 챕터) | `4번 영상_0405.mp4` | 비디오 카드 |
| 18 (W4 핵심 재미) | `1-4-1.jpg` | 큰 이미지 + 한 줄 |
| 19 (W4 토큰 100%) | — | 텍스트 only 인용 |
| 20 (W5 챕터) | — | 텍스트 only 챕터 오픈 |
| 21 (W5 Figma 워크플로) | `5-1-1.jpg` + `5-2-1.jpg` + `5-3-1.jpg` | 큰 3장 그리드 |
| 22 (W5 유지보수) | `5-4-1.jpg` + `5-5-1.jpg` | 큰 2장 그리드 |
| 23 (W5 자체 Tool) | — | 텍스트 only 인사이트 |
| 24 (W6 오케스트라) | — | 4 에이전트 라벨 (텍스트만) |
| 25 (W6 아트 일관성) | — | 텍스트 only |
| 26 (W6 Claude 다재능) | — | 텍스트 only |
| 27 (W6 본질 인용) | — | 텍스트 only |
| 28 (W7 레이드) | `7번 영상.mp4` | 비디오 카드 |
| 29 (W7 액션 3요소) | — | 3 라벨 (텍스트만) |
| 30 (W7 콘텐츠 루프) | `6번 영상.mp4` | 비디오 카드 + 루프 다이어그램 |
| 31 (W7 기획자 시대 인용) | — | 텍스트 only |
| 32 (W8 챕터) | `8-1-1.jpg` | 좌측 60% 풀 이미지 |
| 33 (W8 회귀 인용) | — | 텍스트 only |
| 34 (W8 라이브 그림자) | `8-2-1.jpg` | 큰 이미지 + 한 줄 |
| 42 (구조도) | `ProjectH_Architecture_Poster.png` | 풀-블리드 |
| 43 (영상 갤러리) | `project-h-final.mp4` + 4개 영상 | 5-cell 비디오 카드 그리드 |

### Memo (slides 1·6 수정 사항 — v2 재작업으로 자동 해결됨)
- v1 slide 1: 메인 타이틀 + 푸터 시각 인접 — v2에선 풀-블리드 배경으로 재구성
- v1 slide 6: 8주 카드 컨텐츠 row 초과 — v2에선 텍스트 더 줄여 해결
