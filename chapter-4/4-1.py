import random



def assign_teams(players):
    assert len(players) % 2 == 0
    team = len(players) // 2
    players.sort()

    return [players[:team // 2], players[team // 2 + 1 : team]]



if __name__ == '__main__':
    """
    partition at median, completed in O(n) time
    """
    random.seed(342)
    players = [random.random() for i in range(10)]

    teams = assign_teams(players)
    print(teams)
