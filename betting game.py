
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

bet_game = {}

game_over = False
while not game_over:
  user = input("whats is your name\n")
  money = int(input("whats your bet ?\n"))
  bet_game[user] = money
  play_again = input("ay other players?\n")
  if play_again == "n":
    game_over = True
    # print(bet_game)

top = 0
for val in bet_game:
  if bet_game[val] > top :
    top = bet_game[val]
# print(top)
keys_list = list(bet_game.keys())
values_list = list(bet_game.values())
ewinner  = values_list.index(top)

winner = keys_list[ewinner]

print(f"the winner of the game is {winner} with bet {top}")
