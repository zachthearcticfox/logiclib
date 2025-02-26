from termcolor import colored as clr
import cm2py as cm2

XOR = 1
AND = 2
OR = 3
NOT = 4
INPUT_PIN = 5
OUTPUT_PIN = 6

# ============================
# Logic Functions
# ============================
def xor_(a:int,b:int):
    return a ^ b

def and_(a:int,b:int):
    return a & b

def or_(a:int, b:int):
    return ~(~(a) & ~(b))

def not_(a:int):
    return ~(a)

class Circuit:
    def __init_subclass__(self):
        print('logiclib v0.0.4 (beta)')
        print('class: Circuit')
        self.blocks = []
    
    def add_block(self, id_:int, posx:int, posy:int):
        match id_:
            case 1: self.blocks.append(['XOR', posx, posy])
            case 2: self.blocks.append(['AND', posx, posy])
            case 3: self.blocks.append(['OR', posx, posy])
            case 4: self.blocks.append(['NOT', posx, posy])
            case 5: self.blocks.append(['INPUT_PIN', posx, posy])
            case 6: self.blocks.append(['OUTPUT_PIN', posx, posy])
            case _: print('Invalid ID')

    def list_blocks(self):
        return self.blocks
    
    def color_visualize(self):
        grid_cv = self.get_xy_grid()
        for i in grid_cv:
            for j in i:
                print(j, end=' ')
            print()

    def get_xy_grid(self):
        self.grid = [
            [clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black')],
            [clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black')],
            [clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black')],
            [clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black')],
            [clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black')],
            [clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black')],
            [clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black')],
            [clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black')],
            [clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black')],
            [clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black'),clr('-', 'black')]
        ]

        for i in self.blocks:
            match i[0]:
                case 'XOR': self.grid[i[2]][i[1]] = clr('|', 'magenta')
                case 'AND': self.grid[i[2]][i[1]] = clr('|', 'blue')
                case 'OR': self.grid[i[2]][i[1]] = clr('|', 'green')
                case 'NOT': self.grid[i[2]][i[1]] = clr('|', 'red')
                case 'INPUT_PIN': self.grid[i[2]][i[1]] = clr('|', 'black')
                case 'OUTPUT_PIN': self.grid[i[2]][i[1]] = '|'
                case _: self.grid[i[2]][i[1]] = i[0]

        return self.grid
    
    def to_cm2_save(self):
        tempsave = cm2.Save()
        
        for y in range(10):
            for x in range(10):
                if self.get_xy_grid()[y][x] == clr('|', 'magenta'):
                    tempsave.addBlock(cm2.XOR, (x,0,y))
                elif self.get_xy_grid()[y][x] == clr('|', 'blue'):
                    tempsave.addBlock(cm2.AND, (x,0,y))
                elif self.get_xy_grid()[y][x] == clr('|', 'green'):
                    tempsave.addBlock(cm2.OR, (x,0,y))
                elif self.get_xy_grid()[y][x] == clr('|', 'red'):
                    tempsave.addBlock(cm2.NOR, (x,0,y))
                elif self.get_xy_grid()[y][x] == clr('|', 'black'):
                    tempsave.addBlock(cm2.FLIPFLOP, (x,0,y))
                elif self.get_xy_grid()[y][x] == '|':
                    tempsave.addBlock(cm2.NODE, (x,0,y))
        
        return tempsave.exportSave()