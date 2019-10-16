import random

bank = int(input('How much money do you have:'))
inp = bank
bet = 1

winning_list = []


for x in range(365):
    winnings = 0
    bet = 1
    bank = inp

    for i in range(50):
        if bet > bank:
            print("BANKRUPT")


            print()
            break

        else:
            choice = random.randint(19, 36)
            result = random.randint(0, 36)

            if result <= 18:
                bank -= bet
                winnings -= bet
                bet = bet * 2

            else:

                bank += bet
                winnings += bet
                bet = 1

    winning_list.append(winnings)

print("You have made", winning_list, "dollars")
