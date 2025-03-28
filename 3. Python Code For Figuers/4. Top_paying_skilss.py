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

# SQL Query (Fetching Top 10 High-Paying Skills)
query = """
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
    LIMIT 10
"""

# Fetch Data into Pandas DataFrame
df = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()

# Sort Data for Visualization
df = df.sort_values(by="avg_salary", ascending=True)  # Sorting for a better horizontal plot

# Create the horizontal bar chart
plt.figure(figsize=(12, 8))
ax = sns.barplot(x="avg_salary", y="job_skills", data=df, palette="viridis")

# Add bar labels
for i in ax.containers:
    ax.bar_label(i, fmt='${:,.0f}', padding=5)

# Labels and Title
plt.xlabel("Average Salary (USD)", fontsize=12)
plt.ylabel("Job Skills", fontsize=12)
plt.title("Top 10 Highest-Paying Skills for Data Analyst Roles", fontsize=14, fontweight="bold")

# Format x-axis with commas
plt.xticks(rotation=0)
plt.grid(axis="x", linestyle="--", alpha=0.7)

# Show Plot
plt.tight_layout()
plt.show()
