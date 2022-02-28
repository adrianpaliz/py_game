#  Import libraries that we are going to use
import pygame

# Initialize pygame
pygame.init()

# Set up screen and define it as a variable
screen = pygame.display.set_mode((600, 800))

game_over = False

# Initial ball position variables
x_position = 300
y_position = 400

# Ball speed variables
x_speed = 1
y_speed = 1

# Main while loop
while not game_over:
    # Process events and define it as a variable
    events = pygame.event.get()   

    for event in events:
        if event.type == pygame.QUIT:
            game_over = True    
    
    # Increased movement of the ball, inside the while loop
    x_position += x_speed 
    y_position += y_speed

    # If for rebound
    # Subtract or add ten from the radius
    if x_position >= 600 -10 or x_position <= 0 + 10:
        # Multiply by minus one to change direction
        x_speed *= -1
      
    if y_position >= 800 - 10 or y_position <= 0 + 10:
        y_speed *= -1    

    # Print the screen
    screen.fill((255, 0, 0))

    # Game objects modification
    ball = pygame.draw.circle(screen,(255, 255, 0), (x_position, y_position), 10)    
    
    # Refresh the screen
    pygame.display.flip()

# Desactives the pygame library
pygame.quit()