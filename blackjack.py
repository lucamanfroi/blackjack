import random,art, os
over = False

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 10, 10]
player = []
cpu = []

def new_card(someone):
  return someone.append(random.choice(cards))

def game_start():
  print(art.logo)
  new_card(player)
  new_card(cpu)
  new_card(player)
  if player[1] == 11 and sum(player) > 21:
    player.insert(1, 1)
  print(f'Your cards: {player}')
  print(f'First CPU card: {cpu}')
  new_card(cpu)
  if cpu[1] == 11 and sum(cpu) > 21:
    cpu.insert(1, 1)
  ace(cpu)
  cpu_intelligence()
  ace(cpu)

def cpu_intelligence():
  while sum(cpu) <= 16:
    new_card(cpu)

def scores():
  print(f'YOU: {player} = {sum(player)}')
  print(f'CPU: {cpu} = {sum(cpu)}')

def ace(someone):
  for idx, i in enumerate(someone):
    if i == 11 and sum(someone) > 21:
      someone.remove(i)
      someone.insert(idx, 1)

while not over:
  os.system('cls')
  game_start()
  player_hit = input('Type \'h\' to Hit or \'s\' to Stand? ').lower()
  while player_hit == 'h' and sum(player) < 21:
    new_card(player)
    ace(player)
    print(f'Your cards: {player} = {sum(player)}')
    if sum(player) < 21:
      player_hit = input('Type \'h\' to Hit or \'s\' to Stand? ').lower()
  os.system('cls')
  if sum(player) > sum(cpu) and sum(player) <= 21:
    print('You win')
  elif sum(player) < sum(cpu) and sum(cpu) <= 21:
    print('You lose')
  elif sum(player) < sum(cpu) and sum(cpu) > 21:
    print('You win')
  elif sum(player) > sum(cpu) and sum(player) > 21:
    print('You lose')
  elif sum(player) == sum(cpu):
    print('Draw')
  else:
    print('ERROR')
  scores()
  play_again = input('Wanna play again? Type \'y\' for yes or \'n\' for no.\n')
  if play_again == 'n':
    over = True
  else:
    os.system('cls')
    player = []
    cpu = []