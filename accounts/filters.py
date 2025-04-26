from dj_rql.filter_cls import AutoRQLFilterClass
from accounts.models import Account, Deposit


class AccountFilterClass(AutoRQLFilterClass):
    MODEL = Account


class DepositFilterClass(AutoRQLFilterClass):
    MODEL = Deposit