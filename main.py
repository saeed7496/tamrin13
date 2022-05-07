
import time
import arcade
from player import Player
from aline import Aline
from ground import Grounde
from ground import Space
from ground import Grass
screen_w=1000
screen_y=630
class Game(arcade.Window):
    def __init__(self):
        super().__init__(screen_w,screen_y,'space humans')
        self.background_image=arcade.load_texture('10223830_928.jpg')
        self.t1=time.time()
        self.space=Space()
        self.grass=Grass()
        self.gameover_flag=0
        self.gras_flag=0
        self.player=Player()
        self.aline_list=arcade.SpriteList()
        self.ground=arcade.SpriteList()
        for i in range(0,1000,40):
            self.ground.append(Grounde(i,0))
        
        for i in range(170,300,40):
            self.ground.append(Grounde(i,200))

        for i in range(380,560,40):
            self.ground.append(Grounde(i,300))
        
        for i in range(250,400,40):
            self.ground.append(Grounde(i,500))

        for i in range(640,780,40):
            self.ground.append(Grounde(i,420))

        self.PhysicsEngine=arcade.PhysicsEnginePlatformer(self.player,self.ground,0.4)
        self.enemy_PhysicsEngine=[]
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,screen_w,screen_y,self.background_image)
        self.space.draw()
        if self.gras_flag==0:
            self.grass.draw()
        self.player.draw()
        for aline in self.aline_list:
            aline.draw()
        for ground in self.ground:
            ground.draw()
        if self.gameover_flag==1:
            arcade.draw_text('GAME OVER',350,250,arcade.color.RED,35)
            arcade.exit()
    def on_update(self,deltatime:float):
        self.t2=time.time()
        self.PhysicsEngine.update()
        self.player.update_animation()
        if arcade.check_for_collision(self.player,self.grass):
            self.gras_flag=1
        if arcade.check_for_collision(self.player,self.space) and self.gras_flag==1:
            self.space.move()
        for item in self.enemy_PhysicsEngine:
            item.update()
        if self.t2-self.t1>5:
            self.new_enemy=Aline()
            self.aline_list.append(self.new_enemy)
            self.enemy_PhysicsEngine.append(arcade.PhysicsEnginePlatformer(self.new_enemy,self.ground,0.4))
            self.t1=time.time()
        for aline in self.aline_list:
            #aline.update_animation()
            if arcade.check_for_collision(self.player,aline):
                self.gameover_flag+=1
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol==arcade.key.RIGHT:
            self.player.change_x=3
        elif symbol==arcade.key.LEFT:
            self.player.change_x=-3
        elif symbol==arcade.key.SPACE:
            if self.PhysicsEngine.can_jump():
                self.player.change_y=13
    def on_key_release(self, symbol: int, modifiers: int):
        self.player.change_x=0
game=Game()
arcade.run()