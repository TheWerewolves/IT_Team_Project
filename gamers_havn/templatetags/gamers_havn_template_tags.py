from django import template

from gamers_havn.models import Game


register = template.Library()

@register.inclusion_tag('gamers_havn/list_games.html')
def get_game_list():
    return {'games': Game.objects.all()}


