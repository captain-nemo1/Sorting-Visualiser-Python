#QuickSort code taken from GeeksforGeeks https://www.geeksforgeeks.org/quick-sort/ 
#Quick Sort Code contributed by Mohit Kumra
import random
import pygame
import sys
import time

bars=[]
pygame.init()
num_bar=20  #no. of bars
bar_width=20    #width of bars
space=5 #space between bars
sorting=False
font = pygame.font.SysFont('Times New Roman', 30)
blue = (0, 0, 255)
black=(0,0,0)
screen=pygame.display.set_mode((800,600))
screen.fill((black))
red=(255,0,0)
def drawbar(x, height,color): #to draw rectangle
    pygame.draw.rect(screen, color, (x,400,bar_width, height), 0)

def button(msg,x,y,w,h):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    global sorting
    if x+w > mouse[0] > x and y+h > mouse[1] > y:   #if mouse pointer is over button
        pygame.draw.rect(screen, (225,225,225),(x,y,w,h), 0)

        if click[0] == 1:   #to break the continuos while loop
            sorting = True 

    else:
        pygame.draw.rect(screen, (200,127,168),(x,y,w,h), 0)

    text = font.render(msg, True, (0, 0, 0))    #text on button
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




def partition(arr,low,high): 
    
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
   
    for j in range(low , high):   
        # If current element is smaller than the pivot
        #To color and draw bars initially 
        for m in range(num_bar):    #to color those that are being checked for comparision
                x=(m*bar_width)+(m*space)+(600 -(num_bar *bar_width+num_bar*space))
                if m is j:  
                    color=(200,200,200)  #color the one being scanned white
                elif m is high:#color pivot green
                    color=(0,255,0)            
                else:#color rest blue
                    color=blue 
                drawbar(x,arr[m],color)
              
        pygame.display.update()
        time.sleep(.2)
        screen.fill((black))               
        if   arr[j] < pivot:
            i = i+1  
            
            #to change color for those being swapped
            for k in range(num_bar):    #to color those that are being checked for comparision
                x=(k*bar_width)+(k*space)+(600 -(num_bar *bar_width+num_bar*space))
                if k is high: #color the pivot green
                             color = (0,255,0)
                elif k is i or k is j: #color the one being swapped red
                     color=red
                else:#color the rest blue
                     color=blue         
                drawbar(x,arr[k],color)
            
            text = font.render("Pos:"+str(i), True, (255, 255, 255))
            screen.blit(text, (200, 150))
            text = font.render("Swapped with", True, (255, 255, 255))
            screen.blit(text, (200, 200))
            text = font.render("Pos:"+str(j), True, (255, 255, 255))
            screen.blit(text, (200, 250))
            pygame.display.update()
            time.sleep(.6)
            arr[i],arr[j] = arr[j],arr[i]
            screen.fill(black) 
            #to draw again after swapping
            for k in range(num_bar):    #to color those that are being checked for comparision
                x=(k*bar_width)+(k*space)+(600 -(num_bar *bar_width+num_bar*space))
                if k is high:#color pivot green
                                        color = (0,255,0)
                elif k is i or k is j:#color the one being compared red
                     color=red
                else:#color rest blue
                     color=blue         
                drawbar(x,arr[k],color)
            pygame.display.update()
            time.sleep(1)               
             
    #        
    screen.fill((black))
    #to color pivot again cause it will be swapped later
    for k in range(num_bar):    #to color those that are being checked for comparision
                x=(k*bar_width)+(k*space)+(600 -(num_bar *bar_width+num_bar*space))
                if k is high:
                                        color = (255,0,0)
                else:
                     color=blue         
                drawbar(x,arr[k],color)
    x=((i+1)*bar_width)+((i+1)*space)+(600 -(num_bar *bar_width+num_bar*space))            
    #changing color of the bar which is to replace pivot
    drawbar(x,arr[i+1],(255,0,0))
    text = font.render("Placing Pivot in its Ordered pos", True, (255, 255, 255))
    screen.blit(text, (200, 250))
    pygame.display.update()
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    #To draw and color again before closing the partition() function
    for k in range(num_bar):    #to color those that are being checked for comparision
                x=(k*bar_width)+(k*space)+(600-(num_bar *bar_width+num_bar*space))
                if k is i+1 or k is high:
                                        color = (255,0,0)
                else:
                     color=blue         
                drawbar(x,arr[k],color)
             
    pygame.display.update()
    time.sleep(1)   
    screen.fill(black)
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
  
#Creating all values
for i in range(num_bar):
    height=random.randint(-100,-10)
    x=(i*bar_width)+(i*space)+(600 -(num_bar *bar_width+num_bar*space))
    drawbar(x,height,blue)
    bars.append(height)
    

#To keep working till user clicks Quick Button or Exits
while True:
    button('Quick', 300, 100, 110, 50)
    button2("Exit",500,100,70,50)
    pygame.display.update()
    if sorting:
        break
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            pygame.quit()
            sys.exit()
            
n = len(bars) 
quickSort(bars,0,n-1) 
time.sleep(1)
