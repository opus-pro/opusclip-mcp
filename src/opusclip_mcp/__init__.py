"""opusclip-mcp — thin launcher for the hosted OpusClip MCP server.

OpusClip runs as a hosted (remote) MCP server with OAuth. This wrapper proxies a
local stdio client to the hosted endpoint via mcp-remote (a Node tool), so
clients that only speak stdio (or want a one-line `uvx opusclip-mcp` install)
work too.
"""

import shutil
import subprocess
import sys

ENDPOINT = "https://mcp.opus.pro/mcp"

NO_NODE_HINT = f"""\
opusclip-mcp: `npx` not found — the stdio proxy (mcp-remote) requires Node.js >= 18.

OpusClip is a hosted (remote) MCP server. If your client supports remote MCP
servers, you don't need this launcher at all — connect directly:

  {{"mcpServers": {{"opusclip": {{"url": "{ENDPOINT}"}}}}}}

Otherwise install Node.js (https://nodejs.org) and run `opusclip-mcp` again.
Docs: https://help.opus.pro/api-reference/agent-setup
"""


def main() -> None:
    npx = shutil.which("npx")
    if npx is None:
        sys.stderr.write(NO_NODE_HINT)
        raise SystemExit(1)
    try:
        proc = subprocess.run([npx, "-y", "mcp-remote", ENDPOINT, *sys.argv[1:]])
    except KeyboardInterrupt:
        raise SystemExit(130)
    raise SystemExit(proc.returncode)
