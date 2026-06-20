import pygame
class Paddle:
    def __init__(self, x, y, width=16, height=64):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 6
      
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, up: bool, screen_height: int):
      
        if up:
            self.y -= self.speed
        else:
            self.y += self.speed
            
    
        if self.y < 0:
            self.y = 0
        if self.y + self.height > screen_height:
            self.y = screen_height - self.height
            
   
        self.rect.y = self.y


class Ball:
    def __init__(self, x, y, speed_x=4, speed_y=4, size=16):
        self.x = x
        self.y = y
        self.size = size
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def move(self):
     
        self.x += self.speed_x
        self.y += self.speed_y
        
        self.rect.x = self.x
        self.rect.y = self.y

    def check_collision(self, paddle: Paddle) -> bool:
    
        return self.rect.colliderect(paddle.rect)
