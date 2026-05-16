import os
from report_generator import generate_summary_report

from evaluator import (
    load_dataset,
    evaluate_model
)

# Create reports folder if not exists
os.makedirs("reports", exist_ok=True)

# Load dataset
dataset = load_dataset(
    "dataset/questions.json"
)

print("\nDATASET LOADED SUCCESSFULLY")

# Evaluate model
results_df = evaluate_model(dataset)

# Save CSV results
results_path = "reports/evaluation_results.csv"

results_df.to_csv(results_path, index=False)

print("\nEVALUATION COMPLETED")

print(f"\nResults saved to: {results_path}")

# Display summary
print("\nFIRST 5 RESULTS:\n")

print(results_df.head())
# Generate final report
generate_summary_report(results_path)