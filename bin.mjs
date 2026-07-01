#!/usr/bin/env node
// @opusclip/mcp — thin launcher.
// OpusClip runs as a hosted (remote) MCP server with OAuth. This wrapper just
// proxies a local stdio client to the hosted endpoint via mcp-remote, so clients
// that only speak stdio (or want a one-line `npx @opusclip/mcp` install) work too.
import { spawn } from 'node:child_process'

const ENDPOINT = 'https://mcp.opus.pro/mcp'

const child = spawn('npx', ['-y', 'mcp-remote', ENDPOINT, ...process.argv.slice(2)], {
  stdio: 'inherit',
})

child.on('exit', (code) => process.exit(code ?? 0))
child.on('error', (err) => {
  console.error('[opusclip-mcp] failed to launch mcp-remote:', err.message)
  process.exit(1)
})
