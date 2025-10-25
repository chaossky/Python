import arcade
from grid import Grid

window = arcade.Window(1024,960,title="Tetris Game")
window.center_window()

class GameView(arcade.View):
    def __init__(self)-> None:
        super().__init__()
        self.grid=Grid()
        
    def on_key_press(self, symbol, modifiers)->None:
        if symbol==arcade.key.UP:
            self.grid.rotate_letter()
        elif symbol==arcade.key.LEFT:
            self.grid.move_left()
            
    def on_draw(self):
        self.clear()
        self.grid.draw_all()
      
game=GameView()
window.show_view(game)
arcade.run()
