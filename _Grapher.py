# OOP Graphing Utility by Max Goodridge
# OCR F454 School Project

import pygame, math, sys
from pygame import *
from math import *

pygame.init()

class TextOnScreen:
    ### Define class properties
    # Fonts
    # Title font
    font1 = font.SysFont('Bauhaus 93', 36)

    # Instructions font
    #font2 = font.SysFont('Ariel', 24)
    font2 = font.SysFont('Verdana', 16)

    # Shortcuts font
    #font3 = font.SysFont('Times New Roman', 16)
    font3 = font.SysFont('Verdana', 14)

    # Equation font
    #font4 = font.SysFont('Times New Roman', 20)
    font4 = font.SysFont('Verdana', 20)

    # Font for invalid equation entries
    font5 = font.SysFont('Verdana', 12)

    # Constants
    instructionsWidth = 20
    shortcutsHeight = 0

    def title(self, screen, text, width, height):
        title = self.font1.render(text, 1, GrapherMain.darkBlue)
        screen.blit(title, (width, height))

    def instructions(self, screen, text, height):
        instructions = self.font2.render(text, 1, GrapherMain.black)
        screen.blit(instructions, (self.instructionsWidth, height))

    def shortcuts(self, screen, text, width, wNum):
        if wNum == 1:
            self.shortcutsHeight = 190
        elif wNum == 2:
            self.shortcutsHeight = 250
        elif wNum == 3:
            self.shortcutsHeight = 210
        elif wNum == 4:
            self.shortcutsHeight = 270

        self.shortcutsHeight += 260

        shortcuts = self.font3.render(text, 1, GrapherMain.black)
        screen.blit(shortcuts, (width, self.shortcutsHeight))


