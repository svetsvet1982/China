#!/bin/bash
# usage: tools/finish_jt.sh <file> "<commit msg>"
set -e
cd /home/user/China
n=$(awk '/^## 대화문/{on=1} /^## 낭독/{on=0} on && /^[^#|(-].*：/' "$1" | wc -l)
echo "turns: $n"
python3 tools/toc_jt.py
git add -A
git commit -q -m "$2

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01CehbhUyqNgfNi5xbcCibZE"
for i in 1 2 3 4; do git push -q -u origin claude/eloquent-babbage-uprqzv && break || sleep $((i*2)); done
echo pushed
