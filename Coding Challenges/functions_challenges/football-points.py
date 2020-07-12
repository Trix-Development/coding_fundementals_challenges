def football_points(wins, draws, losses):
  calc_wins = wins * 3
  calc_draw = draws + 0
  calc_losses = losses = 0
  return calc_wins + calc_draw + calc_losses  

print(football_points(3,4,2))