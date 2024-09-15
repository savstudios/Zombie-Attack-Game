import pygame, sys

pygame.init()

clock = pygame.time.Clock()

WINDOW_SIZE = (1280,720)

player_img = pygame.image.load('images/player.png')
player_img = pygame.transform.rotate(player_img, 90)
player_loc = [100,100]
player_flip = False
player_vert_flip = False

zombie_img = pygame.image.load('images/zombie.png')

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

movingRight, movingLeft, movingUp, movingDown = False, False, False, False

while True:

   player_movement = [0,0]

   if movingLeft:
      player_movement[0] = -3
   if movingRight:
      player_movement[0] = 3
   if movingUp:
      player_movement[1] = -3
   if movingDown:
      player_movement[1] = 3

   if player_movement[0] > 0:
      player_flip = True
   if player_movement[0] < 0:
      player_flip = False
   if player_movement[1] > 0:
      player_vert_flip = True
   if player_movement[1] < 0:
      player_vert_flip = False

   player_loc[0] += player_movement[0]
   player_loc[1] += player_movement[1]

   screen.fill((100,100,100))

   screen.blit(pygame.transform.flip(player_img, player_flip, player_vert_flip), player_loc)

   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_w:
            movingUp = True
         if event.key == pygame.K_s:
            movingDown = True
         if event.key == pygame.K_a:
            movingLeft = True
         if event.key == pygame.K_d:
            movingRight = True
      if event.type == pygame.KEYUP:
         if event.key == pygame.K_a:
            movingLeft = False
         if event.key == pygame.K_d:
            movingRight = False
         if event.key == pygame.K_w:
            movingUp = False
         if event.key == pygame.K_s:
            movingDown = False


   pygame.display.update()
   clock.tick(60)