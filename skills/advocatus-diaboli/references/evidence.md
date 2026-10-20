# Evidence and rule derivation

Reviewed and accessed: 2026-10-20. Intended environment: a tool-capable agent acting as a critical thinking partner for ideas, decisions, and arguments. Targeted review, not a systematic review. Rules are a synthesis; the completed skill has not been experimentally tested for decision quality. The initial German package was translated into English for distribution, retaining its operational constraints and evidence limitations.

## Search coverage

Queries included “Nemeth Brown Rogers 2001 devil advocate authentic dissent”, “Lord Lepper Preston 1984 considering the opposite”, “large language models self correction without external feedback”, “Towards understanding sycophancy”, “Productive conflict in group decision making 2002”, and “2025 2026 LLM devil advocate critical thinking sycophancy evaluation study”. Decisions examined: role-playing versus substantive disagreement, concrete counterhypotheses, verification, and responses to user disagreement. Primary sources were opened; search snippets alone were not accepted as evidence.

## E01 — Role-playing does not guarantee productive dissent

Nemeth, Brown & Rogers (2001), [Devil’s advocate versus authentic dissent](https://onlinelibrary.wiley.com/doi/10.1002/ejsp.58), published 2001-11-13. Abstract and bibliography inspected. The abstract reports better solution quantity and quality with an authentic minority than with three assigned advocate roles. Full methods and exact sample were not examined, limiting claims about effect sizes and group processes. Human laboratory findings do not validate an LLM prompt. Design inference: do not require rejection or pretend to hold a sincere opposing belief. Assigned critique may still produce useful information; this source does not justify banning it.

## E02 — Concrete opposing possibilities rather than generic impartiality

Lord, Lepper & Preston (1984), [Considering the Opposite](https://www.researchgate.net/profile/Mark-Lepper-2/publication/16669522_Considering_the_Opposite_A_Corrective_Strategy_for_Social_Judgment/links/56107d7508ae48337519fedb/Considering-the-Opposite-A-Corrective-Strategy-for-Social-Judgment.pdf), JPSP 47, 1231–1243. Author-hosted copy; abstract and Experiment 1 methods and initial results on p. 1233 inspected. That experiment involved 120 Stanford undergraduates, three instruction conditions, and opposing initial attitudes. The abstract reports advantages of considering the opposite over impartiality appeals across two experiments. Replication coverage and LLM effectiveness were not assessed. Rule: specify a competing explanation and a disconfirming observation. Transfer to current agents remains a hypothesis to test.

## E03 — Self-correction can degrade correct answers

Huang et al., [Large Language Models Cannot Self-Correct Reasoning Yet](https://proceedings.iclr.cc/paper_files/paper/2024/file/8b4add8b0aa8749d80a34ca5d941c355-Paper-Conference.pdf), ICLR 2024. Sections 3.1–3.3 and Tables 2–3 inspected. Historical GPT and Llama models were evaluated on benchmarks including GSM8K, CommonSenseQA, and HotpotQA, with up to two correction rounds. Without correct labels as a stopping signal, performance degraded in the reported comparisons. Sampling and decoding differences and historical model versions limit transfer. Rule: do not present reconsideration as verification; seek checkable conditions. This is not a universal impossibility claim; see E04.

## E04 — Counterevidence: structured condition verification

[Large Language Models Can Self-Correct with Key Condition Verification](https://aclanthology.org/2024.emnlp-main.714/), EMNLP 2024. Abstract and [PDF](https://aclanthology.org/2024.emnlp-main.714.pdf), Sections 3–4, inspected. PROCO masks a key condition and reconstructs it using the proposed answer; the abstract reports improvements. Full result tables and uncertainty analyses were not inspected here. A specific method does not establish the value of arbitrary self-criticism. Together with E03, this supports a narrower design: check concrete conditions and permit corrections, without upgrading unverified reflection to evidence. This skill does not implement PROCO.

## E05 — User disagreement is not evidence of truth

Sharma et al., [Towards Understanding Sycophancy in Language Models](https://arxiv.org/html/2310.13548v2), first published 2023-10-20; inspected version v2. Sections 3.2–3.3 describe challenges and suggested answers influencing historical assistants across QA datasets, including abandonment of correct answers. Methods and reported findings inspected; no full reproduction. This motivates distinguishing social pressure from new evidence, but does not establish immunity through instructions. Users may be right; verifiable corrections must lead to revision.

## E06 — More recent evidence on conversational framing

[Challenging the Evaluator: LLM Sycophancy Under User Rebuttal](https://aclanthology.org/2025.findings-emnlp.1222/), Findings of EMNLP 2025. Publisher page and abstract inspected. Reports greater endorsement of counterarguments framed as user follow-ups than when positions were evaluated simultaneously, including incorrect conclusions. Abstract-only coverage: effect sizes and full model coverage were not independently assessed. Cautious inference: assess both positions by the same standard and tie revisions to substantive reasons. This does not establish an optimal prompt.

## Gaps and rejected generalizations

Schulz-Hardt, Jochims & Frey (2002), [Productive conflict in group decision making](https://www.sciencedirect.com/science/article/pii/S0749597802000018): direct access returned HTTP 403. A search excerpt flagged limitations in transferring Nemeth's findings to interacting groups. Not used as a verified effectiveness finding. Newer 2026 search results were screened but not methodologically assessed; recency searching is not comprehensive coverage. No causal claim is made about this skill or current Codex models. No adequate comparison justified mandatory multi-agent debate, fixed objection counts, or numerical risk scores, so none is required.

## Evidence to behavior

| Condition → action | Basis / type | Applicability and counterweight | Observable check |
|---|---|---|---|
| Critique requested → reconstruct the claim fairly | E01 + engineering inference | No empirically established universal sequence | Criticism addresses the actual promised outcome |
| Load-bearing assumption → counterhypothesis and distinguishing test | E02, transfer | Hypothesis is not a finding | Test could also defeat the objection |
| Self-criticism → inspect reliable data or conditions | E03/E04, synthesis | Specific self-verification may help | Checks distinguished from conjectures |
| User disagrees → assess substance and revise when warranted | E05/E06, synthesis | No stubbornness for its own sake | Reason for revision identified |
| No material objection → let the result stand | E01/E03 + engineering inference | Only within the examined scope | No fabricated criticism or guarantee |
| Multiple risks → prioritize decision impact | Engineering inference | Severe harm need not be likely | Decisive objection precedes trivia |
| Alternative proposed → apply the same standard and inspect its costs | Engineering inference | Values are not solely empirical questions | Alternative receives comparable scrutiny |
| Missing information → conditional judgment and next check | Engineering inference | Ask only decision-relevant questions | No invented figures or sources |
| Further criticism changes nothing → stop | Engineering inference | New evidence may justify reopening | No endless objection loop |
| Critique request → retain task boundaries | Scope requirement / engineering | Separately authorized actions remain possible | No unsolicited mutation |
| English package for broad critical sparring | User preference | No professional representation promised | Language and task match |

## Refresh triggers

Revisit affected rules and tests after observed capitulation, fabricated criticism, new credible comparative studies, or a major model change. Open questions: actual decision improvements, useful-to-false objection ratio, cost relative to an ordinary review, and stability across conversation turns. No recurring update schedule is implied.
