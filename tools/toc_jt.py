import os, re
D = "解题人/대화문"
PARTS = {"1": "1부 破题 (민간기업 컨설팅) · 2021.7~2022.12", "2": "2부 掌舵 (제조기업 CEO·CFO) · 2023.3~2024.12",
         "3": "3부 照账 (독립 경영감사) · 2025.1~2025.12", "4": "4부 献策 (정책 자문 싱크탱크) · 2026.1~2026.11"}
files = sorted(f for f in os.listdir(D) if re.match(r"\d-\d\d_", f))
L = ["# 《解题人》 표준중국어 연속 대화문", "",
     "베이징의 로컬 경영컨설팅사에서 출발한 컨설턴트 린즈위안(林知远)과 동료들의 2021~2026년. 4부 × 14화, 화당 120턴.", "",
     "- 기획서: [解题人_기획서.md](解题人_기획서.md) · [엑셀판](解题人_기획서.xlsx)",
     "- 집필 메모: [대화문/_연속성_메모.md](대화문/_연속성_메모.md)",
     "- 각 화 구성: 대화문(120턴) → 낭독 포인트 → 어휘·표현 분석 → 한글 해석", ""]
cur = None
for f in files:
    p = f[0]
    if p != cur:
        L += ["", f"## {PARTS[p]}", ""]; cur = p
    first = open(os.path.join(D, f), encoding="utf-8").readline().strip().lstrip("# ").replace("　", " ", 1)
    L.append(f"- [{first}](대화문/{f})")
L.append(f"\n작성 완료: {len(files)} / 56화")
open("解题人/README.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
