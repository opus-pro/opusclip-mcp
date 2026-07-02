# Installing the OpusClip MCP server

OpusClip is a **remote** MCP server — it is hosted, so there is nothing to build or
run locally. Authentication is **OAuth**, handled in the browser on first use. No API
keys or environment variables are required.

## Add it to Cline

Cline connects to remote servers over Streamable HTTP. Add this to
`cline_mcp_settings.json` (Cline panel → MCP Servers → Configure → Configure MCP Servers),
or use the **Remote Servers** tab: Server Name `opusclip`, Server URL
`https://mcp.opus.pro/mcp`, Add Server.

```json
{
  "mcpServers": {
    "opusclip": {
      "type": "streamableHttp",
      "url": "https://mcp.opus.pro/mcp",
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

No token or `headers` are needed — the server uses OAuth, and Cline opens the browser
sign-in automatically on the first tool call.

## Other MCP clients

Most clients accept the endpoint URL directly:

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
