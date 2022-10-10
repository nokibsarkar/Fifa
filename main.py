import random
team = 4
players = {i : {'id' : i, 'goal' : 0,'score':0} for i in range (1, team + 1)}
# First round 
player = list(players.keys())
random.shuffle(player)
party1, party2 = player[:team // 2], player[team - team // 2 :]
matches_1 = list(zip(party1, party2))
def print_matches(matches):
    for match in matches:
        print(f"{match[0]} vs {match[1]}")
print_matches(matches_1)
winners_1 = []
losers_1 = []
match_count_1 = team // 2
for i in range(match_count_1):
    p1 = int(input("Input the player ID : "))
    if p1 in winners_1 or p1 in losers_1:
        print("Already Added")
    for match in matches_1:
        if p1 in match:
            if match[0] == p1:
                p2 = match[1]
            else:
                p2 = match[0]
            break
    print(f"{p1} played with {p2}")
    p1_goal = int(input(f"\tInput the Goal of {p1} : "))
    p2_goal = int(input(f"\tInput the Goal of {p2} : "))
    players[p1]['goal'] += p1_goal
    players[p2]['goal'] += p2_goal
    if p1_goal == p2_goal:
        print("Match is draw")
        players[p1]['score'] += 1
        players[p2]['score'] += 1
        winners_1.append(p1)
        losers_1.append(p2)
    elif p1_goal > p2_goal:
        players[p1]['score'] += 2
        players[p2]['score'] += 0
        winners_1.append(p1)
        losers_1.append(p2)
    else:
        players[p2]['score'] += 2
        players[p1]['score'] += 0
        winners_1.append(p2)
        losers_1.append(p1)
# print("Winners are : ")
# print(winners_1)
# print("Losers are : ")
# print(losers_1)
def print_score():
    print("Score Table :")
    print("ID\tScore\tGoal")
    for i in players:
        player = players[i]
        print(f"{player['id']}\t{player['score']}\t{player['goal']}")
# round 2
print("\t\tEnd of First round")
print_score()
print("\n\t\t\tSecond Round")

matches_2 = []
winners_1 = winners_1[1:] + winners_1[:1]
matches_2 = list(zip(winners_1, losers_1))
# while True:
#     random.shuffle(winners_1)
#     random.shuffle(losers_1)
#     matches_2 = list(zip(winners_1, losers_1))
#     for m in matches_2:
#         for k in matches_1:
#             if m[0] in k and m[1] in k:
#                 proceed = True
#                 break
#         if proceed:
#             break
#     else:
#         break
print_matches(matches_2)
winners_2 = []
losers_2 = []
match_count_2 = team // 2
for i in range(match_count_2):
    p1 = int(input("Input the player ID : "))
    if p1 in winners_2 or p1 in losers_2:
        print("Already Added")
    for match in matches_2:
        if p1 in match:
            if match[0] == p1:
                p2 = match[1]
            else:
                p2 = match[0]
            break
    print(f"{p1} played with {p2}")
    p1_goal = int(input(f"\tInput the Goal of {p1} : "))
    p2_goal = int(input(f"\tInput the Goal of {p2} : "))
    players[p1]['goal'] += p1_goal
    players[p2]['goal'] += p2_goal
    if p1_goal == p2_goal:
        print("Match is draw")
        players[p1]['score'] += 1
        players[p2]['score'] += 1
        winners_2.append(p1)
        losers_2.append(p2)
    elif p1_goal > p2_goal:
        players[p1]['score'] += 2
        players[p2]['score'] += 0
        winners_2.append(p1)
        losers_2.append(p2)
    else:
        players[p2]['score'] += 2
        players[p1]['score'] += 0
        winners_2.append(p2)
        losers_2.append(p1)
print("End of second round")
print_score()