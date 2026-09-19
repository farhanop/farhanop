#!/usr/bin/env python3

import json
import os
import sys
from datetime import datetime, timezone
from typing import Any

import requests

GITHUB_USERNAME = os.getenv("GITHUB_USERNAME", "farhanop")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")

HEADERS = {
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "readme-updater/2.0",
}
if GITHUB_TOKEN:
    HEADERS["Authorization"] = f"Bearer {GITHUB_TOKEN}"

API_BASE = "https://api.github.com"
README_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "README.md")
DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "projects.json")

FALLBACK_PROJECTS = [
    {
        "id": "library-opac",
        "title": "Library Management System (OPAC)",
        "badge": "🔥 ACTIVE PRODUCTION",
        "scope": "UIGM-IT-Dev",
        "repo": "UIGM-IT-Dev/library",
        "is_private": True,
        "description": "Fullstack library OPAC & repository platform replacing legacy SLiMS for university-wide academic library.",
        "architecture_highlight": "Engineered with Vertical Slice Architecture, high-concurrency catalog queries, and automated circulation workflows.",
        "tags": ["FastAPI", "React", "TypeScript", "PostgreSQL", "Docker", "SQLAlchemy"],
    },
    {
        "id": "cctv-monitoring",
        "title": "Campus CCTV Real-Time Monitoring",
        "badge": "📹 PRODUCTION STREAMING",
        "scope": "UIGM-IT-Dev",
        "repo": "UIGM-IT-Dev/cctv-monitoring",
        "is_private": True,
        "description": "Multi-NVR & multi-channel surveillance engine delivering ultra-low-latency real-time video feeds across campus network.",
        "architecture_highlight": "Implemented WebRTC media streaming pipeline with Redis pub/sub state handling and multi-stream hardware acceleration.",
        "tags": ["FastAPI", "WebRTC", "Redis", "MySQL", "Docker"],
    },
    {
        "id": "lms-integration",
        "title": "LMS Moodle - SIAK Integration Gateway",
        "badge": "🔄 ENTERPRISE GATEWAY",
        "scope": "UIGM-IT-Dev",
        "repo": "UIGM-IT-Dev/lms-integration",
        "is_private": True,
        "description": "Enterprise middleware bridging Moodle LMS with university Academic Information System (SIAK) for seamless synchronization.",
        "architecture_highlight": "Automated bi-directional sync for thousands of student enrollments, course schedules, and academic grade transcripts.",
        "tags": ["Laravel", "REST API", "MySQL", "Redis"],
    },
    {
        "id": "zoom-management",
        "title": "Enterprise Zoom Room & Meeting Manager",
        "badge": "🔒 INTERNAL SYSTEM",
        "scope": "UIGM-IT-Dev",
        "repo": "UIGM-IT-Dev/zoom-management",
        "is_private": True,
        "description": "Centralized meeting booking, license scheduling, and audit trail system managing enterprise institutional Zoom accounts.",
        "architecture_highlight": "Dynamic host license allocation, conflict detection algorithms, and automated audit logging.",
        "tags": ["Node.js", "Express", "Zoom API", "MySQL"],
    },
]


def load_projects() -> list[dict[str, Any]]:
    if os.path.exists(DATA_PATH):
        try:
            with open(DATA_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"Warning: Failed to parse {DATA_PATH}: {e}, using fallback data", file=sys.stderr)
    return FALLBACK_PROJECTS


def api_get(path: str) -> Any:
    url = f"{API_BASE}{path}"
    resp = requests.get(url, headers=HEADERS, timeout=12)
    resp.raise_for_status()
    return resp.json()


def get_repo_data(repo_full: str) -> dict[str, Any] | None:
    try:
        data = api_get(f"/repos/{repo_full}")
        return data if isinstance(data, dict) else None
    except requests.RequestException:
        return None


def build_featured_section() -> str:
    projects = load_projects()
    lines = []

    for info in projects:
        repo_target = info.get("repo", "")
        repo_data = get_repo_data(repo_target) if repo_target else None

        stars = repo_data.get("stargazers_count", 0) if repo_data else 0
        forks = repo_data.get("forks_count", 0) if repo_data else 0

        badge_text = f" &nbsp;`{info['badge']}`" if info.get("badge") else ""
        lines.append(f"### {info['title']}{badge_text}")
        lines.append("")
        lines.append(f"{info['description']}")
        lines.append("")
        if info.get("architecture_highlight"):
            lines.append(f"> **Architecture Highlight:** {info['architecture_highlight']}")
            lines.append("")

        tags_str = " · ".join(f"`{t}`" for t in info.get("tags", []))
        lines.append(f"- **Tech Stack:** {tags_str}")

        if stars or forks:
            meta = []
            if stars:
                meta.append(f"⭐ {stars} stars")
            if forks:
                meta.append(f"🍴 {forks} forks")
            lines.append(f"- **Stats:** {' · '.join(meta)}")

        is_private = info.get("is_private", False)
        scope = info.get("scope", "")

        if is_private:
            if "UIGM" in scope or "UIGM" in repo_target:
                lines.append(f"- **Access:** 🏢 Developed for **[UIGM IT Dev](https://github.com/UIGM-IT-Dev)** · 🔒 _Enterprise Core System_")
            else:
                lines.append("- **Access:** 🔒 _Private Enterprise Repository_")
        else:
            lines.append(f"- **Repository:** [github.com/{repo_target}](https://github.com/{repo_target})")

        lines.append("")

    return "\n".join(lines).strip()




def replace_section(content: str, marker: str, new_content: str) -> str:
    start_tag = f"<!-- {marker}:start -->"
    end_tag = f"<!-- {marker}:end -->"
    start_idx = content.find(start_tag)
    if start_idx == -1:
        return content
    end_idx = content.find(end_tag, start_idx)
    if end_idx == -1:
        return content
    replacement = f"{start_tag}\n{new_content}\n{end_tag}"
    return content[:start_idx] + replacement + content[end_idx + len(end_tag):]




def main():
    abs_readme = os.path.abspath(README_PATH)
    if not os.path.exists(abs_readme):
        print(f"ERROR: {abs_readme} not found", file=sys.stderr)
        sys.exit(1)

    with open(abs_readme, "r", encoding="utf-8") as f:
        content = f.read()

    if "<!-- featured-projects:start -->" in content:
        print("Syncing featured projects section...")
        featured = build_featured_section()
        content = replace_section(content, "featured-projects", featured)




    with open(abs_readme, "w", encoding="utf-8") as f:
        f.write(content)

    print("README.md synchronized successfully.")


if __name__ == "__main__":
    main()
