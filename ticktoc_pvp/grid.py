Skip to content
 
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 @gMatas Sign out
0
0 0 gMatas/Random
 Code  Issues 0  Pull requests 0  Projects 0  Wiki  Insights  Settings
Random/TicToc/TicToc/grid.py
071954a  on Dec 1, 2018
@gMatas gMatas Add visualise_v2 method
    
79 lines (58 sloc)  1.8 KB
from typing import List


class Grid:

    def __init__(self):
        self.grid_mat = Grid.__initialise_grid_mat()

    def visualise(self) -> None:
        grid_mat_element_gen = self.__create_grid_mat_element_generator()

        str_rows = list()

        for ri in range(7):
            if ri % 2 == 0:
                str_rows.append('+---+---+---+')
                continue

            str_row = ''
            for ci in range(13):
                if ci % 4 == 0:
                    str_row += '|'
                elif ci % 2 != 0:
                    str_row += ' '
                else:
                    str_row += next(grid_mat_element_gen)
            str_rows.append(str_row)
     
        print('\n'.join(str_rows))

    def visualise_v2(self):
        str_rows = [
            '  {} | {} | {}  '.format(*self.grid_mat[0][:]),
            '----+---+-----',
            '  {} | {} | {}  '.format(*self.grid_mat[1][:]),
            '----+---+-----',
            '  {} | {} | {}  '.format(*self.grid_mat[2][:])
        ]
        
        print('\n'.join(str_rows))

    def __create_grid_mat_element_generator(self):
        for ri in range(3):
            for ci in range(3):
                yield self.grid_mat[ri][ci]
            
    @staticmethod
    def __initialise_grid_mat() -> List[List[str]]:
        grid = [[' ' for _ in range(3)] for _ in range(3)]
        return grid


print('Visualise grid:')
grid = Grid()

print('Step 1')
grid.grid_mat[1][1] = 'X'
grid.visualise()
print()

print('Step 2')
grid.grid_mat[0][2] = 'O'
grid.visualise()
print()


print('New visualisation method:')
grid = Grid()

print('Step 1')
grid.grid_mat[1][1] = 'X'
grid.visualise_v2()
print()

print('Step 2')
grid.grid_mat[0][2] = 'O'
grid.visualise_v2()
print()
© 2019 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About
Press h to open a hovercard with more details.
