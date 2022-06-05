from customer_payment_summary import Summary
from filter_payment_summaries import not_fully_paid, rank_bankrupts
import persistance.database_reset as database_reset
from persistance.load_database import load_database_into_repo
from persistance.repos import get_all_from_memory, store_in_memory

repo_save = store_in_memory
repo_load = get_all_from_memory


def main():
    database_reset.reset()
    load_database_into_repo(store_in_memory)

    summary = Summary(repo_load).customer_payment_summary()
    bad_clients = not_fully_paid(summary)

    for bankrupt in rank_bankrupts(bad_clients):
        print(format_bankrupt(bankrupt))


def format_bankrupt(bankrupt):
    s = f'Name: {bankrupt.customer.customerName} '
    s += f'Number: {bankrupt.customer.customerNumber} '
    s += f'Balance: {bankrupt.total_balance} '
    s += f'Days till unpaid order date: {bankrupt.days_till_first_unpaid_order} '
    return s


if __name__ == '__main__':
    main()
