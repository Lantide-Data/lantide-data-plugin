# Lantide Data Marketplace listing

Portal-ready copy for the initial skills-only submission. The English fields are the publishing source of truth. The Traditional Chinese section is an internal review aid unless the submission portal explicitly supports localized listing copy.

## Portal fields

**Plugin name**

Lantide Data

**Developer**

Lantide Data

**Category**

Productivity

**Tagline**

Local-first data analysis you can review, trace, and reuse.

**Short description**

Connect Codex to reviewable local data workflows.

**Long description**

Connect Codex to Lantide Data and turn local CSV, Excel, Parquet, and database work into reviewable analysis. Get guided installation, user-approved local MCP pairing, safe troubleshooting, and a structured path from question to plan, evidence, and report.

Lantide Data keeps the analysis workflow visible: inspect the data context, review the plan, follow the SQL and validation evidence, and preserve the final report for another person or agent to continue. The desktop app controls the live tools, workspace context, and permissions.

This is a skills-only companion. It does not read your files, receive pairing credentials, or host a remote copy of your data by itself. Live analysis runs through Lantide Data Desktop on your machine and only within the connection scope you approve. Local-first does not mean every AI request is offline; model requests follow the provider and settings configured in Lantide Data.

## Introduction page

### Make AI analysis reviewable, traceable, and reusable

Lantide Data is a desktop analytics workspace for working with CSV, Excel, Parquet, and database data through SQL and AI. Instead of leaving the reasoning behind a result inside one chat, it keeps the question, plan, query logic, validation evidence, report, and activity together as analysis assets.

The Lantide Data companion plugin helps Codex:

- guide you through installing and safely connecting Lantide Data;
- request local MCP pairing without placing credentials in chat;
- frame a concrete analysis question and reviewable first plan;
- follow the live permissions and operating guidance exposed by Lantide Data;
- diagnose installation, pairing, port, credential, or reload problems safely.

### A connection you approve

On a supported local Codex client, the plugin asks Lantide Data to show its pairing dialog. You review the client, workspace scope, access mode, expiry, exposure, and Codex configuration destination before choosing **Approve & Connect**. Lantide creates and installs the credential locally only after your approval; the plugin does not receive it.

### From a question to a durable result

Use Lantide Data when the work benefits from more than a one-off answer. Start from the decision you need to make, identify the relevant sources, review a bounded plan, inspect the SQL and checks, and keep the resulting report available for follow-up or reruns.

### Requirements

- Lantide Data Desktop for macOS or Windows.
- A local Codex client for the guided Codex pairing path.
- User approval for the workspace scope and access mode requested in Lantide Data.
- A new Codex task or restart after installing a new MCP connection.

## Starter prompts

1. Connect Codex to my installed Lantide Data app and verify the local MCP connection.
2. Help me turn a folder of weekly CSV exports into a reusable Lantide analysis with a reviewable plan and validation checks.
3. Lantide Data is installed, but Codex cannot see its tools. Diagnose the connection without exposing credentials.

## Capability highlights

- Guided Lantide Data installation and onboarding.
- GUI-confirmed local Codex pairing.
- Reviewable analysis framing for CSV, Excel, Parquet, and database data.
- Safe connection troubleshooting without requesting secrets.
- Explicit handoff to Lantide's live tools, resources, permissions, and audit trail.

## Trust and data-handling disclosure

- The submitted plugin is skills-only and contains no remote MCP server.
- The plugin does not independently access local datasets or credentials.
- Lantide Data Desktop is the source of truth for live capabilities and permissions.
- Pairing requires a user-confirmed Lantide dialog; cancellation creates no connection.
- The connection credential is written locally and is not copied into chat during the supported pairing flow.
- AI features may send necessary context to the model endpoint configured by the user; local-first should not be described as fully offline.

## Public links and assets

- Website: <https://lantidedata.com/en>
- Download: <https://lantidedata.com/en/download>
- Support: <https://lantidedata.com/en/contact>
- Privacy policy: <https://lantidedata.com/en/privacy>
- Terms of service: <https://lantidedata.com/en/terms>
- Repository: <https://github.com/Lantide-Data/lantide-data-plugin>
- Logo: `assets/logo.png`
- Composer icon: `assets/icon.png`
- Brand color: `#3388FC`

## Initial release notes

Initial skills-only release of the Lantide Data companion plugin. It guides users through installing and securely connecting Lantide Data, starting a reviewable local-first analysis workflow, and troubleshooting local MCP setup. On supported Codex clients, pairing uses a user-approved Lantide dialog and keeps the credential out of chat.

## Traditional Chinese review copy

**標語**

讓本機 AI 數據分析可審閱、可追溯、可重用。

**短描述**

安全連接 Codex 與可審閱的本機數據工作流程。

**長描述**

將 Codex 連接到 Lantide Data，讓本機 CSV、Excel、Parquet 與資料庫工作成為可審閱的分析。Plugin 提供安裝引導、由使用者核准的本機 MCP 配對、安全的連線排錯，以及從問題、計畫、證據到報告的結構化起步流程。

Lantide Data 會保留可見的分析脈絡：你可以檢查資料環境、審閱計畫、追蹤 SQL 與驗證證據，並保存能由其他人或 Agent 延續的報告。Desktop app 負責即時工具、workspace 脈絡與權限控制。

這是一個 skills-only companion，本身不會讀取檔案、取得配對憑證，也不會在遠端保存你的資料。實際分析透過你電腦上的 Lantide Data Desktop 執行，而且只會使用你核准的連線範圍。本機優先不代表所有 AI 請求都離線；模型請求仍依照使用者在 Lantide Data 中設定的供應商與選項處理。
