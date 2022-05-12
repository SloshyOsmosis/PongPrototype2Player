#Imports the modules, sys adds more functionality such as exiting the game.
import pygame, sys, random

#Required before running any pygame code.
pygame.init()

#Adjusts window size.
screen_width = 1280
screen_height = 960

#Creates the window.
screen = pygame.display.set_mode((screen_width,screen_height))
#Gives the window a title.
pygame.display.set_caption('Pong')

pongball = pygame.Rect(screen_width/2 - 15,screen_height/2 - 15,30,30) #Draws the ball
sprite = pygame.Rect(screen_width - 20,screen_height/2 - 70,10,140) #Draws the player on the screen
opsprite = pygame.Rect(10, screen_height/2 - 70, 10, 140) #Draws the opponent

#Adjusts the color of the window background.
bg_color = pygame.Color('white')
light_grey = (200,200,200)
white = (255,255,255)
black = (0,0,0)

ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1)) #The random library is used to make the direction of the pong ball go in a random direction.
player_speed = 0 #Variable to determine the player speed if no key is being pressed
opponent_speed = 0

#Variables for the score board.
player_score = 0 
opponent_score = 0
game_font = pygame.font.Font(None,108) #Determines the font of the text, the parameters being the font style and font size.

def animation(): #Creates the function for the animation of the ball
  global ball_speed_x, ball_speed_y, player_score, opponent_score #Global allows me to use the ball speed variables outside the function.
  pongball.x += ball_speed_x
  pongball.y += ball_speed_y
  
  if pongball.top <= 0 or pongball.bottom >= screen_height:
    ball_speed_y *= -1 #The minus one causes the ball to go the opposite direction.

  if pongball.left <= 0:
    player_score += 1
    ball_restart()

  if pongball.right >= screen_width:
    ball_restart()
    opponent_score += 1
  
  if pongball.colliderect(sprite) or pongball.colliderect(opsprite):
    ball_speed_x *= -1
    
def player_animation(): #Creates the function for the player boundaries.
  if sprite.top <= 0:
    sprite.top = 0 #Resets the players position to the edge of the screen if the player attempts to go out of bounds by scrolling off the screen.
  if sprite.bottom >=screen_height:
    sprite.bottom = screen_height #Causes the player to be always teleported to the border if they try to scroll off-screen.

def opponent_animation(): #Creates the function for the opponent boundaries.
    
  if opsprite.top <= 0: 
    opsprite.top = 0 
  if opsprite.bottom >=screen_height:
    opsprite.bottom = screen_height #This section is repeated from the player animation function so that the opponent does not also go out of bounds from the screen.

def ball_restart(): #This function will randomise which direction the ball will go in.
  global ball_speed_y, ball_speed_x
  pongball.center = (screen_width/2, screen_height/2)
  ball_speed_y *= random.choice((1,-1))
  ball_speed_x *= random.choice((1,-1))#Use of the random library.
    
while True: #A while loop is used so that the game does not close on startup.
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()  #Creates an event if the user wants to exit the game.
    if event.type == pygame.KEYDOWN: #Creates an event if the player presses the up or down key, this in turn will cause the player to move up or down respectively.
      if event.key == pygame.K_DOWN:#If the down key has been pressed, the player moves down at a certain speed continously, without the player speed variable the player would only move at one smidge at a time, causing the player to repeatedly press the down key to move a significant amount. This has been avoided by use of the player speed variable.
        player_speed += 8.5 #Controls for the right player. The controls used are the up and down key.
      if event.key == pygame.K_UP:
        player_speed -= 8.5
    if event.type == pygame.KEYUP: #Creates an event if the player lets go of the up or down key.
      if event.key == pygame.K_DOWN:
        player_speed -= 8.5
      if event.key == pygame.K_UP:
        player_speed += 8.5

    if event.type == pygame.KEYDOWN: #Controls for the left player. The controls used are the W and S key.
      if event.key == pygame.K_s:
        opponent_speed += 8.5
      if event.key == pygame.K_w:
        opponent_speed -= 8.5
    if event.type == pygame.KEYUP: #Creates an event if the player lets go of the up or down key.
      if event.key == pygame.K_s:
        opponent_speed -= 8.5
      if event.key == pygame.K_w:
        opponent_speed += 8.5



  
  animation()
  player_animation()
  opponent_animation()
  #Calling my functions in the while loop
  sprite.y += player_speed
  opsprite.y += opponent_speed
  
  screen.fill(bg_color)#Sets the background color.
  pygame.draw.rect(screen,black,sprite)#Draws the player rectangle.
  pygame.draw.rect(screen,black,opsprite)#Draws the opponent rectangle.
  pygame.draw.ellipse(screen,black,pongball)#Draws the pong ball.
  pygame.draw.aaline(screen,black,(screen_width/2,0), (screen_width/2,screen_height))#Draws the dividing line.

  player_text = game_font.render(f"{player_score}",False,black)#Displays the score of the player
  screen.blit(player_text,(960,25))

  opponent_text = game_font.render(f"{opponent_score}",False,black)#Displays the score of the player
  screen.blit(opponent_text,(290,25))
  #Updating the window
  pygame.display.flip()
  gametime.tick(60) #Runs the game in 60 Frames per second, without this the game will run as fast as the computer will allow it to.
