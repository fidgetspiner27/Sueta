from django.contrib import admin

from .models import Hero, Attribute, Ability, Item


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'list_heroes',)


@admin.register(Ability)
class AbilityAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Item)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ('name',)


