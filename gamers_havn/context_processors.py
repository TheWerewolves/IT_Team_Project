from django.conf import settings

from gamers_havn.models import Account


def base(request):
    account = None
    if request.user.is_authenticated:
        try:
            account = Account.objects.get(user=request.user)
        except Account.DoesNotExist:
            account = None

    return {'current_account': account}