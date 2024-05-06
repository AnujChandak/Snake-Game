import pygame
import random
from pygame import mixer

mixer.init()
pygame.init()

length,breadth = 1300, 700
win = pygame.display.set_mode((length, breadth))
pygame.display.set_caption("SNAKE GAME!!!")
pos_x=600
pos_y=300
x=0
y=0
score=0
name=input("Enter your name: ")
mixer.music.load("He is a pirate.wav")
mixer.music.play(-1)

fruit_x= random.randrange(0,(length-20)//20)*20
fruit_y= random.randrange(0,(breadth-20)//20)*20    
word_font = pygame.font.SysFont("TimesNewRoman", 60)
snake_List = []
Length_of_snake = 1

FPS = 60
clock=pygame.time.Clock()
run = True
game_over=False

lines=[]
def my_highscore():
    hisc=open("highscore.txt","r+")
    highscore=hisc.readlines()
    new_list=highscore[0].split()
    global high_name
    high_name=new_list[0]
    highscore=new_list[1]
    #readlines makes a list of all characters
    global highscore_in_no
    highscore_in_no=int(highscore)
    if score>highscore_in_no:
        hisc.seek(0)
        hisc.write(name + " " + str(score))
        highscore_in_no=score
        high_name=name
#use the highscore_in_no to print the highscore.
    hisc.close()

while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
            
        if event.type == pygame.KEYDOWN:
            
            if event.key==pygame.K_LEFT:
                x=-20
                y=0
            elif event.key==pygame.K_RIGHT:
                x=20
                y=0
            elif event.key==pygame.K_DOWN:
                y=20
                x=0
            elif event.key==pygame.K_UP:
                y=-20
                x=0
    pos_x+=x
    pos_y+=y            
    
    win.fill((0,250,0))
    snake=pygame.draw.rect(win,(255,255,255),[pos_x,pos_y,20,20])
    fruit=pygame.draw.rect(win,(255,0,0),[fruit_x,fruit_y,20,20])
        
    text=word_font.render("Your SCORE: " + str(score),True,(0,0,0))
    win.blit(text,[2,2]) 
    
    snake_Head = (pos_x,pos_y)
    snake_List.append(snake_Head)
    if len(snake_List) > Length_of_snake:
        del snake_List[0]
 
    for item in snake_List[:-1]:
        if item == snake_Head:
            my_highscore()
            win.fill((0,255,255))
            pygame.display.update()
            text2=word_font.render("GAME OVER!!!",True,(255,0,0))
            if score>highscore_in_no:
                text3=word_font.render(" New Highscore!!! "+"\t Name: " + high_name,True,(255,0,0))
            else:
                text3=word_font.render("Highscore is: " +  str(highscore_in_no) + "\t Name: " + high_name,True,(255,0,0))
            win.blit(text,[400,280])
            win.blit(text2,[400,180])
            win.blit(text3,[300,380])
            pygame.display.update()
            pygame.time.delay(8000)
            run = False
            
    for item in snake_List:
        pygame.draw.rect(win, (255,255,255), [item[0], item[1], 20,20],4)
        
    if pos_x ==fruit_x and pos_y==fruit_y:
        fruit_x= random.randrange(0,(length-20)//20)*20
        fruit_y= random.randrange(0,(breadth-20)//20)*20
        score+=1
        Length_of_snake+=1
    
    pygame.display.update()
    
    if pos_x<=-5 or pos_x>=1285 or pos_y<=-5 or pos_y>=685:
        my_highscore()
        win.fill((0,255,255))
        pygame.display.update()
        text2=word_font.render("GAME OVER!!!",True,(255,0,0))
        if score>highscore_in_no:
            text3=word_font.render("New Highscore!!!" + "\t Name: " + high_name,True,(255,0,0))
        else:
            text3=word_font.render(" Highscore: " +  str(highscore_in_no) + "\t Name: " + high_name,True,(255,0,0))
        win.blit(text,[400,280])
        win.blit(text2,[400,180])
        win.blit(text3,[300,380])
        pygame.display.update()
        pygame.time.delay(8000)
        run = False
        break   
    clock.tick(25)
pygame.quit()
        
