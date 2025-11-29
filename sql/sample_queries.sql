-- sql/sample_queries.sql

-- Example queries that might be used in a panel-data research workflow.

-- 1. Average outcome by treatment status
SELECT
    treated,
    AVG(y) AS avg_outcome
FROM sim_panel
GROUP BY treated;

-- 2. Average outcome by period and treatment
SELECT
    time,
    treated,
    AVG(y) AS avg_outcome
FROM sim_panel
GROUP BY time, treated
ORDER BY time, treated;

-- 3. Simple pre/post comparison for treated units
SELECT
    post,
    AVG(y) AS avg_outcome_treated
FROM sim_panel
WHERE treated = 1
GROUP BY post
ORDER BY post;
