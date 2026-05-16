import json
import pandas as pd
import time

from providers import get_groq_response

from metrics import (
    exact_match_score,
    fuzzy_match_score,
    phrasing_sensitivity,
    llm_judge_score
)


def load_dataset(path):
    """
    Load dataset JSON file.
    """

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def evaluate_model(dataset):
    """
    Evaluate model on all questions and phrasings.
    """

    results = []

    for item in dataset:

        question_id = item["id"]
        category = item["category"]
        difficulty = item["difficulty"]
        expected_answer = item["correct_answer"]

        phrasing_scores = []

        for idx, prompt in enumerate(item["phrasings"], start=1):

            print(f"\nEvaluating Question {question_id} | Phrasing {idx}")

            start_time = time.time()

            response = get_groq_response(prompt)

            end_time = time.time()

            response_time = round(end_time - start_time, 2)

            # Exact Match Score
            exact_score = exact_match_score(
                expected_answer,
                response
            )

            # Fuzzy Match Score
            fuzzy_score = fuzzy_match_score(
                expected_answer,
                response
            )

            # LLM-as-Judge Score
            judge_score = llm_judge_score(
                prompt,
                expected_answer,
                response
            )

            phrasing_scores.append(exact_score)

            results.append({
                "question_id": question_id,
                "category": category,
                "difficulty": difficulty,
                "phrasing_number": idx,
                "prompt": prompt,
                "expected_answer": expected_answer,
                "model_response": response,
                "exact_match_score": exact_score,
                "fuzzy_match_score": fuzzy_score,
                "llm_judge_score": judge_score,
                "response_time": response_time
            })

        # Calculate phrasing sensitivity
        sensitivity = phrasing_sensitivity(
            phrasing_scores
        )

        for row in results:

            if row["question_id"] == question_id:

                row["phrasing_sensitivity"] = sensitivity

    return pd.DataFrame(results)