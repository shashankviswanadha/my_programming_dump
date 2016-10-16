import pygame
import random
pygame.init ()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slither')
img = pygame.image.load ('snake.jpg')



clock = pygame.time.Clock()
font=pygame.font.SysFont(None, 25)
def snake (block_size,snake_list):
    #gameDisplay.blit (img, [snake_list[-1][0],snake_list[-1][1]])
    for XnY in snake_list:
        pygame.draw.rect (gameDisplay, white, [XnY[0],XnY[1],block_size,block_size])
    
def text_objects (text, color):
    textSurf = font.render (text,True,color)
    return textSurf ,textSurf.get_rect()        
    
    
    
def message_to_screen (msg,color):
    textSurf , textRect = text_objects (msg , color)
    textRect.center = (display_width/2) , (display_height/2)
    gameDisplay.blit(textSurf,textRect)
    #screen_text = font.render (msg, True, color)
    #gameDisplay.blit(screen_text, [display_width/2,display_height/2])
def gameLoop():
    FPS = 100
    gameExit = False
    gameOver = False
    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 0
    lead_y_change = 0
    snake_list = []
    snake_length = 1
    block_size = 15
    appleThickness = 2*block_size
    randAppleX = round(random.randrange(0,display_width-block_size)/block_size)*10
    randAppleY = round(random.randrange(0,display_height-block_size)/block_size)*10
    while not gameExit:
      while gameOver == True:
          gameDisplay.fill(white)
          message_to_screen ("Press p to play again or q to quit",red)
          pygame.display.update()
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                      	gameOver = False
    			gameExit = True
              if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_q:
                      gameExit = True
                      gameOver = False
                  if event.key == pygame.K_p:
                      gameLoop()
      for event in pygame.event.get ():
    		if event.type == pygame.QUIT:
    				gameExit = True
    		if event.type == pygame.KEYDOWN:
    			if event.key == pygame.K_LEFT or event.key == pygame.K_a:
    				lead_x_change = -block_size
    				lead_y_change = 0
    			if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
    				lead_x_change = block_size
    				lead_y_change = 0
    			if event.key == pygame.K_UP or event.key == pygame.K_w:
    				lead_y_change = -block_size
    				lead_x_change = 0
    			if event.key == pygame.K_DOWN or event.key == pygame.K_s:
    				lead_y_change = block_size
    				lead_x_change = 0
    		
      if lead_x >= display_width or lead_x <= 0 or lead_y >= display_height or lead_y <= 0:
    		gameOver = True
                 
      lead_x += lead_x_change
      lead_y += lead_y_change
      gameDisplay.fill (black)
      pygame.draw.rect (gameDisplay, red , [randAppleX,randAppleY,appleThickness,appleThickness])
      
      snake_head = []
      snake_head.append(lead_x)
      snake_head.append(lead_y)
      snake_list.append(snake_head)
      if len(snake_list) > snake_length:
          del snake_list[0]
      for segment in snake_list[:-1]:
          if segment == snake_head:
              gameOver = True
      snake (block_size,snake_list)
      pygame.display.update ()
      if ((randAppleX <= lead_x < randAppleX+appleThickness and randAppleY <= lead_y < randAppleY+appleThickness) or (randAppleX < lead_x+block_size <= randAppleX + appleThickness and randAppleY < lead_y+block_size <= randAppleY + appleThickness)):
          randAppleX = round(random.randrange(0,display_width-block_size)/block_size)*10
          randAppleY = round(random.randrange(0,display_width-block_size)/block_size)*10
          snake_length +=1
          FPS +=5
          
      clock.tick(FPS)

    	
    pygame.quit()
    quit()
gameLoop()
