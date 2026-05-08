"""슬라이드 일괄 생성기 v2 (피드백 반영: 헤더 정리, 6컷 B-1:1, 영상 링크, slide 62/67/71)"""
import os, sys

OUT = r'D:/20. Portpolio/느좋 코딩 포스트모텀/slides'

HEAD = '''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300..700&display=swap" rel="stylesheet">
<style>
  *{{margin:0;padding:0;box-sizing:border-box}}
  body{{width:720pt;height:405pt;background:#0F0F0F;color:#FFFFFF;font-family:'Pretendard',-apple-system,sans-serif;overflow:hidden;position:relative}}
  .mono{{font-family:'JetBrains Mono',monospace;letter-spacing:0.18em;text-transform:uppercase}}
  .panel-frame{{background:#1A1A1A;border:1pt solid #333;display:flex;align-items:center;justify-content:center;overflow:hidden;}}
  .panel-frame img{{width:100%;height:100%;object-fit:contain;display:block;}}
  .video-card{{background:#1A1A1A;border:1pt solid #333;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:14pt;overflow:hidden;position:relative;text-decoration:none;}}
  .video-card img.bg{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:brightness(0.65);}}
  .video-card .play{{position:relative;font-size:54pt;color:#FFFFFF;line-height:1.4;text-shadow:0 2pt 8pt rgba(0,0,0,0.6);z-index:1;}}
  .video-card .label{{position:absolute;bottom:14pt;font-size:9pt;color:#FFFFFF;text-shadow:0 1pt 4pt rgba(0,0,0,0.8);z-index:1;font-family:'JetBrains Mono',monospace;letter-spacing:0.18em;text-transform:uppercase;}}
  a.video-card:hover{{border-color:#666;}}
</style>
</head>
<body>
'''
TAIL = '</body>\n</html>\n'

def header(num, top_left, top_right=None):
    if top_right is None:
        top_right = f'P. {num:02d}'
    return f'''  <p class="mono" style="position:absolute;top:32pt;left:48pt;font-size:9pt;color:#707070;">{top_left}</p>
  <p class="mono" style="font-size:9pt;color:#707070;position:absolute;top:32pt;right:48pt;">{top_right}</p>
'''

def header_minimal(num, top_left, top_right=None):
    if top_right is None:
        top_right = f'P. {num:02d}'
    return f'''  <p class="mono" style="position:absolute;top:14pt;left:48pt;font-size:9pt;color:#707070;">{top_left}</p>
  <p class="mono" style="font-size:9pt;color:#707070;position:absolute;top:14pt;right:48pt;">{top_right}</p>
'''

def layout_c11(num, header_text, eyebrow, title_l1, title_l2, body, img, footer):
    h = HEAD.format(title=f'Slide {num}')
    h += header(num, header_text)
    h += f'''  <div style="position:absolute;left:48pt;top:88pt;width:340pt;">
    <p class="mono" style="font-size:9pt;color:#707070;margin-bottom:14pt;">{eyebrow}</p>
    <h1 style="font-size:32pt;font-weight:700;color:#FFFFFF;line-height:1.28;letter-spacing:-0.025em;">{title_l1}<br><span style="color:#B0B0B0;">{title_l2}</span></h1>
    <p style="font-size:12pt;color:#B0B0B0;margin-top:22pt;line-height:1.6;">{body}</p>
  </div>
  <div class="panel-frame" style="position:absolute;right:48pt;top:78pt;width:260pt;height:260pt;">
    <img src="./assets/{img}" alt="">
  </div>
  <p class="mono" style="position:absolute;bottom:24pt;right:48pt;font-size:8pt;color:#707070;">{footer}</p>
'''
    return h + TAIL

def layout_c32(num, header_text, eyebrow, title_l1, title_l2, body, img, footer):
    h = HEAD.format(title=f'Slide {num}')
    h += header(num, header_text)
    h += f'''  <div style="position:absolute;left:48pt;top:88pt;width:340pt;">
    <p class="mono" style="font-size:9pt;color:#707070;margin-bottom:14pt;">{eyebrow}</p>
    <h1 style="font-size:32pt;font-weight:700;color:#FFFFFF;line-height:1.28;letter-spacing:-0.025em;">{title_l1}<br><span style="color:#B0B0B0;">{title_l2}</span></h1>
    <p style="font-size:12pt;color:#B0B0B0;margin-top:22pt;line-height:1.6;">{body}</p>
  </div>
  <div class="panel-frame" style="position:absolute;right:48pt;top:118pt;width:280pt;height:186pt;">
    <img src="./assets/{img}" alt="">
  </div>
  <p class="mono" style="position:absolute;bottom:24pt;right:48pt;font-size:8pt;color:#707070;">{footer}</p>
'''
    return h + TAIL

def layout_b11(num, header_text, headline_l1, headline_l2, img1, img2, cap1_label, cap1_text, cap2_label, cap2_text):
    h = HEAD.format(title=f'Slide {num}')
    h += header(num, header_text)
    h += f'''  <h1 style="position:absolute;top:64pt;left:48pt;right:48pt;font-size:24pt;font-weight:700;color:#FFFFFF;line-height:1.32;letter-spacing:-0.02em;">{headline_l1}<span style="color:#B0B0B0;">{headline_l2}</span></h1>
  <div style="position:absolute;left:48pt;right:48pt;top:130pt;display:flex;gap:14pt;justify-content:center;">
    <div class="panel-frame" style="width:220pt;height:220pt;"><img src="./assets/{img1}" alt=""></div>
    <div class="panel-frame" style="width:220pt;height:220pt;"><img src="./assets/{img2}" alt=""></div>
  </div>
  <div style="position:absolute;left:48pt;right:48pt;top:354pt;display:flex;gap:14pt;justify-content:center;">
    <div style="width:220pt;"><p class="mono" style="font-size:8pt;color:#707070;margin-bottom:4pt;">{cap1_label}</p><p style="font-size:10pt;color:#B0B0B0;line-height:1.4;">{cap1_text}</p></div>
    <div style="width:220pt;"><p class="mono" style="font-size:8pt;color:#FFFFFF;margin-bottom:4pt;">{cap2_label}</p><p style="font-size:10pt;color:#FFFFFF;line-height:1.4;">{cap2_text}</p></div>
  </div>
'''
    return h + TAIL

