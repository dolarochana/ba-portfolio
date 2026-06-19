# Customer Segmentation — K-Means Personas

**Portfolio recreation on public data** (e.g. Kaggle "Mall Customer" / "Customer Personality" datasets). The original retail-banking engagement used confidential data; this reproduces the segmentation methodology.

## Business problem
A retail bank sent identical marketing offers to its entire customer base, producing a low (~2.1%) campaign response rate. There was no actionable way to target offers by customer value.

## BA approach
1. Facilitated a segmentation-criteria workshop with Marketing to agree on the dimensions that mattered (balance, transaction frequency, product holdings).
2. Ran K-Means clustering in Python to group customers into distinct, actionable segments.
3. Defined 4 named personas with Marketing (Dormant, Regular, Valuable, Premium) and recommended offers per tier.
4. Built a Tableau personas dashboard showing segment migration over time.

## What's in this folder
- `customer_segmentation.py` — K-Means pipeline: scaling, elbow method, cluster assignment, persona profiling

## Result (original engagement)
Targeted rollout improved campaign response from ~2.1% to ~6.4% within 3 months; adopted as the standard Marketing planning tool.

## Dashboard
[public.tableau.com/profile/rochana.dixit](https://public.tableau.com/profile/rochana.dixit)

*All figures illustrative, produced on public data to demonstrate methodology.*
