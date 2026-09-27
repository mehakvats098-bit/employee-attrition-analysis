# Employee Attrition Analysis

## Project Overview

This project analyzes employee data using Python and Pandas to identify patterns associated with employee attrition.

The analysis focuses on factors such as department, overtime, job satisfaction, years at the company, work-life balance, and monthly income.

> Note: This project uses a small practice dataset created for learning purposes and does not represent real employee data.

## Objective

The objective of this project is to:

- Calculate the overall employee attrition rate
- Analyze attrition across departments
- Compare overtime with attrition
- Compare job satisfaction between employees who stayed and left
- Analyze employee tenure and attrition
- Analyze work-life balance and attrition
- Compare monthly income between employees who stayed and left
- Create visualizations to communicate the findings

## Dataset

The dataset contains 20 employee records and 10 columns:

- Employee_ID
- Age
- Department
- Job_Role
- Monthly_Income
- Years_At_Company
- Job_Satisfaction
- Overtime
- Work_Life_Balance
- Attrition

## Tools & Technologies

- Python
- Pandas
- Matplotlib
- VS Code
- Git & GitHub

## Data Cleaning

The dataset was checked for:

- Missing values
- Duplicate records
- Data types
- Dataset structure

No missing values or duplicate records were found.

## Analysis Performed

### 1. Overall Attrition

The overall attrition rate was calculated by determining the percentage of employees whose Attrition value was "Yes".

### 2. Department Analysis

Attrition rates were calculated for Finance, HR, IT, and Sales departments.

### 3. Overtime Analysis

The relationship between overtime status and employee attrition was analyzed.

### 4. Job Satisfaction Analysis

Average job satisfaction was compared between employees who stayed and employees who left.

### 5. Tenure Analysis

Average years at the company were compared between employees who stayed and employees who left.

### 6. Work-Life Balance Analysis

Average work-life balance scores were compared between employees who stayed and employees who left.

### 7. Income Analysis

Average monthly income was compared between employees who stayed and employees who left.

## Visualizations

The project includes the following charts:

- Employee Attrition Distribution
- Attrition by Department
- Attrition Rate by Overtime
- Job Satisfaction vs Attrition
- Years at Company vs Attrition
- Work-Life Balance vs Attrition
- Monthly Income vs Attrition

## Key Insights

- The overall attrition rate in the practice dataset was 40%.
- HR and Sales had the highest department-level attrition rate at 50%.
- Employees marked as working overtime had a 100% attrition rate in this dataset.
- Employees who left had lower average job satisfaction than employees who stayed.
- Employees who left had shorter average tenure.
- Employees who left had lower average monthly income.
- Employees who left had lower average work-life balance scores.

## Business Recommendations

Based on the patterns observed in this practice dataset:

- Monitor overtime workload and employee working conditions.
- Investigate factors contributing to lower job satisfaction.
- Pay attention to early-tenure employees and onboarding experiences.
- Review work-life balance and workload management.
- Analyze compensation patterns for employees with higher attrition risk.

These recommendations are based only on the small practice dataset and should not be generalized to a real organization without additional data.

## Project Structure

```text
employee-attrition-analysis/
│
├── data/
│   └── employees.csv
│
├── charts/
│   ├── attrition_distribution.png
│   ├── attrition_by_department.png
│   ├── overtime_vs_attrition.png
│   ├── job_satisfaction_vs_attrition.png
│   ├── years_at_company_vs_attrition.png
│   ├── worklife_balance_vs_attrition.png
│   └── monthly_income_vs_attrition.png
│
├── analysis.py
└── README.md