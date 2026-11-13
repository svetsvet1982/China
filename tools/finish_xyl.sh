#!/bin/bash
# 《向阳里驿站》 한 화 마무리: 턴 수 검증 → 기획서 상태 갱신 → 커밋 → 푸시
# usage: tools/finish_xyl.sh <episode_no> <file>
set -e
cd /home/user/China
f="$2"
n=$(awk '/^## 대화문/{on=1} /^## 낭독/{on=0} on && /^[^#|(-].*：/' "$f" | wc -l)
k=$(awk '/^## 한글 해석/{on=1} on && /^[^#|(-].*: /' "$f" | wc -l)
echo "turns: $n / korean: $k"
if [ "$n" != 120 ] || [ "$k" != 120 ]; then echo "턴 수 불일치 — 커밋 중단"; exit 1; fi
python3 tools/make_plan_xiangyangli.py 向阳里驿站 "$1" >/dev/null
git add -A
git commit -q -m "《向阳里驿站》 제${1}화 초고 추가

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01CehbhWiWvsPt3rNcgiUj3D"
for i in 1 2 3 4; do git push -q -u origin claude/eloquent-edison-1n1zfb && break || sleep $((i*2)); done
echo pushed
