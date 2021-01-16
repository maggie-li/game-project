global x, y, y2
global screen
global obstacles
timeElapsed = None
room_obstacles = [[50, 50, 410, 195], [900, 50, 250, 165], [50, 580, 480, 170], [110, 320, 280, 90], [940, 545, 5, 200]]
outdoor_obstacles = [[170, 110, 256, 256], [800, 120, 256, 256], [230, 475, 198, 170], [785, 510, 178, 126]]
upstairs_obstacles = [[50, 285, 290, 200], [300, 50, 505, 145], [65, 615, 180, 110], [80, 70, 73, 116]]
x = 650
y = 650
y2 = 610
screen = 0


def setup():
    #all images for main room
    global img_floor, img_door, img_croppedfloor, img_couch, img_chest, img_desk, img_carpet, img_stairs, img_table
    #all images for outside
    global img_grass, img_tree, img_berry, img_grassCropped, img_grassCropped2, img_grassCropped3, img_picnic
    #characters
    global img_ted_down, img_ted_left, img_ted_down, img_ted_right, img_ted_up
    #all images for bedroom
    global img_bed, img_bookshelf, img_flowerpot, img_bedside
    #image for winning
    global img_winner
    size(1200, 800)
    background(0)
    img_floor = loadImage("FloorPixel.png")
    img_door = loadImage("door.png")
    img_croppedfloor = loadImage("FloorPixelCropped.png")
    img_couch =loadImage("couch.png")
    img_chest = loadImage("chest.png")
    img_desk = loadImage("desk.png")
    img_carpet = loadImage("carpet.png")
    img_stairs = loadImage("stairs.png")
    img_table = loadImage("table.png")
    img_grass = loadImage("grass.png")
    img_tree = loadImage("tree.png")
    img_berry = loadImage("berry.png")
    img_grassCropped = loadImage("grassCropped.png")
    img_grassCropped2 = loadImage("grassCropped2.png")
    img_grassCropped3 = loadImage("grassCropped3.png") 
    img_picnic = loadImage("picnic.png")
    img_ted_down = loadImage("tedDown.png")
    img_ted_left = loadImage("tedLeft.png")
    img_ted_right = loadImage("tedRight.png")
    img_ted_up = loadImage("tedUp.png")
    img_bed = loadImage("bed.png")
    img_bookshelf = loadImage("bookshelf.png")
    img_flowerpot = loadImage("flowerpot.png")
    img_bedside = loadImage("bedside.png")
    img_winner = loadImage("winner.png")


