"""
This code was written for the purpose of practice in
coding a game. The T-Rex game was created by Edward
Jung and I claim no ownership of the property. This
python program was coded back in the summer of 2018
and uses the pygame library.
"""

import pygame
import random
pygame.init()

# variables for window size
display_width = 600
display_height = 155

# sets the window up
gameDisplay = pygame.display.set_mode((display_width, display_height))

# sets the icon, caption, and the clock
pygame.display.set_icon(pygame.image.load('dicon.png'))
pygame.display.set_caption("T-Rex Run")
clock = pygame.time.Clock()

# sets font sizes
smallfont = pygame.font.SysFont("comicsansms", 23)
medfont = pygame.font.SysFont("comicsansms", 40)
largefont = pygame.font.SysFont("comicsansms", 85)

# imports images
groundFloor = pygame.image.load("ground.png")
dinoA = pygame.image.load("dinosaur.png")
dino1 = pygame.image.load("dinosaur1.png")
dino2 = pygame.image.load("dinosaur2.png")
dino3 = pygame.image.load("dinosaur3.png")
cactusIm = pygame.image.load("cactus.png")
lumpIm = pygame.image.load("lump.png")
cloudIm = pygame.image.load("cloud.png")

# music
pygame.mixer.music.load('dinoMusic.mp3')
pygame.mixer.music.play(-1)

### text based method
def text_objects(text, color,size = "small"):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

