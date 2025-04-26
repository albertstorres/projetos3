from dj_rql.filter_cls import AutoRQLFilterClass
from collects.models import Address, Categorie, Collect


class AddressFilterClass(AutoRQLFilterClass):
    MODEL = Address


class CategorieFilterClass(AutoRQLFilterClass):
    MODEL = Categorie


class CollectFilterClass(AutoRQLFilterClass):
    MODEL = Collect