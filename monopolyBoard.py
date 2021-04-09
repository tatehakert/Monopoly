import pygame
import random
from game import boardPositions

pygame.init()

print("initializing all modules for pygame")

pygame.init()

#colors

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
pink = (238,38,199)
orange = (228,127,7)
light_blue = (21, 203, 240)
brown = (139,69,30)
dark_blue = (5,0,132)
green = (9,176,52)
yellow = (242,245,6)

colorSets = {
    "utilities": white,
    "railroads": black,
    "purple": brown,
    "sky": light_blue,
    "pink": pink,
    "orange": orange,
    "red": red,
    "yellow": yellow,
    "green": green,
    "blue": blue
}
#default background color
default_background = (235, 243, 225)
#current screen dimensions
# need to have these be adjustable
screen_height = 1000
screen_width = round(screen_height*(4/3))
#initialize the screen
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill(default_background)

#print a message of a color at an x,y with given size
def message(msg,color,x_loc, y_loc, size):
    font_style = pygame.font.SysFont(None, size)
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [x_loc, y_loc])

#class for a corner sqare
class corner_square:

   #constructor
    def __init__(self, position, propertyData):
        self.x_loc = 0
        self.y_loc = 0
        self.width = 1/6 * screen_height
        self.height = 1/6 * screen_height
        self.position = position
        self.propertyData = propertyData
    #set location
    def set_x_and_y (self, x_loc, y_loc):
        self.x_loc = x_loc
        self.y_loc = y_loc
    #draw
    def draw(self):
        curr_card = pygame.draw.rect(screen, (0, 0, 0), (self.x_loc, self.y_loc,self.width, self.height), 3)
        message_x = curr_card.centerx
        message_y = curr_card.centery
        message(self.propertyData["name"], (0,0,0), message_x,message_y,25)

#class for a board square
class board_square:
    #constructor
    def __init__(self, position, propertyData):
        self.x_loc = 0
        self.y_loc = 0
        self.width = screen_height * .074
        self.height = screen_height * (1/6)
        self.position = position
        self.propertyData = propertyData

    #change the positions
    def set_x_and_y (self, x_loc, y_loc):
        self.x_loc = x_loc
        self.y_loc = y_loc

    #make the space vertical, used on top and bottom rows
    # def set_to_vertical(self):
    #     temp = self.width
    #     self.width = self.height
    #     self.height = temp

    #make the space horizontal, used on left and right rows
    def set_to_horizontal(self):
        temp = self.width
        self.width = self.height
        self.height = temp

    #set the space to correspond to a color, orientation is which side of the space the color designation needs to go on
    def set_color(self, card_color, orientation):
        if(orientation == "right"):
            sub_rect_x = self.x_loc + (self.width - (self.width/6))
            sub_rect_y = self.y_loc
            sub_rect_width = 1/6 * self.width
            sub_rect_height = self.height

        if(orientation == "left"):
            sub_rect_x = self.x_loc
            sub_rect_y = self.y_loc
            sub_rect_width = 1/6 * self.width
            sub_rect_height = self.height

        if(orientation == "bottom"):
            sub_rect_x = self.x_loc
            sub_rect_y = self.y_loc + (self.height - (self.height/6))
            sub_rect_width = self.width
            sub_rect_height = self.height * 1/6

        if(orientation == "top"):
            sub_rect_x = self.x_loc
            sub_rect_y = self.y_loc
            sub_rect_width = self.width
            sub_rect_height = self.height * 1/6
        #after setting the location and size, draw the color marker and outline it

        color_marker = pygame.draw.rect(screen, card_color, (sub_rect_x, sub_rect_y,sub_rect_width, sub_rect_height), 0)
        color_marker_outline = pygame.draw.rect(screen, (0,0,0), (sub_rect_x, sub_rect_y,sub_rect_width, sub_rect_height), 2)

    #draw the board square
    def draw(self):
        curr_card = pygame.draw.rect(screen, (0, 0, 0), (self.x_loc, self.y_loc,self.width, self.height), 2)
        #message_x = curr_card.centerx
        message_x = self.x_loc + 50
        message_y = curr_card.centery
        message(self.propertyData["name"], (0,0,0), message_x,message_y,15)

# def draw_corners():
#     #top left corner
#     top_left_corner = corner_square()
#     top_left_corner.set_x_and_y(0,0)
#     top_left_corner.draw()
#     #bottom left corner
#     bottom_left_corner = corner_square()
#     bottom_left_corner.set_x_and_y(0,screen_height - screen_height*(1/6))
#     bottom_left_corner.draw()
#     #top right corner
#     top_right_corner = corner_square()
#     top_right_corner.set_x_and_y(screen_height - screen_height*(1/6),0)
#     top_right_corner.draw()
#     #bottom right corner
#     bottom_right_corner = corner_square()
#     bottom_right_corner.set_x_and_y(screen_height - screen_height*(1/6),screen_height - screen_height*(1/6))
#     bottom_right_corner.draw()

