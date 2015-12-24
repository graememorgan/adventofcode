s = """jio a, +19;inc a;tpl a;inc a;tpl a;inc a;tpl a;tpl a;inc a;inc a;tpl a;tpl a;inc a;inc a;tpl a;inc a;inc a;tpl a;jmp +23;tpl a;tpl a;inc a;inc a;tpl a;inc a;inc a;tpl a;inc a;tpl a;inc a;tpl a;inc a;tpl a;inc a;inc a;tpl a;inc a;inc a;tpl a;tpl a;inc a;jio a, +8;inc b;jie a, +4;tpl a;inc a;jmp +2;hlf a;jmp -7"""

instructions = map(lambda x: x.split(" "), s.split(";"))

pc = a = b = 0

# part 2
a = 1

while 0 <= pc < len(instructions):
  instruction = instructions[pc]
  if instruction[0] == "hlf":
    if instruction[1] == "a":
      a /= 2
    else:
      b /= 2
  elif instruction[0] == "tpl":
    if instruction[1] == "a":
      a *= 3
    else:
      b *= 3
  elif instruction[0] == "inc":
    if instruction[1] == "a":
      a += 1
    else:
      b += 1
  elif instruction[0] == "jmp":
    pc += int(instruction[1]) - 1
  elif instruction[0] == "jie":
    if a % 2 == 0:
      pc += int(instruction[2]) - 1
  elif instruction[0] == "jio":
    if a == 1:
      pc += int(instruction[2]) - 1

  pc += 1

print a, b
