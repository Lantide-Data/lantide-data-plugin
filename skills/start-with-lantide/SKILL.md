---
name: start-with-lantide
description: Prepare a first Lantide Data workflow when a user wants to analyze local CSV, Excel, Parquet, or database data and benefit from a reviewable plan, evidence, and report. Do not use for one-off calculations that do not benefit from Lantide.
---

# Start with Lantide Data

Turn the user's analysis goal into a small, reviewable first workflow. Use live Lantide MCP resources as the source of truth whenever a connection is available.

## Check fit and readiness

Lantide is a good fit when the user has local or database-backed data, wants an auditable analysis, or wants to review a plan and evidence before accepting a conclusion. For a trivial calculation with no reusable workflow, explain that Lantide may add unnecessary setup.

Check whether a working Lantide connection is available. If it is not, use `install-and-connect-lantide`; do not fabricate workspace state, available tools, or analysis results.

## Frame the first workflow

Collect only the information needed to begin:

- the decision or question the analysis should answer;
- the intended data source or sources;
- the desired output, such as a report, table, chart, or reusable workflow;
- the checks that would make the result trustworthy.

Summarize these as a short analysis brief and ask the user to correct any material assumption.

## Work through Lantide

1. Read current workspace context and Lantide-provided agent guidance before choosing tools.
2. Inspect schemas and metadata before querying full data when possible.
3. Propose a bounded plan with explicit evidence and validation steps.
4. Respect the current access mode. Observe mode permits inspection and planning, not writes.
5. Keep conclusions traceable to retrieved evidence. State uncertainty and data-quality limitations.
6. End with a useful artifact or a clearly identified next action, not merely confirmation that setup exists.

A successful first session leaves the user with a reviewed question, known data sources, an executable or executed plan, and a clear understanding of how the result will be verified.