def draw():
    global screen
    global x, y
    noFill()
    #character
    rect(x, y, 80, 80)
    #main menu
    if screen == 0:
        background(255, 165, 0)
        fill(255)
        main_menu()
    #living room
    if screen == 1:
        background(0)
        character_movement(x, y, room_obstacles)
        room_graphics()
        room_screenchange()
        display_location(x, y)
        character_animation(x, y)
        if keyPressed and key == "e":
            screen = 6
    #outside
    if screen == 2:
        character_movement(x, y2, outdoor_obstacles)
        outdoor_graphics()
        outdoor_screenchange()
        display_location(x, y2)
        character_animation(x, y2)
    #bedroom
    if screen == 3:
        background(0)
        character_movement(x, y, upstairs_obstacles)
        bedroom_graphics()
        display_location(x, y)
        bedroom_screenchange()
        character_animation(x, y)
    #how to play
    if screen == 5:
        background(255,165,0)
        textSize(30)
        text("Check the funiture for pieces of a riddle,", 30, 50)
        text("Once you've looked at all the pieces find out what the riddle is,", 30, 90)
        text("Choose the correct answer at the chest to win", 30, 130)
        textSize(30)
        text("Back", 1000, 600)
        if (mouseX >= 1000 and mouseX <= 1050 and mouseY >= 590 and mouseY <= 615 
            and mousePressed):
            screen = 0
    #opened chest     
    if screen == 6:
        background(75, 0, 130)
        textSize(40)
        text("Choose the correct answer or lose!", 200, 100)
        text("what is the answer to the riddle??", 205, 150)
        textSize(30)
        text("a shadow", 100, 250)
        if (mouseX >= 50 and mouseX <= 250 and mouseY >= 200 and mouseY <= 400
        and mousePressed):
            screen = 7
            
        text("photography film", 700, 250)
        if (mouseX >= 650 and mouseX <= 850 and mouseY >= 200 and mouseY <= 400
        and mousePressed):
            screen = 10
            
        text("a plant", 100, 650)
        if (mouseX >= 50 and mouseX <= 250 and mouseY >= 600 and mouseY <= 800
        and mousePressed):
            screen = 10
            
        text("a moth", 700, 650)
        if (mouseX >= 650 and mouseX <= 850 and mouseY >= 600 and mouseY <= 800
        and mousePressed):
            screen = 10
    #won game
    if screen == 7:
        import time
        global timeElapsed
        timeElapsed = timeElapsed or millis()
        background(75, 0, 130)
        image(img_winner, 400, 400)
        textSize(50)
        fill(255, 215, 0)
        text("WINNER, WINNER!", 375, 200)
        fill(255)
        if millis() > timeElapsed + 4000:
            screen = 0
    #pre-game
    if screen == 8:
        import time
        global timeElapsed
        timeElapsed = timeElapsed or millis()
        
        background(0)
        
        fill(255)
        textSize(20)
        text("What's your name?", 300, 400)
        
        if millis() > timeElapsed + 2500:
            fill(255)
            textSize(20)
            text("Just kidding. We don't care.", 300, 500)
             
        if millis() > timeElapsed + 5000:
            fill(255)
            textSize(20)
            text("Your new name is Ted Bundy.", 300, 600)
        
        if millis() > timeElapsed + 8000:
            timeElapsed = None
            screen = 1
    #lost game
    if screen == 10:
        import time
        global timeElapsed
        timeElapsed = timeElapsed or millis()    
        background(186, 29, 29)
        fill(0)
        textSize(50)
        text("You Lost  >:)", 450, 400)
        text("Try again", 475, 550)
        fill(255)
        if millis() > timeElapsed + 3000:
            screen = 1
    #piece of riddle 
    if screen == 11:
        background(0, 0, 205)
        textSize(50)
        text("me. What", 500, 550)
        text("back", 50, 50)
        if (mouseX >= 0 and mouseX <= 150 and mouseY >= 0 and mouseY <= 150
        and mousePressed):
            screen = 1
    #piece of riddle     
    if screen == 12:
        background(150, 0, 0)
        textSize(50)
        text("shines on", 500, 550)
        text("back", 50, 50)
        if (mouseX >= 0 and mouseX <= 150 and mouseY >= 0 and mouseY <= 150
        and mousePressed):
            screen = 1
    #piece of riddle       
    if screen == 13:
        background(0, 190, 0)
        textSize(50)
        text("but I", 500, 550)
        text("back", 50, 50)
        if (mouseX >= 0 and mouseX <= 150 and mouseY >= 0 and mouseY <= 150
        and mousePressed):
            screen = 1
    #piece of riddle         
    if screen == 14:
        background(0)
        textSize(50)
        text("where there", 500, 550)
        text("back", 50, 50)
        if (mouseX >= 0 and mouseX <= 150 and mouseY >= 0 and mouseY <= 150
        and mousePressed):
            screen = 1
    #piece of riddle         
    if screen == 15:
        background(178,34,34)
        textSize(50)
        text("die if", 500, 550)
        text("back", 50, 50)
        if (mouseX >= 0 and mouseX <= 150 and mouseY >= 0 and mouseY <= 150
        and mousePressed):
            screen = 3
    #piece of riddle         
    if screen == 16:
        background(221, 160, 221)
        textSize(50)
        text("only live", 500, 550)
        text("back", 50, 50)
        if (mouseX >= 0 and mouseX <= 150 and mouseY >= 0 and mouseY <= 150
        and mousePressed):
            screen = 3
   #piece of riddle 
    if screen == 17:
        background(135, 206, 250)
        textSize(50)
        text("is light", 500, 550)
        text("back", 50, 50)
        if (mouseX >= 0 and mouseX <= 150 and mouseY >= 0 and mouseY <= 150
        and mousePressed):
            screen = 2
    #piece of riddle 
    if screen == 18:
        background(212, 175, 55)
        textSize(50)
        text("the light", 500, 550)
        text("back", 50, 50)
        if (mouseX >= 0 and mouseX <= 150 and mouseY >= 0 and mouseY <= 150
        and mousePressed):
            screen = 2
    #piece of riddle         
    if screen == 19:
        background(230,230,250)
        textSize(50)
        fill(0)
        text("I can", 500, 550)
        text("back", 50, 50)
        fill(255)
        if (mouseX >= 0 and mouseX <= 150 and mouseY >= 0 and mouseY <= 150
        and mousePressed):
            screen = 2
    #piece of riddle         
    if screen == 20:
        background(218, 165, 32)
        textSize(50)
        fill(0)
        text("am I?", 500, 550)
        text("back", 50, 50)
        fill(255)
        if (mouseX >= 0 and mouseX <= 150 and mouseY >= 0 and mouseY <= 150
        and mousePressed):
            screen = 2
        
