from math import ceil

boss = {"hp": 104, "damage": 8, "armor": 1}

weapons = [
  {"cost":  8, "damage": 4, "armor": 0},
  {"cost": 10, "damage": 5, "armor": 0},
  {"cost": 25, "damage": 6, "armor": 0},
  {"cost": 40, "damage": 7, "armor": 0},
  {"cost": 74, "damage": 8, "armor": 0}]

armors = [
  {"cost":   0, "damage": 0, "armor": 0},
  {"cost":  13, "damage": 0, "armor": 1},
  {"cost":  31, "damage": 0, "armor": 2},
  {"cost":  53, "damage": 0, "armor": 3},
  {"cost":  75, "damage": 0, "armor": 4},
  {"cost": 102, "damage": 0, "armor": 5}]

rings = [
  {"cost":   0, "damage": 0, "armor": 0},
  {"cost":  25, "damage": 1, "armor": 0},
  {"cost":  50, "damage": 2, "armor": 0},
  {"cost": 100, "damage": 3, "armor": 0},
  {"cost":  20, "damage": 0, "armor": 1},
  {"cost":  40, "damage": 0, "armor": 2},
  {"cost":  80, "damage": 0, "armor": 3}]

minimum = 100000
maximum = 0

for weapon in weapons:
  for armor in armors:
    for ring1 in rings:
      for ring2 in rings:
        if ring1["cost"] == ring2["cost"]:
          continue
        player = {}
        player["hp"] = 100
        player["armor"] = weapon["armor"] + armor["armor"] + ring1["armor"] + ring2["armor"]
        player["damage"] = weapon["damage"] + armor["damage"] + ring1["damage"] + ring2["damage"]
        cost = weapon["cost"] + armor["cost"] + ring1["cost"] + ring2["cost"]
        if ceil(float(boss["hp"]) / max(player["damage"] - boss["armor"], 1)) <= ceil(float(player["hp"]) / max(boss["damage"] - player["armor"], 1)):
          minimum = min(minimum, cost)
        else:
          maximum = max(maximum, cost)

print minimum, maximum