def draw_board_position(position):
    print("drawing board!")
    if position in [0, 10, 20, 30]: #corner square
        newPosition = corner_square(position, boardPositions[position])
        card_x = 0 if (position == 10 or position == 20) else screen_height - screen_height*(1/6)
        card_y = 0 if (position == 20 or position == 30) else screen_height - screen_height*(1/6)
    else:
        newPosition = board_square(position, boardPositions[position])
        if position in range(0,10): # bottom side
            starting_x = screen_height - screen_height*(1/6) - screen_height*(.074)
            increment = -(screen_height*(.074))
            offset = position - 1
            card_x = starting_x + (increment * offset)
            card_y = screen_height - screen_height*(1/6)
            colorOrientation = "top"
        elif position in range(10,20): # left side
            starting_y = screen_height - screen_height*(1/6) - screen_height*(.074)
            increment = -(screen_height*(.074))
            offset = (position - 1) - 10
            card_x = 0
            card_y = starting_y + (increment * offset)
            colorOrientation = "right"
            newPosition.set_to_horizontal()
        elif position in range(20,30): # top side
            starting_x = screen_height*(1/6)
            increment = screen_height*(.074)
            offset = (position - 1) - 20
            card_x = starting_x + (increment * offset)
            card_y = 0
            colorOrientation = "bottom"
        elif position in range(30,40): # right side
            starting_y =  screen_height*(1/6)
            increment = screen_height*(.074)
            offset = (position - 1) - 30
            card_x = screen_height - screen_height*(1/6)
            card_y = starting_y + (increment * offset)
            colorOrientation = "left"
            newPosition.set_to_horizontal()


        newPosition.set_x_and_y(card_x,card_y)
        newPosition.draw()
        if position in [1,3,6,8,9,11,13,14,16,18,19,21,23,24,26,27,29,31,32,34,37,39]:
            newPosition.set_color(colorSets[boardPositions[position]["propertySet"]], colorOrientation)


# def draw_left_side():
#     card_x = 0
#     card_y = screen_height*(1/6)
#     for i in range (9):
#         test = board_square()
#         test.set_x_and_y(card_x,card_y)

#         test.draw()
#         if( i == 0 ) or (i == 1) or (i == 3):
#             test.set_color(orange, "right")
#         if(i == 5) or (i == 6) or (i == 8):
#             test.set_color(pink, "right")
#         card_y = card_y+ screen_height*(.074)

# def draw_right_side():
#     card_x = screen_height - screen_height*(1/6)
#     card_y = screen_height*(1/6)
#     for i in range (9):
#         test = board_square()
#         test.set_x_and_y(card_x,card_y)
#         test.draw()
#         if( i == 0 ) or (i == 1) or (i == 3):
#             test.set_color(green, "left")
#         if (i == 6) or (i == 8):
#             test.set_color(dark_blue, "left")
#         card_y = card_y + screen_height*(.074)

# def draw_top_side():
#     card_x = screen_height*(1/6)
#     card_y = 0
#     for i in range (9):
#         test = board_square()
#         test.set_to_vertical()
#         test.set_x_and_y(card_x,card_y)
#         test.draw()
#         if(i == 0) or( i== 2) or (i == 3):
#             test.set_color(red, "bottom")
#         if(i == 5) or (i == 6) or (i == 8):
#             test.set_color(yellow, "bottom")
#         card_x = card_x + screen_height*(.074)

# def draw_bottom_side():
#     card_x = screen_height*(1/6)
#     card_y = screen_height - screen_height*(1/6)
#     for i in range (9):
#         test = board_square()
#         test.set_to_vertical()
#         test.set_x_and_y(card_x,card_y)
#         test.draw()
#         if( i == 0 ) or (i == 1) or (i == 3):
#             test.set_color(light_blue, "top")
#         if (i == 6) or (i == 8):
#             test.set_color(brown,"top")

#         card_x = card_x + screen_height*(.074)

# def draw_board():
#     #chance sqaures
#     community_chance_card_stack = pygame.draw.rect(screen, (0, 0, 0), (screen_height*1.5/6, screen_height*1.5/6,200, 125), 3)  # width = 3
#     chance_card_stack = pygame.draw.rect(screen, (0, 0, 0), ((screen_height*4.5/6)-200, (screen_height*4.5/6)-125,200, 125), 3)  # width = 3

#     draw_left_side()
#     draw_right_side()
#     draw_top_side()
#     draw_bottom_side()
#     draw_corners()
#     pygame.display.flip()
#     pygame.display.set_caption('Monopoly Game')

def draw_board():
    #largest subsqare
    inline_cards = pygame.draw.rect(screen, (0, 0, 0), (screen_height*(1/6),screen_height*(1/6), screen_height - screen_height*(2/6), screen_height - screen_height*(2/6)), 3)  # width = 3
    outline_cards = pygame.draw.rect(screen, (0, 0, 0), (0, 0, screen_height, screen_height), 3)  # width = 3
    community_chance_card_stack = pygame.draw.rect(screen, (0, 0, 0), (screen_height*1.5/6, screen_height*1.5/6,200, 125), 3)  # width = 3
    chance_card_stack = pygame.draw.rect(screen, (0, 0, 0), ((screen_height*4.5/6)-200, (screen_height*4.5/6)-125,200, 125), 3)  # width = 3
    for position in boardPositions:
        draw_board_position(position)


draw_board()




clock = pygame.time.Clock()

test = True
while(test):
    for event in pygame.event.get():
        message("Monopoly", red,420,550,120)
        print(event)
        if event.type == pygame.QUIT:
            print("quitting test screen")
            quit()
        pygame.display.flip()



#gameLoop()
