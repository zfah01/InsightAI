
import pandas as pd

from src.analytics import (
    calculate_total_revenue,
    calculate_revenue_by_region,
    calculate_revenue_by_product,
    get_order_status_counts,
    calculate_average_order_value,
    calculate_cancellation_rate
)


def test_calculate_total_revenue():
    df = pd.DataFrame({
        "order_status": ["Completed", "Completed", "Cancelled"],
        "revenue": [100, 200, 500]
    })

    result = calculate_total_revenue(df)

    assert result == 300


def test_calculate_revenue_by_region():
    df = pd.DataFrame({
        "order_status": ["Completed", "Completed", "Completed"],
        "region": ["Scotland", "England", "Scotland"],
        "revenue": [100, 200, 300]
    })

    result = calculate_revenue_by_region(df)

    assert result["Scotland"] == 400
    assert result["England"] == 200


def test_calculate_revenue_by_product():
    df = pd.DataFrame({
        "order_status": ["Completed", "Completed"],
        "product": ["Laptop", "Phone"],
        "revenue": [500, 300]
    })

    result = calculate_revenue_by_product(df)

    assert result["Laptop"] == 500
    assert result["Phone"] == 300


def test_get_order_status_counts():
    df = pd.DataFrame({
        "order_status": ["Completed", "Completed", "Cancelled"]
    })

    result = get_order_status_counts(df)

    assert result["Completed"] == 2
    assert result["Cancelled"] == 1



def test_calculate_average_order_value():
    df = pd.DataFrame({
        "order_status": ["Completed", "Completed", "Cancelled"],
        "revenue": [100, 200, 500]
    })

    assert calculate_average_order_value(df) == 150


def test_calculate_cancellation_rate():
    df = pd.DataFrame({
        "order_status": ["Completed", "Cancelled", "Completed", "Cancelled"]
    })

    assert calculate_cancellation_rate(df) == 50
