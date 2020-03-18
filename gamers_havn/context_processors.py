from django.conf import settings

from gamers_havn.models import Account


def base(request):
    account = Account.objects.filter(user=request.user)[0]
    return {'current_account': account}