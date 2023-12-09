def parse(file):
  guide = dict()
  for line in [x.strip() for x in file.readlines()]:
    position,fork = line.split("=")
    left,right = fork.strip()[1:-1].split(',')
    guide[position.strip()] = (left.strip(), right.strip())
  return guide


def main():
#   file = open("day08/sample1.txt", "r")
#   file = open("day08/sample2.txt", "r")
  file = open("day08/input.txt", "r")
  directions = file.readline().strip()
  file.readline()

  guide = parse(file)
  length = len(directions)
  step = 0
  location = "AAA"

  while location != "ZZZ":
    side = "LR".find(directions[step % length])
    next = guide[location][side]
    print(f"{step}.{location}.{directions[step%length]}{side}: {guide[location]} => {next}")

    location = next
    step += 1
  print(step)
 

if __name__ == "__main__":
  main()