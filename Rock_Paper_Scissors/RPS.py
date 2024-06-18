# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random


def player(prev_play, opponent_history=[], player_history = [], player_last_two = [
    {
        'RR': 0, 'RP': 0, 'RS': 0, 'PR': 0, 'PP': 0, 'PS': 0, 'SR': 0, 'SP': 0, 'SS': 0
    }
]):
    opponent_history.append(prev_play)

    # Clear list for each opponent
    if len(opponent_history) > 1000 or len(player_history) > 1000:
        opponent_history.clear()
        player_history.clear()
        player_last_two[0] = {move : 0 for move in player_last_two[0].keys()}


    winner_choice = {'R': 'P', 'P': 'S', 'S': 'R'}

    # First move -> Random

    if not player_history:
        guess = random.choice(list(winner_choice.keys()))
    
    # Beat Quincy

    elif "RPPSR" * 4 in "".join(opponent_history):
        pattern = opponent_history[-5:]
        index_S = pattern.index('S')
        guess = ['R', 'P', 'P', 'S', 'S'][-index_S]
    
    # Beat Kris

    elif all(winner_choice[p] == opponent_history[-10:][o] for o, p in enumerate(player_history[-11:-1])):
        
        kris_choice = winner_choice[player_history[-1]]
        guess = winner_choice[kris_choice]

    # Beat MRugesh

    elif prev_play == winner_choice[max(set(player_history[-11:-1]), key=player_history.count)]:
        mrugesh_choice = winner_choice[max(set(player_history[-10:]), key=player_history.count)]
        guess = winner_choice[mrugesh_choice]

    # Beat Abbey

    else:
        next_play = [
            player_history[-1] + 'R',
            player_history[-1] + 'P',
            player_history[-1] + 'S'
        ]

        search_dict = {
            moves : player_last_two[0][moves]
            for moves in next_play
        }

        abbey_choice = winner_choice[max(search_dict, key=search_dict.get)[-1]]

        guess = winner_choice[abbey_choice]
    

    player_history.append(guess)
    if len(player_history) > 1:
        player_last_two[0][''.join(player_history[-2:])] += 1

    return guess
