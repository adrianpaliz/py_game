import pygame

# Initialize
pygame.init()
# Set up screen
screen = pygame.display.set_mode((600, 800))

game_over = False

# Initial ball position
position_on_x_axis = 300
position_on_y_axis = 400

# Ball speed 
x_axis_speed = 1
y_axis_speed = 1


# Main while loop
while not game_over:
    # Process events
    events = pygame.event.get()    
    for event in events:
        if event.type == pygame.QUIT:
            game_over = True    
    
    # Increased ball movement (Cartesian plane)
    position_on_x_axis += x_axis_speed 
    position_on_y_axis += y_axis_speed 

    #rebound
    if position_on_x_axis >= 600 -10 or position_on_x_axis <= 0 + 10:
        x_axis_speed *= -1
      
    if position_on_y_axis >= 800 - 10 or position_on_y_axis <= 0 + 10:
        y_axis_speed *= -1
    

    # Refresh screen
    screen.fill((255, 0, 0))

    #Game objects modification
    ball = pygame.draw.circle(screen,(255, 255, 0), (position_on_x_axis, position_on_y_axis), 10)
    #Commented line for basic debuging the ball position
    #print(x, y)
    
    pygame.display.flip()

pygame.quit()