---
name: install-and-connect-lantide
description: Install Lantide Data and guide a user through safe local Agent Integration setup when they want local-first analysis or help connecting an MCP-capable client. Do not use for ordinary data analysis after a working Lantide connection already exists.
---

# Install and connect Lantide Data

Help the user reach a working local connection that can complete the intended onboarding flow. Keep credentials out of chat, logs, commands, and screenshots.

## Determine the path

1. Confirm the user is on macOS or Windows and whether Lantide Data is already installed.
2. If it is not installed, direct the user to the official download page: <https://lantidedata.com/en/download>.
3. If this environment can inspect local applications or open deep links, use those capabilities only when the user requested setup and the host permits it. Never claim a local check succeeded when it was not performed.
4. If local actions are unavailable, give short manual steps and continue after the user confirms each external milestone.

## Pair safely

1. Prefer the code-based pairing request over GUI automation:
   - In a local Codex environment, open `lantidedata://agent-integration/pair?client=codex&source=openai-plugin&action=configure` with the host's safe external-URL capability or the operating-system URL opener. This only requests pairing; it does not create a credential.
   - Do not use computer-use or repeated GUI clicks to fill the persistent-connection form when the configure deep link is supported.
   - For other local clients, open the base `lantidedata://agent-integration/pair` route and use their supported secure handoff.
   - If local URL opening is unavailable, give the user the link or the short manual route: **Agent Integration → Persistent connections → Create connection**.
2. Match Lantide's in-app connection model instead of imposing a separate plugin default:
   - For a new, empty, or not-yet-configured installation with a trusted local agent, keep the Create connection default: **Persistent**, **All workspaces**, **Admin**. This permits the agent to discover, create, and select a workspace and finish the first useful workflow.
   - When a workspace already exists and the user wants bounded formal analysis, prefer **Single workspace + Execute**. Use **All workspaces + Execute** when discovery across workspaces is needed before selecting one.
   - Use **Observe** only when the user explicitly wants read-only inventory, low-trust evaluation, or review assistance. Do not make Observe the generic new-user default.
3. Explain that Admin is a capability ceiling, not permission to skip Plan review, evidence, Report, Activity, or audit. The user still confirms scope and access mode in Lantide.
4. For a Codex configure request, stop at Lantide's **Approve Codex connection** dialog. The user must review the client, scope, access mode, expiry, exposure, and Codex config destination, then personally choose **Approve & Connect** or cancel. Never click the approval on the user's behalf.
5. Let Lantide Data generate and install the local credential only after that approval. Never ask the user to paste it into the conversation or move it through shell arguments, URLs, logs, screenshots, or clipboard unless Lantide explicitly falls back to its one-time manual Copy flow.
6. After Lantide reports **Codex connection installed**, run `codex mcp list` if local shell access is available and report only connection status and server name. Tell the user that a new Codex task or restart is required before the newly configured MCP tools can appear.
7. If automatic configuration fails, use Lantide's one-time Copy fallback and target only a trusted local client configuration. Do not read or echo the copied credential.
8. Do not recommend disabling authentication, safeguards, or operating-system security controls to make pairing work.

## Verify the connection

1. Confirm that the client can initialize the Lantide MCP connection.
2. If Lantide exposes live guidance such as an external-agent playbook or workspace context, read that guidance before proposing actions.
3. Respect the granted access mode. In Observe mode, do not attempt mutations.
4. After connection succeeds, immediately offer to help frame the user's first analysis rather than ending at setup.

If verification fails, use the `troubleshoot-lantide` skill. For product details and downloads, treat <https://lantidedata.com/en> as authoritative.
