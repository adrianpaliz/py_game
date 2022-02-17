import pygame

class Ball:
    def __init__(self, position_x_axis, position_y_axis, color = (255, 255, 0), radius = 10):
        self.position_x_axis = position_x_axis
        self.position_y_axis = position_y_axis
        self.color = color
        self.radius = radius

    def move(self):
        self.position_x_axis += 1
        self.position_y_axis += 1


class Game:
    #initialize function
    def __init__(self, width = 600, height = 800):
        # Instance for screen set up 
        self.screen = pygame.display.set_mode((width, height))
        # Instance for ball set up 
        self.ball = Ball(width // 2, height // 2, (255, 255, 0))

    


    def main_loop(self):
        # While loop end condition
        game_over = False

        # Main while loop
        while not game_over:
            
            # Process events
            events = pygame.event.get()    
            for event in events:
                if event.type == pygame.QUIT:
                    game_over = True


            # Paint the screen
            self.screen.fill((255, 0, 0))

            pygame.draw.circle(self.screen, self.ball.color, 
                                (self.ball.position_x_axis, self.ball.position_x_axis),
                                self.ball.radius)

            # Refresh the screen
            pygame.display.flip()

    

if __name__ == '__main__':
    # Initialize
    pygame.init()

    script = Game()

    script.main_loop()

    pygame.quit()
