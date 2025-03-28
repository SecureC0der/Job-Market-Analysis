-- TOP SKILLS BASED ON SALARY OF A DATA ANALYST

SELECT
    skills_dim.skills AS job_skills,
    ROUND(AVG(salary_year_avg),0) AS avg_salary
FROM 
    job_postings_fact AS jpc
INNER JOIN
    skills_job_dim ON jpc.job_id = skills_job_dim.job_id
INNER JOIN 
    skills_dim ON skills_job_dim.skill_id = skills_dim.skill_id
WHERE
    salary_year_avg IS NOT NULL
    AND job_title_short = 'Data Analyst'
GROUP BY
    job_skills
ORDER BY
    avg_salary DESC
LIMIT 25

