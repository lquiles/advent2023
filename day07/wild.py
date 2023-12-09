from collections import Counter
from functools import cmp_to_key
from operator import mul

def cardRank(card):
  return 'J23456789TQKA'.find(card)

def promote(total, counter, jays):
  if counter.most_common(1)[0][1] == 4:
    return 7
  elif total == 4:
    return 3
  elif counter.most_common(1)[0][1] == 2:
    type = 3
  elif counter.most_common(2)[1][1] == 2:
    type = 5
  elif counter.most_common(1)[0][1] == 3:
    type = 4
  else:
    type = 0

def handType(handTyple):
  hand, bid = handTyple
  counter = Counter(list(hand))
  total = len(counter.keys())
  jays = counter['J']

  # Five of a kind, no promotion
  if total == 1:
    type = 7
  
  # High Card (1)
  # One Pair (2) if J2345
  elif total == 5:
    type = 1 if jays == 0 else 2
  
  # One Pair (2)
  # Three of a Kind (4) if J2234 or JJ234
  elif total == 4:
    type = 2 if jays == 0 else 4
  
  # Four of a Kind (6)
  # Five of a Kind (7) if J2222
  elif counter.most_common(1)[0][1] == 4:
    type = 6 if jays == 0 else 7
  
  # Two Pair (3)
  # (3,2) Full House (5) if J2233
  # Four of a Kind (6) if JJ223
  elif counter.most_common(1)[0][1] == 2:
    type = 3 if jays == 0 else 4 + jays
  
  # (3,2) Full House (5)
  # Five of a Kind (7) if JJ222 or JJJ22
  elif counter.most_common(2)[1][1] == 2:
    type = 5 if jays == 0 else 7

  # Three of a Kind (4)
  # Four of a Kind (6) J2223 or JJJ23
  elif counter.most_common(1)[0][1] == 3:
    type = 4 if jays == 0 else 6
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
  # for index, hand in enumerate(ranked):
  #   cards, bet, rank = hand
  #   counter = Counter(list(hand[0]))
  #   jays = counter['J']
  #   print(f"{(rank, cards, jays)} {'{:<50}'.format(str(counter))} {('{:>4}'.format(bet), '{:>4}'.format(index + 1), '{:>7}'.format(bet * (index + 1)))}")
  # print(f"{output}")
  print(sum(output))
  

  

if __name__ == "__main__":
  main()