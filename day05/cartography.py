import collections

def readMap(file):
  almanac = dict()
  line = file.readline().strip()
#   print(line[:-1])
  while True:
    line = file.readline().strip()
    if line == "":
      return  collections.OrderedDict(sorted(almanac.items()))
    #sorted(almanac)
    target, source, distance = [int(x) for x in line.split(' ') if x]
    almanac[(source, source + distance)] = (target, target + distance)



def main():
  file = open("day05/sample.txt", "r")
#   file = open("day05/input.txt", "r")
  line = file.readline().split(':')[1].strip()
  line = [int(x) for x in line.split(' ') if x]
  it = iter(line)
  seedlist = []
  for x, y in zip(it, it):
    seedlist.extend(range(x, x + y))
  # print(f"{seedlist}")
  file.readline()
  
#   almanac = []
  mapping = readMap(file)
  navigator = [readMap(file)]*6
  for page in navigator:
    almanac = mapping
    mapping = collections.OrderedDict()
    for interval in almanac.keys():
      intervalStart, intervalEnd = interval
      source = almanac[interval]
      sourceStart, sourceEnd = source
      
      for target in page.keys():
        interval = (intervalStart, intervalEnd)
        source = (sourceStart, sourceEnd)
        targetStart, targetEnd = target
        destination = page[target]
        destinationStart, destinationEnd = destination

        if (sourceStart, sourceEnd) == (targetStart, targetEnd):
          mapping[interval] = page[target]
          sourceStart = sourceEnd
          intervalStart = intervalEnd
          break
      
        if sourceStart in range(targetStart, targetEnd):
          startDiff = sourceStart - targetStart
          if sourceEnd in range(targetStart, targetEnd) or sourceEnd == targetEnd:
            endDiff = targetEnd - sourceEnd
            iv = (intervalStart, intervalEnd)
            ds = (destinationStart + startDiff, destinationEnd - endDiff)
            mapping[iv] = ds
            sourceStart = sourceEnd
            intervalStart = intervalEnd
            break
          else:
            endDiff = sourceEnd - targetEnd
            iv = (intervalStart, intervalEnd - endDiff)
            ds = (destinationStart + startDiff, destinationEnd)
            mapping[iv] = ds
            shift = targetEnd - sourceStart
            sourceStart = targetEnd
            intervalStart += shift
            continue
      
        if targetStart in range(sourceStart, sourceEnd):
          startDiff = targetStart - sourceStart
          if targetEnd in range(sourceStart, sourceEnd) or targetEnd == sourceEnd:
            endDiff = sourceEnd - targetEnd
            iv = (intervalStart + startDiff, intervalEnd - endDiff)
            ds = (destinationStart, destinationEnd)
            mapping[iv] = ds
            shift = targetEnd - sourceStart
            sourceStart = targetEnd
            intervalStart += shift
            continue
          else:
            endDiff = targetEnd - sourceEnd
            iv = (intervalStart + startDiff, intervalEnd)
            ds = (destinationStart, destinationEnd - endDiff)
            mapping[iv] = ds
            sourceStart = sourceEnd
            intervalStart = intervalEnd
            break
    
      if intervalStart < intervalEnd:
        iv = (intervalStart, intervalEnd)
        ds = (sourceStart, sourceEnd)
        mapping[iv] = ds
    print(f"{almanac}")
    print(f"{mapping}")

    #   if sourceStart >= min(sourceEnd, targetEnd):
        # break
# def storage():
#       if sourceStart in range(targetStart, targetEnd):
#         stop = min(targetEnd, sourceEnd)
#         startDiff = sourceStart - targetStart
#         endDiff = targetEnd - sourceEnd
#         # start = navigator[destination][0]
#         # end = start + diff
#         mapping[(intervalStart + startDiff, intervalEnd - endDiff)] = (destinationStart + startDiff, destinationEnd - endDiff)
#         intervalStart += (stop - sourceStart)
#         sourceStart = stop

#       if sourceStart != targetEnd and (sourceEnd - 1) in range(targetStart, targetEnd):
#         stop = max(sourceStart, targetStart)
#         endDiff = targetEnd - sourceEnd
#         # end = navigator[destination][1]
#         # start = end - diff
#         mapping[(intervalEnd - endDiff, intervalEnd)] = (destinationEnd - endDiff, destinationEnd)
#         sourceEnd = stop
    
#     if sourceStart < sourceEnd:
#       startDiff = sourceStart - almanac[interval][0]
#       endDiff = almanac[interval][1] - sourceEnd
#       mapping[(intervalStart + startDiff, intervalEnd - endDiff)] = (sourceStart, sourceEnd)
#     print(f"{almanac}")
#     print(f"{mapping}")


def other():
  for page in range(1, 7):
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