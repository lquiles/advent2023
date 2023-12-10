from queue import Queue

def init():
  # file = open('day10/sample1.txt', 'r')
  # file = open('day10/sample2.txt', 'r')
  file = open('day10/input.txt', 'r')

  pipes = [['.'] + list(line.strip()) + ['.'] for line in file.readlines()]
  pipes = [['.']*len(pipes[0])] + pipes + [['.']*len(pipes[0])]

  startY,startX = [(y,line.index('S')) for y,line in enumerate(pipes) if 'S' in line][0]

  return (pipes, startY, startX)

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

  for y,x,v in setup:
    if pipes[y][x] in v:
      q.put((y, x, 1))

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
      
  return steps


def main():
  (pipes, startY, startX) = init()
  print((startY, startX))
  steps = solve(pipes, startY, startX)
  print(steps)


if __name__ == "__main__":
  main()