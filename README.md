# Build an LLM Evaluation Harness to Measure Model Reliability

## Overview

This project implements an automated LLM evaluation harness that benchmarks language model reliability across multiple prompt phrasings and categories.

The system evaluates model responses using:
- Exact Match Scoring
- Fuzzy Match Scoring
- LLM-as-Judge Evaluation
- Response Time Benchmarking
- Phrasing Sensitivity Analysis

The evaluation pipeline automatically generates:
- CSV evaluation results
- Markdown analysis reports
- Accuracy visualization charts

---

# Features

- Automated dataset evaluation
- Multi-phrasing prompt testing
- Groq API integration
- Exact match scoring
- Fuzzy similarity scoring
- LLM-as-judge scoring
- Response timing analysis
- Phrasing sensitivity metrics
- CSV report generation
- Markdown report generation
- Accuracy chart visualization
- Dockerized reproducible environment

---

# Project Structure

```text
llm-evaluation-harness/
│
├── dataset/
│   └── questions.json
│
├── reports/
│   ├── evaluation_results.csv
│   ├── evaluation_report.md
│   └── charts/
│       └── accuracy_chart.png
│
├── src/
│   ├── main.py
│   ├── providers.py
│   ├── evaluator.py
│   ├── metrics.py
│   └── report_generator.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── .dockerignore
├── .gitignore
└── README.md
```

---

# Technologies Used

- Python 3.11
- Groq API
- OpenAI SDK
- Pandas
- Matplotlib
- Docker
- Docker Compose

---

# Dataset Details

The dataset contains:
- 20 benchmark questions
- Multiple categories:
  - factual
  - math
  - logic
  - coding
- 3 phrasing variations per question

This enables robustness and phrasing sensitivity analysis.

---

# Evaluation Metrics

## 1. Exact Match Score

Checks whether the expected answer exists in the model response.

## 2. Fuzzy Match Score

Measures partial similarity between expected and generated answers.

## 3. LLM-as-Judge Score

Uses another LLM call to evaluate answer quality on a scale of 1–5.

## 4. Response Time

Measures inference latency for each prompt.

## 5. Phrasing Sensitivity

Calculates consistency across different prompt phrasings.

---

# Setup Instructions

## Clone Repository

```bash
git clone <your_repository_url>
cd llm-evaluation-harness
```

---

# Create Virtual Environment

## Windows Git Bash

```bash
python -m venv venv
source venv/Scripts/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Configure Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
```

---

# Run Project

```bash
python src/main.py
```

---

# Docker Execution

## Build Docker Container

```bash
docker-compose build
```

## Run Docker Container

```bash
docker-compose up
```

---

# Generated Outputs

After execution the following files are automatically generated:

- `reports/evaluation_results.csv`
- `reports/evaluation_report.md`
- `reports/charts/accuracy_chart.png`

---

# Sample Analysis

The system evaluates:
- model accuracy
- response consistency
- robustness against phrasing changes
- category-wise performance
- response latency

---

# Future Improvements

- Multi-model comparison support
- Advanced semantic similarity metrics
- Hallucination detection
- Additional benchmark datasets
- Web dashboard visualization