def layout_b3(num, header_text, headline_l1, headline_l2, img1, img2, img3, cap1_label, cap1_text, cap2_label, cap2_text, cap3_label, cap3_text):
    """3-패널 가로 (스크린샷 등 세로 portrait 이미지에 적합)"""
    h = HEAD.format(title=f'Slide {num}')
    h += header(num, header_text)
    h += f'''  <h1 style="position:absolute;top:64pt;left:48pt;right:48pt;font-size:22pt;font-weight:700;color:#FFFFFF;line-height:1.32;letter-spacing:-0.02em;">{headline_l1}<span style="color:#B0B0B0;">{headline_l2}</span></h1>
  <div style="position:absolute;left:48pt;right:48pt;top:120pt;display:flex;gap:10pt;justify-content:center;">
    <div class="panel-frame" style="width:198pt;height:230pt;"><img src="./assets/{img1}" alt=""></div>
    <div class="panel-frame" style="width:198pt;height:230pt;"><img src="./assets/{img2}" alt=""></div>
    <div class="panel-frame" style="width:198pt;height:230pt;"><img src="./assets/{img3}" alt=""></div>
  </div>
  <div style="position:absolute;left:48pt;right:48pt;top:358pt;display:flex;gap:10pt;justify-content:center;">
    <div style="width:198pt;"><p class="mono" style="font-size:7pt;color:#707070;margin-bottom:3pt;">{cap1_label}</p><p style="font-size:9pt;color:#B0B0B0;line-height:1.35;">{cap1_text}</p></div>
    <div style="width:198pt;"><p class="mono" style="font-size:7pt;color:#707070;margin-bottom:3pt;">{cap2_label}</p><p style="font-size:9pt;color:#B0B0B0;line-height:1.35;">{cap2_text}</p></div>
    <div style="width:198pt;"><p class="mono" style="font-size:7pt;color:#FFFFFF;margin-bottom:3pt;">{cap3_label}</p><p style="font-size:9pt;color:#FFFFFF;line-height:1.35;">{cap3_text}</p></div>
  </div>
'''
    return h + TAIL

def layout_b32(num, header_text, headline_l1, headline_l2, img1, img2, cap1_label, cap1_text, cap2_label, cap2_text):
    h = HEAD.format(title=f'Slide {num}')
    h += header(num, header_text)
    h += f'''  <h1 style="position:absolute;top:64pt;left:48pt;right:48pt;font-size:24pt;font-weight:700;color:#FFFFFF;line-height:1.32;letter-spacing:-0.02em;">{headline_l1}<span style="color:#B0B0B0;">{headline_l2}</span></h1>
  <div style="position:absolute;left:48pt;right:48pt;top:130pt;display:flex;gap:14pt;justify-content:center;">
    <div class="panel-frame" style="width:300pt;height:200pt;"><img src="./assets/{img1}" alt=""></div>
    <div class="panel-frame" style="width:300pt;height:200pt;"><img src="./assets/{img2}" alt=""></div>
  </div>
  <div style="position:absolute;left:48pt;right:48pt;top:336pt;display:flex;gap:14pt;justify-content:center;">
    <div style="width:300pt;"><p class="mono" style="font-size:8pt;color:#707070;margin-bottom:4pt;">{cap1_label}</p><p style="font-size:10pt;color:#B0B0B0;line-height:1.4;">{cap1_text}</p></div>
    <div style="width:300pt;"><p class="mono" style="font-size:8pt;color:#FFFFFF;margin-bottom:4pt;">{cap2_label}</p><p style="font-size:10pt;color:#FFFFFF;line-height:1.4;">{cap2_text}</p></div>
  </div>
'''
    return h + TAIL

def layout_d(num, header_text, img, footer_text):
    h = HEAD.format(title=f'Slide {num}')
    h += header_minimal(num, header_text)
    h += f'''  <div style="position:absolute;top:36pt;left:48pt;right:48pt;bottom:34pt;display:flex;align-items:center;justify-content:center;">
    <img src="./assets/{img}" alt="" style="max-width:100%;max-height:100%;height:100%;width:auto;object-fit:contain;">
  </div>
  <p class="mono" style="position:absolute;bottom:14pt;left:48pt;right:48pt;text-align:center;font-size:8pt;color:#707070;">{footer_text}</p>
'''
    return h + TAIL

def layout_video(num, header_text, eyebrow, title_l1, title_l2, body, video_thumb, video_label, video_src, footer):
    """HTML5 video 임베드 — 16:9 프레임 + object-fit:contain (잘림 X). PDF에서는 poster 이미지로 표시."""
    h = HEAD.format(title=f'Slide {num}')
    h += header(num, header_text)
    h += f'''  <div style="position:absolute;left:48pt;top:88pt;width:290pt;">
    <p class="mono" style="font-size:9pt;color:#707070;margin-bottom:14pt;">{eyebrow}</p>
    <h1 style="font-size:30pt;font-weight:700;color:#FFFFFF;line-height:1.28;letter-spacing:-0.025em;">{title_l1}<br><span style="color:#B0B0B0;">{title_l2}</span></h1>
    <p style="font-size:12pt;color:#B0B0B0;margin-top:20pt;line-height:1.6;">{body}</p>
  </div>
  <video controls preload="metadata" poster="./assets/{video_thumb}" style="position:absolute;right:48pt;top:130pt;width:320pt;height:180pt;background:#1A1A1A;border:1pt solid #333;object-fit:contain;">
    <source src="./assets/{video_src}" type="video/mp4">
  </video>
  <p class="mono" style="position:absolute;bottom:24pt;right:48pt;font-size:8pt;color:#707070;">{video_label} · {footer}</p>
'''
    return h + TAIL

def layout_quote(num, header_text, eyebrow, q_l1, q_l2, q_l3, footer):
    h = HEAD.format(title=f'Slide {num}')
    h += header(num, header_text)
    extra_line = f'<br>{q_l3}' if q_l3 else ''
    h += f'''  <div style="position:absolute;left:48pt;right:48pt;top:50%;transform:translateY(-50%);">
    <p class="mono" style="font-size:9pt;color:#707070;margin-bottom:18pt;">{eyebrow}</p>
    <h1 style="font-size:42pt;font-weight:700;color:#FFFFFF;line-height:1.3;letter-spacing:-0.025em;max-width:640pt;">{q_l1}<br><span style="color:#B0B0B0;">{q_l2}</span>{extra_line}</h1>
  </div>
  <p class="mono" style="position:absolute;bottom:36pt;left:48pt;font-size:9pt;color:#707070;">{footer}</p>
'''
    return h + TAIL

