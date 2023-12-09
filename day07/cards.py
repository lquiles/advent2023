from collections import Counter
from functools import cmp_to_key
from operator import mul

def cardRank(card):
  return '23456789TJQKA'.find(card)


def handType(handTyple):
  hand, bid = handTyple
  counter = Counter(list(hand))
  total = len(counter.keys())

  if total == 1:
    type = 7
  elif total == 4:
    type = 2
  elif total == 5:
    type = 1
  elif counter.most_common(1)[0][1] == 4:
    type = 6
  elif counter.most_common(1)[0][1] == 2:
    type = 3
  elif counter.most_common(2)[1][1] == 2:
    type = 5
  elif counter.most_common(1)[0][1] == 3:
    type = 4
  else:
    type = 0
  return (hand, bid, type)

def compareHand(leftTuple, rightTuple):
  lc, lb, lt = leftTuple
  rc, rb, rt = rightTuple
  if lt > rt:
    return 1
  if lt < rt:
    return -1
  for i in range(0, 5):
    l = cardRank(lc[i])
    r = cardRank(rc[i])
    if l > r:
      return 1
    if l < r:
      return -1
  return 0

def parse(line):
  hand, bid = [x for x in line.strip().split() if x]
  return handType((hand, int(bid)))

def main():
  # file = open("day07/sample.txt", "r")
  file = open("day07/input.txt", "r")
  input = [parse(line) for line in file.readlines()]
  ranked = sorted(input, key=cmp_to_key(lambda x, y: compareHand(x, y)))
  output = [hand[1] * (index + 1) for index,hand in enumerate(ranked)]
  # print(f"{input}")
  # print(f"{ranked}")
  # print(f"{output}")
  print(sum(output))
  

  

if __name__ == "__main__":
  main()