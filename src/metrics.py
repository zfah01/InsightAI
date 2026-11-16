
def get_metric_definitions():
    """
    Return the approved business metric definitions
    used by InsightAI.
    """

    metrics = {
        "total_revenue": {
            "description": "Total revenue generated from completed orders.",
            "calculation": "Sum of revenue where order_status is Completed.",
            "unit": "GBP"
        },

        "total_orders": {
            "description": "Total number of orders placed.",
            "calculation": "Count of all orders.",
            "unit": "orders"
        },

        "average_order_value": {
            "description": "Average revenue generated per completed order.",
            "calculation": "Completed-order revenue divided by completed orders.",
            "unit": "GBP"
        },

        "cancellation_rate": {
            "description": "Percentage of orders that were cancelled.",
            "calculation": "Cancelled orders divided by total orders, multiplied by 100.",
            "unit": "percentage"
        }
    }

    return metrics
