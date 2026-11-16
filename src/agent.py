
from google.genai import types

from src.ai_engine import client

from src.analytics import (
    calculate_total_revenue,
    calculate_revenue_by_region,
    calculate_revenue_by_product,
    get_order_status_counts,
    calculate_average_order_value,
    calculate_cancellation_rate
)


def create_agent(df):
    """
    Create an InsightAI conversation with access
    to approved Python analytics functions.
    """

    def get_total_revenue() -> float:
        """Get total revenue from completed orders in GBP."""
        return float(calculate_total_revenue(df))

    def get_revenue_by_region() -> dict:
        """Get completed-order revenue by region in GBP."""
        revenue = calculate_revenue_by_region(df)
        return {
            str(region): float(amount)
            for region, amount in revenue.items()
        }

    def get_revenue_by_product() -> dict:
        """Get completed-order revenue by product in GBP."""
        revenue = calculate_revenue_by_product(df)
        return {
            str(product): float(amount)
            for product, amount in revenue.items()
        }

    def get_order_status() -> dict:
        """Get the number of orders in each status."""
        counts = get_order_status_counts(df)
        return {
            str(status): int(count)
            for status, count in counts.items()
        }

    def get_average_order_value() -> float:
        """Get average order value for completed orders in GBP."""
        return float(calculate_average_order_value(df))

    def get_cancellation_rate() -> float:
        """Get cancellation rate as a percentage."""
        return float(calculate_cancellation_rate(df))

    # Create Gemini conversation
    chat = client.chats.create(
        model="gemini-3.5-flash-lite",
        config=types.GenerateContentConfig(
            system_instruction="""
            You are InsightAI, a business analytics assistant.

            Help users understand business performance using
            the approved Python analytics tools.

            Rules:
            - Always use Python tools for business calculations.
            - Never invent numerical results.
            - Always report revenue in GBP (£).
            - Understand follow-up questions using conversation history.
            - Clearly explain results in plain English.
            """,
            tools=[
                get_total_revenue,
                get_revenue_by_region,
                get_revenue_by_product,
                get_order_status,
                get_average_order_value,
                get_cancellation_rate
            ]
        )
    )

    return chat


def answer_business_question(chat, question):
    """
    Send a question within an existing conversation.
    """

    response = chat.send_message(question)

    return response.text
