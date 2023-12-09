
def readMap(file):
  almanac = dict()
  line = file.readline().strip()
#   print(line[:-1])
  while True:
    line = file.readline().strip()
    if line == "":
      return almanac
    target, source, distance = [int(x) for x in line.split(' ') if x]
    almanac[source] = (target, source + distance, target + distance)



def main():
#   file = open("day05/sample.txt", "r")
  file = open("day05/input.txt", "r")
  line = file.readline().split(':')[1].strip()
  line = [int(x) for x in line.split(' ') if x]
  it = iter(line)
  seedlist = []
  for x, y in zip(it, it):
    seedlist.extend(range(x, x + y))
  # print(f"{seedlist}")
  file.readline()
  
  almanac = []
  for page in range(0, 7):
    almanac.append(readMap(file))
    # print(f"{page}: {almanac[page]}")
    keys = sorted(almanac[page].keys())
    for index, seed in enumerate(seedlist):
      for source in keys:
        target, sourceEnd, targetEnd = almanac[page][source]
        if source <= seed and seed < sourceEnd:
          seedlist[index] = target + (seed - source)
          print(f"{index}: {source} < {seed} < {sourceEnd} => {target} < {seedlist[index]} < {targetEnd}")
          break
    #   print(f"{page}: {seed}")
  print(f"{min(seedlist)}")

def other():
  almanac = []
  for page in range(0, 7):
    almanac.append(readMap(file))
    # print(f"{page}: {almanac[page]}")
    keys = sorted(almanac[page].keys())

    for index, seed in enumerate(seedlist):
      for source in keys:
        target, sourceEnd, targetEnd = almanac[page][source]
        if source <= seed and seed < sourceEnd:
          seedlist[index] = target + (seed - source)
          print(f"{index}: {source} < {seed} < {sourceEnd} => {target} < {seedlist[index]} < {targetEnd}")
          break
    #   print(f"{page}: {seed}")
  print(f"{min(seedlist)}")

  




if __name__ == "__main__":
  main()