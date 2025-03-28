-- Top 10 highest-paying Data Analyst job postings available remotely

SELECT
    cd.name AS company_name,
    job_location,
    salary_year_avg,
    job_schedule_type
FROM job_postings_fact
LEFT JOIN
    company_dim AS cd ON job_postings_fact.company_id = cd.company_id 
WHERE
    salary_year_avg IS NOT NULL
    AND job_title_short = 'Data Analyst'
    AND job_location = 'Anywhere'
ORDER BY 
    salary_year_avg DESC
LIMIT 10


