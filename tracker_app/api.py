"""
Handles external api connection to fetch b3 data
"""
from celery import shared_task

from yahooquery import Ticker

# def stock_tracker():
#     stock = Ticker("SÍMBOLO DA AÇÃO")
#     while(True):
#         stock.history
    

@shared_task()
def stock_tracker():
     stock = Ticker("SÍMBOLO DA AÇÃO")
     stock.history(period="1d",  interval = "30m")

petr = Ticker("PETR4.SA")
a=petr.history(period="1d",  interval = "30m")
print(a)