class GrapherMain:

    ### Define class properties

    # Colours
    white = (255, 255, 255)
    black = (0, 0, 0)
    lightBlue = (100, 250, 240)
    darkBlue = (20, 100, 220)
    blue = (51, 153, 255)
    orange = (255, 153, 51)
    red = (255, 0, 0)
    gray = (127, 127, 127)
    lightGray = (245, 245, 245)
    linesGray = (200, 200, 200)

    # Window size
    width = 600
    extraWidth = 450
    height = 600

    # Possible k values for graph resizing
    kValues = [20, 25, 50, 100, 150]
    kIndex = 3

    # Property linked to graph number
    graph = 1

    # Init method will run automatically when class is instantiated
    def __init__(self, Graphs, eq):
        screen = display.set_mode((self.width + self.extraWidth, self.height))

        # Name of standard window
        display.set_caption("Grapher")
        screen.fill(self.white)

        ### Create the graph paper
        # k is the number of pixels per unit on the grid
        # k must always be a factor of width and height
        k = self.kValues[self.kIndex]

        COLOUR = self.blue
        if Graphs == 1:
            screen.fill(self.white)
            self.graphPaper(k, screen)
            equation = []
            eq2 = ' '
        elif Graphs == 2:
            screen.set_clip(0, 0, self.extraWidth + self.width, self.height)
            screen.fill(self.white)
            screen.set_clip(None)
            self.graphPaper(k, screen)
            eq2 = eq
            equation = []
            self.plotLine(screen, k, eq2, self.blue)

        ### Create all text and blit on screen
        # Create an instance of TextOnScreen class
        screenOneInfo = TextOnScreen()

        # Create title
        screenOneInfo.title(screen, "Grapher", 20, 20)

        # Create instructions
        screenOneInfo.instructions(screen, "One square represents one unit.", 70)
        screenOneInfo.instructions(screen, "Press 'enter' when done or 'delete' to clear.", 100)
        screenOneInfo.instructions(screen, "Type an equation e.g. 2sin(x) - 3.", 130)

        ### Create shortcuts
        # 80px between shortcuts horizontally
        # Short
        screenOneInfo.shortcuts(screen, "s", 20, 1)
        screenOneInfo.shortcuts(screen, "c", 100, 1)
        screenOneInfo.shortcuts(screen, "t", 180, 1)
        screenOneInfo.shortcuts(screen, "r", 260, 1)
        screenOneInfo.shortcuts(screen, "a", 340, 1)
        screenOneInfo.shortcuts(screen, "l", 20, 2)
        screenOneInfo.shortcuts(screen, "n", 100, 2)
        screenOneInfo.shortcuts(screen, "e", 180, 2)
        screenOneInfo.shortcuts(screen, "p", 260, 2)

        # Long
        screenOneInfo.shortcuts(screen, "sin(", 20, 3)
        screenOneInfo.shortcuts(screen, "cos(", 100, 3)
        screenOneInfo.shortcuts(screen, "tan(", 180, 3)
        screenOneInfo.shortcuts(screen, "sqrt(", 260, 3)
        screenOneInfo.shortcuts(screen, "abs(", 340, 3)
        screenOneInfo.shortcuts(screen, "log10(", 20, 4)
        screenOneInfo.shortcuts(screen, "ln(", 100, 4)
        screenOneInfo.shortcuts(screen, "e (~2.72)", 180, 4)
        screenOneInfo.shortcuts(screen, "pi (~3.14)", 260, 4)


        while True:
            # Constantly refresh the screen
            display.update()

            # Equation array refreshing
            buffer1 = 20
            screen.set_clip(buffer1, 180, self.extraWidth - 2* buffer1, 40)
            screen.fill(self.white)
            screen.set_clip(None)
            screen.set_clip(buffer1, 227, self.extraWidth - 2*buffer1, 40)
            screen.fill(self.lightGray)
            screen.set_clip(None)

            ### Join strings to equation array without commas
            eq = "".join(equation)

            # Remove spaces
            eq = eq.replace(" ", "")

            # Render and blit equation
            showEqLabel = screenOneInfo.font4.render("Equation:", 1, self.black)
            screen.blit(showEqLabel, (30, 195))
            showEq = screenOneInfo.font4.render("y = " + eq, 1, self.black)
            screen.blit(showEq, (30, 232))

            # Prepare equation for the main processing algorithm in self.plotLine
            eq = eq.replace("^", "**")
            eq = eq.replace("ln(", "log(")
            eq = eq.replace("pix", "pi*x")
            for num in range(10):
                eq = eq.replace(str(num)+ "x", str(num) + "*x")
                eq = eq.replace(str(num)+ "sin(", str(num) + "*sin(")
                eq = eq.replace(str(num)+ "cos(", str(num) + "*cos(")
                eq = eq.replace(str(num)+ "tan(", str(num) + "*tan(")
                eq = eq.replace(str(num)+ "sqrt(", str(num) + "*sqrt(")
                eq = eq.replace(str(num)+ "abs(", str(num) + "*abs(")
                eq = eq.replace(str(num)+ "log10(", str(num) + "*log10(")
                eq = eq.replace(str(num)+ "log(", str(num) + "*log(")
                eq = eq.replace(str(num)+ "e", str(num) + "*e")
                eq = eq.replace(str(num)+ "pi", str(num) + "*pi")
                eq = eq.replace(str(num)+ "ex", str(num) + "e*x")

            # Check for any necessary events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # When a key is pressed, do something
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
                        equation.append("^")

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
                        equation.append("ln(")
                    elif event.key == K_e:
                        equation.append("e")
                    elif event.key == K_p:
                        equation.append("pi")

                    elif event.key == K_x:
                        equation.append("x")
                    elif event.key == K_RETURN:
                        if len(equation) > 0:
                            # Amend eq where necessary to avoid an exception
                            if eq.count("(") > eq.count(")"):
                                count = eq.count("(") - eq.count(")")
                                eq += ")" * count

                            # Clip screen
                            screen.set_clip(0, 0, self.extraWidth, 190)
                            screen.fill(self.white)
                            screen.set_clip(0, 300, self.extraWidth, self.height - 300)
                            screen.fill(self.white)
                            screen.set_clip(None)

                            # Reset to correct colour
                            if Graphs == 1:
                                COLOUR = self.blue
                            else:
                                COLOUR = self.orange

                            # Plot the graph based on the equation input
                            self.plotLine(screen, k, eq, COLOUR)
                            self.presentScreenTwo(screen, k, eq, eq2)
                        break

                    elif event.key == K_DELETE:
                        equation = []
                        screen.fill(white)
                    elif event.key == K_BACKSPACE:
                        if len(equation) > 0:
                            del equation[-1]
                    elif event.key == K_g:
                        screen.fill(self.white)
                        GrapherMain(1, ' ')
        #sys.exit()

    def graphPaper(self, k, screen):
        # k is the number of pixels per unit on the grid
        screen.set_clip(self.extraWidth, 0, self.width, self.height)
        screen.fill(self.lightGray)

        # Draw graph paper
        for i in range(int(self.width/k + 1)):
            if i != self.width/k:
                gridx = k * i
                gridy = k * i
            else:
                gridx = k * i - 1
                gridy = k * i - 1

            draw.line(screen, self.linesGray, (self.extraWidth + gridx, 0),
                      (self.extraWidth + gridx, self.height), 1)
            draw.line(screen, self.linesGray, (self.extraWidth, gridy),
                      (self.extraWidth + self.width, gridy), 1)

        # thick line between instructions and graph
        draw.line(screen, self.black, (self.extraWidth, 0),
                  (self.extraWidth, self.height), 5)

        # x and y axes
        midx = self.width/(2*k)
        midy = self.height/(2*k)

        # y axis
        draw.line(screen, self.black, (self.extraWidth + midx*k, 0), (self.extraWidth + midx*k, self.height), 2)

        # x axis
        draw.line(screen, self.black, (self.extraWidth, midy*k), (self.extraWidth + self.width, midy*k), 2)

        # Reset the clip on 'screen' to entire window
        screen.set_clip(None)

    def plotLine(self, screen, k, eq, COLOUR):

        # Graph the line, one pixel at a time
        for i in range(self.width):
            try:
                x = (self.width/2 - i)/float(k)
                y = eval(eq)
                pos1 = (self.width/2 + x * k + self.extraWidth, self.height/2 - y * k)

                nx = x = (self.width/2 - i - 1)/float(k)
                ny = eval(eq)
                pos2 = (self.width/2 + nx * k + self.extraWidth, self.height/2 - ny * k)

                BIG_NUM = 1000
                ### Do not plot asymptotes!
                if (self.width/2 + x * k + self.extraWidth) - (self.width/2 + nx * k + self.extraWidth) > BIG_NUM:
                    # Asyptote so do not draw a line (horizontal)
                    pass

                elif (self.width/2 + nx * k + self.extraWidth) - (self.width/2 + x * k + self.extraWidth) > BIG_NUM:
                    # Asyptote so do not draw a line (horizontal)
                    pass

                elif (self.height/2 - y * k) - (self.height/2 - ny * k) > BIG_NUM:
                    # Asyptote so do not draw a line (vertical)
                    pass

                elif (self.height/2 - ny * k) - (self.height/2 - y * k) > BIG_NUM:
                    # Asyptote so do not draw a line (vertical)
                    pass
                else:
                    pygame.draw.line(screen, COLOUR, pos1, pos2, 2)
            except:
                # Add label for user feedback
                message = "INVALID EQUATION - Press enter, then type another equation."
                invalid = TextOnScreen.font5.render(message, 1, self.red)
                screen.blit(invalid, (20, 170))
                break

    def presentScreenTwo(self, screen, k, eq, eq2):
        screenTwoInfo = TextOnScreen()

        # Display info on second screen
        screenTwoInfo.instructions(screen, "Use '+' and '-' to change the size of the grid.", 40)
        screenTwoInfo.instructions(screen, "Press 'return' to draw another graph.", 70)

        if self.graph != 2:
            screenTwoInfo.instructions(screen, "Press 'backspace' to add a graph on a new layer.", 100)

        # Calculate y-intercept
        x = 0
        try:
            yInt = eval(eq)
            yInt = round(yInt, 2)
        except:
            yInt = 'dne'

        screenTwoInfo.instructions(screen, "The y-intercept is at (0," + str(yInt) + ").", 130)

        while True:

            # Update the screen
            display.update()

            # Keyboard and mouse actions - second screen
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                # When a key is pressed, do something
                elif event.type == pygame.KEYDOWN:

                    # Return replaces graph
                    if event.key == K_RETURN:
                        GrapherMain.graph = 1
                        newGrapherNext = GrapherMain(GrapherMain.graph, ' ')
                        self.graphPaper(k, screen)

                    # Backspace adds graph on a new layer
                    elif event.key == K_BACKSPACE and GrapherMain.graph == 1:
                        GrapherMain.graph = 2
                        newGrapherNext = GrapherMain(GrapherMain.graph, eq)

                    elif event.unicode == u'+' or event.unicode == u'=':
                        # next value in array kValues
                        if (self.kIndex >= len(self.kValues) - 1) == False:
                            self.kIndex += 1
                            k = self.kValues[self.kIndex]

                        # Refresh screen, fix jagged text bug
                        screen.set_clip(0, 0, self.extraWidth, 190)
                        screen.fill(self.white)
                        screen.set_clip(0, 300, self.extraWidth, self.height - 300)
                        screen.fill(self.white)
                        screen.set_clip(None)

                        self.graphPaper(k, screen)

                        # Colour the graph based on the equation number (1 or 2)
                        if GrapherMain.graph == 1:
                            self.plotLine(screen, k, eq, self.blue)
                            self.presentScreenTwo(screen, k, eq, eq2)
                        elif GrapherMain.graph == 2:
                            self.plotLine(screen, k, eq, self.orange)
                            self.plotLine(screen, k, eq2, self.blue)
                            self.presentScreenTwo(screen, k, eq, eq2)

                    elif event.unicode == u'-':
                        # previous value in array kValues
                        if (self.kIndex <= 0) == False:
                            self.kIndex -= 1
                            k = self.kValues[self.kIndex]

                        # Refresh screen, fix jagged text bug
                        screen.set_clip(0, 0, self.extraWidth, 190)
                        screen.fill(self.white)
                        screen.set_clip(0, 300, self.extraWidth, self.height - 300)
                        screen.fill(self.white)
                        screen.set_clip(None)

                        self.graphPaper(k, screen)

                        # Colour the graph based on the equation number (1 or 2)
                        if GrapherMain.graph == 1:
                            self.plotLine(screen, k, eq, self.blue)
                            self.presentScreenTwo(screen, k, eq, eq2)
                        elif GrapherMain.graph == 2:
                            self.plotLine(screen, k, eq, self.orange)
                            self.plotLine(screen, k, eq2, self.blue)
                            self.presentScreenTwo(screen, k, eq, eq2)

if __name__=='__main__':
    # Instantiate the main class (main program start point)
    initialGrapher = GrapherMain(GrapherMain.graph, ' ')