def room_graphics():
    global obstacles
    global x, y
    image(img_floor, 50, 50)
    image(img_floor, 50, 145)
    image(img_floor, 50, 240)
    image(img_floor, 50, 335)
    image(img_floor, 50, 430)
    image(img_floor, 50, 525)
    image(img_floor, 50, 620)
    image(img_door, 510, 40)
    image(img_croppedfloor, 780, 50)
    image(img_floor, 355, 145)
    image(img_croppedfloor, 780, 240)
    image(img_floor, 355, 335)
    image(img_croppedfloor, 780, 430)
    image(img_floor, 355, 525)
    image(img_croppedfloor, 780, 620)
    image(img_floor, 355, 655)
    image(img_floor, 50, 655)
    image(img_carpet, 200, 100)
    image(img_couch, 50, 50)
    image(img_chest, 900, 50)
    image(img_desk, 0, 525)
    image(img_stairs, 945, 540)
    image(img_stairs, 945, 640)
    image(img_table, 110, 320)
    fill(0)
    rect(940, 540, 10, 230)
    noFill()
    noStroke()
    for furniture in room_obstacles:
        rect(*furniture)
    noFill()
    #character
    rect(x, y, 60, 0)
    
def room_screenchange():
    global x, y
    global screen
    if (x >= 505 and x <= 670 and y >= 45 and y <= 65):
        textSize(15)
        text("press i to go outside", 520, 150)
        if keyPressed:
            if (key == "i"):
                screen = 2
    #stairs
    if (x >= 800 and x <= 900 and y >= 600 and y <= 750):
        textSize(15)
        text("press x to inspect the stairs", 760, 540)
        if keyPressed:
            if (key == "x"):
                screen = 11
    #chest
    if (x >= 900 and x <= 1050 and y >= 50 and y <= 280):
        textSize(15)
        text("press o to open chest", 700, 250)
        if (keyPressed):
            if (key == 'o'):
                screen = 6
    #couch
    if (x >= 100 and x <= 350 and y >= 50 and y <= 280):
        textSize(15)
        text("press x to inspect the couch", 200, 250)
        if (keyPressed):
            if (key == 'x'):
                screen = 12
    #goldfish
    if (x >= 100 and x <= 350 and y >= 500 and y <= 1050):
        textSize(15)
        text("press x to inspect the goldfish", 300, 550)
        if (keyPressed):
            if (key == 'x'):
                screen = 13
                
    #table 
    if (x >= 45 and x <= 395 and y >= 305 and y <= 420):
        textSize(15)
        text("press x to inspect the table", 400, 340)
        if (keyPressed):
            if (key == 'x'):
                screen = 14 
    #upstairs
    if (x >= 950 and x <= 1100 and y >= 620 and y <= 750):
        textSize(15)
        text("press i to go upstairs", 770, 600)
        if keyPressed:
            if (key == "i"):
              screen = 3 
                
def display_location(x, y):
    textSize(15)
    text(str(x), 10, 20)
    text(str(y), 10, 40)
        
def character_movement(playerx, playery, obstacles_ar):
    global x, y, y2

    if keyPressed and key == CODED:
        if keyCode == UP and y >= 50:
            y -= 5
            if point_collide(playerx, playery, obstacles_ar) == True:
                y += 5
        if (keyCode == DOWN and y <= 650):
            y += 5
            if point_collide(playerx, playery, obstacles_ar) == True:
                y -= 5
        if screen == 2 and keyPressed and key == CODED:
            if keyCode == UP and y2 >= 50:
                y2 -= 5
                if point_collide(playerx, playery, outdoor_obstacles) == True:
                    y2 += 5
            if (keyCode == DOWN and y2 <= 650):
                y2 += 5
                if point_collide(playerx, playery, outdoor_obstacles) == True:
                    y2 -= 5
        if (keyCode == LEFT and x >= 50):
            x -= 5
            if point_collide(playerx, playery, obstacles_ar) == True:
                x += 5
        if (keyCode == RIGHT and x <= 1090):
            x += 5
            if point_collide(playerx, playery, obstacles_ar) == True:
                x -= 5
                
def character_animation(x, y):
    if keyCode == LEFT:
        image(img_ted_left, x, y)
    elif keyCode == DOWN:
        image(img_ted_down, x, y)
    elif keyCode == UP:
        image(img_ted_up, x, y)
    elif keyCode == RIGHT:
        image(img_ted_right, x, y)
    else:
        image(img_ted_down, x, y)
        
def point_collide(playerx, playery, obstacles_ar):
    global x, y, y2
    
    if screen == 2:
        y = y2
        
    player_x1 = x
    player_x2 = x + 60
    player_y1 = y
    player_y2 = y + 60

    for furniture in obstacles_ar:

        x_coll = False
        y_coll = False
        
        obstical_x1 = furniture[0]
        obstical_y1 = furniture[1]
        obstical_x2 = furniture[0] + furniture[2]
        obstical_y2 = furniture[1] + furniture[3]
        
        if (player_x2 >= obstical_x1) and (player_x1 <= obstical_x2):
            x_coll = True
            
        if (player_y2 >= obstical_y1) and (player_y1 <= obstical_y2):
            y_coll = True
        
        if x_coll is True and y_coll is True:
            return True
        
    return False
            

