from dataclasses import dataclass
from typing import Callable, List
from entities import Customer, Order, OrderDetails, Payment
from datetime import date


@dataclass
class CustomerPaymentSummaryResult:
    customer: Customer
    total_amount: float
    total_payments: float
    total_balance: float
    days_till_first_unpaid_order: int


class Summary:
    def __init__(self, repo_load: Callable[[str], List[Order]]):
        self.repo_load = repo_load

    def customer_payment_summary(self) -> List[CustomerPaymentSummaryResult]:
        customers: List[Customer] = self.repo_load('customers')
        payments: List[Payment] = self.repo_load('payments')
        orders: List[Order] = self.repo_load('orders')
        orderdetails: List[OrderDetails] = self.repo_load('orderdetails')

        customer_summary_results = []
        for customer in customers:
            customer_orders = [
                o for o in orders if o.customerNumber == customer.customerNumber]
            if customer.customerNumber == 456:
                customer
            customer_payment_amounts = [
                p.amount for p in payments if p.customerNumber == customer.customerNumber]

            customer_payments_sum = sum(customer_payment_amounts)

            total_balance = customer_payments_sum
            first_unpaid_order_date = None

            total_required_payment = 0
            for order in customer_orders:
                if order.status != 'Shipped':
                    continue
                orderdetails_for_order = [
                    od for od in orderdetails if order.orderNumber == od.orderNumber]

                orderdetail_price = [
                    od.priceEach * od.quantityOrdered for od in orderdetails_for_order]

                total_required_payment += sum(orderdetail_price)
                total_balance -= total_required_payment
                if not first_unpaid_order_date and total_balance < 0:
                    first_unpaid_order_date = date.today() - order.orderDate

            summary_result = CustomerPaymentSummaryResult(
                customer, total_required_payment, customer_payments_sum, total_balance, first_unpaid_order_date)

            customer_summary_results.append(summary_result)

        return customer_summary_results
