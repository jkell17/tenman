from boards.models import Game
from boards.models import Player
from boards.models import Competition

def run():
	rankings = {}

	p = Player.objects.all()
	c = Competition.objects.all()
	g = Game.objects.all()

	for comp in c:   	
		rankings[comp] = {key:[0,0] for key in p}

	print rankings

	for game in g:
		rankings[game.comp][game.winner][0] += 1
		rankings[game.comp][game.loser][1] += 1
	print rankings



