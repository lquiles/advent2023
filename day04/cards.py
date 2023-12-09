import re

cardPattern = re.compile("Card\s+(\d+):\s+((?:\d+ )+)\s*\|\s*((?: \d+)?)")

def main():
  input = open("day04/input.txt", "r").readlines()
  total = 0
  count = {index:1 for index, line in enumerate(input)}

  for index, line in enumerate(input):
    matcher = cardPattern.match(line)
    card, line = line.strip().split(':')
    winners, numbers = line.split('|')
    # winners = matcher.group(2).split(' ')
    # numbers = [x for x in matcher.group(3).split(' ') if x in winners]
    winners = sorted([int(x) for x in winners.strip().split(' ') if x])
    # map(int, winners.strip().split(' '))

    numbers = sorted([int(x) for x in numbers.strip().split(' ') if x])
    # map(int, numbers.strip().split(' '))
    
    found = [x for x in numbers if x in winners]
    duplicates = len(found)
    power = duplicates - 1
    
    if (duplicates):
      for x in range(index + 1, min(len(input), index + duplicates + 1)):
        count[x] += count[index] 
    
    if (power >= 0):
      diff = 2**power
    #   print(line.strip())
    #   print(f"{numbers} => {diff}\n")
      total += diff

  print(f"Points: {total}")
  duplicates = [c for _,c in count.items()]
  print(f"Cards: {sum(duplicates)}")
      

if __name__ == "__main__":
  main()