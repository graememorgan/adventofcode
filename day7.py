
values = {k: v for v, k in [line.split(" -> ") for line in open("day7-input").read().split("\n") if line]}

# for part 2:
#values["b"] = 46065

# gets the value associated with a register, and (importantly) caches it
def getValue(register):
  global values
  # return the integer represented if the register is just an integer
  if register.isdigit():
    return int(register)

  expression = values[register]
  # if this has already been computed and cached, return it
  if type(expression) is int:
    return expression

  words = expression.split(" ")
  if "AND" in expression:
    value = getValue(words[0]) & getValue(words[2])
  elif "NOT" in expression:
    value = ~getValue(words[1])
  elif "LSHIFT" in expression:
    value = getValue(words[0]) << getValue(words[2])
  elif "RSHIFT" in expression:
    value = getValue(words[0]) >> getValue(words[2])
  elif "OR" in expression:
    value = getValue(words[0]) | getValue(words[2])
  elif expression.isdigit(): 
    value = int(expression)
  else: # must just be a simple assignment
    value = getValue(expression)

  values[register] = value
  return value

print getValue("a")

