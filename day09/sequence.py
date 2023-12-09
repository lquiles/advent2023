from functools import reduce

def solve(line):
  seq = [int(x) for x in line.split(' ') if x]
  matrix = [seq]
  cursor = seq

  while reduce(lambda x,y: y if x == 0 else x, cursor) != 0:
    cursor = cursor.copy()
    
    for j in range(0, len(cursor)):
      cursor[j] -= (cursor[j] if j < len(matrix) else matrix[-1][j - 1])
    
    matrix.append(cursor)
    
  lsum,rsum = (0, 0)
  for i in reversed(range(0, len(matrix))):
    lsum = matrix[i][i] - lsum
    rsum += matrix[i][-1]
#   print(f"{seq[0:5]} :: {matrix[-1]}")
#   print(f"{(lsum, rsum)}")

  return (lsum, rsum)



def main():
#   file = open('day09/sample.txt', 'r')
  file = open('day09/input.txt', 'r')
  result = [solve(line.strip()) for line in file.readlines()]

  left = [r[0] for r in result]
  right = [r[1] for r in result]
  print((sum(left), sum(right)))



if __name__ == "__main__":
  main()