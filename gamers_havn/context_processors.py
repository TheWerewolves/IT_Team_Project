from django.conf import settings

from gamers_havn.models import Account


def base(request):
    account = None
    accounts = []
    if request.user.is_authenticated:
        accounts = Account.objects.filter(user=request.user)
        if len(accounts) != 0:
            account = accounts[0]

    return {'current_account': account}