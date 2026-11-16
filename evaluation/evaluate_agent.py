
import pandas as pd

from src.agent import create_agent, answer_business_question


# Load the sales dataset
df = pd.read_csv("data/sales.csv")


# Evaluation test cases
evaluation_cases = [
    {
        "question": "What is our total revenue?",
        "expected": ["841,475"]
    },
    {
        "question": "Which region generates the most revenue?",
        "expected": ["England", "224,875"]
    },
    {
        "question": "Which product generates the most revenue?",
        "expected": ["Monitor", "188,375"]
    },
    {
        "question": "How many orders are completed, cancelled and returned?",
        "expected": ["863", "96", "41"]
    },
    {
        "question": "What is our average order value?",
        "expected": ["975.06"]
    },
    {
        "question": "What is our cancellation rate?",
        "expected": ["9.6"]
    }
]


def evaluate_agent():

    passed = 0
    failed = 0

    print("\nStarting InsightAI Evaluation\n")

    for case in evaluation_cases:

        question = case["question"]
        expected = case["expected"]

        print(f"Question: {question}")

        try:
            # Create a fresh conversation for each test
            chat = create_agent(df)

            # Ask InsightAI the question
            answer = answer_business_question(chat, question)

            print(f"Answer: {answer}")

            # Check expected results
            answer_lower = answer.lower()

            missing = [
                item for item in expected
                if item.lower() not in answer_lower
            ]

            if not missing:
                print("Result: PASS\n")
                passed += 1

            else:
                print(f"Result: FAIL - Missing {missing}\n")
                failed += 1

        except Exception as error:

            print(f"Result: ERROR - {error}\n")
            failed += 1

    # Evaluation summary
    total = passed + failed

    print("=" * 40)
    print("INSIGHTAI EVALUATION SUMMARY")
    print("=" * 40)

    print(f"Total tests: {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")

    if total > 0:
        accuracy = (passed / total) * 100
        print(f"Pass rate: {accuracy:.1f}%")


if __name__ == "__main__":
    evaluate_agent()
