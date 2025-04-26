from dj_rql.filter_cls import AutoRQLFilterClass
from administrators.models import Administrator


class AdministratorFielterClass(AutoRQLFilterClass):
    MODEL = Administrator