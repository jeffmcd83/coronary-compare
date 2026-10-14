# ROLLBACK — Coronary Products and Accessories guide

Current known-good live state is tagged **`stable`** (also `stable-2026-10-14`). List tags: `git tag -l`.

Tags named `live-…` point at **gh-pages** commits (exactly what was live):
```bash
cd /workspace/coronary-specs
git fetch origin --tags
git push -f origin live-stable^{commit}:refs/heads/gh-pages      # or live-pre-hardening-2026-10-14, etc.
```
Then fix `site/` on master (e.g. `git checkout stable -- site && git commit -m "Rollback site"`) so the next publish doesn't re-push the bad build. Version tags (`v1.x`, `preview-passNN`) are master commits; to go live from one: `git subtree split --prefix site <tag> -b rb && git push -f origin rb:gh-pages && git branch -D rb`.

Verify: open https://jeffmcd83.github.io/coronary-compare/ (refresh once), check the version/pass label in the header.
