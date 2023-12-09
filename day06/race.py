# x + y = t
# x * y > d
# x * (t - x) > d
# t*x - x^2 > d
# t - x > d/x
# t - d/x > x

# (t - x + 1) - x = solution
# t - 2x + 1 = solution

from functools import reduce
from operator import mul

def main():
#   file = open("day06/sample.txt", "r")
  file = open("day06/input.txt", "r")

  racetime = [int(x) for x in file.readline().split(':')[1].strip().split(' ') if x]
  racedist = [int(x) for x in file.readline().split(':')[1].strip().split(' ') if x]
  print(f"{racetime}")
  print(f"{racedist}")
  win = []
  for idx in range(0, len(racetime)):
    time = racetime[idx]
    dist = racedist[idx]
    
    for x in range(0, time):
      if x > time:
        win.append(0)
        break
      if x * (time - x) > dist:
        win.append(time + 1 - (2 * x))
        break
  print(f"{win}")
  print(f"{reduce(mul, win, 1)}")
  

if __name__ == "__main__":
  main()