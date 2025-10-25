import arcade
import letters

CELL_SIZE=64 # 64X64 pixels
GRID_WIDTH=12 # number of columns
GRID_HEIGHT=15 # number of rows

GRID_H_SIZE=CELL_SIZE*GRID_WIDTH
GRID_V_SIZE=CELL_SIZE*GRID_HEIGHT
GRID_LINE_COLOR=(255,255,255,35)

"""Each letter starts at row1, and column 4 """
START_X=4
START_Y=1

"""Active letter current x (column) and y (row) position on Grid."""
current_x=START_X
current_y=START_Y

class Grid:
    def __init__(self):
        self.main_grid=self.create()
        self.active_letter=letters.letter_T
        self.copy_letter_to_grid()
        self.letter_rotation=1
        
    def try_move(self,x:int,y:int)->bool:
        """ Check if we can move left or right. """
        if self.get_cell(x,y) !=0 :
            return False
        else:
            return True
        
    def move_left(self)->None:
        """ Move the active letter left. """
        global current_x
        breaker=False
        for x in range(GRID_WIDTH):
            if breaker:
                break
            for y in range(GRID_HEIGHT):
                if self.get_cell(x,y)==1:
                    if self.try_move(x-1,y):
                        self.set_cell(x,y,0)
                        self.set_cell(x-1,y,1)
                    else:
                        breaker=True
                        break
        if not breaker:
            current_x-=1
                         
        if self.try_move(current_x-1,current_y):
            self.clear_grid()
            
        
        
    def draw_all(self)->None:
        self.draw_walls()
        self.draw_lines()
        self.draw_letter()
        
    def draw_walls(self)->None:
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                square_x=x*CELL_SIZE
                square_y=(GRID_V_SIZE-CELL_SIZE)-y*CELL_SIZE
                
                if self.get_cell(x,y)==8:
                    arcade.draw_lbwh_rectangle_filled(square_x,square_y,
                                                      CELL_SIZE,CELL_SIZE,
                                                      arcade.color.WHITE)
                    arcade.draw_lbwh_rectangle_outline(square_x,square_y,
                                                      CELL_SIZE,CELL_SIZE,
                                                      arcade.color.AMAZON,2)
                       
    def draw_lines(self)->None:
        for x in range(1,GRID_WIDTH):
            arcade.draw_line(x*CELL_SIZE,0,x*CELL_SIZE,
                             GRID_V_SIZE,GRID_LINE_COLOR,1)
        for y in range(1,GRID_HEIGHT):
            arcade.draw_line(0,y*CELL_SIZE,GRID_H_SIZE,
                             y*CELL_SIZE,GRID_LINE_COLOR,1)
        
    def draw_letter(self)->None:
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                square_x=x*CELL_SIZE
                square_y=(GRID_V_SIZE-CELL_SIZE)-y*CELL_SIZE
                if self.get_cell(x,y)==1:
                    arcade.draw_lbwh_rectangle_filled(square_x,square_y,
                                                      CELL_SIZE,CELL_SIZE,
                                                      self.active_letter["color"])
                    arcade.draw_lbwh_rectangle_outline(square_x,square_y,
                                                       CELL_SIZE,CELL_SIZE,
                                                       arcade.color.BLACK,2)
                    
    def rotate_letter(self)->None:
        """ Rotate the active letter."""
        self.clear_grid()
        self.letter_rotation+=1
        if self.letter_rotation>self.active_letter["num_rotations"]:
            self.letter_rotation=1
        rot=self.active_letter[self.letter_rotation]
        for y in range(len(rot)):
            for x in range(len(rot[y])):
                if rot[y][x]==1:
                    self.set_cell(x+current_x,y+current_y,1)
                    
    def clear_grid(self)->None:
        """ Set the whol grid to 0, except for walls and letters."""
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if self.get_cell(x,y)!=8:
                    self.set_cell(x,y,0)
                           
    def create(self)->list[list]:
        """ Create the Grid structure as a list[list] """
        grid=[]
        for y in range(GRID_HEIGHT):
            grid.append([])
            for x in range(GRID_WIDTH):
                if x==0 or x==GRID_WIDTH-1 or y==GRID_HEIGHT-1:
                    grid[y].append(8)
                else:
                    grid[y].append(0)
        return grid
    
    def get_cell(self,x:int,y:int)->int:
        """ Return the cell value at x(column) and y(row) position from grid. """
        return self.main_grid[y][x]
    
    def set_cell(self,x:int,y:int,value:int)->None:
        """ Sets the cell value at x(column) and y(row) position from grid. """
        self.main_grid[y][x]=value
        
    def copy_letter_to_grid(self)->None:
        """ Copy the active letter to grid. """
        rot=self.active_letter[1]
        for y in range(len(rot)):
            for x in range(len(rot[y])):
                if rot[y][x]==1:
                    if self.get_cell(x+START_X,y+START_Y)==0:
                        self.set_cell(x+START_X,y+START_Y,1)
                    
if __name__=="__main__":
    from pprint import pprint
    g=Grid()
    pprint(g.main_grid)
    
    
# 34:35
 
 