import random
import arcade
class Aline(arcade.Sprite):
    def __init__(self):
        super().__init__(':resources:images/alien/alienBlue_front.png')
        self.width=40
        self.height=60
        self.center_x=random.randint(0,1000)
        self.center_y=700
        self.change_x=random.choice([-1,1])
        '''
        self.stand_right_textures=[arcade.load_texture(':resources:images/alien/alienBlue_front.png')]
        
        self.stand_left_textures=[arcade.load_texture(':resources:images/alien/alienBlue_front.png',mirrored=True)]
        
        self.walk_right_textures=[arcade.load_texture(':resources:images/alien/alienBlue_walk1.png'),
                                arcade.load_texture(':resources:images/alien/alienBlue_walk2.png')]
        
        self.walk_left_textures=[arcade.load_texture(':resources:images/alien/alienBlue_walk1.png',mirrored=True),
                                arcade.load_texture(':resources:images/alien/alienBlue_walk2.png',mirrored=True)]
        
        '''
        