import os, csv
from collections import defaultdict

from django.conf import settings

from .models import Order

SALES_AMOUNT = 'sales_amount'
SALES_QTY = 'sales_quantity'
ORDER_COUNT = 'order_count'

def audit_sales():
    '''
    Count the total sales amount of each shop_id
          the total sold amount of each shop_id
          the total order of each shop_id
    Then output as csv file.
    '''

    def return_defual_value():
        return {
            SALES_AMOUNT:0, 
            SALES_QTY: 0, 
            ORDER_COUNT: 0
            }

    shop_sales = defaultdict(return_defual_value)
    
    orders = Order.objects.all()
    for order in orders:
        shop_id = order.shop_id
        shop_sales[shop_id][SALES_AMOUNT] += int(order.total_price)
        shop_sales[shop_id][SALES_QTY] += int(order.quantity)
        shop_sales[shop_id][ORDER_COUNT] += 1

    try:
        file_name = os.path.join(settings.BASE_DIR, 'audit_sales.csv')
        with open(file_name, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)

            for key in shop_sales.keys():
                writer.writerow([
                    key,
                    shop_sales[key][SALES_AMOUNT],
                    shop_sales[key][SALES_QTY],
                    shop_sales[key][ORDER_COUNT]
                ])
                
    except Exception as e:
        print("Unable to generate 'audit_sales.csv'")
        print(e)

def find_most_popular():
    print('******find_most_popular*******')