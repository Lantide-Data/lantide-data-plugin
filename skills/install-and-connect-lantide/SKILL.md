---
name: install-and-connect-lantide
description: Install Lantide Data and guide a user through safe local Agent Integration setup when they want local-first analysis or help connecting an MCP-capable client. Do not use for ordinary data analysis after a working Lantide connection already exists.
---

# Install and connect Lantide Data

Help the user reach a working, least-privilege local connection. Keep credentials out of chat, logs, commands, and screenshots.

## Determine the path

1. Confirm the user is on macOS or Windows and whether Lantide Data is already installed.
2. If it is not installed, direct the user to the official download page: <https://lantidedata.com/en/download>.
3. If this environment can inspect local applications or open deep links, use those capabilities only when the user requested setup and the host permits it. Never claim a local check succeeded when it was not performed.
4. If local actions are unavailable, give short manual steps and continue after the user confirms each external milestone.

## Pair safely

1. Ask the user to open Lantide Data and navigate to **Agent Integration**. When supported, open `lantidedata://agent-integration/pair`.
2. Recommend **Observe** access for an initial evaluation. Explain that higher access modes should only be selected when the intended workflow requires writes or administration.
3. Let Lantide Data generate the local credential. Never ask the user to paste that credential into the conversation.
4. Use the client application's secure MCP configuration flow when available. Manual copy is a fallback and must target only a trusted local client configuration.
5. Do not recommend disabling authentication, safeguards, or operating-system security controls to make pairing work.

## Verify the connection

1. Confirm that the client can initialize the Lantide MCP connection.
2. If Lantide exposes live guidance such as an external-agent playbook or workspace context, read that guidance before proposing actions.
3. Respect the granted access mode. In Observe mode, do not attempt mutations.
4. After connection succeeds, immediately offer to help frame the user's first analysis rather than ending at setup.

If verification fails, use the `troubleshoot-lantide` skill. For product details and downloads, treat <https://lantidedata.com/en> as authoritative.