def layout_divider(num, part_num, header_text, part_label, title, subtitle):
    h = HEAD.format(title=f'Slide {num}')
    h += header(num, header_text)
    h += f'''  <p style="position:absolute;right:48pt;top:50%;transform:translateY(-50%);font-size:240pt;font-weight:800;line-height:1.2;color:#1A1A1A;letter-spacing:-0.06em;">{part_num}</p>
  <div style="position:absolute;left:48pt;top:50%;transform:translateY(-50%);">
    <p class="mono" style="font-size:10pt;color:#707070;margin-bottom:18pt;">{part_label}</p>
    <h1 style="font-size:72pt;font-weight:700;color:#FFFFFF;line-height:1.2;letter-spacing:-0.03em;">{title}</h1>
    <p style="font-size:14pt;color:#B0B0B0;margin-top:20pt;line-height:1.5;">{subtitle}</p>
  </div>
'''
    return h + TAIL

# ============================================================
# 슬라이드 정의 (20-71) — 헤더에서 만화 ID 제거
# ============================================================

slides = {}

# Slide 20: Week 4 비교 빌드 영상 카드
slides[20] = layout_video(20, 'WEEK 04 · CHAPTER OPEN',
    'A BUILD WORTH COMPARING',
    '비교할 수 있는', '빌드.',
    '가장 큰 변경점 2가지 — UI · 핵심재미 연출.<br>다음은 3D 액션 게임 예정.',
    'video_4_thumb.jpg', '4번 영상_0405.MP4', 'v4.mp4',
    'WEEK 4 빌드 비교 영상')

# Slide 21~24: Week 4 만화 페어 (4-1-1, 4-2-1 모두 4컷 3:2)
slides[21] = layout_b32(21, 'WEEK 04 · 02 / 05',
    '캐릭터 모집·정보·인벤토리·제작 UI · ', '핵심 재미 연출.',
    'panels/4-1-1_p1.png', 'panels/4-1-1_p2.png',
    'UI', '캐릭터 모집·정보·사무실·인벤토리·제작',
    'FUN', '실시간 직관·개입·결과의 경험')

slides[22] = layout_b32(22, 'WEEK 04 · 03 / 05',
    'Claude 토큰 100% 소진. ', '"세상이 멈췄다."',
    'panels/4-1-1_p3.png', 'panels/4-1-1_p4.png',
    'TOKEN', 'UI 프리팹 제작 시키니 토큰 다 털림',
    'STOP', 'Codex는 23%, 초기화는 너무 멀다')

slides[23] = layout_b32(23, 'WEEK 04 · 04 / 05',
    'AI 쓰면 일 줄겠지? ', '프로토타입은 순식간에 완성.',
    'panels/4-2-1_p1.png', 'panels/4-2-1_p2.png',
    'ASSUMPTION', '"AI 쓰면 일이 줄겠지?"',
    'REALITY', 'AI 덕분에 순식간에 프로토타입 완성')

slides[24] = layout_b32(24, 'WEEK 04 · 05 / 05',
    '새 아이디어가 폭발한다. ', '"멈춤은 없었고 다음만 있었다."',
    'panels/4-2-1_p3.png', 'panels/4-2-1_p4.png',
    'IDEAS', '어? 이것도 되겠는데? 새 아이디어 폭발',
    'INSIGHT', 'AI는 일을 줄이는 것이 아니라 오히려 늘린다')

# Slide 25~28: Week 5 6-cut 만화 (5-6-1) — 1:1 패널이므로 B-1:1 사용
slides[25] = layout_c32(25, 'WEEK 05 · CHAPTER OPEN',
    'SUBSCRIPTION UPGRADE',
    'Pro → Max.', '"더 많은 다음을 위해."',
    '"이번주는 개발 진도보다 어셋 작업 환경 위주."<br>구독 업그레이드 결정.',
    'panels/5-6-1_p1.png',
    'WEEK 5 · OPENING')

slides[26] = layout_b11(26, 'WEEK 05 · 02 / 08',
    'Claude → Figma 환경 구축. ', '진짜 그려준다.',
    'panels/5-6-1_p2.png', 'panels/5-6-1_p3.png',
    'SETUP', 'API · 토큰 · MCP — "진짜 힘들었다"',
    'WORKING', '와우! 직접 하는 것보단 빠르고 편하다')

slides[27] = layout_b11(27, 'WEEK 05 · 03 / 08',
    'Claudecode가 시안 작성. ', '에디터 스크립트로 프리팹 제작.',
    'panels/5-6-1_p4.png', 'panels/5-6-1_p5.png',
    'DRAFT', '시안 → 유니티 에디터 스크립트 → 버튼 한 번',
    'NOTE', '아스키 시안 → 택1 → 피그마. 시간 낭비 NO!')

slides[28] = layout_c32(28, 'WEEK 05 · 04 / 08',
    'PRO → MAX DECISION',
    'Pro → Max.', '결국 더 많은 다음을 만들기 위한 선택.',
    '더 많은 가능성, 더 많은 시도, 더 많은 결과물.<br>그래서… Max로 갑니다.',
    'panels/5-6-1_p6.png',
    'WEEK 5 · DECISION')

# Slide 29~30: Week 5 5-7-1 페어 (4-cut 1:1)
slides[29] = layout_b11(29, 'WEEK 05 · 05 / 08',
    '퀄리티 UI 리뉴얼. ', '좌표 X, 수학적 분할.',
    'panels/5-7-1_p1.png', 'panels/5-7-1_p2.png',
    'BEFORE/AFTER', '퀄리티 떨어지던 UI를 리뉴얼',
    'ARCHITECTURE', '전체 영역을 잡고 수학적으로 분할')

slides[30] = layout_b11(30, 'WEEK 05 · 06 / 08',
    '간단한 offset 수정 불가능. ', '규격화 · 규격화 · 규격화.',
    'panels/5-7-1_p3.png', 'panels/5-7-1_p4.png',
    'LIMITATION', '"여기 10px만 옮기고 싶은데" — 안 됨',
    'CONCLUSION', 'AI 작업 결과의 유지보수 — 코드뿐 아니라 UI도 어렵다')

