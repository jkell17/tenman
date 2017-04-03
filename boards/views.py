from django.http import HttpResponse
from django.shortcuts import render
from .models import Player, Game, GameForm, Competition
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

class PlayerElo:
    def __init__(self, elo):
        self.elo = elo

    def expected(self, opp):
         return 1. / (1. + 10.**((opp.elo -self.elo)/ 400.))

    def play(self, opp, win):
        if win:
            result = 1
        else:
            result = -1
        self.elo = self.elo + 32.*(result - self.expected(opp))
        opp.elo = opp.elo + 32.*(-1*result - opp.expected(self))
        return self.elo

def make_rankings():
	rankings = {}

	p = Player.objects.all()
	c = Competition.objects.all()
	g = Game.objects.all()

	for comp in c:
		rankings[comp] = {key:[0,0,1200] for key in p}
	for game in g:
		elo_win = PlayerElo(rankings[game.comp][game.winner][2])
		elo_lose = PlayerElo(rankings[game.comp][game.loser][2])
		elo_win.play(elo_lose, win=True)
		rankings[game.comp][game.winner][2] = elo_win.elo
		rankings[game.comp][game.loser][2] = elo_lose.elo
		rankings[game.comp][game.winner][0] += 1
		rankings[game.comp][game.loser][1] += 1

	final = {}
	for r in rankings:
		i = []
		keys= rankings[r].keys()
		for k in keys:
			l = {}
			l['name'] = k.name
			l['wins'] = rankings[r][k][0]
			l['loses'] = rankings[r][k][1]
			l['elo'] = rankings[r][k][2]
			i.append(l)
		final[r]= sorted(i, key=lambda k: -k['elo'])
	return final

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
	return render(request, 'boards/success.html')

def failure(request):
	return render(request, 'boards/failure.html')
