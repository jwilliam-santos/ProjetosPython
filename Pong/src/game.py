import pygame
from .physics import Paddle, Ball

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        
      
        self.player1 = Paddle(30, self.screen_height // 2 - 32) #
        self.player2 = Paddle(self.screen_width - 30 - 16, self.screen_height // 2 - 32) 
        self.ball = Ball(self.screen_width // 2 - 8, self.screen_height // 2 - 8)
        
        self.paddle_img = pygame.image.load("assets/Paddle.png").convert_alpha()
        self.ball_img = pygame.image.load("assets/ball.png").convert_alpha()
        self.hit_sound = pygame.mixer.Sound("assets/hit.wav")
        self.score_sound = pygame.mixer.Sound("assets/score.wav")
        
       
        self.score1 = 0
        self.score2 = 0

    def handle_input(self):
    
        keys = pygame.key.get_pressed()
       
        if keys[pygame.K_w]:
            self.player1.move(up=True, screen_height=self.screen_height)
        if keys[pygame.K_s]:
            self.player1.move(up=False, screen_height=self.screen_height)
            
    
        if keys[pygame.K_UP]:
            self.player2.move(up=True, screen_height=self.screen_height)
        if keys[pygame.K_DOWN]:
            self.player2.move(up=False, screen_height=self.screen_height)

    def update(self):
        
        self.ball.move()
   
        if self.ball.y <= 0 or self.ball.y + self.ball.size >= self.screen_height:
            self.ball.speed_y *= -1
            self.hit_sound.play() #
       
        if self.ball.check_collision(self.player1):
            self.ball.speed_x = abs(self.ball.speed_x) 
            self.hit_sound.play()
        elif self.ball.check_collision(self.player2):
            self.ball.speed_x = -abs(self.ball.speed_x) 
            self.hit_sound.play()

  
        if self.ball.x < 0:
            self.score2 += 1
            print(self.score2)
            self.score_sound.play()
            self.reset_ball()
        elif self.ball.x > self.screen_width:
            self.score1 += 1
            print(self.score1)
            self.score_sound.play()
            self.reset_ball()

    def reset_ball(self):
        
        self.ball.x = self.screen_width // 2 - 8
        self.ball.y = self.screen_height // 2 - 8
        self.ball.speed_x *= -1

    def draw(self):
  
        self.screen.fill((0, 0, 0))
        
   
        self.screen.blit(self.paddle_img, (self.player1.x, self.player1.y))
        self.screen.blit(self.paddle_img, (self.player2.x, self.player2.y))
        
     
        self.screen.blit(self.ball_img, (self.ball.x, self.ball.y))