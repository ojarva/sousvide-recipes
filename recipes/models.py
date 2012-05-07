# -*- coding: utf-8
from django.db import models

import datetime

class Ingredient(models.Model):
    """ Single ingredient --basically not used nowadays (*RecipeGroup* is used instead) """
    name = models.CharField(max_length=60, verbose_name="Nimi")

    class Meta:
        ordering = ["name"]

    def __unicode__(self):
        return self.name

class ImageFile(models.Model):
    """ Image attachment for single "Making" (log entry for ingredient) """
    recipe = models.ForeignKey('Making')
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/")
    def __unicode__(self):
        return "%s (%s)" % (self.recipe, self.timestamp)

class RecipeGroup(models.Model):
    """ Item in main list """
    main_ingredient = models.ForeignKey("Ingredient", verbose_name="Pääruoka-aine")
    description = models.TextField(blank=True, verbose_name="Lämpötila")



    class Meta:
        ordering = ['main_ingredient__name']

    def first_letter(self):
        return self.main_ingredient.name and self.main_ingredient.name[0] or ''

    @models.permalink
    def get_absolute_url(self):
        return ('recipe_info', [str(self.id)])

    def __unicode__(self):
        return "%s" % self.main_ingredient.name

class Making(models.Model):
    """ Single log entry """
    group = models.ForeignKey("RecipeGroup", verbose_name="Ryhmä")
    started = models.DateTimeField(default=datetime.datetime.now, verbose_name="Aloitettu")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Luotu")
    modified = models.DateTimeField(auto_now=True, verbose_name="Muokattu")
    time = models.IntegerField(verbose_name="Aika (minuutteja)")
    temperature = models.FloatField(verbose_name="Lämpötila")
    comments = models.TextField(blank=True, verbose_name="Kommentit")
    rating = models.IntegerField(verbose_name="Arvosana")
    in_progress = models.BooleanField(default=False, verbose_name="Kesken")

    def get_start(self):
        return self.started.isoformat(" ")

    def get_end(self):
        return (self.started + datetime.timedelta(minutes=self.time)).isoformat(" ")

    @models.permalink
    def get_absolute_url(self):
        return ('making_edit', [str(self.id)])

    def until_ready(self):
        time_tmp = (self.started + datetime.timedelta(minutes=self.time)) - datetime.datetime.now()
        return str(time_tmp).split(".")[0]

    def __unicode__(self):
        return "%s (%s)" % (self.group, self.created)
