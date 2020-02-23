import random
import pygame
import sys
import time

bars=[]
pygame.init()
num_bar=20  #no. of bars
bar_width=15    #width of bars
space=5 #space between bars
sorting=False
font = pygame.font.SysFont('Times New Roman', 30)
blue = (0, 0, 255)
black=(0,0,0)
screen=pygame.display.set_mode((800,600))
screen.fill((black))

#To make the graph
def drawbar(x, height,color):  
    pygame.draw.rect(screen, color, (x,400,bar_width, height), 0) 

def button(msg,x,y,w,h):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    global sorting
    if x+w > mouse[0] > x and y+h > mouse[1] > y:      #if mouse pointer is over button
        pygame.draw.rect(screen, (225,225,225),(x,y,w,h), 0)

        if click[0] == 1:     #to break the continuos while loop
            sorting = True 

    else:
        pygame.draw.rect(screen, (200,127,168),(x,y,w,h), 0)

    text = font.render(msg, True, (0, 0, 0))        #text on button
    screen.blit(text, (x + 10, y + 10))
    
#Exit Button    
def button2(msg,x,y,w,h):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    global sorting
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, (225,225,225),(x,y,w,h), 0)

        if click[0] == 1:
            pygame.quit() 

    else:
        pygame.draw.rect(screen, (200,127,168),(x,y,w,h), 0)

    text = font.render(msg, True, (0, 0, 0))
    screen.blit(text, (x + 10, y + 10))    


def insertionsort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,i+1):
            for k in range(num_bar): #to color those that are being checked for comparision
                x=(k*bar_width)+(k*space)+(600-(num_bar *bar_width+num_bar*space))
                height=bars[k]
                if bars[k] is bars[i] or bars[k] is bars[j]:
                    color = (255,127,80)
                else:
                    color=blue  
                drawbar(x,height,color)     
            pygame.display.update()
            time.sleep(.2)
            if arr[j]>arr[i]:
                 arr[j], arr[i]=arr[i], arr[j]
            screen.fill((black))     
            text = font.render("Sorting ", True, (blue))
            screen.blit(text, (300, 100))
            
        
                 

                
#Creating all values
for i in range(num_bar):
    height=random.randint(-100,-10)
    x=(i*bar_width)+(i*space)+(600 -(num_bar *bar_width+num_bar*space))
    drawbar(x,height,blue)
    bars.append(height)
    

#To keep working till user clicks Selection Button or Exits
while True:
    button('Insertion', 300, 100, 130, 50)
    button2("Exit",500,100,70,50)
    pygame.display.update()
    if sorting:
        break
    for event in pygame.event.get():
        if(event==pygame.QUIT):
            pygame.quit()
            sys.exit()

insertionsort(bars)
print("SORTED")
time.sleep(1)
