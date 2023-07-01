from collections import OrderedDict
from django.db.models.query import QuerySet
from transaction.models import Transactions






def group_transaction_by_date(trans_history:QuerySet[Transactions]):

    transactions_by_date = OrderedDict()
  
    for transaction in trans_history:
        if len(transactions_by_date) == 0:
            transactions_by_date[transaction.date_added.date().strftime("%B %d %Y")] = [transaction.to_dict()]
        else:
            if transaction.date_added.date().strftime("%B %d %Y") in transactions_by_date:
                transactions_by_date[transaction.date_added.date().strftime("%B %d %Y")].append(transaction.to_dict())
            else:
                transactions_by_date[transaction.date_added.date().strftime("%B %d %Y")] = [transaction.to_dict()]

    return transactions_by_date