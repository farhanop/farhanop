#!/usr/bin/env python3

import os
import re
import sys
from datetime import datetime, timezone
from typing import Any

import requests

GITHUB_USERNAME = os.getenv("GITHUB_USERNAME", "farhanop")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")

HEADERS = {
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "readme-updater/1.0",
}
if GITHUB_TOKEN:
    HEADERS["Authorization"] = f"Bearer {GITHUB_TOKEN}"

API_BASE = "https://api.github.com"
README_PATH = "README.md"

FEATURED_REPOS = [
    {
        "repo": "farhanop/library",
        "title": "Library Management System",
        "badge": "CURRENT",
        "description": "Fullstack library OPAC system replacing SLiMS for university library",
        "tags": ["FastAPI", "React", "TypeScript", "PostgreSQL", "Docker"],
    },
    {
        "repo": "farhanop/cctv-monitoring",
        "title": "CCTV Monitoring System",
        "badge": "",
        "description": "Multi-NVR & multi-channel architecture with real-time WebRTC streaming",
        "tags": ["FastAPI", "WebRTC", "Redis", "MySQL", "Docker"],
    },
    {
        "repo": "farhanop/lms-integration",
        "title": "LMS Integration System",
        "badge": "",
        "description": "Moodle-SIAK integration with API-based student/course/grade sync",
        "tags": ["Laravel", "MySQL", "REST API"],
    },
    {
        "repo": "farhanop/zoom-management",
        "title": "Zoom Management System",
        "badge": "",
        "description": "Centralized meeting request and approval system with audit logging",
        "tags": ["Node.js", "MySQL"],
    },
]


