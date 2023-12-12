def init(file):
  # (y,x) Location of every galaxy
  galaxies = []
  # All known y coordinates
  ys = set()
  # All known x coordinates
  xs = set()

  for y,line in enumerate([line.strip() for line in file.readlines()]):
    for x,cell in enumerate(list(line)):
      if cell == '#':
        galaxies.append((y,x))
        ys.add(y)
        xs.add(x)
  return (galaxies, ys, xs)

# For a given dimension, compute the expanded travel distance
# pointsInAxis - array of points from all coordinates in one dimension
# point1 - value of the first coordinate in one dimension
# point2 - value of the second coordinate in one dimension
def distance(pointsInAxis, point1, point2):
  # Normal distance
  distance = abs(point1 - point2)
  # Intersect all known values of this dimension with the path
  path = set(range(min(point1,point2), max(point1,point2)))
  # Expanded distance = Normal distance - Path intersection
  expandedDistance = distance - len(pointsInAxis & path)

  scale = int(1E6-1)
  return (distance + expandedDistance, distance + (scale * expandedDistance))


def solve(galaxies, ys, xs):
  total = (0, 0)
  for i in range(0, len(galaxies) - 1):
    for j in range(i + 1, len(galaxies)):
      y1,x1 = galaxies[i]
      y2,x2 = galaxies[j]
      dy,ey = distance(ys,y1,y2) 
      dx,ex = distance(xs,x1,x2)
      total = (total[0] + dy + dx, total[1] + ey + ex)
  return total


def main():
#   file = open('day11/sample.txt', 'r')
  file = open('day11/input.txt', 'r')
  galaxies,ys,xs = init(file)
  total = solve(galaxies,ys,xs)
  print(total)



if __name__ == "__main__":
  main()