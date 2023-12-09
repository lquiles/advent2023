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

#   for y in range(starty, endy + 1):
#     print(input[y][startx:endx + 1])

  for y in range(starty, endy + 1):
    for x in range(startx, endx + 1):
      c = input[y][x]
      if c != "." and c.isdigit() == False and c != '\n':
        # print(f"\033[93m{(tuple[0], tuple[1], tuple[2], tuple[3], y, x, c)}\033[0m")
        # print(f"\nT {tuple[4]} L {tuple[1]} V {tuple[0]} P {(c, y - tuple[1], x - tuple[2], x - tuple[3])}")
        # print(f"\n{(tuple[0], c, y - tuple[1], x - tuple[2], x - tuple[3])} L {tuple[1]} T {tuple[4]}")
        # for z in range(starty, endy + 1):
        #   print(input[z][startx:endx + 1])
        # print(f"{(c, y - tuple[1], x - tuple[2], x - tuple[3])}")
        positions[tuple[1]].append(tuple[2])
        return tuple[0]
      
#   print(f"\033[91m{(tuple[0], tuple[1], tuple[2], tuple[3], False)}\033[0m")
  return 0

def main():
  input = open("day03/input.txt", "r").readlines()
  digits = []
  count = 0

  for index, line in enumerate(input):
    matcher = digitPattern.finditer(line)
    for match in matcher:
      coordinates = (int(match.group(0)), index, match.start(), match.end() - 1, count)
      count += 1
    #   print(coordinates)
      digits.append(coordinates)

  sum = 0
  count = 0
  row = 0
#   uniq = set()
  positions = {key: [] for key in range(0, 140)}

  for index, tuple in enumerate(digits):
    if tuple[1] == row:
      print(f"\nLine {row}")

      for y in range(max(0, row - 1), min(len(input), row + 2)):
        print(input[y].strip())
      row += 1

    # print(f"\nTuple {index} Line {tuple[1]}")
    value = process(input, tuple, positions)
    if value > 0:
      count += 1
    #   print(f"{sum + value} = {sum} + {value}")

    sum += value
#   print(sorted(uniq))

  print(positions)
  print(f"\nFound {count} values totalling {sum}")
      

if __name__ == "__main__":
  main()