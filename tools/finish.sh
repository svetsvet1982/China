#!/bin/bash
# usage: tools/finish.sh <episode_no> <file>
set -e
cd /home/user/China
n=$(awk '/^## 대화문/{on=1} /^## 낭독/{on=0} on && /^[^#|(-].*：/' "$2" | wc -l)
echo "turns: $n"
python3 tools/make_plan.py "槐荫胡同十七号_기획서.xlsx" "$1" >/dev/null
git add -A
git commit -q -m "제${1}화 초고 추가

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01CehbhVxQKqRTvPGdDEme5a"
for i in 1 2 3 4; do git push -q origin claude/elegant-gauss-3n9lnl && break || sleep $((i*2)); done
echo pushed
