# Graphing program

import pygame, math, sys
from pygame import *
from math import *
pygame.init()

font = pygame.font.SysFont('Times New Roman', 20)
font2 = pygame.font.SysFont('Bauhaus 93', 36)
font3 = pygame.font.SysFont('Times New Roman', 16)
white = (255, 255, 255)
black = (0, 0, 0)
lightblue = (100, 250, 240)
darkblue = (0, 0, 128)
blue = (51, 153, 255)
orange = (255, 153, 51)
gray = (127, 127, 127)

width, extraW, height = 600, 450, 600
screen = pygame.display.set_mode((width + extraW, height))
pygame.display.set_caption("Max's Personal Grapher")
screen.fill(white)


def graphpaper(k):
    screen.set_clip(0, 0, width, height)
    screen.fill(white)

    for i in range(width/k):
        gridx = k * i
        gridy = k * i
        pygame.draw.line(screen, black, (gridx,0), (gridx,height), 1)
        pygame.draw.line(screen, black, (0,gridy), (width,gridy), 1)
    # thick line
    pygame.draw.line(screen, black, (width,0), (width, height), 10)
    
    # axes (x and y)
    midx, midy = width/(2*k), height/(2*k)
    pygame.draw.line(screen, black, (midx*k,0), (midx*k,height), 3)
    pygame.draw.line(screen, black, (0,midy*k), (width,midy*k), 3)

    # clip reset to all the window
    screen.set_clip(None)
    
