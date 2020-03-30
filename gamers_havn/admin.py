from django.contrib import admin

from gamers_havn.models import Account, Game, Article, Comment


class AccountAdmin(admin.ModelAdmin):
    filter_horizontal = ('favorite_articles', 'followed_games')


admin.site.register(Account, AccountAdmin)
admin.site.register(Game)
admin.site.register(Article)
admin.site.register(Comment)

