def printGrid(grid):
  print('\n')
  print(f' {grid[0][0]} | {grid[0][1]} | {grid[0][2]}')
  print('---|---|---')
  print(f' {grid[1][0]} | {grid[1][1]} | {grid[1][2]}')
  print('---|---|---')
  print(f' {grid[2][0]} | {grid[2][1]} | {grid[2][2]}')
  print('\n')

def swapPositions(grid, c1, c2):
  tmpVal = grid[c1[1]][c1[0]]
  grid[c1[1]][c1[0]] = grid[c2[1]][c2[0]]
  grid[c2[1]][c2[0]] = tmpVal

def extractColumns(grid):
  cols = []
  for x in range(3):
    col = []
    for y in range(3):
      col.append(grid[y][x])
    cols.append(col) 
  return cols 

def findThree(grid):
  # check rows
  for row in grid:
    if row.count(row[0]) == len(row):
      return 'Legal move'
  
  #check columns
  for col in extractColumns(grid):
    if col.count(col[0] == len(col)):
      return 'Legal move'

  return 'Illegal move'



def validateMove(inp, grid):
  splitInput = inp.split(' ')

  if len(splitInput) != 3:
    return 'Invalid input'

  x = splitInput[0]
  y = splitInput[1]
  dir = splitInput[2]

  if not x.isdigit() or not y.isdigit():
    return 'Input valid integer numbers'

  # can now cast safely to int
  x = int(x)
  y = int(y)

  if (x < 0 or x > 2) or (y < 0 or y > 2):
    return 'Values for x and y must be between 0 and 2'

  if dir not in ['up', 'down', 'left', 'right']:
    return 'Value for dir must be one of [up, down, left, right]'

  # input should be valid

  if (dir == 'up' and y == 0) or (dir == 'down' and y == 2) or (dir == 'left' and x == 0) or (dir == 'right' and x == 2):
    return 'Out of bounds move'
   
  newGrid = [row[:] for row in grid]
  c1 = [x, y]
  c2 = [x, y]

  if dir == 'up':
    c2[1] = y - 1
  elif dir == 'down':
    c2[1] = y + 1
  elif dir == 'left':
    c2[0] = x - 1
  elif dir == 'right':
    c2[0] = x + 1
    
  swapPositions(newGrid, c1, c2)

  print('Your move:')
  printGrid(newGrid)
  return findThree(newGrid)

initialGrid = [[1, 2, 3], [4, 4, 5], [5, 3, 4]]
printGrid(initialGrid)

print('Insert coordinates for your move, and a direction, which must be one of [up, down, left, right].\nCoordinates start from the top left, which is 0 0 and end on the bottom right, which is 2 2. Please provide the x value first, followed by the y value and then the direction value.\nA valid input looks like "1 2 down"\n\n')
print(validateMove(input(), initialGrid))
