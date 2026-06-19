# Healthcare Claims Denial Analysis

**Portfolio recreation on public/synthetic claims data.** The original engagement was delivered on confidential client data; this version reproduces the methodology and dashboard design using openly available data (e.g. CMS Synthetic Public Use Files / public Kaggle claims datasets).

## Business problem

A healthcare client faced a claim denial rate far above the industry benchmark, driving significant annual rework cost. Stakeholders held conflicting hypotheses about the root cause, and no agreed analysis existed to settle the question.

## BA approach

1. **Stakeholder interviews** to surface the competing hypotheses and define what a "denial" meant across teams.
2. **Exploratory data analysis** (SQL + Python) on claims records to quantify denial drivers rather than argue them.
3. **Root-cause identification** — isolated the top denial categories (prior authorization, eligibility, duplicate submission) by share of total denials.
4. **Process redesign** — mapped the as-is submission workflow and a to-be flow that addressed the root causes.
5. **Executive presentation** (SCQA structure) to drive a decision in the room.

## What's in this folder

- `claims_denial_analysis.sql` — aggregation queries: denial rate, denials by reason, by provider/payer, by procedure
- `claims_eda.py` — Python EDA: load, clean, denial-driver breakdown, turnaround-time outliers
- `README.md` — this file

## Result (original engagement)

Denial rate reduced from ~43% to ~19% within 90 days of the redesigned workflow, eliminating the bulk of the rework cost.

## Dashboard

Interactive Tableau version: [public.tableau.com/profile/rochana.dixit](https://public.tableau.com/profile/rochana.dixit)

## Note on data

All figures in this repository are illustrative, produced on public/synthetic data. They demonstrate the analytical approach, not actual client outcomes.
