import random

class Player:
    def __init__(self, name, ranking):
        self.name = name
        self.ranking = ranking
        self.total_points = 0
        self.elo_rating = ranking

def calculate_elo_prob(player1, player2): # calculating probabilities according to elo accepted rules
    ratio = player1.ranking / player2.ranking
    reverse_ratio = 1-ratio if player1.ranking > player2.ranking else -1*(1-ratio)
    player1_win_prob = 0.4 + reverse_ratio
    player2_win_prob = 0.4 - reverse_ratio
    return player1_win_prob, player2_win_prob, 0.2

def simulate_game(player1, player2):
    player1_win_prob, player2_win_prob, draw_prob = calculate_elo_prob(player1, player2)
    outcome = random.uniform(0, 1) # assuming the chess outcome after the round ended.
    if outcome < draw_prob:
        return 0.5
    elif outcome < draw_prob + player1_win_prob:
        return 1  
    else:
        return 2

def update_elo(player, opponent, result):
    if result == 0.5:
        return 
    k_factor = 16  # assuming the players are strong
    expected_score = 1 / (1 + 10**((opponent.elo_rating - player.elo_rating) / 400)) 
    score = 1.0 if result == 1 else 0.0   
    change_in_elo = k_factor * (score - expected_score)
  
    player.elo_rating += change_in_elo
    opponent.elo_rating -= change_in_elo  


def simulate_round_robin(players): #iterate according to robin
    for i in range(len(players)):
        for j in range(i + 1, len(players)):
            result = simulate_game(players[i], players[j])
            players[i].total_points += result
            players[j].total_points += 2 - result  
            update_elo(players[i], players[j], result)

def print_results(players, initial_elo_ratings):
    print("Player\t\tPoints\t\tElo Rating")
    print("*" * 45)
    print("Sorted by Final Ranking (Asc Order):")
    for player in sorted(players, key=lambda x: x.total_points, reverse=True):
        print(f"{player.name}\t{player.total_points}\t\t{player.elo_rating:.2f}")
    
    print("\nSorted by Change in Elo Rating (Desc Order):")
    for player in sorted(players, key=lambda x: initial_elo_ratings[x.name] - x.elo_rating, reverse=True):
        change_in_elo = initial_elo_ratings[player.name] - player.elo_rating
        print(f"{player.name}\t{change_in_elo:.6f}\t\t{player.elo_rating:.2f}")


def main():
    player_names = ["Player 1", "Player 2", "Player 3", "Player 4"]
    players = [Player(name, random.randint(1500, 2000)) for name in player_names]

    initial_elo_ratings = {player.name: player.elo_rating for player in players} 
    simulate_round_robin(players)
    print_results(players, initial_elo_ratings)

main()



