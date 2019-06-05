from collections import defaultdict
import pandas as pd

matrix = []
d = defaultdict(list)
nb_rows, nb_cols = 1000, 1000
neighbor_locs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class Cell:
    def __init__(self, value, length, loc, child_loc, bottom):
        self.value = value
        self.length = length
        self.loc = loc
        self.child_loc = child_loc
        self.bottom = value
    
    def __str__(self):
        return '{}, {}, {}, {}'.format(self.value, self.length, self.loc, self.child_loc, self.bottom)
    
    def __repr__(self):
        return '{}, {}, {}, {}'.format(self.value, self.length, self.loc, self.child_loc, self.bottom)

    def update_values(self, loc):
        for dxy in neighbor_locs:
            x = loc[0] + dxy[0]
            y = loc[1] + dxy[1]
            
            # find all the neighbour cell with lower value
            if (x >= 0) and (y >= 0) and (x < nb_rows) and (y < nb_cols) and (self.value > matrix[x][y].value):
                lower_cell = matrix[x][y]
                need_update = False
                
                # update path if (1) there are longer path can be constructed or (2) exists path with same length but larger drop value
                if self.length <= lower_cell.length:
                    need_update = True
                elif self.length == lower_cell.length + 1:
                    if (self.value - self.bottom) < (self.value - lower_cell.bottom):
                        need_update = True
                if need_update:
                    self.length = lower_cell.length + 1
                    self.child_loc = lower_cell.loc
                    self.bottom = lower_cell.bottom    
        
with open('./map.txt', 'r') as f:
    nb_rows, nb_cols = map(int, f.readline().split(' '))
    row = 0
    for line in f:
        values = map(int, line.split(' '))
        data = [Cell(value, 1, (row, col), (row, col), value) for col, value in enumerate(values)]
        matrix.append(data)
        for col, value in enumerate(values):
            d[value].append((row, col))
        row += 1    
        
for i in range(1, 1500):
    cell_locs = d[i]
    for loc in cell_locs:
        matrix[loc[0]][loc[1]].update_values(loc)
max_len = 0
max_location = None
for i in range(nb_rows):
    for j in range(nb_cols):
        if max_len < matrix[i][j].length:
            max_len = matrix[i][j].length
            max_location = (i, j)
print max_len, max_location # 15 (161, 395)

# print path
cell = matrix[max_location[0]][max_location[1]]
while cell.bottom != cell.value:
    print cell.loc, cell.value
    child_loc = cell.child_loc
    cell = matrix[child_loc[0]][child_loc[1]]
print cell.loc, cell.value

"""
(161, 395) 1466
(161, 396) 1078
(160, 396) 932
(159, 396) 915
(159, 395) 848
(159, 394) 820
(159, 393) 527
(160, 393) 516
(160, 394) 355
(161, 394) 126
(162, 394) 76
(162, 395) 71
(162, 396) 67
(162, 397) 56
(161, 397) 47
"""

# result: 151419: length of the longest path: 15, largest drop: 1466 - 47: 1419
