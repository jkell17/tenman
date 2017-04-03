from boards.models import Game
from boards.models import Player
from boards.models import Competition

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

def run():
	# rankings = {}
    #
	# p = Player.objects.all()
	# c = Competition.objects.all()
	# g = Game.objects.all()
    #
	# for comp in c:
	# 	rankings[comp] = {key:[0,0,1200] for key in p}
	# for game in g:
	# 	elo_win = PlayerElo(rankings[game.comp][game.winner][2])
	# 	elo_lose = PlayerElo(rankings[game.comp][game.loser][2])
	# 	elo_win.play(elo_lose, win=True)
	# 	rankings[game.comp][game.winner][2] = elo_win.elo
	# 	rankings[game.comp][game.loser][2] = elo_lose.elo
	# 	rankings[game.comp][game.winner][0] += 1
	# 	rankings[game.comp][game.loser][1] += 1
    #
	# final = {}
	# for r in rankings:
	# 	i = []
	# 	keys= rankings[r].keys()
	# 	for k in keys:
	# 		l = {}
	# 		l['name'] = k.name
	# 		l['wins'] = rankings[r][k][0]
	# 		l['loses'] = rankings[r][k][1]
	# 		l['elo'] = rankings[r][k][2]
	# 		i.append(l)
	# 	final[r]= i
	# return final

    last_game = Game.objects.latest('date')
    rankings = {}

    p = Player.objects.all()
    c = Competition.objects.all()
    g = Game.objects.exclude(id = last_game.id)
    # g = Game.objects.all()

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


    preA = rankings[last_game.comp][last_game.winner][2]
    preB = rankings[last_game.comp][last_game.loser][2]

    A = PlayerElo(preA)
    B = PlayerElo(preB)
    A.play(B, win=True)
    print A.elo, preA, A.elo - preA
    print B.elo, preB, B.elo - preB



    return
