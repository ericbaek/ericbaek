"""Render the profile's year-to-date public activity card using GitHub CLI."""

from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess

now = datetime.now(timezone.utc)
query = """
query($start: DateTime!, $end: DateTime!) {
  user(login: "ericbaek") {
    contributionsCollection(from: $start, to: $end) {
      totalCommitContributions
      totalPullRequestContributions
    }
  }
}
"""
result = subprocess.check_output([
    "gh", "api", "graphql", "-f", f"query={query}",
    "-f", f"start={now.year}-01-01T00:00:00Z",
    "-f", f"end={now:%Y-%m-%dT%H:%M:%SZ}",
])
stats = json.loads(result)["data"]["user"]["contributionsCollection"]
commits = stats["totalCommitContributions"]
prs = stats["totalPullRequestContributions"]
svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="460" height="148" viewBox="0 0 460 148" role="img" aria-labelledby="title desc">
  <title id="title">Public GitHub activity · @ericbaek</title>
  <desc id="desc">{now.year} year to date. {commits:,} commit contributions and {prs:,} pull requests opened.</desc>
  <rect x="0.5" y="0.5" width="459" height="147" rx="12" fill="#0d1117" stroke="#3d4855"/>
  <g font-family="system-ui, sans-serif">
    <text x="22" y="31" fill="#f0f6fc" font-size="17" font-weight="600">GitHub activity</text>
    <text x="438" y="31" text-anchor="end" fill="#b6c2cf" font-size="12">@ericbaek</text>
    <path d="M22 46h416 M232 59v46" fill="none" stroke="#303b47"/>
    <g fill="#7ee2a8" font-size="29" font-weight="650">
      <text x="22" y="83">{commits:,}</text>
      <text x="254" y="83">{prs:,}</text>
    </g>
    <g fill="#e6edf3" font-size="13">
      <text x="22" y="104">Commit contributions</text>
      <text x="254" y="104">Pull requests opened</text>
    </g>
    <text x="22" y="132" font-size="12" fill="#b6c2cf">Public repositories · 1 Jan – {now.day} {now:%b %Y} UTC</text>
  </g>
</svg>
"""
Path("github-activity.svg").write_text(svg)
