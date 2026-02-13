import random

players = [sorted(random.sample(range(1, 91), 5)) for _ in range(2)]

print("Tickets:")
for i, t in enumerate(players, start=1):
    print(f"Player {i}: {t}")

drawn_numbers = list(range(1, 91))
random.shuffle(drawn_numbers)

print("\nNumbers drawn:", drawn_numbers[:8], "...")

first_five = drawn_numbers[:5]
print("First five numbers:", first_five)

for i, ticket in enumerate(players, start=1):
    matched = [num for num in first_five if num in ticket]
    if len(matched) == 5:
        print(f"Player {i} wins with ticket {ticket}")
        break
else:
    print("No winner with the first five numbers.")