### text based method
def message_to_screen(msg,color, y_displace = 0, x_displace = 0, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (int(display_width / 2)+x_displace, int(display_height / 2)+y_displace)
    gameDisplay.blit(textSurf, textRect)

### moves the ground
def groundMove(x):
    # creates four seperate chunks of ground
    gameDisplay.blit(groundFloor,(x-245,133),(0,0,245,26))
    gameDisplay.blit(groundFloor,(x,133),(0,0,245,26))
    gameDisplay.blit(groundFloor,(x+245,133),(0,0,245,26))
    gameDisplay.blit(groundFloor,(x+245*2,133),(0,0,245,26))

### sets dinosaur images
def dinosaurImage(dinoIm,y):
    # dino images 1 and 2 are walk cycles, 0 is a standing dino, and 3 is the gameOver sprite
    if dinoIm == 0:
        gameDisplay.blit(dinoA,(17,y),(0,0,40,43))
    elif dinoIm == 1:
        gameDisplay.blit(dino1,(17,y),(0,0,40,43))
    elif dinoIm == 2:
        gameDisplay.blit(dino2,(17,y),(0,0,40,43))
    elif dinoIm == 3:
        gameDisplay.blit(dino3,(17,y),(0,0,40,43))

### displays all cacti on screen
def cactusImage(cactusList):
    for x in cactusList:
        gameDisplay.blit(cactusIm,(x,97),(0,0,40,43))

### displays all mounds on screen
def moundImage(moundList):
    for x in moundList:
        gameDisplay.blit(lumpIm,(x,133),(0,0,40,43))

### displays all clouds on screen
def cloudImage(cloudList):
    for x in cloudList:
        gameDisplay.blit(cloudIm,x,(0,0,46,43))

### Method for the game ###
def gameLoop():
    # sets boolean values
    gameExit = jump = False
    gameStart = True
    
    # placement of ground on screen
    x = 245
    
    # y value of dinosaur on screen
    y = 97
    
    # height of jump
    z = -28
    
    #Standing dinosaur image is set to dinosaur
    dinoIm = 0

    # no initial score or high score
    score = 0
    highScore = 0

    # speed of game
    speedTraveled = 30

    # creates a list of cactus, clouds, and dirt mounds that spawn between a specified area
    cactusList = [random.randrange(600,750),random.randrange(1050,1200)]
    moundList = [random.randrange(600,750),random.randrange(1050,1200)]
    cloudList = [(random.randrange(600,800),random.randrange(15,45)),(random.randrange(1000,1200),random.randrange(15,45))]

    ### Begin while loop gameExit ###
    while not gameExit:
        for event in pygame.event.get():
            # if window prompted to close 
            if event.type == pygame.QUIT:
                gameExit = True
                
            if event.type == pygame.KEYDOWN:
                # if spacebar pressed, dinosaur will jump
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    jump = True


        # if cactus is within the x coordinates of dinosaur, and the dinosaur is falling to a certain point,
        # or if the game is started

        ### Starting/Restarting the Game ###
        if 17 < cactusList[0] < 57 and y > 53 or gameStart == True:
            # if score is higher than highscore, make the highscore the new score
            if score > highScore:
                highScore = score

            # pause the game so screen shows the defeated dinosaur
            gamePause = True
            
            # game over dinosaur image
            if not gameStart:
                dinoIm = 3
                
            ### While gameOver screen ###
            while gamePause:
                for event in pygame.event.get():
                    # if window prompted to close 
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gamePause = False
                    # pressing space restarts the game with values being reset
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                            jump = True
                            x = 245
                            y = 97
                            z = -28
                            dinoIm = 0
                            speedTraveled = 30
                            score = 0
                            cactusList = [random.randrange(600,750),random.randrange(1050,1200)]
                            moundList = [random.randrange(600,750),random.randrange(1050,1200)]
                            cloudList = [(random.randrange(600,800),random.randrange(15,45)),(random.randrange(1000,1200),random.randrange(15,45))]
                            gameDisplay.fill((20,165,220))
                            gamePause = False
                            gameStart = False

                ### Code Set 1.0 ###
                # fill screen with a sky blue color       
                gameDisplay.fill((20,165,220))

                # draws ground, cacti, and clouds on screen
                groundMove(x)
                cactusImage(cactusList)
                moundImage(moundList)
                cloudImage(cloudList)

                # draws the scores to screen
                message_to_screen(str(int(score)),(255,0,0),-58,150)
                message_to_screen(str(int(highScore)),(255,0,0),-58,-150)

                # draws the dinosaur
                dinosaurImage(dinoIm,y)

                # updates the screen and ticks for 14 frames
                pygame.display.update()
                clock.tick(14)
                ### End Code Set 1.0 ###
                ### End gameOver Screen ###
                
                ### End while Start/Restart ###



        ### Dinosaur Starts Running ###

        # deals with the cacti on screen
        for x in range(0,len(cactusList)):
            # brings the cacti towards the dino based on the speed
            cactusList[x] = cactusList[x]-speedTraveled
            
            # removes a cactus when it goes off screen then adds another
            if cactusList[x] < -23 and x == 0:
                cactusList.remove(cactusList[x])
                cactusList.append(cactusList[0]+random.randrange(300,600))

        # deals with mounds on screen
        for x in range(0,len(moundList)):
            moundList[x] = moundList[x]-speedTraveled
            if moundList[x] < -14 and x == 0:
                moundList.remove(moundList[x])
                moundList.append(moundList[0]+random.randrange(300,600))

        # deals with clouds on screen
        for x in range(0,len(cloudList)):
            cloudList[x] = (cloudList[x][0]-int(speedTraveled/6),cloudList[x][1])
            if cloudList[x][0] < -46 and x == 0:
                cloudList.remove(cloudList[x])
                # same idea as the cacti and mounds, but also has a random value from 15 to 45 for y value
                cloudList.append((cloudList[0][0]+random.randrange(600,650),random.randrange(15,45)))


        # Completes same set of code as Code Set 1.0 ###
        gameDisplay.fill((20,165,220))
        groundMove(x)
        cactusImage(cactusList)
        moundImage(moundList)
        cloudImage(cloudList)
        message_to_screen(str(int(score)),(0,0,0),-58,150)
        message_to_screen(str(int(highScore)),(50,50,50),-58,-150)
        dinosaurImage(dinoIm,y)
        ### End Code Set 1.0
        
        # placement of ground moving
        x -= speedTraveled
        
        # speed gradually gets faster
        speedTraveled += .01

        # adds score
        score += .5

        # procedes to next dinosaur image
        dinoIm += 1

        # resets dinosaur walk cycle after image 3 is hit
        if dinoIm == 3:
            dinoIm = 1
            
        # once a complete chunk of ground is off screen it loops over
        if x < 0:
            x = 245

        ### the dinosaur is brought up, as it passes 0, it goes down and back to the ground
        if jump == True:
            # standing while jumping image
            dinoIm = 0

            # brings the dinosaur up by z
            y += z

            # adds 7 to z
            z+=7

            # if z reaches 35, reset z
            if z == 35:
                z = -28
                # if space is held, continue jumping
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                        jump = True
                # otherwise, make the jumping stop
                else:
                    jump = False

        # update screen and ticks the clock 14 frames
        pygame.display.update()
        clock.tick(14)

    ### End gameExit while loop ###

    # quits the pygame window
    pygame.quit()
### End Method for game ###





# calls the game's method
gameLoop()

### End Code ###
