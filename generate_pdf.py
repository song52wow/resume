#!/usr/bin/env python3
"""Convert README.md to styled HTML files for PDF generation (Chinese & English)."""

from markdown_it import MarkdownIt

LANG_CONFIGS = [
    {
        "input": "README.md",
        "output": "docs/index.html",
        "lang": "zh-CN",
    },
    {
        "input": "README_EN.md",
        "output": "docs/index_en.html",
        "lang": "en",
    },
]

CSS = """
@page {
  size: A4;
  margin: 20mm 18mm;
}
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans SC", sans-serif;
  font-size: 13px;
  line-height: 1.7;
  color: #24292e;
  max-width: 100%;
}
h1 {
  font-size: 28px;
  text-align: center;
  margin-bottom: 2px;
}
h3[align="center"] {
  text-align: center;
  color: #586069;
  font-weight: 400;
  margin-top: 4px;
}
p[align="center"], .center {
  text-align: center;
}
hr {
  border: none;
  border-top: 1px solid #e1e4e8;
  margin: 20px 0;
}
h2 {
  font-size: 20px;
  border-bottom: 2px solid #e1e4e8;
  padding-bottom: 6px;
  margin-top: 32px;
  margin-bottom: 16px;
}
h3 {
  font-size: 16px;
  text-align: left;
  color: #24292e;
  font-weight: 600;
  margin-top: 24px;
  margin-bottom: 12px;
}
h4 {
  font-size: 14px;
  margin-top: 20px;
  margin-bottom: 8px;
}
blockquote {
  border-left: 4px solid #dfe2e5;
  padding: 4px 16px;
  color: #6a737d;
  margin: 12px 0;
  background: #f6f8fa;
}
table {
  border-collapse: collapse;
  width: 100%;
  font-size: 12px;
  margin: 12px 0;
}
th, td {
  border: 1px solid #e1e4e8;
  padding: 8px 12px;
  text-align: left;
  vertical-align: top;
}
th {
  background: #f6f8fa;
  font-weight: 600;
}
code {
  background: #f6f8fa;
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 12px;
  font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
}
pre {
  background: #f6f8fa;
  padding: 12px;
  border-radius: 6px;
  overflow-x: auto;
}
pre code {
  background: none;
  padding: 0;
}
img {
  vertical-align: middle;
  max-width: 100%;
}
ul, ol {
  padding-left: 24px;
  margin-top: 8px;
  margin-bottom: 12px;
}
li {
  margin-bottom: 6px;
}
kbd {
  background: #fafbfc;
  border: 1px solid #d1d5da;
  border-radius: 4px;
  padding: 1px 6px;
  font-size: 12px;
  font-family: "SFMono-Regular", Consolas, monospace;
}
a {
  color: #0366d6;
  text-decoration: none;
}
strong {
  font-weight: 600;
}
em {
  font-style: italic;
}
/* Badge images styling */
p a img, p > img {
  height: auto;
  margin: 4px 2px;
  display: inline-block;
  vertical-align: middle;
}
p[align="center"] {
  font-size: 14px;
  line-height: 2;
  margin-bottom: 20px;
}
"""

md = MarkdownIt().enable("table")

for config in LANG_CONFIGS:
    with open(config["input"], "r", encoding="utf-8") as f:
        md_text = f.read()

    html_body = md.render(md_text)

    html = f"""<!DOCTYPE html>
<html lang="{config['lang']}">
<head>
<meta charset="UTF-8">
<style>
{CSS}
</style>
</head>
<body>
{html_body}
</body>
</html>"""

    with open(config["output"], "w", encoding="utf-8") as f:
        f.write(html)

    print(f"HTML written to {config['output']}")
