from django.core.validators import FileExtensionValidator
from django.db import (models)
from django.utils.translation import gettext_lazy as _


class Attribute(models.Model):
    ATTRIBUTE_NAME_CHOICES = (("STRENGTH", _("Strength")),
                              ("INTELLIGENCE", _("Intelligence")),
                              ("AGILITY", _("Agility")),
                              ("UNIVERSAL", _("Universal")))
    name = models.CharField(max_length=16, unique=True, null=False, blank=False, verbose_name=_("DOTA2 attribute"),
                            choices=ATTRIBUTE_NAME_CHOICES, help_text=_("The name of DOTA2 the attribute."))

    def __str__(self):
        return self.name

    @property
    def list_heroes(self):
        return str(list(self.hero_set.all().values_list("name", flat=True)))


class Hero(models.Model):
    name = models.CharField(max_length=32, unique=True, null=False, blank=False, verbose_name=_("DOTA2 hero name"))
    main_attribute = models.ForeignKey(to=Attribute, on_delete=models.PROTECT,
                                       verbose_name=_("DOTA2 hero main attribute"))
    ATTACK_TYPE_CHOICES = (("MELEE", _("MELEE")),
                           ("RANGE", _("RANGE")))
    attack_type = models.CharField(max_length=8, unique=True, null=False, blank=False,
                                   verbose_name=_("DOTA2 hero attack type"),
                                   choices=ATTACK_TYPE_CHOICES)
    abilities = models.ManyToManyField(to='polls.Ability', blank=False, verbose_name=_("DOTA2 hero abilities"))

    image = models.ImageField(upload_to='hero_images/', null=True, blank=True, verbose_name=_("Hero Image"))

    melody = models.FileField(upload_to='melodies/', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['mp3'])], verbose_name=_("Melody"))

    def __str__(self):
        return self.name

# class HeroImage(models.Model):


class Ability(models.Model):
    name = models.CharField(max_length=128, unique=True, null=False, blank=False, verbose_name=_("DOTA2 ability"))
    description = models.TextField(null=False, blank=False, verbose_name=_("DOTA2 ability description"))

    class Meta:
        verbose_name = _("ability")
        verbose_name_plural = _("abilities")

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=128, unique=True, null=False, blank=False, verbose_name=_("DOTA2 item name"))
    description = models.TextField(null=False, blank=False, verbose_name=_("DOTA2 item description"))
    ITEM_TYPE_CHOICES = (("PASSIVE", _("PASSIVE")),
                         ("ACTIVE", _("ACTIVE")))
    item_type = models.CharField(max_length=10, unique=True, null=False, blank=False,
                                   verbose_name=_("DOTA2 item type"),
                                   choices=ITEM_TYPE_CHOICES)
    image = models.ImageField(upload_to='item_images/', null=True, blank=True, verbose_name=_("Item Image"))

    class Meta:
        verbose_name = _("item")
        verbose_name_plural = _("items")

    def __str__(self):
        return self.name