def main_menu():
    global screen
    textSize(70)
    text("Welcome To Yikes", 320, 300)
    textSize(50)
    text("Play", 550, 500)
    text("How to Play", 450, 600)
    if (mouseX >= 550 and mouseX <= 650 and mouseY >= 475 and
    mouseY <= 515 and mousePressed):
        screen = 8
    if (mouseX >= 500 and mouseX <= 775 and mouseY >= 575 and mouseY <=615
        and mousePressed):
        screen = 5
    
def outdoor_screenchange():
    global screen
    global y
    # tree 
    if (x >= 105 and x <= 430 and y2 >= 45 and y2 <= 375):
        textSize(15)
        text("press x to inspect", 430, 205)
        text("the tree", 430, 225)
        if (keyPressed):
            if (key == 'x'):
                screen = 17
    #tree on right     
    if (x >= 730 and x <= 1060 and y2 >= 55 and y2 <= 385):
        textSize(15)
        text("press x to inspect", 625, 190)
        text("the tree", 660, 210)
        if (keyPressed):
            if (key == 'x'):
                screen = 18
    #berry farm
    if (x >= 165 and x <= 430 and y2 >= 410 and y2 <= 645):
        textSize(15)
        text("press x to inspect", 255, 450)
        text("the berry farm", 255, 470)
        if (keyPressed):
            if (key == 'x'):
                screen = 19
    #picnic table        
    if (x >= 720 and x <= 975 and y2 >= 445 and y2 <= 645):
        textSize(15)
        text("press x to inspect picnic table", 790, 650)
        if (keyPressed):
            if (key == 'x'):
                screen = 20
    #going inside
    if (x >= 505 and x <= 685 and y2 >= 620 and y2 <= 700):
        textSize(15)
        text("press o to go inside", 510, 675)
        if (keyPressed):
            if (key == 'o'):
                screen = 1
                if screen == 1:
                    y = 100

def outdoor_graphics():
    background(135,206,250)
    rect(50, 50, 1100, 700)
    image(img_grass, 50, 50)
    image(img_grass, 519, 50)
    image(img_grass, 50, 355)
    image(img_grass, 519, 355)
    image(img_grassCropped, 50, 450)
    image(img_grassCropped, 519, 450)
    image(img_grassCropped2, 989, 50)
    image(img_grassCropped2, 989, 350)
    image(img_grassCropped3, 989, 655)
    image(img_door, 510, 735)
    image(img_tree, 170, 110)
    image(img_tree, 800, 120)
    image(img_berry, 230, 475)
    image(img_picnic, 785, 510)

def bedroom_screenchange():
    global screen
    if (x >= 950 and x <= 1100 and y >= 620 and y <= 750):
        textSize(15)
        text("press r to go downstairs", 770, 600)
        if (keyPressed):
            if (key == "r"):
                screen = 1 
    # book shelf            
    if (x >= 235 and x <= 815 and y >= 45 and y <= 205):
        textSize(15)
        fill(255)
        text("press x to inspect the book shelf", 500, 200)
        if (keyPressed):
            if (key == 'x'):
                screen = 15
    # bed            
    if (x >= 45 and x <= 345 and y >= 220 and y <= 490):
        textSize(15)
        text("press x to inspect the bed", 345, 390)
        if (keyPressed):
            if (key == 'x'):
                screen = 16
      
def bedroom_graphics():
    image(img_floor, 50, 50)
    image(img_floor, 50, 145)
    image(img_floor, 50, 240)
    image(img_floor, 50, 335)
    image(img_floor, 50, 430)
    image(img_floor, 50, 525)
    image(img_floor, 50, 620)
    image(img_croppedfloor, 780, 50)
    image(img_floor, 355, 145)
    image(img_croppedfloor, 780, 240)
    image(img_floor, 355, 335)
    image(img_croppedfloor, 780, 430)
    image(img_floor, 355, 525)
    image(img_croppedfloor, 780, 620)
    image(img_floor, 355, 655)
    image(img_floor, 50, 655)
    image(img_carpet, 200, 100)
    image(img_bed, 45, 285)
    image(img_bookshelf, 300, 50)
    image(img_stairs, 945, 640)
    image(img_bedside, 65, 615)
    image(img_flowerpot, 80, 70)
    
def test_cases():
    assert y >= 50, "Character out of range"
    assert y <= 650, "Character out of range"
    assert x >= 50, "Character out of range"
    assert x <= 1090, "Character out of range"
    assert screen < 21, "No such screen, check buttons for possible misnumbering."
    assert screen >= 0, "No such screen, check buttons for possible misnumbering."

#test_cases()
