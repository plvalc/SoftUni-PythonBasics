actor_name = input()
academy_points = float(input())
jury_qty = int(input())

actor_points = 0
nominee = 0

for i in range(jury_qty):
    if i == 0:
        actor_points += academy_points
    jury_name = input()
    jury_points = float(input())

    actor_points += len(jury_name) * jury_points / 2
    if actor_points > 1250.5 and nominee == 0:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {actor_points:.1f}!")
        nominee = 1

if nominee == 0:
    diff = 1250.5 - actor_points
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")
