#!/bin/bash
# Open the LinkedIn feed, the LinkedIn profile and the GitHub profile in
# Google Chrome. The LinkedIn profile URL comes from LINKEDIN_URL in .env.
# Runs Chrome's binary, not `open -a`: open can send the URLs to a hidden
# headless Chrome. With the default profile, a running Chrome takes the
# tabs; if Chrome is closed, this starts it.
env_file="$(dirname "$0")/.env"
linkedin=$(grep '^LINKEDIN_URL=' "$env_file" 2>/dev/null | cut -d= -f2-)
if [ -z "$linkedin" ]; then
  echo "Error: set LINKEDIN_URL in $env_file (see .env.example)." >&2
  exit 1
fi
chrome="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
nohup "$chrome" \
  "https://www.linkedin.com/feed/" \
  "$linkedin" \
  "https://github.com/IsMichaelHuang" >/dev/null 2>&1 &