# Slide 31~32: Week 5 5-8-1 페어 (4-cut 1:1)
slides[31] = layout_b11(31, 'WEEK 05 · 07 / 08',
    '자체 Tool 제작. ', '만들고, 폐기하고, 다시.',
    'panels/5-8-1_p1.png', 'panels/5-8-1_p2.png',
    'TOOL', '콘텐츠 개발 효율을 위한 Tool 제작',
    'CYCLE', '아이디어 → 만들고 → 별로네 → 쓰레기통으로')

slides[32] = layout_b11(32, 'WEEK 05 · 08 / 08',
    '나만의 생산성 도구들. ', '효율 강박은 아직 무리.',
    'panels/5-8-1_p3.png', 'panels/5-8-1_p4.png',
    'TOOLBOX', '시도→폐기→개선을 빠르게 반복할 수 있다',
    'LIMIT', 'AI는 AI대로, 나는 다른 일 — 아직 무리')

# Slide 33~35: Week 6 6-1-1 6컷 페어 — 1:1 패널 → B-1:1
slides[33] = layout_b11(33, 'WEEK 06 · CHAPTER OPEN',
    '4명 에이전트 — 디렉터·아이템·전투·내러티브. ', '"서로 싸워라."',
    'panels/6-1-1_p1.png', 'panels/6-1-1_p2.png',
    'CAST', '디렉터 + 아이템 + 전투 + 내러티브 디자이너',
    'DEBATE', '"서로 싸워라. 디렉터 네가 잘 중재해줘"')

slides[34] = layout_b11(34, 'WEEK 06 · 02 / 12',
    'GPT vs Gemini 아트풍 충돌. ', 'Claude 병렬 처리.',
    'panels/6-1-1_p3.png', 'panels/6-1-1_p4.png',
    'ART STYLE', '동일 프롬프트인데 GPT와 Gemini 결과 차이 큼',
    'PARALLEL', 'Claude 병렬 에이전트로 빠르게 토큰 소모 → 다른 일')

slides[35] = layout_b11(35, 'WEEK 06 · 03 / 12',
    'Codex 시뮬레이터 구축 중. ', '엔드콘텐츠 개발.',
    'panels/6-1-1_p5.png', 'panels/6-1-1_p6.png',
    'SIMULATOR', 'Codex로 코드 리팩토링 + 로그 기반 밸런스 시뮬',
    'END CONTENT', '엔드콘텐츠 개발 중 — 이것까지면 빌드 얼추 완성')

# Slide 36: Week 6 영상 (클릭 재생)
slides[36] = layout_video(36, 'WEEK 06 · BUILD VIDEO',
    'BUILD IN PROGRESS',
    'Week 6 빌드.', '오케스트라가 만든 변화.',
    '4명 에이전트 + Codex 시뮬레이터로<br>완성된 빌드의 모습.',
    'video_6_thumb.jpg', '6번 영상.MP4', 'v6.mp4',
    'WEEK 6 빌드 영상')

# Slide 37~38: Week 6 6-2-1 페어 (4-cut 1:1)
slides[37] = layout_b11(37, 'WEEK 06 · 05 / 12',
    'Claude는 다 한다. ', '단, 편집 단가가 비싸다.',
    'panels/6-2-1_p1.png', 'panels/6-2-1_p2.png',
    'SWISS-ARMY', '영상·디자인·문서·코드까지 — 다 한다',
    'COST', '편집할 때마다 자연어 입력 → 토큰 소모 → 비효율')

slides[38] = layout_b11(38, 'WEEK 06 · 06 / 12',
    '왜 비효율일까? ', '자동화·규격화 후 찍어내야.',
    'panels/6-2-1_p3.png', 'panels/6-2-1_p4.png',
    'WHY', '편집 → 토큰 소모 → 시간 → 비용 — 반복',
    'SOLUTION', '자동화 + 규격화 = 효율적인 Claude 활용법')

# Slide 39~40: Week 6 6-3-1 페어 (4-cut 3:2)
slides[39] = layout_b32(39, 'WEEK 06 · 07 / 12',
    'AI 결과의 한계. ', '70→85점은 가파르다.',
    'panels/6-3-1_p1.png', 'panels/6-3-1_p2.png',
    'LIMIT', 'AI 결과는 어차피 내 기준에 못 미친다',
    'CURVE', '70점까진 빠르게, 75·80·85점은 정말 힘들다')

slides[40] = layout_b32(40, 'WEEK 06 · 08 / 12',
    '여러 업무 동시 컨펌. ', '결국 도메인 + 멀티태스킹.',
    'panels/6-3-1_p3.png', 'panels/6-3-1_p4.png',
    'MULTITASKING', '피드백·전달·우선순위 정리 — 여러 업무 동시 컨펌',
    'FORMULA', 'AI + 나의 역량 = 최고의 결과물')

# Slide 41~44: Week 6 6-4-1 풀 분할 (핵심, 4-cut 3:2)
slides[41] = layout_c32(41, 'WEEK 06 · 09 / 12',
    'PHASE 01 · OPTIMIZATION',
    '처음엔 토큰 효율화로,', '최대한 퍼포먼스를 올리는 방향.',
    '프로세스 압축, 불필요한 출력 제거,<br>컨텍스트 정리, 반복 작업 자동화 — 퍼포먼스 UP!',
    'panels/6-4-1_p1.png',
    'WEEK 6 RECAP · PHASE 01')

slides[42] = layout_c32(42, 'WEEK 06 · 10 / 12',
    'PHASE 02 · CEILING',
    '그런데 한계가 있었다.', '더 이상 퍼포먼스가 안 올라간다.',
    '퍼포먼스 그래프 — 정체.<br>"한계인가 보네…"',
    'panels/6-4-1_p2.png',
    'WEEK 6 RECAP · PHASE 02')

slides[43] = layout_c32(43, 'WEEK 06 · 11 / 12',
    'PHASE 03 · STAGNATION',
    '구조를 깎고 다듬어도', '원하는 선까지 안 올라간다.',
    '구조 개선 ✗ 안 올라감.<br>프로세스 다듬기 ✗ 안 올라감.<br>퀄리티 업 ✗ 안 올라감.',
    'panels/6-4-1_p3.png',
    'WEEK 6 RECAP · PHASE 03')

