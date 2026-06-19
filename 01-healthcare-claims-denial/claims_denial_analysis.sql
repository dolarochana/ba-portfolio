-- Healthcare Claims Denial Analysis
-- Portfolio recreation on public/synthetic claims data.
-- Demonstrates the SQL aggregation approach used to quantify denial drivers.
-- Column names assume a typical claims table; adjust to your dataset.

-- =====================================================================
-- 1. Overall denial rate
-- =====================================================================
SELECT
    COUNT(*)                                            AS total_claims,
    SUM(CASE WHEN claim_status = 'Denied' THEN 1 ELSE 0 END) AS denied_claims,
    ROUND(
        100.0 * SUM(CASE WHEN claim_status = 'Denied' THEN 1 ELSE 0 END) / COUNT(*),
        1
    )                                                   AS denial_rate_pct
FROM claims;

-- =====================================================================
-- 2. Denials by reason  (the root-cause breakdown)
--    Identifies which categories drive the most denials.
-- =====================================================================
SELECT
    denial_reason,
    COUNT(*)                                            AS denied_count,
    ROUND(
        100.0 * COUNT(*) / SUM(COUNT(*)) OVER (),
        1
    )                                                   AS pct_of_denials
FROM claims
WHERE claim_status = 'Denied'
GROUP BY denial_reason
ORDER BY denied_count DESC;

-- =====================================================================
-- 3. Denial rate by provider  (operational drill-down)
-- =====================================================================
SELECT
    provider,
    COUNT(*)                                            AS total_claims,
    SUM(CASE WHEN claim_status = 'Denied' THEN 1 ELSE 0 END) AS denied_claims,
    ROUND(
        100.0 * SUM(CASE WHEN claim_status = 'Denied' THEN 1 ELSE 0 END) / COUNT(*),
        1
    )                                                   AS denial_rate_pct
FROM claims
GROUP BY provider
HAVING COUNT(*) >= 30          -- focus on providers with meaningful volume
ORDER BY denial_rate_pct DESC;

-- =====================================================================
-- 4. Denial rate by payer
-- =====================================================================
SELECT
    payer,
    COUNT(*)                                            AS total_claims,
    ROUND(
        100.0 * SUM(CASE WHEN claim_status = 'Denied' THEN 1 ELSE 0 END) / COUNT(*),
        1
    )                                                   AS denial_rate_pct
FROM claims
GROUP BY payer
ORDER BY denial_rate_pct DESC;

-- =====================================================================
-- 5. Monthly denial trend  (is it improving over time?)
-- =====================================================================
SELECT
    DATE_TRUNC('month', submission_date)                AS claim_month,
    COUNT(*)                                            AS total_claims,
    SUM(CASE WHEN claim_status = 'Denied' THEN 1 ELSE 0 END) AS denied_claims,
    ROUND(
        100.0 * SUM(CASE WHEN claim_status = 'Denied' THEN 1 ELSE 0 END) / COUNT(*),
        1
    )                                                   AS denial_rate_pct
FROM claims
GROUP BY DATE_TRUNC('month', submission_date)
ORDER BY claim_month;

-- =====================================================================
-- 6. Average turnaround time by claim status (bottleneck check)
-- =====================================================================
SELECT
    claim_status,
    ROUND(AVG(processed_date - submission_date), 1)     AS avg_turnaround_days,
    MAX(processed_date - submission_date)               AS max_turnaround_days
FROM claims
WHERE processed_date IS NOT NULL
GROUP BY claim_status
ORDER BY avg_turnaround_days DESC;
