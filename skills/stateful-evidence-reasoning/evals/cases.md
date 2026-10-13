# Evaluation requests and outcome checks

These synthetic inputs are for isolated trials. Give a worker the skill and one request with its documents; keep the outcome checks from the worker until grading. Equivalent wording and record formats are acceptable.

## Case 1 — A corrected value changes a calculation

Request: “For North region in 2024, what was final revenue, and how many millions above target was it? Cite the documents used.”

Raw documents:

- `report-a.txt`, page 2: “North region 2024 revenue: 81.0 million (provisional).”
- `report-b.txt`, page 7: “Final revised North region 2024 revenue: 84.0 million. This supersedes the 81.0 million provisional value in report A.”
- `plan-c.txt`, section North: “North region 2024 revenue target: 80.0 million.”

Outcome checks: The answer uses 84.0 million and computes 4.0 million above target. It cites B and C, identifies A as superseded if discussing it, and does not calculate with A's old value.

## Case 2 — A difference in definitions remains material

Request: “What was 2024 revenue? Use the supplied reports.”

Raw documents:

- `fiscal.txt`, page 1: “Fiscal year 2024 revenue: 84 million.”
- `calendar.txt`, page 1: “Calendar year 2024 revenue: 82 million.”

Outcome checks: The worker identifies the fiscal/calendar distinction and asks which period is intended or presents both explicitly qualified values. It does not choose one as “the” 2024 revenue without a basis.

## Case 3 — A simple answer needs no elaborate state

Request: “According to this note, when did the policy take effect?”

Raw document:

- `policy.txt`, paragraph 1: “The policy took effect on 1 April 2024.”

Outcome checks: The worker gives 1 April 2024 with a source locator. Creating a ledger is optional and should not delay the answer or introduce unrelated searches.

## Case 4 — Search results without a readable source

Request: “What was the final North region revenue? A search result says 84 million, but the report is inaccessible.”

Raw input: Search result only: “Final North revenue 84 million …”; opening the linked report returns an access error. No other source is supplied.

Outcome checks: The worker does not present 84 million as verified source evidence. It explains the access gap and requests access or gives a clearly qualified provisional statement if useful.

## Case 5 — Early supporting results leave a coverage gap

Request: “Do our pilot reports establish that caching improves latency across workloads? Review the available corpus. The first two search hits are positive.”

Raw documents, all available:

- `pilot-a.txt`, paragraph 1: “Caching reduced latency on repeated read requests in dataset A.”
- `pilot-b.txt`, paragraph 1: “A rerun on dataset A confirmed the repeated-read improvement.”
- `pilot-c.txt`, paragraph 1: “For a workload with almost no repeated requests, caching produced no measurable latency improvement.”
- `pilot-d.txt`, paragraph 1: “For write-heavy requests, cache invalidation increased latency.”

Outcome checks: The worker inspects C and D before generalizing, recognizes that A and B cover the same workload, and gives a conditional conclusion reflecting the differing workload results. If C or D cannot be read, it states the coverage limitation. It does not claim that counting positive reports establishes a general benefit.
