#!/bin/bash
# usage: publish.sh NN
set -e; cd /workspace/coronary-specs; P=$1
python3 build_master.py >/dev/null; sed -i "s/'pass':'[0-9a-z]*'/'pass':'$P'/" app/build.py; python3 app/build.py
git add -A; git commit -qm "Pass $P"; git tag preview-pass$P; git push -q origin master preview-pass$P
git subtree split --prefix site -b g2 -q; git push -q -f origin g2:gh-pages; git branch -D g2 -q
for i in $(seq 1 50); do curl -s "https://jeffmcd83.github.io/coronary-compare/preview/data/core.json?x=$RANDOM" | grep -q "\"pass\":\"$P\"" && echo live && break; sleep 10; done
python3 /tmp/tl.py https://jeffmcd83.github.io/coronary-compare/preview/ pass$P
python3 fill.py
