import pgzrun
from random import randint

WIDTH= 800
HEIGHT= 350

witch=Actor("witch1")
witch.y=HEIGHT//2
witch.x=WIDTH//2
background1='bg'
background0='bg0'
background_time=10
pumpkins=[]
pumpkin_y_speed = 2
pumpkin_x_speed = 2
game_over = False
score=0
potions=[]
potion_x_speed=1

back0=Actor(background0, (500,350))
back1=Actor(background1,(1500,350))
g_backgrounds=[back0,back1]


def draw():
	screen.clear()
	b0, b1 = g_backgrounds
	b1.draw()
	b0.draw()
	witch.draw()
	draw_pumpkin()
	draw_potion()
	heal()

def background_repeat():
    b0 = g_backgrounds.pop(0)
    g_backgrounds.append(b0)
    scroll_backgrounds(g_backgrounds)
    return

def scroll_backgrounds(backs):
    left = 400
    bottom = 200
    b0, b1 = backs

    b0.pos = (left, bottom)
    animate(b0,
        tween= 'linear',
        duration= background_time,
        on_finished= background_repeat,
        pos= (left - 800, bottom))

    b1.pos = (left + 800, bottom)
    animate(g_backgrounds[1],
        tween= 'linear',
        duration= background_time,
        on_finished= None,
        pos= (left, bottom))

scroll_backgrounds(g_backgrounds)	

def update():
	if not game_over:
		move_player()
		move_pumpkin()
		move_potion()
		check_player_collision()
		

def create_new_pumpkin():
	pumpkin = Actor("pumpkinf")
	pumpkin.x = WIDTH
	pumpkin.y =randint(50, 300) 
	pumpkins.append(pumpkin)	


def draw_pumpkin():
    for pumpkin in pumpkins:
        pumpkin.draw()

def move_pumpkin():
	global score
	for pumpkin in pumpkins:
		pumpkin.x -= pumpkin_x_speed
		if pumpkin.x == WIDTH//2:
			score+=1
			create_new_pumpkin()
			
			
			              
def move_player():
	if keyboard.up:	
		witch.y-=1.5
	elif keyboard.down:	
		witch.y+=1.5
	elif witch.y> HEIGHT: 
		witch.y= HEIGHT-100
	elif witch.y == 0:		
		witch.y=100

def heal():		
	screen.draw.text("Score: "+str(score), (740,10), fontsize=20, color="white")
	screen.draw.text("press the up and down arrow in your keyboard to move and avoid the pumpkins--collect the potions for extra points", (40,333), fontsize=20, color="white")
	if game_over== True:
		screen.draw.text("Game Over", (WIDTH//2-80,300), fontsize=50, color="white")

def draw_potion():
	for potion in potions:
		potion.draw()

def create_new_potion():
	potion=Actor("potion")
	potion.x= WIDTH
	potion.y=HEIGHT//2
	potions.append(potion)	

def move_potion():
	global score
	for potion in potions:
		potion.x -= potion_x_speed
		if potion.colliderect(witch):
			potions.remove(potion)
			sounds.twinkle.play()
			score+=5
			create_new_potion()
		elif potion.x==0:	
			create_new_potion()
		

def check_player_collision():		
	global game_over
	for pumpkin in pumpkins:
		if pumpkin.colliderect(witch):
			sounds.gameover.play()
			game_over=True 


create_new_potion()
create_new_pumpkin()	

pgzrun.go()