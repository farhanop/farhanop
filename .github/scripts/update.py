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


def build_activity_section() -> str:
    lines = []

    try:
        # If token is provided, try authenticated events endpoint (covers org & private commits)
        # Fall back to public endpoint if needed
        events = None
        if GITHUB_TOKEN:
            try:
                events = api_get(f"/users/{GITHUB_USERNAME}/events?per_page=25")
            except requests.RequestException:
                events = None

        if not events:
            events = api_get(f"/users/{GITHUB_USERNAME}/events/public?per_page=20")

        if isinstance(events, list) and events:
            seen_activities = 0
            for event in events:
                if seen_activities >= 7:
                    break

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

                is_org_repo = "UIGM-IT-Dev" in repo_name
                repo_display_link = (
                    f"[`{repo_name}`](https://github.com/UIGM-IT-Dev)"
                    if is_org_repo
                    else f"[`{repo_name}`](https://github.com/{repo_name})"
                )
                org_badge = " 🏢 _(UIGM IT Dev)_" if is_org_repo else ""

                if event_type == "PushEvent":
                    commits = event.get("payload", {}).get("commits", [])
                    count = len(commits) if commits else event.get("payload", {}).get("size", 1)
                    msg = commits[0].get("message", "").split("\n")[0][:65] if commits else "Update code"
                    lines.append(
                        f"- 🚀 Pushed **{count} commit(s)** to {repo_display_link}{org_badge} — _{msg}_"
                    )
                    seen_activities += 1
                elif event_type == "CreateEvent":
                    ref_type = event.get("payload", {}).get("ref_type", "branch")
                    ref = event.get("payload", {}).get("ref", "")
                    target = f"`{ref}`" if ref else "repository"
                    lines.append(f"- ✅ Created {ref_type} {target} in {repo_display_link}{org_badge}")
                    seen_activities += 1
                elif event_type == "IssuesEvent":
                    action = event.get("payload", {}).get("action", "opened")
                    title = event.get("payload", {}).get("issue", {}).get("title", "")
                    lines.append(f"- 📝 {action.capitalize()} issue **{title}** in {repo_display_link}{org_badge}")
                    seen_activities += 1
                elif event_type == "PullRequestEvent":
                    action = event.get("payload", {}).get("action", "opened")
                    title = event.get("payload", {}).get("pull_request", {}).get("title", "")
                    lines.append(f"- 🔀 {action.capitalize()} PR **{title}** in {repo_display_link}{org_badge}")
                    seen_activities += 1
                elif event_type == "WatchEvent":
                    lines.append(f"- ⭐ Starred [`{repo_name}`](https://github.com/{repo_name})")
                    seen_activities += 1
                elif event_type == "ForkEvent":
                    fork = event.get("payload", {}).get("forkee", {}).get("full_name", "")
                    lines.append(f"- 🍴 Forked [`{repo_name}`](https://github.com/{repo_name}) → [`{fork}`](https://github.com/{fork})")
                    seen_activities += 1
                elif event_type == "ReleaseEvent":
                    name = event.get("payload", {}).get("release", {}).get("name", "") or "New Release"
                    lines.append(f"- 🎉 Released **{name}** in {repo_display_link}{org_badge}")
                    seen_activities += 1

                if ts and lines and not lines[-1].endswith(f"_{ts}_"):
                    lines[-1] = f"{lines[-1]} <sub>({ts})</sub>"

        if not lines:
            lines.append("- _Active daily on institutional repositories and system architecture._")

    except requests.RequestException as e:
        lines.append(f"- _Currently focusing on core backend architecture & campus systems._")
        print(f"Notice: Activity fetch encountered network issue: {e}", file=sys.stderr)

    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines.append("")
    lines.append(f"<sub>⚡ Last activity sync: {now_utc}</sub>")
    return "\n".join(lines).strip()


def build_stats_section() -> str:
    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    return f"""<table width="100%">
  <tr>
    <td width="50%" align="center">
      <a href="https://github.com/{GITHUB_USERNAME}">
        <img src="https://github-readme-stats-fast.vercel.app/api?username={GITHUB_USERNAME}&show_icons=true&hide_border=true&bg_color=0d1117&title_color=38bdf8&text_color=94a3b8&icon_color=38bdf8" width="100%" alt="GitHub Stats" />
      </a>
    </td>
    <td width="50%" align="center">
      <a href="https://github.com/{GITHUB_USERNAME}">
        <img src="https://streak-stats.demolab.com/?user={GITHUB_USERNAME}&hide_border=true&background=0d1117&ring=38bdf8&fire=38bdf8&currStreakLabel=38bdf8" width="100%" alt="GitHub Streak" />
      </a>
    </td>
  </tr>
  <tr>
    <td colspan="2" align="center">
      <a href="https://github.com/{GITHUB_USERNAME}">
        <img src="https://github-readme-stats-fast.vercel.app/api/top-langs/?username={GITHUB_USERNAME}&layout=compact&hide_border=true&bg_color=0d1117&title_color=38bdf8&text_color=94a3b8" width="58%" alt="Top Languages" />
      </a>
    </td>
  </tr>
</table>

<p align="center">
  <sub>⚡ Automated metrics synced at {now_utc}</sub>
</p>""".strip()


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

    print("Syncing recent activity section...")
    activity = build_activity_section()
    content = replace_section(content, "recent-activity", activity)

    print("Syncing stats section...")
    stats = build_stats_section()
    content = replace_section(content, "stats", stats)

    with open(abs_readme, "w", encoding="utf-8") as f:
        f.write(content)

    print("README.md synchronized successfully.")


if __name__ == "__main__":
    main()
