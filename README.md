# OpusClip MCP

Turn long videos into AI-curated short clips — from your agent. Submit a video file or
URL and OpusClip finds the best moments, adds captions, reframes to vertical, and returns
ready-to-post clips. It can also generate thumbnails and social copy, pull transcripts,
and schedule posts to your connected social accounts.

**OpusClip is a hosted (remote) MCP server** — nothing to build or run locally.
Authentication is OAuth, handled in the browser on first use. No API keys required.

- **Endpoint:** `https://mcp.opus.pro/mcp` (Streamable HTTP + OAuth)
- **Docs:** https://help.opus.pro/api-reference/agent-setup

## Quick start

Add OpusClip to your MCP client's config:

```json
{
  "mcpServers": {
    "opusclip": {
      "url": "https://mcp.opus.pro/mcp"
    }
  }
}
```

For stdio-only clients, use the npm launcher instead:

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

On the first tool call, a browser window opens to sign in to your OpusClip account and
approve access.

### Per-client setup

| Client | How |
| --- | --- |
| **Claude.ai / Claude Desktop** | Settings → Connectors → add a custom connector with the URL above |
| **Cursor** | Settings → Tools & MCP → New MCP Server, or the one-click **Add to Cursor** button in our [docs](https://help.opus.pro/api-reference/agent-setup) |
| **Cline** | Add the config above to `cline_mcp_settings.json` (see [llms-install.md](./llms-install.md)) |
| **Claude Code** | `claude mcp add --transport http opusclip https://mcp.opus.pro/mcp` |

## What you can do

- **Curate** — submit a video (file or URL) and get AI-picked clips scored for virality
- **Edit** — apply an editing script (trim, reframe, layout, captions) to a clip
- **Caption & transcript** — pull the transcript, generate styled captions
- **Thumbnails** — generate thumbnail options for a clip
- **Social copy** — generate titles, descriptions, and hashtags per platform
- **Collections** — group clips and export them
- **Schedule & publish** — post or schedule clips to connected social accounts
- **Usage** — check your remaining credits and plan

See the full tool reference in the [OpusClip API docs](https://help.opus.pro/api-reference/agent-setup).

## Registry

This server is listed in the official MCP Registry as `io.github.opus-pro/opusclip`
(see [`server.json`](./server.json)).

## License

[MIT](./LICENSE) © Opus Pro, Inc.