# main function
def main(Graphs, eq):
    k = 50

    if Graphs == 1:
        screen.fill(white)
        graphpaper(k)
        equation = []
        eq2 = ' '
    else:
        screen.set_clip(width, 0, width + extraW, height)
        screen.fill(white)
        screen.set_clip(None)
        eq2 = eq
        equation = []
        

    title = font2.render("Max's Personal Grapher", 1, darkblue)
    screen.blit(title, (width + 20, 20))

    title = font.render("Type an equation E.G. x^2+2*x+4.", 1, black)
    screen.blit(title, (width + 20, 70))

    title = font.render("Press 'enter' when done or 'delete' to clear.", 1, black)
    screen.blit(title, (width + 20, 100))

    title = font.render("One square on the graph represents one unit.", 1, black)
    screen.blit(title, (width + 20, 130))

    # Line 1
    shortcuts_height = 190
    shortcuts2_height = 250
    # Line 2
    longversions_height = 210
    longversions2_height = 270

    
    shortcut = font3.render("s",1, black)
    screen.blit(shortcut, (width + 20, shortcuts_height))

    shortcut = font3.render("c",1, black)
    screen.blit(shortcut, (width + 90, shortcuts_height))

    shortcut = font3.render("t",1, black)
    screen.blit(shortcut, (width + 160, shortcuts_height))

    shortcut = font3.render("r",1, black)
    screen.blit(shortcut, (width + 230, shortcuts_height))

    shortcut = font3.render("a",1, black)
    screen.blit(shortcut, (width + 300, shortcuts_height))

    shortcut = font3.render("l",1, black)
    screen.blit(shortcut, (width + 20, shortcuts2_height))

    shortcut = font3.render("n",1, black)
    screen.blit(shortcut, (width + 90, shortcuts2_height))

    shortcut = font3.render("e",1, black)
    screen.blit(shortcut, (width + 160, shortcuts2_height))

    shortcut = font3.render("p",1, black)
    screen.blit(shortcut, (width + 230, shortcuts2_height))



    longversion = font3.render("sin(",1, black)
    screen.blit(longversion, (width + 20, longversions_height))

    longversion = font3.render("cos(",1, black)
    screen.blit(longversion, (width + 90, longversions_height))

    longversion = font3.render("tan(",1, black)
    screen.blit(longversion, (width + 160, longversions_height))

    longversion = font3.render("sqrt(",1, black)
    screen.blit(longversion, (width + 230, longversions_height))

    longversion = font3.render("abs(",1, black)
    screen.blit(longversion, (width + 300, longversions_height))

    longversion = font3.render("log10(",1, black)
    screen.blit(longversion, (width + 20, longversions2_height))

    longversion = font3.render("log(",1, black)
    screen.blit(longversion, (width + 90, longversions2_height))

    longversion = font3.render("e (~2.72)",1, black)
    screen.blit(longversion, (width + 160, longversions2_height))

    longversion = font3.render("pi (~3.14)",1, black)
    screen.blit(longversion, (width + 230, longversions2_height))


    done = False
    active = True
    
    while active:

        # update the screen
        screen.set_clip(width + 10, height - 50, width + extraW, height)
        screen.fill(white)

        eq = str().join(equation)

        eqshow = font.render("Function: y = " + eq, 1, black)
        screen.blit(eqshow, (width + 20, height - 40))
        
        pygame.display.update()

        # keyboard and mouse actions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
                done = True

            elif event.type == pygame.KEYDOWN:
                
                if event.unicode == u'*':
                    equation.append("*")
                elif event.unicode == u'+':
                    equation.append("+")
                elif event.unicode == u'-':
                    equation.append("-")
                elif event.unicode == u'/':
                    equation.append("/")
                elif event.unicode == u'.':
                    equation.append(".")
                elif event.unicode == u'(':
                    equation.append("(")
                elif event.unicode == u')':
                    equation.append(")")
                elif event.unicode == u'^':
                    equation.append("**")
                    
                
                elif event.key == K_1:
                    equation.append("1")
                elif event.key == K_2:
                    equation.append("2")
                elif event.key == K_3:
                    equation.append("3")
                elif event.key == K_4:
                    equation.append("4")
                elif event.key == K_5:
                    equation.append("5")
                elif event.key == K_6:
                    equation.append("6")
                elif event.key == K_7:
                    equation.append("7")
                elif event.key == K_8:
                    equation.append("8")
                elif event.key == K_9:
                    equation.append("9")
                elif event.key == K_0:
                    equation.append("0")

                # Math function commands    s c t r a l n e pi
                elif event.key == K_s:
                    equation.append("sin(")
                elif event.key == K_c:
                    equation.append("cos(")
                elif event.key == K_t:
                    equation.append("tan(")
                elif event.key == K_r:
                    equation.append("sqrt(")
                elif event.key == K_a:
                    equation.append("abs(")
                elif event.key == K_l:
                    equation.append("log10(")
                elif event.key == K_n:
                    equation.append("log(")
                elif event.key == K_e:
                    equation.append("e")
                elif event.key == K_p:
                    equation.append("pi")

                    
                elif event.key == K_x:
                    equation.append("x")

                elif event.key == K_RETURN:
                    active = False
                elif event.key == K_DELETE:
                    equation = []
                    screen.fill(white)
                elif event.key == K_BACKSPACE:
                    del equation[-1]
                elif event.key == K_g:
                    screen.fill(white)
                    main(1, ' ')


    if done:
        pygame.quit()
    else:
        screen.set_clip(width, 0, width + extraW, height - 50)
        screen.fill(white)
        screen.set_clip(None)

        GraphEq(eq, eq2, k)
    sys.exit()

