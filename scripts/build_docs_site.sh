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
# Parallelized conversion using xargs for speed.
convert_file() {
  local md_file="$1"
  local target_dir="$2"
  local rel_path="${md_file#docs/}"
  local out_file="$target_dir/${rel_path%.md}.html"
  mkdir -p "$(dirname "$out_file")"
  local title="$(basename "${rel_path%.md}")"
  sed -E 's/\(([^) "]+)\.md((#[^) "]*)?( "[^"]*")?)\)/(\1.html\2)/g' "$md_file" \
    | pandoc -f gfm -t html5 --standalone --metadata "title=$title" -o "$out_file"
}
export -f convert_file

NUM_PROCS="$(getconf _NPROCESSORS_ONLN 2>/dev/null || nproc 2>/dev/null || echo 4)"
find docs -name '*.md' -print0 | xargs -0 -n 1 -P "$NUM_PROCS" -I {} bash -c 'convert_file "$1" "$2"' _ {} "$SITE_DIR"

# Build a top-level index linking prominently to top-level schemas,
# followed by an expandable list of detailed schema fragments.
python3 - "$SITE_DIR" << 'EOF'
import sys, os, glob, json, html, re

site_dir = sys.argv[1]

schema_pages = {}
for readme in glob.glob('docs/**/README.md', recursive=True):
    readme_dir = os.path.dirname(readme)
    with open(readme, encoding='utf-8') as fp:
        for line in fp:
            match = re.search(r'\]\(([^)]+\.md)[^)]*\).*?`([^`]+)`', line)
            if match and match.group(2).startswith(
                    'https://impresso.github.io/impresso-schemas/'):
                doc_path = os.path.normpath(
                    os.path.join(readme_dir, match.group(1))
                )
                site_path = os.path.relpath(
                    doc_path[:-3] + '.html', 'docs'
                )
                schema_pages[match.group(2)] = site_path

def resolve_html(p, is_imp2):
    schema_url = (
        'https://impresso.github.io/impresso-schemas/' + p
    )
    if schema_url in schema_pages:
        return schema_pages[schema_url]

    base = os.path.basename(p)
    if is_imp2:
        clean_name = base.replace('.v1.schema.json', '').replace('.v2.schema.json', '')
        cand = f'impresso-2/{clean_name}.html'
        if os.path.exists(os.path.join(site_dir, cand)):
            return cand
        return None
    else:
        area = p.split('/')[1]
        clean_name = base.replace('.schema.json', '')
        cand = f'legacy/{area}/{clean_name}.html'
        if os.path.exists(os.path.join(site_dir, cand)):
            return cand
        return None

imp2_groups = {
    'Data Preparation': [],
    'Text Processing': [],
    'Semantic Enrichment': [],
    'Solr Indexing': [],
    'Common Schemas': [],
    'Web App': []
}

legacy_groups = {
    'Canonical Formats': [],
    'Rebuilt Content Items': [],
    'Text Processing & OCR': [],
    'Topic Modeling': [],
    'Semantic Enrichment & Reuse': [],
    'Embeddings': [],
    'Visualizer & Image Classification': [],
    'Versioning': []
}

for p in sorted(glob.glob('json/**/*.schema.json', recursive=True)):
    with open(p, encoding='utf-8') as fp:
        try:
            d = json.load(fp)
        except Exception:
            d = {}
    title = d.get('title') or os.path.basename(p)
    desc = d.get('description', '')
    is_imp2 = 'impresso-2' in p
    html_target = resolve_html(p, is_imp2)
    entry = {
        'path': p,
        'title': title,
        'desc': desc,
        'html': html_target,
        'filename': os.path.basename(p)
    }
    if is_imp2:
        rel = p.replace('json/impresso-2/', '')
        area = rel.split('/')[0]
        if area == 'data-preparation':
            imp2_groups['Data Preparation'].append(entry)
        elif area == 'text-processing':
            imp2_groups['Text Processing'].append(entry)
        elif area == 'semantic-enrichment':
            imp2_groups['Semantic Enrichment'].append(entry)
        elif area == 'solr-indexing':
            imp2_groups['Solr Indexing'].append(entry)
        elif area == 'common':
            imp2_groups['Common Schemas'].append(entry)
        elif area == 'web-app':
            imp2_groups['Web App'].append(entry)
    else:
        area = p.split('/')[1]
        if area == 'canonical':
            legacy_groups['Canonical Formats'].append(entry)
        elif area == 'rebuilt':
            legacy_groups['Rebuilt Content Items'].append(entry)
        elif area in ('language_identification', 'linguistic_annotation', 'ocr_qa'):
            legacy_groups['Text Processing & OCR'].append(entry)
        elif area == 'topic_model':
            legacy_groups['Topic Modeling'].append(entry)
        elif area in ('entities', 'text_reuse'):
            legacy_groups['Semantic Enrichment & Reuse'].append(entry)
        elif area in ('embeddings', 'image_embeddings'):
            legacy_groups['Embeddings'].append(entry)
        elif area in ('visualizer', 'image_classification'):
            legacy_groups['Visualizer & Image Classification'].append(entry)
        elif area == 'versioning':
            legacy_groups['Versioning'].append(entry)

