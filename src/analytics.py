
import pandas as pd


def calculate_total_revenue(df):
    """Calculate revenue from completed orders."""
    completed_orders = df[df["order_status"] == "Completed"]
    return completed_orders["revenue"].sum()


def calculate_revenue_by_region(df):
    """Calculate completed-order revenue for each region."""
    completed_orders = df[df["order_status"] == "Completed"]

    return (
        completed_orders.groupby("region")["revenue"]
        .sum()
        .sort_values(ascending=False)
    )


def calculate_revenue_by_product(df):
    """Calculate completed-order revenue for each product."""
    completed_orders = df[df["order_status"] == "Completed"]

    return (
        completed_orders.groupby("product")["revenue"]
        .sum()
        .sort_values(ascending=False)
    )


def get_order_status_counts(df):
    """Count orders by status."""
    return df["order_status"].value_counts()


def calculate_average_order_value(df):
    """Calculate average revenue per completed order."""
    completed_orders = df[df["order_status"] == "Completed"]

    if completed_orders.empty:
        return 0

    return completed_orders["revenue"].sum() / len(completed_orders)


def calculate_cancellation_rate(df):
    """Calculate the percentage of orders that were cancelled."""
    if df.empty:
        return 0

    cancelled_orders = df[df["order_status"] == "Cancelled"]

    return (len(cancelled_orders) / len(df)) * 100