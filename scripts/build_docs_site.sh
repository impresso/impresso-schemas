#!/usr/bin/env bash
# Convert the Markdown produced by `make documentation` into a static HTML
# site suitable for publishing to GitHub Pages. Run this after
# `make documentation` has (re)generated docs/legacy/ and docs/impresso-2/.
#
# Usage: scripts/build_docs_site.sh <site-output-dir>

set -euo pipefail

SITE_DIR="${1:?Usage: scripts/build_docs_site.sh <site-output-dir>}"

if ! command -v pandoc >/dev/null 2>&1; then
  echo "ERROR: pandoc not found. Install it, e.g. 'apt-get install pandoc' or 'brew install pandoc'." >&2
  exit 1
fi

if [ ! -d docs ]; then
  echo "ERROR: docs/ not found. Run 'make documentation' first." >&2
  exit 1
fi

rm -rf "$SITE_DIR"
mkdir -p "$SITE_DIR"

# Convert every generated Markdown file to HTML, preserving the docs/
# directory structure, and rewrite intra-doc .md links to .html so they
# resolve once served as static pages.
while IFS= read -r -d '' md_file; do
  rel_path="${md_file#docs/}"
  out_file="$SITE_DIR/${rel_path%.md}.html"
  mkdir -p "$(dirname "$out_file")"
  title="$(basename "${rel_path%.md}")"
  sed -E 's/\(([^) "]+)\.md((#[^) "]*)?( "[^"]*")?)\)/(\1.html\2)/g' "$md_file" \
    | pandoc -f gfm -t html5 --standalone --metadata "title=$title" -o "$out_file"
done < <(find docs -name '*.md' -print0)

# Build a top-level index linking to every generated page, grouped by
# namespace directory (legacy/<area> and impresso-2).
{
  echo '<!DOCTYPE html>'
  echo '<html lang="en"><head><meta charset="utf-8">'
  echo '<title>Impresso JSON Schemas — Documentation</title></head><body>'
  echo '<h1>Impresso JSON Schemas — Documentation</h1>'
  for namespace_dir in "$SITE_DIR"/legacy "$SITE_DIR"/impresso-2; do
    [ -d "$namespace_dir" ] || continue
    namespace="$(basename "$namespace_dir")"
    echo "<h2>${namespace}</h2><ul>"
    while IFS= read -r -d '' html_file; do
      rel="${html_file#"$SITE_DIR"/}"
      echo "<li><a href=\"${rel}\">${rel%.html}</a></li>"
    done < <(find "$namespace_dir" -name '*.html' -print0 | sort -z)
    echo '</ul>'
  done
  echo '</body></html>'
} > "$SITE_DIR/index.html"

echo "Static docs site built in $SITE_DIR"
