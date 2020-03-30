from django import template
from django.template.defaultfilters import stringfilter

from gamers_havn.models import Game

import markdown as md


register = template.Library()

@register.inclusion_tag('gamers_havn/list_games.html')
def get_game_list():
    return {'games': Game.objects.all()}

@register.filter()
@stringfilter
def markdown(value):
    return md.markdown(value, extensions=[
                                    'markdown.extensions.fenced_code',
                                    'markdown.extensions.extra',
                                    'markdown.extensions.codehilite',
                                    'markdown.extensions.toc',])
