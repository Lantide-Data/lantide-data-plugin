---
name: troubleshoot-lantide
description: Diagnose Lantide Desktop installation, launch, local MCP, pairing, port, credential, or version problems. Do not use for failures inside a successful data analysis workflow unless connection health is the likely cause.
---

# Troubleshoot Lantide Data

Find the failing layer before suggesting a change. Use non-sensitive checks and preserve Lantide's authentication and access controls.

## Isolate the layer

Check in this order:

1. **Installation:** the operating system is supported and the official application is installed.
2. **Application readiness:** Lantide launches and Agent Integration is enabled.
3. **Local endpoint:** the configured local MCP endpoint is reachable from the same machine and client context.
4. **Pairing:** the client configuration matches the endpoint and the credential is current.
5. **Protocol:** the client can initialize MCP and list the capabilities exposed by the running Lantide version.

Report which checks were actually performed and which rely on user confirmation.

## Safe remediation

- Prefer reopening Agent Integration and creating a fresh pairing over exposing or editing a credential in chat.
- Check for stale client configuration, a changed local port, multiple running app versions, or a client that needs to reload its MCP configuration.
- Recommend the minimum access mode needed. Never suggest Admin access as a generic connection fix.
- Never ask the user to paste tokens, credentials, private file contents, or full configuration files containing secrets.
- Do not disable authentication, firewall protections, code signing, or operating-system security controls.
- Before reinstalling or deleting configuration, explain the impact and obtain confirmation.

After each change, retry only the failed layer, then perform a complete initialization check once it passes. When local inspection is unavailable, provide one short check at a time.

If the issue persists, record the app version, operating system, client name and version, the failing step, and a redacted error message. Direct the user to `support@lantidedata.com` without including credentials or sensitive data.
