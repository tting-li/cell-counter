SELECT 
    p.project_id,
    COUNT(s.sample_id) AS sample_count
FROM 
    samples s
JOIN 
    projects p ON s.project_id = p.project_id
JOIN 
    subjects sb ON s.subject_id = 'cancer'
JOIN 
    treatments t ON s.treatment_id = t.treatment_id
GROUP BY 
    p.project_id;