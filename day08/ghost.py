from functools import reduce
from operator import mul
from math import gcd

def parse(file):
  guide = dict()
  for line in [x.strip() for x in file.readlines()]:
    position,fork = line.split("=")
    left,right = fork.strip()[1:-1].split(',')
    guide[position.strip()] = (left.strip(), right.strip())
  return guide

def ghosting(cycles):
  if all(c > 0 for c in cycles):
    return False
  return True

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

def main():
  # file = open("day08/sample3.txt", "r")
  file = open("day08/input.txt", "r")
  directions = file.readline().strip()
  file.readline()

  guide = parse(file)
  length = len(directions)
  step = 0
  locations = [x for x in guide.keys() if x[2] == 'A']
  cycles = [0]*len(locations)
  print(f"begin: 0 {locations} {cycles}")

  while ghosting(cycles):
    side = "LR".find(directions[step % length])
    navigation = [guide[position][side] for position in locations]

    locations = navigation
    step += 1

    for idx,nav in enumerate(navigation):
      if nav[2] == 'Z' and cycles[idx] <= 0:
        cycles[idx] += step if cycles[idx] < 0 else -step
        print(f"{step}: {navigation} {cycles}")
  
  result = reduce(lambda x,y: lcm(x,y), cycles)
  print(f"Step {step}: {cycles} => {result}")  

 

if __name__ == "__main__":
  main()