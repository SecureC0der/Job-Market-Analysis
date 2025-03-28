import psycopg2  # PostgreSQL connector
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Step 1: Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="admin",      # Replace with your actual database name
    user="admin",        # Replace with your PostgreSQL username
    password="123456",    # Replace with your PostgreSQL password
    host="localhost",            # Replace with your host (or server IP)
    port="5432"                  # Default PostgreSQL port
)

# Step 2: Define SQL Query
query = '''
    SELECT
    cd.name AS company_name,
    job_location,
    salary_year_avg
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

'''
# Step 3: Fetch Data into Pandas DataFrame
df = pd.read_sql(query, conn)

# Step 4: Close the Connection
conn.close()

# Step 5: Create a Bar Plot using Matplotlib
plt.style.use('ggplot')
plt.figure(figsize=(10, 6))


norm = plt.Normalize(df["salary_year_avg"].min(), df["salary_year_avg"].max())  # Normalize values
colors = cm.Blues(norm(df["salary_year_avg"]))  # Choose a colormap (Blues, Viridis, Plasma, etc.)

plt.barh(df["company_name"], df["salary_year_avg"], color=colors)

# Step 6: Customize the Plot
plt.xlabel("Average Salary (USD)", fontsize=12)
plt.ylabel("Company", fontsize=12)
plt.title("Top 10 High-Paying Remote Data Analyst Jobs", fontsize=14)
plt.gca().invert_yaxis()  # Invert to show highest salary on top
plt.grid(axis="x", linestyle="--", alpha=0.7)
plt.tight_layout()

# Step 7: Show the Plot
plt.show()
