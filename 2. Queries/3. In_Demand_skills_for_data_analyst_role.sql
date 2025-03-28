-- MOST IN-DEMAND SKILLS FOR DATA ANALYST ROLE

WITH top_skills AS (
    SELECT 
        skill_ID,
        COUNT(*) AS skills_count
    FROM 
        job_postings_fact jpc
    INNER JOIN  
    skills_job_dim AS skills_to_job ON jpc.job_id = skills_to_job.job_id
    WHERE 
        job_title_short = 'Data Analyst'
    GROUP BY
        skill_id

)

SELECT skills_dim.skills,
        top_skills.skills_count
FROM 
    skills_dim
INNER JOIN
    top_skills ON skills_dim.skill_id = top_skills.skill_ID
LIMIT 5