slides[44] = layout_c32(44, 'WEEK 06 · 12 / 12',
    'PHASE 04 · REVELATION',
    '결국 막대한 토큰을', '쏟아부어야 아웃풋이 나온다.',
    '아아… 젠슨 황이시여… 이제야 깨닫습니다.<br><strong style="color:#FFFFFF;">"사람이! 비루한 토큰이! 병목이구나!"</strong>',
    'panels/6-4-1_p4.png',
    'WEEK 6 KEY INSIGHT')

# Slide 45~46: Week 7 7-1-1 페어 (4-cut 3:2)
slides[45] = layout_b32(45, 'WEEK 07 · CHAPTER OPEN',
    '레이드 — 12인 보스 도전. ', '밸런스 시뮬레이터.',
    'panels/7-1-1_p1.png', 'panels/7-1-1_p2.png',
    'RAID', 'Wave 7 클리어! 도달 wave까지 보상 획득',
    'SIMULATOR', '시뮬레이터로 명확한 형태 지시 — 더 잘됨')

slides[46] = layout_b32(46, 'WEEK 07 · 02 / 11',
    '컨디션·입장 가능 처리. ', '캐릭터 정보창 리뉴얼.',
    'panels/7-1-1_p3.png', 'panels/7-1-1_p4.png',
    'ENTRY', '계정 레벨 등 컨디션 → 입장 가능 처리',
    'UI POLISH', '캐릭터 정보창 — Before / After (리뉴얼)')

# Slide 47~48: Week 7 7-2-1 페어 (4-cut 3:2)
slides[47] = layout_b32(47, 'WEEK 07 · 03 / 11',
    '액션의 3요소 — Animation·Effect·Sound. ', '구색 갖춤.',
    'panels/7-2-1_p1.png', 'panels/7-2-1_p2.png',
    'ACTION', '이펙트 시스템·리소스 적용 → CRITICAL!',
    'SOUND', '효과음·스킬·피격·보상 획득 — 몰입감 UP!')

slides[48] = layout_b32(48, 'WEEK 07 · 04 / 11',
    '액션 3요소 — 구색 갖춤. ', '태그 이전 시스템.',
    'panels/7-2-1_p3.png', 'panels/7-2-1_p4.png',
    'TRIAD', 'Ani · Effect · Sound — 구색 갖췄다',
    'TAG MIGRATION', '태그를 다른 캐릭터에 옮길 수 있다')

# Slide 49~50: Week 7 7-3-1 페어 (4-cut 3:2)
slides[49] = layout_b32(49, 'WEEK 07 · 05 / 11',
    '콘텐츠 루프 완성. ', '재료→재능→상위→레이드→다시.',
    'panels/7-3-1_p1.png', 'panels/7-3-1_p2.png',
    'LOOP DONE', '드디어 루프 완성! 콘텐츠 흐름 완성',
    '5-STEP', '재료 → 재능 → 상위 지역 → 레이드 → 다시 재료')

slides[50] = layout_b32(50, 'WEEK 07 · 06 / 11',
    '이후는? ', '연출·UI/UX·데이터 폴리싱 — 끝없다.',
    'panels/7-3-1_p3.png', 'panels/7-3-1_p4.png',
    'TODO LIST', '연출 다듬기, UI/UX 개선, 데이터 폴리싱',
    'ENDLESS', '"끝없는 개선의 길" — 우리 팀내서 완성하자!')

# Slide 51: Week 7 영상 (클릭 재생)
slides[51] = layout_video(51, 'WEEK 07 · BUILD VIDEO',
    'CONTENT LOOP COMPLETE',
    'Week 7 빌드.', '레이드와 콘텐츠 루프.',
    '12인 캐릭터 레이드 + 액션 3요소<br>+ 콘텐츠 흐름 완성된 빌드.',
    'video_7_thumb.jpg', '7번 영상.MP4', 'v7.mp4',
    'WEEK 7 빌드 영상')

# Slide 52~55: Week 7 7-4-1 풀 분할 (핵심, 4-cut 3:2)
slides[52] = layout_c32(52, 'WEEK 07 · 08 / 11',
    'PHASE 01 · DISAPPOINTMENT',
    'Claude 사용경험이', '점점 아쉽다.',
    'AI 의존적 개발 → AI 개발사 라이브 업데이트에<br>퀄리티·경험이 좌우된다.',
    'panels/7-4-1_p1.png',
    'WEEK 7 RECAP · PHASE 01')

slides[53] = layout_c32(53, 'WEEK 07 · 09 / 11',
    'PHASE 02 · COMPETITION',
    'Codex 업데이트로', '사용경험이 좋아졌다.',
    'Claude Code 아쉬움 → Codex 약진.<br>"두 회사가 중간에 퍼지지 말고 완주 잘 했으면."',
    'panels/7-4-1_p2.png',
    'WEEK 7 RECAP · PHASE 02')

slides[54] = layout_c32(54, 'WEEK 07 · 10 / 11',
    'PHASE 03 · OLD WAY',
    '게임쟁이는', '게임으로 말한다.',
    '평소의 꼰대정신 — 결과물로 증명한다.<br>그러나 규모 있는 게임은 오래 걸린다.',
    'panels/7-4-1_p3.png',
    'WEEK 7 RECAP · PHASE 03')

slides[55] = layout_c32(55, 'WEEK 07 · 11 / 11',
    'PHASE 04 · NEW ERA',
    '결과로 증명하던 기획자의 역량을,', 'AI로 보여줄 수 있는 시대가 왔다.',
    '아이디어 + 실행력 + AI = 결과.<br>기존 시대와 AI 시대 — 완전히 다른 게임.',
    'panels/7-4-1_p4.png',
    'WEEK 7 KEY INSIGHT')

# Slide 56~57: Week 8 8-3-1 페어 (4-cut 3:2)
slides[56] = layout_b32(56, 'WEEK 08 · CHAPTER OPEN',
    '리팩토링 + 밸런스 + 버그 수정. ', '리팩토링은 Codex가 잘함.',
    'panels/8-3-1_p1.png', 'panels/8-3-1_p2.png',
    'WORK', '코드 리팩토링 · 밸런스 조정 · 버그 수정 — 정리의 한 주',
    'CODEX', 'Before / After — Codex가 잘해줌')

