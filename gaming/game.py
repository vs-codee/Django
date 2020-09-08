import pygame
import random

pygame.init()

# Colors
white = (255, 255, 255);
red = (255, 0, 0);
black = (0, 0, 0);
green=(123,43,43);

Font=pygame.font.SysFont('Purisa', 30, bold=True, italic=False)
Font1=pygame.font.SysFont('DejaVu Sans', 40, bold=True, italic=False)

#text display
# def screen_text(text,color,x,y):

# Creating window
screen_width = 900 
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Game of Snake");
pygame.display.update();

# Game specific variables


clock = pygame.time.Clock();

def snake_plot(lst):
    for x,y in lst:
        pygame.draw.rect(gameWindow, black, [x, y, 25, 25]);



def gameloop():
    exit_game = False;
    game_over = False;
    snake_x = 45 ;
    snake_y = 55;
    velocity_x = 0;
    velocity_y = 0;
    lst=[];
    for i in range(50,76,5):
        lst.append([i,55]);
    snake_length=1;

    food_x = random.randint(20, screen_width//2);
    food_y = random.randint(20, screen_height//2);
    score = 0;
    init_velocity = 5;
    snake_size = 25;
    fps = 30;
    while not exit_game:
        if game_over:
            gameWindow.fill(white);
            screen_text=Font1.render("Your Game is Over",True,green);
            gameWindow.blit(screen_text,[200,250]);
            screen_text1=Font1.render("Press Enter To Play Again",True,green);
            gameWindow.blit(screen_text1,[160,300]);
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        gameloop();
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score*=score;


            snake_x+= velocity_x
            snake_y+= velocity_y

            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                score +=1
                # print("Score: ", score * 10)
                food_x = random.randint(20, screen_width // 2)
                food_y = random.randint(20, screen_height // 2)
                snake_length+=5;
            
            gameWindow.fill(white)
            screen_text=Font.render("SCORE: "+str(score),True,green);
            gameWindow.blit(screen_text,[10,10]);
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size]);

            head=[];
            print(snake_x,snake_y);
            # head.append(snake_x);
            # head.append(snake_y);
            lst.append([snake_x,snake_y]);

            if len(lst)>snake_length:
                del lst[0]
            print(lst);
            snake_plot(lst);
            for i in range(len(lst)):
            	for j in range(i+1,len(lst)):
            		if(lst[i][0]==lst[j][0] and lst[i][1]==lst[j][1]):
            			game_over=True;
                                              
        pygame.display.update();
        clock.tick(fps)
    pygame.quit()
    quit()
gameloop();


