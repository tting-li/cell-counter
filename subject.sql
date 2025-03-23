SELECT conditions, COUNT(DISTINCT subject_id) AS subject_count
FROM subjects
GROUP BY conditions;