slides[57] = layout_b32(57, 'WEEK 08 · 02 / 04',
    '"넌 시키는대로만 해!" ', '판단은 인간, 처리는 AI.',
    'panels/8-3-1_p3.png', 'panels/8-3-1_p4.png',
    'TRIAL/ERROR', '판단 통째로 시키니 안됨 — "내가 너무 뇌 빼고 했네"',
    'WORKING', '내가 판단 / AI가 처리 — 그제서야 값이 맞기 시작')

# Slide 58~59: Week 8 8-4-1 페어 (4-cut 3:2)
slides[58] = layout_b32(58, 'WEEK 08 · 03 / 04',
    '라이브 서비스의 그림자. ', 'AI 의존을 자각하다.',
    'panels/8-4-1_p1.png', 'panels/8-4-1_p2.png',
    'COMPLEX', '라이브 서비스의 모든 요소를 점수화 → AI를 갈군다',
    'DEPENDENCE', '판단마저 AI에 맡겨버리는 나를 경험 — 지식 없으면 끌려간다')

slides[59] = layout_b32(59, 'WEEK 08 · 04 / 04',
    '테이블 작업도 AI에. ', '"AI는 도구, 나는 설계자."',
    'panels/8-4-1_p3.png', 'panels/8-4-1_p4.png',
    'TABLES', '캐릭터·스킬·몬스터 테이블 — 토큰 한 번이면 끝',
    'MINDSET', '판단은 내가 / 시스템과 프로세스도 내가 — AI는 도구!')

# Slide 60: PART 2 Divider
slides[60] = layout_divider(60, '02', 'SECTION DIVIDER',
    'PART TWO', '5가지 인사이트.', '도구 너머의 발견.')

# Slide 61: Insight 1 — 도메인
slides[61] = layout_quote(61, 'PART 2 · INSIGHT 01 — DOMAIN',
    'INSIGHT 01',
    '도메인 지식이', '우위다.', '',
    'AI 시대일수록 업의 근본이 결과물 퀄리티를 결정한다')

# Slide 62: Insight 2 — 70/80 (Layout D 풀-블리드)
slides[62] = layout_d(62, 'PART 2 · INSIGHT 02 — 70/80 CURVE',
    'token-consumption.png',
    '70점은 빠르고, 80점은 가파르다 — AI 결과물의 품질과 비용의 비대칭 구조')

# Slide 63: Insight 3 — 판단 vs 처리
slides[63] = layout_quote(63, 'PART 2 · INSIGHT 03 — JUDGMENT',
    'INSIGHT 03',
    '판단은 인간,', '처리는 AI.', '',
    '판단을 AI에 맡기면 값이 안 맞는다 — "넌 시키는대로만 해"')

# Slide 64: Insight 4 — 병목
slides[64] = layout_quote(64, 'PART 2 · INSIGHT 04 — BOTTLENECK',
    'INSIGHT 04',
    '사람과 토큰이', '병목이다.', '',
    '"사람이! 비루한 토큰이! 병목이구나!"')

# Slide 65: Insight 5 — 다음만 있다
slides[65] = layout_quote(65, 'PART 2 · INSIGHT 05 — ENDLESS',
    'INSIGHT 05',
    'AI는 일을', '줄이지 않는다.', '',
    '"멈춤은 없었고, 다음만 있었다."')

# Slide 66: PART 3 Divider
slides[66] = layout_divider(66, '03', 'SECTION DIVIDER',
    'PART THREE', '결과물.', '8주가 남긴 것.')

# Slide 67: Project H 구조도 — Structure.png로 교체
slides[67] = layout_d(67, 'PART 3 · PROJECT H — STRUCTURE MAP',
    'ProjectH_Structure.png',
    'PROJECT H — 코드 · 데이터 · UI · 문서의 4축 시스템 맵')

# Slide 68: 빌드 영상 갤러리 — Final 영상은 정사이즈, 4개 기록 썸네일은 작게
slides[68] = HEAD.format(title='Slide 68') + header(68, 'PART 3 · BUILD VIDEO GALLERY')
slides[68] += '''  <h1 style="position:absolute;top:64pt;left:48pt;right:48pt;font-size:22pt;font-weight:700;color:#FFFFFF;line-height:1.32;letter-spacing:-0.02em;">빌드의 발전 과정. <span style="color:#B0B0B0;">최종 빌드 + 4편의 기록.</span></h1>

  <!-- 좌측: 4개 작은 썸네일 (2x2 그리드, 기록 용도) -->
  <div style="position:absolute;left:48pt;top:122pt;width:240pt;display:grid;grid-template-columns:1fr 1fr;gap:6pt;">
'''
for vthumb, vlabel in [
    ('video_3_thumb.jpg','3번 · 0311'),
    ('video_4_thumb.jpg','4번 · 0405'),
    ('video_6_thumb.jpg','6번 빌드'),
    ('video_7_thumb.jpg','7번 빌드'),
]:
    slides[68] += f'''    <div style="background:#1A1A1A;border:1pt solid #333;height:84pt;position:relative;overflow:hidden;">
      <img src="./assets/{vthumb}" alt="" style="width:100%;height:100%;object-fit:cover;filter:brightness(0.85);">
      <p class="mono" style="position:absolute;bottom:4pt;left:6pt;font-size:6.5pt;color:#FFFFFF;text-shadow:0 1pt 2pt rgba(0,0,0,0.8);">{vlabel}</p>
    </div>
'''
slides[68] += '''  </div>
  <p class="mono" style="position:absolute;left:48pt;top:300pt;width:240pt;font-size:7pt;color:#707070;">RECORD · 4편의 빌드 진화 (썸네일만)</p>

  <!-- 우측: Final 영상 (큰 사이즈, 인라인 재생 가능) -->
  <video controls preload="metadata" poster="./assets/video_final_thumb.jpg" style="position:absolute;right:48pt;top:122pt;width:336pt;height:189pt;background:#1A1A1A;border:1pt solid #333;object-fit:contain;">
    <source src="./assets/vfinal.mp4" type="video/mp4">
  </video>
  <p class="mono" style="position:absolute;right:48pt;top:316pt;width:336pt;font-size:8pt;color:#FFFFFF;">FINAL BUILD · PROJECT-H-FINAL.MP4</p>
  <p style="position:absolute;right:48pt;top:332pt;width:336pt;font-size:11pt;color:#B0B0B0;line-height:1.5;">8주차 최종 빌드. ▶ 버튼 클릭 시 슬라이드 안에서 재생.</p>

  <p class="mono" style="position:absolute;bottom:24pt;left:48pt;right:48pt;text-align:center;font-size:8pt;color:#707070;">3번 → 4번 → 6번 → 7번 → FINAL · 8주의 시각 기록</p>
''' + TAIL