def api_get(path: str) -> Any:
    url = f"{API_BASE}{path}"
    resp = requests.get(url, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    return resp.json()


def get_repo_data(repo_full: str) -> dict[str, Any] | None:
    try:
        data = api_get(f"/repos/{repo_full}")
        return data if isinstance(data, dict) else None
    except requests.HTTPError:
        return None


def build_featured_section() -> str:
    lines = []
    lines.append("## 📌 Featured Projects")
    lines.append("")

    for info in FEATURED_REPOS:
        repo_data = get_repo_data(info["repo"])
        stars = repo_data.get("stargazers_count", 0) if repo_data else 0
        forks = repo_data.get("forks_count", 0) if repo_data else 0
        lang = repo_data.get("language", "") if repo_data else ""

        badge = f" 🔥 **{info['badge']}**" if info["badge"] else ""
        lines.append(f"### {info['title']}{badge}")
        lines.append("")
        lines.append(f"_{info['description']}_")
        lines.append("")
        tags = " · ".join(f"`{t}`" for t in info["tags"])
        if lang:
            tags = f"`{lang}` · {tags}"
        lines.append(f"**Tech:** {tags}")
        if stars or forks:
            meta = []
            if stars:
                meta.append(f"⭐ {stars} stars")
            if forks:
                meta.append(f"🍴 {forks} forks")
            lines.append(f"**Stats:** {' · '.join(meta)}")
        lines.append("")
        lines.append(f"[View Repository](https://github.com/{info['repo']})")
        lines.append("")

    return "\n".join(lines)


def build_activity_section() -> str:
    lines = []
    lines.append("## 🔄 Recent Activity")
    lines.append("")

    try:
        events = api_get(f"/users/{GITHUB_USERNAME}/events/public?per_page=10")
        if isinstance(events, list) and events:
            for event in events:
                created = event.get("created_at", "")
                repo_name = event.get("repo", {}).get("name", "")
                event_type = event.get("type", "")
                ts = ""
                if created:
                    try:
                        dt = datetime.fromisoformat(created.replace("Z", "+00:00"))
                        ts = dt.strftime("%Y-%m-%d %H:%M UTC")
                    except ValueError:
                        ts = created

                if event_type == "PushEvent":
                    commits = event.get("payload", {}).get("commits", [])
                    count = len(commits)
                    msg = commits[0].get("message", "").split("\n")[0][:60] if commits else ""
                    lines.append(f"- 🚀 Pushed **{count} commit(s)** to [`{repo_name}`](https://github.com/{repo_name}) — _{msg}_")
                elif event_type == "CreateEvent":
                    ref_type = event.get("payload", {}).get("ref_type", "")
                    ref = event.get("payload", {}).get("ref", "")
                    lines.append(f"- ✅ Created {ref_type} `{ref}` in [`{repo_name}`](https://github.com/{repo_name})")
                elif event_type == "IssuesEvent":
                    action = event.get("payload", {}).get("action", "")
                    title = event.get("payload", {}).get("issue", {}).get("title", "")
                    url = event.get("payload", {}).get("issue", {}).get("html_url", "")
                    lines.append(f"- 📝 {action.capitalize()} issue **[{title}]({url})** in [`{repo_name}`](https://github.com/{repo_name})")
                elif event_type == "IssueCommentEvent":
                    title = event.get("payload", {}).get("issue", {}).get("title", "")
                    url = event.get("payload", {}).get("comment", {}).get("html_url", "")
                    lines.append(f"- 💬 Commented on issue **[{title}]({url})** in [`{repo_name}`](https://github.com/{repo_name})")
                elif event_type == "PullRequestEvent":
                    action = event.get("payload", {}).get("action", "")
                    title = event.get("payload", {}).get("pull_request", {}).get("title", "")
                    url = event.get("payload", {}).get("pull_request", {}).get("html_url", "")
                    lines.append(f"- 🔀 {action.capitalize()} PR **[{title}]({url})** in [`{repo_name}`](https://github.com/{repo_name})")
                elif event_type == "WatchEvent":
                    lines.append(f"- ⭐ Starred [`{repo_name}`](https://github.com/{repo_name})")
                elif event_type == "ForkEvent":
                    fork = event.get("payload", {}).get("forkee", {}).get("full_name", "")
                    lines.append(f"- 🍴 Forked [`{repo_name}`](https://github.com/{repo_name}) → [`{fork}`](https://github.com/{fork})")
                elif event_type == "ReleaseEvent":
                    name = event.get("payload", {}).get("release", {}).get("name", "") or event.get("payload", {}).get("release", {}).get("tag_name", "")
                    url = event.get("payload", {}).get("release", {}).get("html_url", "")
                    lines.append(f"- 🎉 Released **{name}** in [`{repo_name}`](https://github.com/{repo_name})")
                else:
                    lines.append(f"- 📌 {event_type} in [`{repo_name}`](https://github.com/{repo_name})")

                if ts:
                    lines[-1] = f"{lines[-1]} _{ts}_"
        else:
            lines.append("_No recent public activity._")
    except requests.HTTPError as e:
        lines.append(f"_Error fetching activity: {e}_")

    lines.append("")
    lines.append(f"<sub>Last updated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}</sub>")
    lines.append("")
    return "\n".join(lines)


def build_stats_section() -> str:
    return f"""## 📊 GitHub Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username={GITHUB_USERNAME}&theme=dark&hide_border=true&show_icons=true" width="48%" />
  <img src="https://nirzak-streak-stats.vercel.app/?user={GITHUB_USERNAME}&theme=dark&hide_border=true" width="48%" />
</p>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username={GITHUB_USERNAME}&theme=dark&hide_border=true&layout=compact" width="48%" />
</p>

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username={GITHUB_USERNAME}&theme=darkhub&no-frame=true&no-bg=true&row=2&column=4" />
</p>

<sub>Last updated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}</sub>"""


def replace_section(content: str, marker: str, new_content: str) -> str:
    start_tag = f"<!-- {marker}:start -->"
    end_tag = f"<!-- {marker}:end -->"
    start_idx = content.find(start_tag)
    if start_idx == -1:
        print(f"WARNING: Marker '{start_tag}' not found in README", file=sys.stderr)
        return content
    end_idx = content.find(end_tag, start_idx)
    if end_idx == -1:
        print(f"WARNING: Marker '{end_tag}' not found in README", file=sys.stderr)
        return content
    replacement = f"{start_tag}\n{new_content}\n{end_tag}"
    return content[:start_idx] + replacement + content[end_idx + len(end_tag):]


def main():
    if not os.path.exists(README_PATH):
        print(f"ERROR: {README_PATH} not found", file=sys.stderr)
        sys.exit(1)

    with open(README_PATH, "r") as f:
        content = f.read()

    print("Building featured projects section...")
    featured = build_featured_section()
    content = replace_section(content, "featured-projects", featured)

    print("Building recent activity section...")
    activity = build_activity_section()
    content = replace_section(content, "recent-activity", activity)

    print("Updating stats section...")
    stats = build_stats_section()
    content = replace_section(content, "stats", stats)

    with open(README_PATH, "w") as f:
        f.write(content)

    print("README.md updated successfully")


if __name__ == "__main__":
    main()
