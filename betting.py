import pygame, sys
from random import randint

pygame.init()
screen = pygame.display.set_mode((1280, 850))
clock = pygame.time.Clock()

#VARIABLES
font = pygame.font.SysFont("Ariel", 36, True)
balance = 10000
bet_ammount = 100
heads_won = False
tails_won = False
bets_won = 0
bets_lost = 0

#COLORS
darkpink = (255, 158, 252)
lightpink = (255, 181, 253)
lightblue = (168, 208, 230)
white = (255, 255, 255)
red = (255, 54, 54)
black = (0, 0, 0)

#IMAGES
coin_waiting = pygame.image.load('images/waiting.png')
coin_tails = pygame.image.load('images/tails.png')
coin_heads = pygame.image.load('images/heads.png')

def display_current_balance():
    text_balance = font.render('Current Balance: $' + str(balance), 1, white)
    screen.blit(text_balance, (15, 15))

def display_bet_ammount():
    text_bet = font.render('Bet Ammount: $' + str(bet_ammount), 1, white)
    screen.blit(text_bet, (485, 765))

# If bet was invalid this is called and will put the proper error message on the screen 
def display_bet_error():
    bet_error_zero = font.render('Error: Bet cannot be zero or negative!', 1, red)
    bet_error_balance = font.render('Error: Bet must be lower than balance!', 1, red)

    if bet_ammount > balance:
        screen.blit(bet_error_balance, (375, 710))
    elif bet_ammount <= 0:
        screen.blit(bet_error_zero, (375, 710))

# 1. Checks if bet is valid  2. If the bet is valid, checks to see if the player won  3. If bet isn't valid calls bet_error() function to display an error message
def won_or_lost():

    global balance
    global heads_won
    global tails_won
    global bets_won 
    global bets_lost

    if bet_ammount > balance:
        error = True
    elif bet_ammount <= 0:
        error = True
    elif bet_ammount <= balance and bet_ammount > 0:
        error = False

    number = randint(1, 2)
    if error == False:
        if place_bet_on == "heads" and number == 1:
            balance += bet_ammount
            heads_won = True
            tails_won = False
            bets_won += 1
        elif place_bet_on == "tails" and number == 1:
            balance -= bet_ammount
            heads_won = True
            tails_won = False
            bets_lost += 1
        elif place_bet_on == "heads" and number == 2:
            balance -= bet_ammount
            heads_won = False
            tails_won = True
            bets_lost += 1
        elif place_bet_on == "tails" and number == 2:
            balance += bet_ammount
            heads_won = False
            tails_won = True
            bets_won += 1
    else:
        display_bet_error()

# Displays the proper coin image based on the outcome of the coin flip [If no coin has been flipped it displays a blank coin image]
def display_coin():
    if heads_won == True:
        screen.blit(coin_heads, (384,80))
    elif tails_won == True:
        screen.blit(coin_tails, (384,80))
    elif tails_won == False and heads_won == False:
        screen.blit(coin_waiting, (384,80))

# Displays total wins and losses on the screen + win rate percentage
def display_wins_and_losses():
    bets_won_total = font.render("Total Bets Won: " + str(bets_won), 1, white)
    screen.blit(bets_won_total, (15, 50))

    bets_lost_total = font.render("Total Bets Lost: " + str(bets_lost), 1, white)
    screen.blit(bets_lost_total, (15, 85))
    try: 
        win_rate = (bets_won / (bets_lost + bets_won)) * 100
        win_rate_formated = format(win_rate, '.2f')
        win_rate_percent = font.render("Win Rate: %" + str(win_rate_formated), 1, white)
        screen.blit(win_rate_percent, (15, 120))
    except: 
        pass

"""
def previous_bets():
    x_position = 610
    heads = " Heads,"
    tails = " Tails,"
    last_flips = 'Last 10 Coins Flipped:'

    last_coins_flipped = font.render('Last 10 Coins Flipped:', 1, white)
    flipped_heads = font.render(heads, 1, white)
    flipped_tails = font.render(tails, 1, white)
    screen.blit(last_coins_flipped, (350, 20))

    coin_flips = []
    if heads_won == True:
        heads + heads
        coin_flips.append(flipped_heads)
    elif tails_won == True:
        tails + tails
        flipped_tails = font.render(tails, 1, white)
        coin_flips.append(flipped_tails)

    for coin in coin_flips:
        if coin == flipped_heads:
            screen.blit(flipped_heads, (650, 20))
        elif coin == flipped_tails:
            screen.blit(flipped_tails, (650, 20))
        
    coin_flips.count(flipped_heads)
"""

