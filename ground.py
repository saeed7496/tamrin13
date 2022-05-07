import arcade

class Grounde(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__(':resources:gui_basic_assets/red_button_normal.png')
        self.center_x=x
        self.center_y=y
        self._width=40
        self.height=40

class Space(arcade.Sprite):
    def __init__(self):
        super().__init__(':resources:images/space_shooter/playerShip3_orange.png')
        self.height=180
        self.width=120
        self.center_x=900
        self.center_y=145
        self.change_y=700
    
    def move(self):
        self.center_y+=self.change_y
        
class Grass(arcade.Sprite):
    def __init__(self):
        super().__init__(':resources:images/tiles/grass_sprout.png')

        self.height=80
        self.width=60
        self.center_x=250
        self.center_y=560
