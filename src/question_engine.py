
from src.analytics import (
    calculate_total_revenue,
    calculate_revenue_by_region,
    calculate_revenue_by_product,
    get_order_status_counts,
    calculate_average_order_value,
    calculate_cancellation_rate
)


def interpret_question(question):
    """
    Identify which analytical function matches a user's question.
    """

    question = question.lower()

    if "average order value" in question or "average order" in question:
        return "average_order_value"

    elif "cancellation rate" in question or "cancelled" in question:
        return "cancellation_rate"

    elif "region" in question:
        return "revenue_by_region"

    elif "product" in question:
        return "revenue_by_product"

    elif "order status" in question or "order count" in question:
        return "order_status"

    elif "total revenue" in question or "revenue" in question:
        return "total_revenue"

    else:
        return None


def answer_question(question, df):
    """
    Execute the analytical function selected by the interpreter.
    """

    intent = interpret_question(question)

    if intent == "total_revenue":
        return calculate_total_revenue(df)

    elif intent == "revenue_by_region":
        return calculate_revenue_by_region(df)

    elif intent == "revenue_by_product":
        return calculate_revenue_by_product(df)

    elif intent == "order_status":
        return get_order_status_counts(df)

    elif intent == "average_order_value":
        return calculate_average_order_value(df)

    elif intent == "cancellation_rate":
        return calculate_cancellation_rate(df)

    else:
        return "Sorry, I don't understand that question yet."
