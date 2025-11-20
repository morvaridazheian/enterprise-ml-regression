# enterprise-ml-regression
Multivariable linear regression to analyze how enterprise cost features impact appointment numbers. Calculates feature contributions and provides insights for data-driven decision-making.

# Enterprise Cost Contribution Regression (ML)

This project performs multivariable linear regression to estimate how different enterprise cost components contribute to the final number of appointments.

## 🔥 What this project does

- Loads any CSV dataset  
- Automatically detects:
  - Numeric columns
  - Categorical columns
- One-Hot encodes categorical variables
- Trains a machine learning regression model
- Calculates:
  - How many appointments are gained per +1 unit of each feature
  - How many units are needed for +1 appointment
- Saves results to Excel
- Generates:
  - Feature importance bar chart
  - Predicted vs actual scatter plot
  - Residual distribution histogram

---

