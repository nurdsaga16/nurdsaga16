#!/usr/bin/env python3
"""Generate Nurdaulet Sagnadin's terminal-style profile card."""
import html
import textwrap
from pathlib import Path

NAME = "Nurdaulet Sagnadin"
PAD = 32
WIDTH = 664
LINE_HEIGHT = 25
VALUE_X = 182
VALUE_CHARS = (WIDTH - PAD - VALUE_X) // 10
C = {"bg": "#0d1117", "border": "#30363d", "sect": "#d2a8ff",
     "label": "#ffa657", "dots": "#484f58", "val": "#e6edf3"}

SECTIONS = [
    ("Profile", [
        ("Role", "Software Engineer"),
        ("Location", "Almaty, Kazakhstan"),
        ("Education", "Computer Science @ SDU"),
        ("Stack", "Java, Spring Boot, React, PostgreSQL"),
        ("Cloud", "AWS, Docker"),
    ]),
]

def text_line(x, y, text, fill, size=16, bold=False):
    weight = ' font-weight="bold"' if bold else ""
    return (
        f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
        f'font-family="monospace"{weight}>{html.escape(text)}</text>'
    )


def make_svg():
    """Build a card with wrapped values and content-driven height."""
    out = [text_line(PAD, PAD, "Nurdaulet Sagnadin:~$ whoami", C["label"], 18, True)]
    y = PAD + LINE_HEIGHT + 8
    out.append(
        f'<line x1="{PAD}" y1="{y}" x2="{WIDTH - PAD}" y2="{y}" '
        f'stroke="{C["border"]}"/>'
    )
    for heading, fields in SECTIONS:
        y += LINE_HEIGHT
        out.append(text_line(PAD, y, heading, C["sect"], bold=True))
        for label, value in fields:
            y += LINE_HEIGHT
            out.append(text_line(PAD, y, label, C["label"]))
            out.append(text_line(PAD + len(label) * 10 + 12, y,
                                 "." * (13 - len(label)), C["dots"]))
            for index, line in enumerate(textwrap.wrap(value, width=VALUE_CHARS)):
                if index:
                    y += LINE_HEIGHT
                out.append(text_line(VALUE_X, y, line, C["val"]))
        y += 8
    height = y + PAD
    return "\n".join([
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{height}" '
        f'viewBox="0 0 {WIDTH} {height}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{html.escape(NAME)} — Software Engineer</title>',
        '<desc id="desc">Software engineer in Almaty, studying Computer Science at SDU. '
        'Stack: Java, Spring Boot, React, PostgreSQL, AWS and Docker.</desc>',
        f'<rect width="{WIDTH}" height="{height}" rx="10" '
        f'fill="{C["bg"]}" stroke="{C["border"]}" stroke-width="2"/>',
        *out,
        '</svg>',
    ])


def main():
    Path(__file__).with_name("profile.svg").write_text(make_svg(), encoding="utf-8", newline="\n")
    print(f"Generated profile.svg | {NAME}")


if __name__ == "__main__":
    main()