# Slide 69: AI 스택
slides[69] = HEAD.format(title='Slide 69') + header(69, 'PART 3 · AI STACK CATALOG')
slides[69] += '''  <h1 style="position:absolute;top:64pt;left:48pt;right:48pt;font-size:26pt;font-weight:700;color:#FFFFFF;line-height:1.3;letter-spacing:-0.02em;">8주간 동원한 AI 도구. <span style="color:#B0B0B0;">7개 카테고리.</span></h1>
  <div style="position:absolute;left:48pt;right:48pt;top:130pt;display:grid;grid-template-columns:1fr 1fr;gap:8pt;">
    <div style="background:#1A1A1A;border:1pt solid #333;padding:14pt 18pt;">
      <p class="mono" style="font-size:8pt;color:#707070;margin-bottom:6pt;">코드</p>
      <p style="font-size:13pt;color:#FFFFFF;font-weight:500;line-height:1.45;">Codex (CLI) · ClaudeCode (Pro→Max) · Opus</p>
    </div>
    <div style="background:#1A1A1A;border:1pt solid #333;padding:14pt 18pt;">
      <p class="mono" style="font-size:8pt;color:#707070;margin-bottom:6pt;">티케팅·기획</p>
      <p style="font-size:13pt;color:#FFFFFF;font-weight:500;line-height:1.45;">GPT</p>
    </div>
    <div style="background:#1A1A1A;border:1pt solid #333;padding:14pt 18pt;">
      <p class="mono" style="font-size:8pt;color:#707070;margin-bottom:6pt;">아트</p>
      <p style="font-size:13pt;color:#FFFFFF;font-weight:500;line-height:1.45;">GPT · Gemini · Varco · Meshy · Tripo</p>
    </div>
    <div style="background:#1A1A1A;border:1pt solid #333;padding:14pt 18pt;">
      <p class="mono" style="font-size:8pt;color:#707070;margin-bottom:6pt;">사운드 · UI</p>
      <p style="font-size:13pt;color:#FFFFFF;font-weight:500;line-height:1.45;">Suno (BGM) · Claude → Figma 파이프라인</p>
    </div>
    <div style="background:#1A1A1A;border:1pt solid #333;padding:14pt 18pt;grid-column:span 2;">
      <p class="mono" style="font-size:8pt;color:#707070;margin-bottom:6pt;">스킬·세팅 보조</p>
      <p style="font-size:13pt;color:#B0B0B0;font-weight:400;line-height:1.45;">Claude 스킬 — web-design-guidelines · vercel-react-best-practices · frontend-design</p>
    </div>
  </div>
  <p class="mono" style="position:absolute;bottom:32pt;left:48pt;right:48pt;font-size:8pt;color:#707070;">포기한 도구: 유니티 MCP (토큰 부담) · ComfyUI (GPU 한계)</p>
''' + TAIL

# Slide 70: Closing
slides[70] = HEAD.format(title='Slide 70') + header(70, 'CLOSING')
slides[70] += '''  <div style="position:absolute;left:48pt;right:48pt;top:50%;transform:translateY(-50%);">
    <p class="mono" style="font-size:9pt;color:#707070;margin-bottom:18pt;">REFLECTION</p>
    <h1 style="font-size:38pt;font-weight:700;color:#FFFFFF;line-height:1.3;letter-spacing:-0.025em;max-width:640pt;">결과로 증명해온 기획자의 역량,<br><span style="color:#B0B0B0;">AI 네이티브 시대에 가장 빛난다.</span></h1>
  </div>
  <p class="mono" style="position:absolute;bottom:36pt;left:48pt;font-size:9pt;color:#707070;">유 병 휘 · 2026 · W01—W08</p>
  <p class="mono" style="position:absolute;bottom:36pt;right:48pt;font-size:9pt;color:#707070;">CONTINUE →</p>
''' + TAIL

# Slide 71: 다음 프로젝트 준비중 — 마스터 시트 크게, 스트립 작게
slides[71] = HEAD.format(title='Slide 71') + header(71, 'NEXT PROJECT · IN PROGRESS')
slides[71] += '''  <!-- 우측 상단: 타이틀 (compact) -->
  <div style="position:absolute;left:230pt;top:64pt;right:48pt;height:120pt;">
    <p class="mono" style="font-size:9pt;color:#707070;margin-bottom:10pt;">NEXT VOYAGE</p>
    <h1 style="font-size:22pt;font-weight:700;color:#FFFFFF;line-height:1.3;letter-spacing:-0.02em;">다음 프로젝트 준비중.</h1>
    <p style="font-size:11pt;color:#B0B0B0;margin-top:10pt;line-height:1.55;">GPT로 규격화된 이미지를 만들고<br>스프라이트 제작을 시도하는 중.</p>
  </div>

  <!-- 좌측: 마스터 시트 (커진 사이즈, 슬라이드 거의 풀 높이) -->
  <div style="position:absolute;left:48pt;top:64pt;bottom:30pt;width:170pt;background:#1A1A1A;border:1pt solid #333;display:flex;align-items:center;justify-content:center;overflow:hidden;">
    <img src="./assets/seri_master_sheet.png" alt="" style="max-width:100%;max-height:100%;width:auto;height:100%;object-fit:contain;">
  </div>
  <p class="mono" style="position:absolute;left:48pt;bottom:14pt;width:170pt;font-size:7pt;color:#707070;text-align:center;">MASTER SHEET · 이세리 (DPS)</p>

  <!-- 우측 하단: 3개 애니메이션 스트립 stacked (작아짐) -->
  <div style="position:absolute;left:230pt;right:48pt;top:200pt;bottom:30pt;display:flex;flex-direction:column;gap:5pt;">
    <div style="background:#1A1A1A;border:1pt solid #333;padding:4pt 10pt;height:50pt;display:flex;flex-direction:column;overflow:hidden;">
      <p class="mono" style="font-size:6pt;color:#707070;margin-bottom:1pt;">JUMP · 4 FRAMES</p>
      <div style="flex:1;display:flex;align-items:center;justify-content:center;overflow:hidden;">
        <img src="./assets/seri_jump_4x1_transparent.png" alt="" style="max-width:100%;max-height:100%;width:auto;height:100%;object-fit:contain;">
      </div>
    </div>
    <div style="background:#1A1A1A;border:1pt solid #333;padding:4pt 10pt;height:50pt;display:flex;flex-direction:column;overflow:hidden;">
      <p class="mono" style="font-size:6pt;color:#707070;margin-bottom:1pt;">RUN · 6 FRAMES</p>
      <div style="flex:1;display:flex;align-items:center;justify-content:center;overflow:hidden;">
        <img src="./assets/seri_run_6x1_transparent.png" alt="" style="max-width:100%;max-height:100%;width:auto;height:100%;object-fit:contain;">
      </div>
    </div>
    <div style="background:#1A1A1A;border:1pt solid #333;padding:4pt 10pt;height:50pt;display:flex;flex-direction:column;overflow:hidden;">
      <p class="mono" style="font-size:6pt;color:#707070;margin-bottom:1pt;">ATTACK · 6 FRAMES</p>
      <div style="flex:1;display:flex;align-items:center;justify-content:center;overflow:hidden;">
        <img src="./assets/seri_attack_thrust_6x1_transparent.png" alt="" style="max-width:100%;max-height:100%;width:auto;height:100%;object-fit:contain;">
      </div>
    </div>
  </div>

  <p class="mono" style="position:absolute;right:48pt;bottom:14pt;font-size:7pt;color:#707070;">— DRAFT v2 —</p>
''' + TAIL

