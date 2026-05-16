from metrics import (
    exact_match_score,
    fuzzy_match_score,
    phrasing_sensitivity
)

expected = "New Delhi"

response1 = "The capital of India is New Delhi."
response2 = "India's capital city is Delhi."
response3 = "Mumbai"

# Exact match
score1 = exact_match_score(expected, response1)
score2 = exact_match_score(expected, response2)
score3 = exact_match_score(expected, response3)

print("\nEXACT MATCH SCORES:")
print(score1)
print(score2)
print(score3)

# Fuzzy match
fuzzy1 = fuzzy_match_score(expected, response1)
fuzzy2 = fuzzy_match_score(expected, response2)
fuzzy3 = fuzzy_match_score(expected, response3)

print("\nFUZZY MATCH SCORES:")
print(fuzzy1)
print(fuzzy2)
print(fuzzy3)

# Sensitivity
scores = [score1, score2, score3]

sensitivity = phrasing_sensitivity(scores)

print("\nPHRASING SENSITIVITY:")
print(sensitivity)