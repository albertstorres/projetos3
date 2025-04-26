from dj_rql.filter_cls import AutoRQLFilterClass
from products.models import Product


class ProductFilterClass(AutoRQLFilterClass):
    MODEL = Product