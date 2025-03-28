SELECT
    skills_dim.skill_ID,
    skills_dim.skills,
    COUNT(skills_job_dim.job_id) demand_count,
    ROUND(AVG(job_postings_fact.salary_year_avg),0) AS average_salary
FROM 
    job_postings_fact
INNER JOIN
    skills_job_dim ON job_postings_fact.job_id = skills_job_dim.job_id
INNER JOIN
    skills_dim ON skills_job_dim.skill_id = skills_dim.skill_id
WHERE 
    job_title_short = 'Data Analyst' AND
    salary_year_avg IS NOT NULL
GROUP BY
    skills_dim.skill_ID,
    skills_dim.skills
HAVING
    COUNT(skills_job_dim.job_id) > 10
ORDER BY
    average_salary DESC
LIMIT 25