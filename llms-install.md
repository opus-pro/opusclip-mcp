# Installing the OpusClip MCP server

OpusClip is a **remote** MCP server — it is hosted, so there is nothing to build or
run locally. Authentication is **OAuth**, handled in the browser on first use. No API
keys or environment variables are required.

## Add it to your MCP client

Point your client at the hosted endpoint (Streamable HTTP):

```json
{
  "mcpServers": {
    "opusclip": {
      "url": "https://mcp.opus.pro/mcp"
    }
  }
}
```

For clients that only speak stdio, use the npm launcher instead:

```json
{
  "mcpServers": {
    "opusclip": {
      "command": "npx",
      "args": ["-y", "@opusclip/mcp"]
    }
  }
}
```

## First run

On the first tool call, a browser window opens to sign in to your OpusClip account and
approve access. After that, the agent can submit videos, curate and edit clips, generate
thumbnails and social copy, pull transcripts, and schedule posts to connected social
accounts.

Settings files by client: `.cursor/mcp.json` (Cursor), `cline_mcp_settings.json` (Cline),
`claude_desktop_config.json` (Claude Desktop).
