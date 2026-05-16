from providers import get_groq_response

prompt = "What is the capital of India?"

response = get_groq_response(prompt)

print("\nMODEL RESPONSE:\n")
print(response)