out = []
out.append('<!DOCTYPE html>')
out.append('<html lang="en">')
out.append('<head>')
out.append('  <meta charset="utf-8">')
out.append('  <meta name="viewport" content="width=device-width, initial-scale=1.0">')
out.append('  <title>Impresso JSON Schemas — Documentation</title>')
out.append('  <style>')
out.append('    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; line-height: 1.5; color: #24292f; max-width: 960px; margin: 0 auto; padding: 2rem 1rem; }')
out.append('    h1 { border-bottom: 2px solid #d0d7de; padding-bottom: .4rem; }')
out.append('    h2 { border-bottom: 1px solid #d0d7de; padding-bottom: .3rem; margin-top: 2rem; color: #0969da; }')
out.append('    h3 { margin-top: 1.5rem; margin-bottom: 0.5rem; }')
out.append('    ul { padding-left: 1.5rem; }')
out.append('    li { margin-bottom: 0.35rem; }')
out.append('    a { color: #0969da; text-decoration: none; }')
out.append('    a:hover { text-decoration: underline; }')
out.append('    code { background-color: #f6f8fa; padding: 0.2em 0.4em; border-radius: 4px; font-size: 85%; font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, monospace; }')
out.append('    .desc { color: #57606a; font-size: 0.9em; margin-left: 0.3rem; }')
out.append('    details { background: #f6f8fa; border: 1px solid #d0d7de; border-radius: 6px; padding: 0.75rem 1rem; margin-top: 2rem; }')
out.append('    summary { font-weight: 600; cursor: pointer; }')
out.append('    .all-files { columns: 2; margin-top: 1rem; font-size: 0.85em; }')
out.append('    @media (max-width: 600px) { .all-files { columns: 1; } }')
out.append('  </style>')
out.append('</head>')
out.append('<body>')
out.append('  <h1>Impresso JSON Schemas — Documentation</h1>')
out.append('  <p>Interactive reference documentation generated from repository schemas for the <a href="https://impresso-project.ch/">Impresso project</a>.</p>')

# Section: Impresso 2 Schemas
out.append('  <h2>Impresso 2 Schemas (Current)</h2>')
for group_name, items in imp2_groups.items():
    if not items: continue
    out.append(f'  <h3>{html.escape(group_name)}</h3>')
    out.append('  <ul>')
    for item in items:
        link_text = html.escape(item['title'])
        file_label = f"<code>{html.escape(item['filename'])}</code>"
        desc_text = f"<span class=\"desc\">— {html.escape(item['desc'])}</span>" if item['desc'] else ""
        if item['html']:
            out.append(f'    <li><a href="{html.escape(item["html"])}"><strong>{link_text}</strong></a> ({file_label}){desc_text}</li>')
        else:
            out.append(f'    <li><strong>{link_text}</strong> ({file_label}){desc_text}</li>')
    out.append('  </ul>')

# Section: Legacy Schemas
out.append('  <h2>Legacy Schemas (Impresso 1)</h2>')
for group_name, items in legacy_groups.items():
    if not items: continue
    out.append(f'  <h3>{html.escape(group_name)}</h3>')
    out.append('  <ul>')
    for item in items:
        link_text = html.escape(item['title'])
        file_label = f"<code>{html.escape(item['filename'])}</code>"
        desc_text = f"<span class=\"desc\">— {html.escape(item['desc'])}</span>" if item['desc'] else ""
        if item['html']:
            out.append(f'    <li><a href="{html.escape(item["html"])}"><strong>{link_text}</strong></a> ({file_label}){desc_text}</li>')
        else:
            out.append(f'    <li><strong>{link_text}</strong> ({file_label}){desc_text}</li>')
    out.append('  </ul>')

# Collapsible section for all detailed schema fragments
all_html_files = []
for root, dirs, files in os.walk(site_dir):
    for f in files:
        if f.endswith('.html') and f != 'index.html':
            full_path = os.path.join(root, f)
            rel = os.path.relpath(full_path, site_dir)
            all_html_files.append(rel)

all_html_files.sort()
out.append('  <details>')
out.append(f'    <summary>All Generated Schema Pages &amp; Property Fragments ({len(all_html_files)} pages)</summary>')
out.append('    <ul class="all-files">')
for fpath in all_html_files:
    out.append(f'      <li><a href="{html.escape(fpath)}">{html.escape(fpath[:-5])}</a></li>')
out.append('    </ul>')
out.append('  </details>')

out.append('</body>')
out.append('</html>')

with open(os.path.join(site_dir, 'index.html'), 'w', encoding='utf-8') as fp:
    fp.write('\n'.join(out) + '\n')
EOF

echo "Static docs site built in $SITE_DIR"
