spells = {"poison": 173, "shield": 113, "magic missile": 53, "drain": 73, "recharge": 229}

def simulate(casts):
  player_hp, player_mana, player_armor = 50, 500, 0
  mana_expended = 0

  boss_hp, boss_damage = 71, 10

  ticks = {"shield": 0, "poison": 0, "recharge": 0}
  turn = True

  while True:
    # apply shield effect
    player_armor = 7 if ticks["shield"] else 0
    # apply poison effect
    if ticks["poison"]:
      boss_hp -= 3
    # apply recharge
    if ticks["recharge"]:
      player_mana += 101

    # hard mode!
    if turn:
      player_hp -= 1

    # have we lost?
    if player_hp <= 0 or player_mana <= 0:
      return (False, -1)
    # have we won?
    if boss_hp <= 0:
      return (True, mana_expended)

    for k in ticks.keys():
      ticks[k] = max(0, ticks[k] - 1)

    if turn:
      # player turn
      if len(casts):
        cast = casts.pop(0)
        player_mana -= spells[cast]
        mana_expended += spells[cast]
        if cast == "magic missile":
          boss_hp -= 4
        elif cast == "drain":
          player_hp += 2
          boss_hp -= 2
        elif cast == "shield":
          if ticks["shield"] != 0:
            return (False, -1)
          ticks["shield"] = 6
        elif cast == "poison":
          if ticks["poison"] != 0:
            return (False, -1)
          ticks["poison"] = 6
        elif cast == "recharge":
          if ticks["recharge"] != 0:
            return (False, -1)
          ticks["recharge"] = 5
      else:
        break
    else:
      # boss turn
      player_hp -= boss_damage - player_armor

    # have we lost?
    if player_hp <= 0 or player_mana <= 0:
      return (False, -1)
    # have we won?
    if boss_hp <= 0:
      return (True, mana_expended)

    turn = not turn


  return (False, mana_expended)

best = 100000

def recurse(casts):
  global best
  for spell in spells.keys():
    won, expended = simulate(casts[:])
    if won:
      print casts
      print expended
      best = min(expended, best)
    if not won and expended != -1 and expended < best:
      recurse(casts + [spell])

recurse([])

print best
