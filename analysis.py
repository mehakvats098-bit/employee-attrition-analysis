# 1. Import Libraries
import pandas as pd
import matplotlib.pyplot as plt


# 2. Load Dataset
data = pd.read_csv("data/employees.csv")


# 3. Data Inspection
print(data.head())
print(data.shape)
print(data.columns)
print(data.info())


# 4. Data Cleaning
print("Missing values:")
print(data.isnull().sum())

print("Duplicate rows:")
print(data.duplicated().sum())


# 5. Overall Attrition Analysis
print("Attrition Count:")
print(data["Attrition"].value_counts())

attrition_rate = (data["Attrition"] == "Yes").mean() * 100
print("Attrition Rate:", attrition_rate, "%")


# 6. Department Analysis
department_attrition = data.groupby("Department")["Attrition"].apply(
    lambda x: (x == "Yes").mean() * 100
)

print("Department Attrition Rate:")
print(department_attrition)


# 7. Overtime Analysis
overtime_attrition = data.groupby("Overtime")["Attrition"].apply(
    lambda x: (x == "Yes").mean() * 100
)

print("Overtime vs Attrition:")
print(overtime_attrition)


# 8. Job Satisfaction Analysis
satisfaction_attrition = data.groupby("Attrition")["Job_Satisfaction"].mean()

print("Job Satisfaction:")
print(satisfaction_attrition)


# 9. Years at Company Analysis
experience_attrition = data.groupby("Attrition")["Years_At_Company"].mean()

print("Years at Company:")
print(experience_attrition)


# 10. Work-Life Balance Analysis
worklife_attrition = data.groupby("Attrition")["Work_Life_Balance"].mean()

print("Work-Life Balance:")
print(worklife_attrition)


# 11. Monthly Income Analysis
income_attrition = data.groupby("Attrition")["Monthly_Income"].mean()

print("Monthly Income:")
print(income_attrition)


# 12. Visualizations

# Attrition Distribution
attrition_counts = data["Attrition"].value_counts()

attrition_counts.plot(kind="bar")
plt.title("Employee Attrition Distribution")
plt.xlabel("Attrition")
plt.ylabel("Number of Employees")
plt.savefig("charts/attrition_distribution.png")
plt.show()


# Attrition by Department
department_attrition.plot(kind="bar")
plt.title("Attrition by Department")
plt.xlabel("Department")
plt.ylabel("Attrition Rate (%)")
plt.savefig("charts/attrition_by_department.png")
plt.show()


# Overtime vs Attrition
overtime_attrition.plot(kind="bar")
plt.title("Attrition Rate by Overtime")
plt.xlabel("Overtime")
plt.ylabel("Attrition Rate (%)")
plt.savefig("charts/overtime_vs_attrition.png")
plt.show()


# Job Satisfaction vs Attrition
satisfaction_attrition.plot(kind="bar")
plt.title("Job Satisfaction vs Attrition")
plt.xlabel("Attrition")
plt.ylabel("Average Job Satisfaction")
plt.savefig("charts/job_satisfaction_vs_attrition.png")
plt.show()


# Years at Company vs Attrition
experience_attrition.plot(kind="bar")
plt.title("Years at Company vs Attrition")
plt.xlabel("Attrition")
plt.ylabel("Average Years at Company")
plt.savefig("charts/years_at_company_vs_attrition.png")
plt.show()


# Work-Life Balance vs Attrition
worklife_attrition.plot(kind="bar")
plt.title("Work-Life Balance vs Attrition")
plt.xlabel("Attrition")
plt.ylabel("Average Work-Life Balance")
plt.savefig("charts/worklife_balance_vs_attrition.png")
plt.show()


# Monthly Income vs Attrition
income_attrition.plot(kind="bar")
plt.title("Monthly Income vs Attrition")
plt.xlabel("Attrition")
plt.ylabel("Average Monthly Income")
plt.savefig("charts/monthly_income_vs_attrition.png")
plt.show()