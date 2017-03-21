from __future__ import unicode_literals
from django.db import models
import django
from django.core.exceptions import ValidationError
from django import forms

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    hometown = models.CharField(max_length=200)

    def __str__(self):              # __unicode__ on Python 2
        return "%s" % self.name

class Competition(models.Model):
	name =  models.CharField(max_length=200)
	def __str__(self):              # __unicode__ on Python 2
		return "%s" % self.name

class Game(models.Model):
	winner = models.ForeignKey(Player, related_name='winner')
	loser = models.ForeignKey(Player, related_name='loser')
	comp = models.ForeignKey(Competition)
	date = models.DateTimeField(default=django.utils.timezone.now, blank=True)
	def __str__(self):              # __unicode__ on Python 2
		return "%s | Winner: %s, Loser: %s" %  (self.comp, self.winner, self.loser)

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('comp', 'winner', 'loser')

    def clean(self):	
    	if self.cleaned_data.get('winner') == self.cleaned_data.get('loser'):
    		raise ValidationError("same winner and loser")
    	return self.cleaned_data