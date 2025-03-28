import pandas as pd
import psycopg2
import matplotlib.pyplot as plt
import seaborn as sns

# Database connection details (Update with your credentials)
conn = psycopg2.connect(
    dbname="admin",      
    user="admin",        
    password="admin",    
    host="localhost",            
    port="5432"                  
)

# SQL Query (Fetching Top 25 High-Paying Skills with Demand)
query = """
    SELECT
        skills_dim.skill_ID,
        skills_dim.skills,
        COUNT(skills_job_dim.job_id) AS demand_count,
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
"""

# Fetch Data into Pandas DataFrame
df = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()

# Set figure size
plt.figure(figsize=(14, 8))

# Create a bubble chart
sns.scatterplot(
    x="skills", 
    y="average_salary", 
    size="demand_count", 
    hue="average_salary", 
    data=df, 
    palette="coolwarm", 
    sizes=(50, 1000), 
    edgecolor="black", 
    alpha=0.7
)

# Labels and Title
plt.xlabel("Skills", fontsize=12)
plt.ylabel("Average Salary (USD)", fontsize=12)
plt.title("Top 25 Highest-Paying Skills for Data Analysts", fontsize=14, fontweight="bold")

# Rotate x-axis labels for better visibility
plt.xticks(rotation=75, ha="right")

# Add grid lines
plt.grid(axis="y", linestyle="--", alpha=0.6)

# Show Plot
plt.tight_layout()
plt.show()
