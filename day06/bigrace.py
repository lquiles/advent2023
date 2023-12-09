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
  # file = open("day06/sample1.txt", "r")
  file = open("day06/input.txt", "r")

  racetime = int(''.join([x for x in file.readline().split(':')[1].strip().split(' ') if x]))
  racedist = int(''.join([x for x in file.readline().split(':')[1].strip().split(' ') if x]))
  print(f"{racetime}")
  print(f"{racedist}")
  win = 0
  for x in range(0, racetime):
    if x > (racetime + 1) / 2:
      break
    if x * (racetime - x) > racedist:
      win = (racetime + 1 - (2 * x))
      break
  print(f"{win}")
  

if __name__ == "__main__":
  main()