from django.http import HttpResponse
from django.shortcuts import render
from .models import Player, Game, GameForm, Competition
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def make_rankings():
	rankings = {}

	p = Player.objects.all()
	c = Competition.objects.all()
	g = Game.objects.all()

	for comp in c:   	
		rankings[comp] = {key:[0,0] for key in p}
	for game in g:
		rankings[game.comp][game.winner][0] += 1
		rankings[game.comp][game.loser][1] += 1
	return rankings

def index(request):
	if request.method == 'POST':
		form = GameForm(request.POST)
		if form.is_valid():
			form.save()		
			return HttpResponseRedirect('/success')
		else:
			return HttpResponseRedirect('/failure')

	else:   	
		players = Player.objects.all()
		games = Game.objects.all()
		form = GameForm()
		rankings = make_rankings()
		context = {'players_list': players, 'games': games, 'form':form, 'rankings': rankings}
		return render(request, 'boards/index.html', context)

def success(request):
	return HttpResponse("Success")

def failure(request):
	return HttpResponse("Failure")