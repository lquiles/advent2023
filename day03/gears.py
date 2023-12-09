#     0 1 2 3 4
#   | - - - - -
# 0 | . . . . .
# 1 | . . 9 8 .
# 2 | . . . . .
# => (98, 1, 2, 3)

# partNumbers: list[(id: int, ly: int, lx: int, rx: int)]
# parts: list[y: int][x: int]
# for tuple in partsNumbers
#   if any value in parts[ly-1:ly+1][lx-1:rx+1] exists
#     sum += id

import re

digitPattern = re.compile("([0-9]+)")

def process(input, tuple, positions):
  maxlen = len(input) - 1
  maxwidth = len(input[0]) - 1
  starty = max(0, tuple[1] - 1)
  startx = max(0, tuple[2] - 1)
  endy = min(maxlen, tuple[1] + 1)
  endx = min(maxwidth, tuple[3] + 1)
  
  for y in range(starty, endy + 1):
    for x in range(startx, endx + 1):
      c = input[y][x]
      if c == '*':
        key = y * maxwidth + x
        pos = positions[key] if key in positions else []
        pos.append(tuple[0])
        positions[key] = pos

def main():
  # input = open("day03/sample.txt", "r").readlines()
  input = open("day03/input.txt", "r").readlines()
  digits = []
  count = 0

  for index, line in enumerate(input):
    matcher = digitPattern.finditer(line)
    for match in matcher:
      coordinates = (int(match.group(0)), index, match.start(), match.end() - 1, count)
      count += 1
      digits.append(coordinates)

  positions = {key: [] for key in range(0, 140)}
  for index, tuple in enumerate(digits):
    process(input, tuple, positions)

  sum = 0
  for key, val in positions.items():
    if len(val) == 2:
      print(f"{key}: {val}")
      sum += val[0] * val[1]

  print(sum)
      

if __name__ == "__main__":
  main()