# Slide 72: 감사합니다 (NEW) — LinkedIn 참고 이미지 우측 배치
slides[72] = HEAD.format(title='Slide 72') + header(72, 'THANK YOU')
slides[72] += '''  <!-- 좌측: 감사합니다 + 컨택트 -->
  <div style="position:absolute;left:48pt;right:280pt;top:50%;transform:translateY(-50%);">
    <p class="mono" style="font-size:9pt;color:#707070;margin-bottom:18pt;">CLOSING</p>
    <h1 style="font-size:74pt;font-weight:700;color:#FFFFFF;line-height:1.25;letter-spacing:-0.03em;">감사합니다.</h1>
    <div style="margin-top:28pt;">
      <p class="mono" style="font-size:8pt;color:#707070;margin-bottom:6pt;">WRITTEN BY</p>
      <p style="font-size:18pt;font-weight:600;color:#FFFFFF;margin-bottom:14pt;">유 병 휘</p>
      <p class="mono" style="font-size:8pt;color:#707070;margin-bottom:6pt;">EMAIL</p>
      <p class="mono" style="font-size:14pt;font-weight:500;color:#FFFFFF;">uu_sara@naver.com</p>
    </div>
  </div>

  <!-- 우측: LinkedIn 참고 이미지 (포트레이트) -->
  <div style="position:absolute;right:48pt;top:64pt;bottom:30pt;width:200pt;background:#1A1A1A;border:1pt solid #333;display:flex;align-items:center;justify-content:center;overflow:hidden;">
    <img src="./assets/linkedin.png" alt="" style="width:100%;height:100%;object-fit:contain;">
  </div>
  <p class="mono" style="position:absolute;right:48pt;bottom:14pt;width:200pt;font-size:7pt;color:#707070;text-align:center;">LINKEDIN · #OPENTOWORK · PD·시니어 기획</p>

  <p class="mono" style="position:absolute;bottom:36pt;left:48pt;font-size:9pt;color:#707070;">2026 · W01—W08</p>
''' + TAIL

# ============================================================
# 신규 추가 슬라이드 (스크린샷 활용 - 실증 슬라이드 3장)
# ============================================================

# Slide A: Week 5 결과물 — 실제 게임 UI (현재 28 다음 → 새 29)
slides[28.5] = layout_b3(29, 'WEEK 05 · GAME UI · IN-GAME RESULT',
    'Claude → Figma 워크플로의 ', '결과물 — 실제 게임 UI.',
    '5-1-1.jpg', '5-2-1.jpg', '5-3-1.jpg',
    'MAIN', '"인력소장은 살고싶다" 메인 — 7명 캐릭터 + 현장 파견',
    'RECRUIT', '모집 화면 — 6명 캐릭터 카드 (DPS·SUPPORT·TANK)',
    'DEPLOY', '시흥 사거리 — 4/4명 용병 선택 + 장비 슬롯')

# Slide B: Week 5 자체 Tool 실제 화면 (현재 32 다음 → 새 34)
slides[32.5] = layout_b32(34, 'WEEK 05 · CUSTOM TOOLS · IN-PROGRESS',
    '자체 Tool 2종. ', '만들고 폐기하고 다듬고.',
    '5-4-1.jpg', '5-5-1.jpg',
    'TOOL 01 · 프롬프트 스튜디오', 'Project H — 캐릭터·스킬 prompt 생성기. 슬롯·장비·스킬 선택→GPT 프롬프트 자동 빌드',
    'TOOL 02 · ASSET PROCESSOR', 'GPT 이미지 → 게임 리소스 변환. 배경 제거·리사이징·멀티 해상도 일괄')

# Slide C: Week 8 밸런스 작업 환경 (현재 56 다음 → 새 59)
slides[56.5] = layout_b32(59, 'WEEK 08 · BALANCE WORK · IN-PROGRESS',
    '밸런스 시행착오의 ', '실제 화면.',
    '8-1-1.jpg', '8-2-1.jpg',
    'MATRIX', '시나리오 매트릭스 — 케이스 × 지역 × 목표 wave 정의',
    'SIMULATOR', '자체 밸런스 시뮬레이터 + Telemetry Batch Runner — wave별 검증')

# ============================================================
# 자동 재번호: 키 정렬 → 20부터 순차 번호 부여 + HTML 내 P. NN 갱신
# ============================================================
import re
sorted_keys = sorted(slides.keys())
final_html = {}
for new_num, old_key in enumerate(sorted_keys, start=20):
    html = slides[old_key]
    # 페이지 번호 P. NN을 새 번호로 교체
    html = re.sub(r'(P\.\s*)\d+', lambda m: f'{m.group(1)}{new_num:02d}', html)
    final_html[new_num] = html

# Write all
for n, html in final_html.items():
    with open(os.path.join(OUT, f'slide-{n:02d}.html'), 'w', encoding='utf-8') as f:
        f.write(html)
print(f'Total: {len(final_html)} slides (20~{20+len(final_html)-1})')
