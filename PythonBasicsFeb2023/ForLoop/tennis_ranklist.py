import math
tournament_qty = int(input())
start_points = int(input())

tournament_points = 0
avg_points = 0
wins = 0

for i in range(tournament_qty):
    rank = input()
    if rank == "W":
        tournament_points += 2000
        wins += 1
    elif rank == "F":
        tournament_points += 1200
    elif rank == "SF":
        tournament_points += 720

final_points = start_points + tournament_points
avg_points = math.floor(tournament_points / tournament_qty)
wins_percent = wins / tournament_qty * 100

print(f"Final points: {final_points}")
print(f"Average points: {avg_points}")
print(f"{wins_percent:.2f}%")
