import collections

def readMap(file):
  almanac = dict()
  line = file.readline().strip()

  while True:
    line = file.readline().strip()
    if line == "":
      return  collections.OrderedDict(sorted(almanac.items()))
    
    target, source, distance = [int(x) for x in line.split(' ') if x]
    almanac[(source, source + distance)] = (target, target + distance)


def main():
  # file = open("day05/sample.txt", "r")
  file = open("day05/input.txt", "r")
  line = file.readline().split(':')[1].strip()
  line = [int(x) for x in line.split(' ') if x]
  it = iter(line)
  seedlist = list(zip(it, it))
  seedlist = [(l,l+r) for l,r in seedlist]
  file.readline()

  for page in range(0, 7):
    almanac = readMap(file)
    mapping = []
    for interval in seedlist:
      intervalStart, intervalEnd = interval
      
      for target in almanac.keys():
        targetStart, targetEnd = target
        destination = almanac[target]
        destinationStart, destinationEnd = destination

        if interval == target:
          mapping.append(destination)
          intervalStart = intervalEnd
          break

        if intervalStart in range(targetStart, targetEnd):
          startDiff = intervalStart - targetStart

          if intervalEnd in range(targetStart, targetEnd + 1):
            # target..interval..interval..target
            endDiff = targetEnd - intervalEnd
            ds = (destinationStart + startDiff, destinationEnd - endDiff)
            mapping.append(ds)
            intervalStart = intervalEnd 
            break
          else:
            # target..interval..target..interval
            ds = (destinationStart + startDiff, destinationEnd)
            mapping.append(ds)
            intervalStart = targetEnd

        if targetStart in range(intervalStart, intervalEnd):
          startDiff = targetStart - intervalStart
          
          # interval..target..??..??
          mapping.append((intervalStart, targetStart))

          if targetEnd in range(intervalStart, intervalEnd + 1):
            # interval..target..target..interval
            endDiff = intervalEnd - targetEnd
            ds = (destinationStart, destinationEnd)
            mapping.append(ds)
            intervalStart = targetEnd
            continue
          else:
            # interval..target..interval..target
            endDiff = targetEnd - intervalEnd
            ds = (destinationStart, destinationEnd - endDiff)
            mapping.append(ds)
            intervalStart = intervalEnd
            break

      if intervalStart < intervalEnd:
        ds = (intervalStart, intervalEnd)
        mapping.append(ds)

    seedlist = sorted(mapping)
  print(min(seedlist))


if __name__ == "__main__":
  main()