class Button():
    def __init__(self, color, x, y, width, height, text=""):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
    
    def draw(self, screen, outline = None):
        #Calling this will draw the button on the screen
        if outline:
            pygame.draw.rect(screen, outline, (self.x-2, self.y-2, self.width + 4, self.height + 4), 0)
        
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text !="":
            font = pygame.font.SysFont("Ariel", 48)
            text = font.render(self.text, 1, white)
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position in (X, Y) coordinates inside of a tuple
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

def redrawWindow():
    screen.fill(lightblue)
    headsButton.draw(screen, white)
    tailsButton.draw(screen, white)
    raise10Button.draw(screen, white)
    lower10Button.draw(screen, white)
    raise100Button.draw(screen, white)
    lower100Button.draw(screen, white)
    raise500Button.draw(screen, white)
    lower500Button.draw(screen, white)
    quitButton.draw(screen)
    display_current_balance()
    display_bet_ammount()
    display_coin()
    display_wins_and_losses()
    display_bet_error()

# Defining all the buttons
headsButton = Button(lightblue, 346, 640, 250, 50, "HEADS")
tailsButton = Button(lightblue, 684, 640, 250, 50, "TAILS")
raise10Button = Button(lightblue, 809, 750, 125, 50, "$10")
lower10Button = Button(lightblue, 346, 750, 125, 50, "-$10")
raise100Button = Button(lightblue, 966, 750, 125, 50, "$100")
lower100Button = Button(lightblue, 189, 750, 125, 50, "-$100")
raise500Button = Button(lightblue, 1123, 750, 125, 50, "$500")
lower500Button = Button(lightblue, 32, 750, 125, 50, "-$500")
quitButton = Button(lightblue, 1180, 0, 100, 50, "Quit")

# GAME LOOP 
running = True
while running:
    redrawWindow()
    pygame.display.update()
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if headsButton.isOver(pos):
                place_bet_on = "heads"
                won_or_lost()

            if tailsButton.isOver(pos):
                place_bet_on = "tails"
                won_or_lost()

            if raise10Button.isOver(pos):
                bet_ammount += 10

            if lower10Button.isOver(pos):
                bet_ammount -= 10

            if raise100Button.isOver(pos):
                bet_ammount += 100

            if lower100Button.isOver(pos):
                bet_ammount -= 100

            if raise500Button.isOver(pos):
                bet_ammount += 500

            if lower500Button.isOver(pos):
                bet_ammount -= 500

            if quitButton.isOver(pos):
                pygame.quit()

        if event.type == pygame.MOUSEMOTION:
            if headsButton.isOver(pos):
                headsButton.color = (darkpink)
            else:
                headsButton.color = (lightpink)
            
            if tailsButton.isOver(pos):
                tailsButton.color = (darkpink)
            else:
                tailsButton.color = (lightpink)

            if raise10Button.isOver(pos):
                raise10Button.color = (darkpink)
            else:
                raise10Button.color = (lightpink)

            if lower10Button.isOver(pos):
                lower10Button.color = (darkpink)
            else:
                lower10Button.color = (lightpink)

            if raise100Button.isOver(pos):
                raise100Button.color = (darkpink)
            else:
                raise100Button.color = (lightpink)

            if lower100Button.isOver(pos):
                lower100Button.color = (darkpink)
            else:
                lower100Button.color = (lightpink)

            if raise500Button.isOver(pos):
                raise500Button.color = (darkpink)
            else:
                raise500Button.color = (lightpink)

            if lower500Button.isOver(pos):
                lower500Button.color = (darkpink)
            else:
                lower500Button.color = (lightpink)

            if quitButton.isOver(pos):
                quitButton.color = (lightblue)
            else:
                quitButton.color = (lightblue)
