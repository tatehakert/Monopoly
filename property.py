#!/usr/bin/env python
from game import boardPositions
import pygame
from pygame.locals import *
import math

class Property:
    def __init__(self, window, data, loc):
        self.win = window
        self.data = data
        self.loc = loc

    def draw(self):
        x = self.loc[0]
        y = self.loc[1]
        width = 350 # width = 7
        height = 400 # height = 8
        deed_color = (210,129,175)
        bg_color = (250,250,250)
        black = (0,0,0)
        pygame.draw.rect(self.win, bg_color, pygame.Rect(x, y, width, height))
        # Top banner is 90% width with 5% pad on either side
        # 2.5% of height pad from top
        # 16.25% of height for banner height
        top_banner_x = x + (width * 0.05)
        top_banner_y = y + (height * 0.025)
        top_banner_width = width * 0.9
        top_banner_height = height * 0.1625
        pygame.draw.rect(self.win, deed_color, pygame.Rect(top_banner_x,
                                                    top_banner_y,
                                                    top_banner_width,
                                                    top_banner_height))
        pygame.draw.rect(self.win, black, pygame.Rect(top_banner_x,
                                                    top_banner_y,
                                                    top_banner_width,
                                                    top_banner_height), 2)


        # Title deed font, centered
        banner_font = pygame.font.SysFont('Futura', int(width / 20))
        deed_text = banner_font.render('T I T L E  D E E D',
                                            True,
                                            black)
        deed_rect = deed_text.get_rect()
        deed_text_x = top_banner_x + ((top_banner_width - deed_rect.width) / 2)
        deed_text_y = top_banner_y + height * 0.02
        self.win.blit(deed_text, (deed_text_x, deed_text_y))

        name_font = pygame.font.SysFont('Futura', int(width/ 13))
        deed_name = self.data['name']
        name_text = name_font.render(deed_name, True, black)
        name_rect = name_text.get_rect()
        name_text_x = top_banner_x + ((top_banner_width - name_rect.width) / 2)
        name_text_y = deed_text_y + height * 0.05
        self.win.blit(name_text, (name_text_x, name_text_y))

        rent_font = pygame.font.SysFont('Arial', int(width/13))
        rent_text = rent_font.render('Rent $' + str(self.data['baseRent']),
                                      True,
                                      black)
        rent_rect = rent_text.get_rect()
        rent_text_x = x + ((width - rent_rect.width) / 2)
        rent_text_y = name_text_y + height * 0.1125
        self.win.blit(rent_text, (rent_text_x, rent_text_y))

        house_y = rent_text_y
        for i in range(1,5):
            s = 'Houses'
            if i == 1:
                s = 'House'
            string = 'With ' + str(i) + ' ' + s
            house_text = rent_font.render(string, True, black)
            house_x = x + width * 0.105
            house_y = house_y + height * 0.0625
            self.win.blit(house_text, (house_x, house_y))

        dollar = rent_font.render('$', True, black)
        dollar_x = x + width * 0.72
        dollar_y = rent_text_y + height * 0.0625
        self.win.blit(dollar, (dollar_x, dollar_y))

        house_rent_y = rent_text_y
        for i in range(4):
            house_rent = math.ceil(self.data['baseRent'] * self.data['rentMultiplier'][i+1])
            string = str(house_rent) + '.'
            house_rent_text = rent_font.render(string, True, black)
            house_rent_rect = house_rent_text.get_rect()
            house_rent_x = x + width * 0.89 - house_rent_rect.width
            house_rent_y = house_rent_y + height * 0.0625
            self.win.blit(house_rent_text, (house_rent_x, house_rent_y))


        hotel_price = self.data['baseRent'] * self.data['rentMultiplier'][-1]
        string = 'With Hotel $' + str(hotel_price) + '.'
        hotel_text = rent_font.render(string, True, black)
        hotel_rect = hotel_text.get_rect()
        hotel_text_x = x + ((width - hotel_rect.width) / 2)
        hotel_text_y = house_rent_y + height * 0.0625
        self.win.blit(hotel_text, (hotel_text_x, hotel_text_y))

        # TODO: Get mortgage data for properties
        mortgage_text = rent_font.render('Mortgage Value $000.', True, black)
        mortgage_rect = mortgage_text.get_rect()
        mortgage_x = x + ((width - mortgage_rect.width) / 2)
        mortgage_y = hotel_text_y + height * 0.08
        self.win.blit(mortgage_text, (mortgage_x, mortgage_y))

        string = 'Houses cost $' + str(self.data['houseCost']) + '. each'
        house_price_text = rent_font.render(string, True, black)
        house_price_rect = house_price_text.get_rect()
        house_price_x = x + ((width - house_price_rect.width) / 2)
        house_price_y = mortgage_y + height * 0.0625
        self.win.blit(house_price_text, (house_price_x, house_price_y))

        string = 'Hotels, $' + str(self.data['houseCost']) + '. plus 4 houses'
        hotel_price_text = rent_font.render(string, True, black)
        hotel_price_rect = hotel_price_text.get_rect()
        hotel_price_x = x + ((width - hotel_price_rect.width) / 2)
        hotel_price_y = house_price_y + height * 0.0625
        self.win.blit(hotel_price_text, (hotel_price_x, hotel_price_y))

        subfont = pygame.font.SysFont('Arial', int(width/26))
        subtext1 = subfont.render('If a player owns ALL the Lots of any Color-Group, the', True, black)
        subtext2 = subfont.render('rent is Doubled on Unimproved Lots in that group.', True, black)
        sub_x = x + width * 0.055
        sub_y1 = hotel_price_y + height * 0.0875
        sub_y2 = sub_y1 + height * 0.04
        self.win.blit(subtext1, (sub_x, sub_y1))
        self.win.blit(subtext2, (sub_x, sub_y2))


def main():
    pygame.init()
    pygame.font.init()
    win = pygame.display.set_mode((500,500))
    pygame.display.set_caption('Title Deed Test')

    deed = Property(win, boardPositions[3], (50,50))
    run = True
    while run:

        deed.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()

if __name__ == '__main__':
    main()
