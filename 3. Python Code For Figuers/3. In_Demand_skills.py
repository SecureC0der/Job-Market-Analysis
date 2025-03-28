import pandas as pd
import psycopg2
import matplotlib.pyplot as plt

# Database connection details (Update with your credentials)
conn = psycopg2.connect(
    dbname="admin",      
    user="admin",        
    password="admin",    
    host="localhost",            
    port="5432"                  
)

# SQL Query (Fetching Top 5 Skills for Data Analysts)
query = """
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
    SELECT 
        skills_dim.skills,
        top_skills.skills_count
    FROM 
        skills_dim
    INNER JOIN
        top_skills ON skills_dim.skill_id = top_skills.skill_ID
    ORDER BY 
        top_skills.skills_count DESC
    LIMIT 5;
"""

# Fetch Data into Pandas DataFrame
df = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()

# Define colors and explode settings for better visualization
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0']
explode = (0.1, 0, 0, 0, 0)  # Explode the first slice for emphasis

# Create a pie chart
plt.figure(figsize=(10, 6))
plt.pie(
    df["skills_count"], 
    labels=df["skills"], 
    autopct="%1.1f%%", 
    colors=colors, 
    explode=explode,
    startangle=140, 
    shadow=True, 
    wedgeprops={'edgecolor': 'black'}
)

# Title
plt.title("Top 5 Skills for Data Analyst Roles", fontsize=14, fontweight="bold")

# Show Plot
plt.tight_layout()
plt.show()
