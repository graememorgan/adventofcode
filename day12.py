from re import findall
from json import loads

s = open("day12-input").read()

print sum(map(int, findall("(-?[0-9]+)", s)))

def recurse(i):
  if type(i) is int:
    return i
  if type(i) is list:
    return sum(recurse(j) for j in i)
  if type(i) is not dict:
    return 0
  if 'red' in i.values():
    return 0
  return recurse(i.values())

print recurse(loads(s))
