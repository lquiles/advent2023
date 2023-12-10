from queue import Queue

def init():
  # file = open('day10/sample1.txt', 'r')
  # file = open('day10/sample2.txt', 'r')
  # file = open('day10/sample3.txt', 'r')
  # file = open('day10/sample4.txt', 'r')
  file = open('day10/input.txt', 'r')

  pipes = [['.'] + list(line.strip()) + ['.'] for line in file.readlines()]
  pipes = [['.']*len(pipes[0])] + pipes + [['.']*len(pipes[0])]

  startY,startX = [(y,line.index('S')) for y,line in enumerate(pipes) if 'S' in line][0]

  return (pipes, startY, startX)

def startSymbol(value):
  # ULDR = 1248
  # UL.. =  3 = J
  # U.D. =  5 = |
  # .LD. =  6 = 7
  # U..R =  9 = L
  # .L.R = 10 = -
  # ..DR = 12 = F
  return {
    3:  'J',
    5:  '|',
    6:  '7',
    9:  'L',
    10: '-',
    12: 'F'
  }[value]

def solve(pipes, startY, startX):
  s = set([(startY, startX)])
  q = Queue()

  down = ['7', 'F', '|']
  right = ['F', 'L', '-']
  up = ['J', 'L', '|']
  left = ['7', 'J', '-']

  setup = [
    (startY - 1, startX, down),
    (startY, startX - 1, right),
    (startY + 1, startX, up),
    (startY, startX + 1, left)
  ]

  val = 0
  for i,r in enumerate(setup):
    y,x,v = r
    
    if pipes[y][x] in v:
      val += 2**i
      q.put((y, x, 1))
  
  pipes[startY][startX] = startSymbol(val)

  steps = 1
  while not q.empty():
    y,x,i = q.get()
    s.add((y, x))
    steps = max(steps, i)

    if pipes[y][x] in up    and pipes[y - 1][x] in down  and (y - 1, x) not in s:
      q.put((y - 1, x, i + 1))
    if pipes[y][x] in left  and pipes[y][x - 1] in right and (y, x - 1) not in s:
      q.put((y, x - 1, i + 1))
    if pipes[y][x] in down  and pipes[y + 1][x] in up    and (y + 1, x) not in s:
      q.put((y + 1, x, i + 1))
    if pipes[y][x] in right and pipes[y][x + 1] in left  and (y, x + 1) not in s:
      q.put((y, x + 1, i + 1))
      
  enclosed = 0
  for y,line in enumerate(pipes):
    inside = False
    corner = '.'
    for x,c in enumerate(line):
      if (y,x) in s:
        if c in ['F','L']:
          corner = c

        # Treat F--7 as - and F--J as |
        # Horizontally, a space is inside for odd number of crossing |
        if c == '|' or (c in down and corner in up) or (c in up and corner in down):
          inside = not inside
          corner = '.'
        continue

      if inside:
        enclosed += 1

  return (steps, enclosed)


def main():
  (pipes, startY, startX) = init()
  print((startY, startX))
  steps,enclosed = solve(pipes, startY, startX)
  print((steps, enclosed))


if __name__ == "__main__":
  main()