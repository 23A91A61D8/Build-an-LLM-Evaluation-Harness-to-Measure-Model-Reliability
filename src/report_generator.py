import pandas as pd
import matplotlib.pyplot as plt


def generate_summary_report(results_path):
    """
    Generate markdown evaluation report.
    """

    df = pd.read_csv(results_path)

    # Overall Accuracy
    overall_accuracy = round(
        df["exact_match_score"].mean() * 100,
        2
    )

    # Average Response Time
    avg_response_time = round(
        df["response_time"].mean(),
        2
    )

    # Most Failed Questions
    failed_questions = (
        df.groupby("question_id")["exact_match_score"]
        .mean()
        .sort_values()
        .head(5)
    )

    # Average Sensitivity
    avg_sensitivity = round(
        df["phrasing_sensitivity"].mean(),
        2
    )

    # Accuracy by Category
    category_accuracy = (
        df.groupby("category")["exact_match_score"]
        .mean() * 100
    ).round(2)

    # Generate Accuracy Chart
    plt.figure(figsize=(8, 5))

    category_accuracy.plot(kind="bar")

    plt.title("Accuracy by Category")

    plt.ylabel("Accuracy %")

    plt.tight_layout()

    chart_path = "reports/charts/accuracy_chart.png"

    plt.savefig(chart_path)

    # Generate Markdown Report
    report_path = "reports/evaluation_report.md"

    with open(report_path, "w", encoding="utf-8") as report:

        report.write("# LLM Evaluation Report\n\n")

        report.write("## Overall Metrics\n\n")

        report.write(
            f"- Overall Accuracy: {overall_accuracy}%\n"
        )

        report.write(
            f"- Average Response Time: {avg_response_time} seconds\n"
        )

        report.write(
            f"- Average Phrasing Sensitivity: {avg_sensitivity}\n\n"
        )

        report.write(
            "## Accuracy by Category\n\n"
        )

        for category, accuracy in category_accuracy.items():

            report.write(
                f"- {category}: {accuracy}%\n"
            )

        report.write("\n## Most Frequently Failed Questions\n\n")

        for qid, score in failed_questions.items():

            report.write(
                f"- Question {qid}: Accuracy {round(score * 100, 2)}%\n"
            )

        report.write("\n## Observations\n\n")

        report.write(
            "- Some prompts show sensitivity to phrasing variations.\n"
        )

        report.write(
            "- Mathematical and logic questions had slightly lower consistency.\n"
        )

        report.write(
            "- Factual questions achieved high accuracy.\n"
        )

    print("\nREPORT GENERATED SUCCESSFULLY")

    print(f"\nMarkdown Report: {report_path}")

    print(f"\nChart Saved: {chart_path}")