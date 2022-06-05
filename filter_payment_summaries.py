from typing import List
from customer_payment_summary import CustomerPaymentSummaryResult


def not_fully_paid(summaries: List[CustomerPaymentSummaryResult]) -> List[CustomerPaymentSummaryResult]:
    return [summary for summary in summaries if summary.total_balance < 0]

def rank_bankrupts(summaries: List[CustomerPaymentSummaryResult]) -> List[CustomerPaymentSummaryResult]:
    return sorted(summaries, key=lambda summary: summary.total_balance)

