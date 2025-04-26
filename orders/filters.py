from dj_rql.filter_cls import AutoRQLFilterClass
from orders.models import Order, OrderProducts


class OrderFilterClass(AutoRQLFilterClass):
    MODEL = Order


class OrderProductsFilterClass(AutoRQLFilterClass):
    MODEL = OrderProducts