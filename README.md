# Lantide Data plugin

The Lantide Data plugin helps people discover, install, connect, troubleshoot, and start using [Lantide Data](https://lantidedata.com/en) for local-first, reviewable AI data analysis.

This repository is the public integration layer. Lantide Data itself remains the source of truth for live tools, workspace context, permissions, and analysis behavior.

## What is included

- `install-and-connect-lantide`: safe installation and least-privilege local pairing guidance.
- `start-with-lantide`: a guided path from a data question to a reviewable first workflow.
- `troubleshoot-lantide`: connection and setup diagnosis without exposing credentials.

The initial release is skills-only. It does not access local data by itself and does not embed a remote MCP server. Live analysis requires Lantide Data Desktop and its local Agent Integration.

Portal-ready Marketplace copy is maintained in [`submission/marketplace-listing.md`](submission/marketplace-listing.md). The manifest carries the same short description, long description, and starter prompts so the personal Marketplace preview stays aligned with the submission draft.

## Connection defaults

The plugin follows Lantide's in-app connection model. A trusted agent onboarding a new or empty installation uses the current Create connection default: **Persistent + All workspaces + Admin**, so it can establish the workspace and complete a useful first workflow. For an existing, clearly scoped workspace, **Single workspace + Execute** is the bounded formal-analysis path. **Observe** is reserved for explicitly read-only evaluation or review; it is not the generic new-user default.

The user confirms scope and access mode in Lantide. Admin does not bypass Plan lifecycle, evidence, Report, Activity, or audit requirements.

On supported local Codex clients, the install skill opens Lantide's GUI-confirmed configure deep link. Lantide shows the requested access and Codex config destination; only the user's **Approve & Connect** action creates the persistent credential and updates the local MCP setting. The plugin never creates or receives the credential, and the existing one-time Copy flow remains the fallback.

## Development

Requirements: Python 3.9 or newer.

```bash
python3 scripts/validate.py
```

The validator checks the plugin manifest, skill metadata, referenced assets, and repository layout. During Codex plugin development, also run the current official plugin and skill validators available in your Codex installation.

## Security

Never include a Lantide pairing credential, private dataset, or unredacted client configuration in an issue. See [SECURITY.md](SECURITY.md) for responsible disclosure instructions.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). By participating, you agree to keep contributions provider-neutral and compatible with least-privilege local workflows.

## License

[MIT](LICENSE) © 2026 Lantide Data.
