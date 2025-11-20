from enterprise_ml_regression import analyze_enterprise_regression

# -----------------------------------------------------
# Test: Check the Results
# -----------------------------------------------------
results, r2, model = analyze_enterprise_regression(
    csv_path="sample_appointments.csv",
    target_column="Appointments",
    output_excel="regression_results.xlsx"
)

print(f"R² score on test dataset: {r2:.4f}")
print("Regression results saved to 'regression_results.xlsx'.")
