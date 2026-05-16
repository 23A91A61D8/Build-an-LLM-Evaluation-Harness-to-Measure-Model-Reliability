import re
import statistics
from providers import get_groq_response

def normalize_text(text):
    """
    Normalize text for comparison.
    """

    text = text.lower().strip()

    # Remove punctuation
    text = re.sub(r"[^\w\s]", "", text)

    return text


def exact_match_score(expected, actual):
    """
    Exact match scoring.
    Returns 1 if correct, otherwise 0.
    """

    expected = normalize_text(expected)
    actual = normalize_text(actual)

    if expected in actual:
        return 1

    return 0


def fuzzy_match_score(expected, actual):
    """
    Fuzzy matching score.
    """

    expected = normalize_text(expected)
    actual = normalize_text(actual)

    expected_words = set(expected.split())
    actual_words = set(actual.split())

    overlap = expected_words.intersection(actual_words)

    if len(expected_words) == 0:
        return 0

    similarity = len(overlap) / len(expected_words)

    return round(similarity, 2)


def phrasing_sensitivity(scores):
    """
    Calculate standard deviation across phrasing scores.
    """

    if len(scores) <= 1:
        return 0

    return round(statistics.stdev(scores), 2)
def llm_judge_score(question, expected, actual):
    """
    Use LLM as judge to score response quality.
    Returns score between 1 and 5.
    """

    judge_prompt = f"""
You are an AI evaluator.

Question:
{question}

Expected Answer:
{expected}

Model Response:
{actual}

Evaluate how correct the response is.

Rules:
- 5 = Fully correct
- 4 = Mostly correct
- 3 = Partially correct
- 2 = Slightly correct
- 1 = Incorrect

Only return a single number from 1 to 5.
"""

    try:

        judgment = get_groq_response(judge_prompt)

        score = int(
            ''.join(filter(str.isdigit, judgment))
        )

        if score < 1 or score > 5:
            return 1

        return score

    except:
        return 1