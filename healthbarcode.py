import pygame, sys #this will be changted and used, just putting this here so I don't lose this overall and you guys could pull things from this

class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()#this gives this class access to the functions inside the group class
        self.image = pygame.Surface((40, 40))
        self.image.fill(((240, 240, 240)))
        self.rect = self.image.get_rect(center = (400, 400))
        self.current_health = 200
        self.target_health = 500
        self.maximum_health = 1000
        self.health_bar_length = 400
        self.health_ratio = self.maximum_health / self.health_bar_length
        self.health_change_speed = 5
            
    def get_damage(self,amount):
        if self.target_health > 0:
            self.target_health -= amount
        if self.target_health < 0:
            self.target_health = 0

    def get_health(self,amount):
        if self.target_health < self.maximum_health:
            self.target_health += amount
        if self.target_health > self.maximum_health:
            self.target_health = self.maximum_health
            
    def update(self, amount):
        self.advanced_health()
            
        
    def advanced_health(self):
        transition_width = 0
        transition_color = (255, 0, 0)

        if self.current_health < self.target_health:
            self.current_health += self.health_change_speed
            transition_width = int((self.target_health - self.current_health)/self.health_ratio)
            transition_color = (0, 255, 0)
        if self.current_health > self.target_health:
            self.current_health -= self.health_change_speed
            transition_width = int((self.target_health - self.current_health)/self.health_ratio)
            transition_color = (255, 255, 0)
        
        health_bar_width = int(self.current_health / self.health_ratio)
        health_bar_rect = pygame.Rect(10, 45, self.current_health / self.health_ratio, 25)
        transition_bar_rect = pygame.Rect(health_bar_rect.right, 45, 25, 25)

        pygame.draw.rect(screen, (255, 0, 0), health_bar_rect)
        pygame.draw.rect(screen, transition_color, transition_bar_rect)
        pygame.draw.rect(screen, (255, 255, 255), (10, 45, self.health_bar_length,25), 4)
           
        
        
        
        
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
player = pygame.sprite.GroupSingle(player())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_UP:
            player.sprite.get_health(200)
          if event.key == pygame.K_DOWN:
            player.sprite.get_damage(200)
            
    
    screen.fill((30, 30, 30))
    player.draw(screen)
    player.update(2)
    pygame.display.update()
    clock.tick(60)