def GraphEq(eq, eq2, k):

    for i in range(width):
        try:
            x = (width/2 - i)/float(k)
            y = eval(eq)
            pos1 = (width/2 + x * k, height/2 - y * k)
            
            nx = x = (width/2 - i - 1)/float(k)
            ny = eval(eq)
            pos2 = (width/2 + nx * k, height/2 - ny * k)

            pygame.draw.line(screen, blue, pos1, pos2, 3)
        except:
            pass

        try:
            x = (width/2 - i)/float(k)
            y2 = eval(eq2)
            pos1 = (width/2 + x * k, height/2 - y2 * k)
            
            nx = x = (width/2 - i - 1)/float(k)
            ny2 = eval(eq2)
            pos2 = (width/2 + nx * k, height/2 - ny2 * k)

            pygame.draw.line(screen, blue, pos1, pos2, 3)
        except:
            pass

    # keep text sharp
    screen.set_clip(width, 0, width + extraW, height - 50)
    
    # title
    title = font2.render("Max's Personal Grapher", 1, darkblue)
    screen.blit(title, (width + 20, 20))

    # resizing grid
    title = font.render("To resize the grid, press 's' 'm' or 'l'.", 1, black)
    screen.blit(title, (width + 20, 70))

    title = font.render("You can also press '+' to zoom in and '-' to zoom", 1, black)
    screen.blit(title, (width + 20, 100))

    title = font.render("out until a certain point.", 1, black)
    screen.blit(title, (width + 20, 130))

    # new graph
    title = font.render("Press 'g' to add a graph on a new layer.", 1, black)
    screen.blit(title, (width + 20, 290))

    title = font.render("Press 'n' to replace this graph with another.", 1, black)
    screen.blit(title, (width + 20, 260))



    
    x = 0
    try:
        yint = eval(eq)
        yint = round(yint, 2)
        yint = int(yint)
    except:
        yint = 'dne'

    title = font.render("The y-intercept is at (0, " + str(yint) + ").", 1, black)
    screen.blit(title, (width + 20, 180))

    if yint != 'dne':
        title = font.render("Select 'y' to plot the y-intercept.", 1, black)
        screen.blit(title, (width + 20, 210))

    title = font.render("Type in a value, then select 'enter' to plot the point.", 1, black)
    screen.blit(title, (width + 20, 340))

    # plotting x values
    xValue = []
    xVal = '?'
    yVal = '?'
    

    # reset clip of screen
    screen.set_clip(None)
        
    active = True
    while active:
        
        screen.set_clip(width + 20, 370, width + extraW, 100)
        screen.fill(white)
        xDisplay = string.join(xValue)
        xDisplay = string.replace(xDisplay, " ", "")
        
        plotx = font.render("x = " + str(xDisplay), 1, black)
        screen.blit(plotx, (width + 20, 370))

        ploty = font.render("(" + str(xVal) + ",  " + str(yVal) + ")", 1, black)
        screen.blit(ploty, (width + 150, 370))
        screen.set_clip(None)

        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False

            elif event.type == pygame.KEYDOWN:
                if event.key == K_g: # to draw a new graph overlay
                    main(2, eq)
                elif event.key == K_y:
                    pygame.draw.circle(screen, lightblue, (width/2, height/2 - yint * k), 3)

                # resize commands
                elif event.key == K_l:
                    k = 100
                    screen.fill(white)
                    graphpaper(k)
                    GraphEq(eq, eq2, k)
                    
                elif event.key == K_m:
                    k = 50
                    screen.fill(white)
                    graphpaper(k)
                    GraphEq(eq, eq2, k)
                    
                elif event.key == K_s:
                    k = 25
                    screen.fill(white)
                    graphpaper(k)
                    GraphEq(eq, eq2, k)

                elif event.key == K_n: # to add another graph, replacing this one
                    main(1, ' ')

                elif event.key == K_RETURN:
                    try:
                        x = xVal = float(xDisplay)
                        yVal = eval(eq)
                        pygame.draw.circle(screen, black, (width/2 + x * k, height/2 - yVal * k), 4)
                        xValue = []
                    except:
                        pass

                elif event.unicode == u'=':
                    k = k + 10
                    screen.fill(white)
                    graphpaper(k)
                    GraphEq(eq, eq2, k)

                elif event.unicode == u'-':
                    xValue.append("-")

                elif event.unicode == u'+':
                    k = k + 10
                    screen.fill(white)
                    graphpaper(k)
                    GraphEq(eq, eq2, k)

                elif event.unicode == u'/':
                    xValue.append("/")


                elif event.key == K_1:
                    xValue.append("1")
                elif event.key == K_2:
                    xValue.append("2")
                elif event.key == K_3:
                    xValue.append("3")
                elif event.key == K_4:
                    xValue.append("4")
                elif event.key == K_5:
                    xValue.append("5")
                elif event.key == K_6:
                    xValue.append("6")
                elif event.key == K_7:
                    xValue.append("7")
                elif event.key == K_8:
                    xValue.append("8")
                elif event.key == K_9:
                    xValue.append("9")
                elif event.key == K_0:
                    xValue.append("0")

                elif event.unicode == u'.':
                    xValue.append(".")


    pygame.quit()
    sys.exit()

if __name__=='__main__':
    main(1, ' ')
    
