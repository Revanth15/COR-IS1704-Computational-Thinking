change = float(input("What is the change? "))
change_cents = change * 100

note_10 = int(change_cents) // 1000
change_cents %= 1000
if note_10 > 0:
    print("$10 note:", note_10)

note_2 = int(change_cents) // 200
change_cents %= 200
if note_2 > 0:
    print("$2 note:", note_2)

coin_100 = int(change_cents) // 100
change_cents %= 100
if coin_100 > 0:
    print("$1 coin:", coin_100)

coin_10 = int(change_cents) // 10
change_cents %= 10
if coin_10 > 0:
    print("10 cents coin:", coin_10)

coin_1 = int(change_cents) // 1
change_cents %= 1
if coin_1 > 0:
    print("1 cent coin:", coin_1)