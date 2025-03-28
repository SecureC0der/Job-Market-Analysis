-- SKILLS REQUIERD FOR FOR TOP PAYING ROLES
SELECT
    jpc.job_id,
    jpc.job_title,
    skills_dim.skills AS skill_name,
    jpc.salary_year_avg
FROM 
    job_postings_fact AS jpc
INNER JOIN skills_job_dim ON jpc.job_id = skills_job_dim.job_id
INNER JOIN skills_dim ON skills_job_dim.skill_id = skills_dim.skill_id
WHERE
    jpc.salary_year_avg IS NOT NULL
    AND jpc.job_title_short = 'Data Analyst'
    AND jpc.job_location = 'Anywhere'
ORDER BY 
    jpc.salary_year_avg DESC
LIMIT 10;




