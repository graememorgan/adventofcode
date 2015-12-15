import itertools, operator
from re import findall

s = """Sprinkles: capacity 5, durability -1, flavor 0, texture 0, calories 5;PeanutButter: capacity -1, durability 3, flavor 0, texture 0, calories 1;Frosting: capacity 0, durability -1, flavor 4, texture 0, calories 6;Sugar: capacity -1, durability 0, flavor 0, texture 2, calories 8"""

values = [map(int, findall("(-?[0-9]+)", line)) for line in s.split(";")]

# Found on StackOverflow somewhere
def combinations_with_replacement_counts(n, r):
  size = n + r - 1
  for indices in itertools.combinations(range(size), n-1):
    starts = [0] + [index+1 for index in indices]
    stops = indices + (size,)
    yield tuple(map(operator.sub, stops, starts))

print max(
  reduce(operator.mul, nutrition[:-1], 1)
  for nutrition
  in [
    [ # transpose the ingredients--nutritional information list, and take the sum of each
      max(0, sum(line))
      for line
      in zip(
        *[ # add up the nutritional information for each ingredient
          [teaspoons * v for v in value]
          for teaspoons, value
          in zip(combination, values)
        ]
      )
    ]
    for combination
    in combinations_with_replacement_counts(len(values), 100)
  ]
  # for part 2
  #if nutrition[-1] == 500
  )

