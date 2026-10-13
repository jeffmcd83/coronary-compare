#!/bin/bash
# usage: release.sh TAG  — copy current site/preview build to site/ root (live)
set -e; cd /workspace/coronary-specs; T=$1
rm -rf site/data site/index.html site/sw.js site/favicon.svg
cp -r site/preview/data site/preview/index.html site/preview/sw.js site/preview/favicon.svg site/
sed -i "s/const P='cor-preview-',C=P+'\([0-9a-f]*\)'/const P='cor-live-',C=P+'\1-$T'/" site/sw.js
sed -i "s/'Preview · pass '/'$T · pass '/" site/index.html
