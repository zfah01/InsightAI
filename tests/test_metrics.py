
from src.metrics import get_metric_definitions


def test_metric_definitions_exist():
    metrics = get_metric_definitions()

    assert "total_revenue" in metrics
    assert "total_orders" in metrics
    assert "average_order_value" in metrics
    assert "cancellation_rate" in metrics


def test_total_revenue_definition():
    metrics = get_metric_definitions()

    assert metrics["total_revenue"]["unit"] == "GBP"
