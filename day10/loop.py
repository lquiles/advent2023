def init():
  # file = open('day10/sample1.txt', 'r')
  # file = open('day10/sample2.txt', 'r')
  file = open('day10/input.txt', 'r')

  pipes = [['.'] + list(line.strip()) + ['.'] for line in file.readlines()]
  pipes = [['.']*len(pipes[0])] + pipes + [['.']*len(pipes[0])]

  startY,startX = [(y,line.index('S')) for y,line in enumerate(pipes) if 'S' in line][0]

  return (pipes, startY, startX)

def main():
  (pipes, startY, startX) = init()
  print(startY, startX)


if __name__ == "__main__":
  main()