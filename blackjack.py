#!/usr/bin/env python3
import random

print("")
print("BlackJack v0.1")
print("--------------")

dw = 0
pw = 0

game_count = 0;
dv = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10,"A":11}

def winner(dc1, dc2, pc1, pc2):
	
	ds = dv[dc1] + dv[dc2] 		
	ps = dv[pc1] + dv[pc2]
	
	global pw
	global dw

	if ds > ps:
		dw += 1
		print("Dealer wins!")
	elif ds == ps:
		print("It's a draw!")
	else:
		pw += 1
		print("Player wins!")

def game():

	d = list(dv.keys())

	random.shuffle(d)

	print("Dealer's Hand: {} {}".format(d[0], d[1]))
	print("Player's Hand: {} {}".format(d[2], d[3]))

	winner(d[0],d[1],d[2],d[3])

	print("Dealer {} Player {}".format(dw, pw))

while(True):
	game_count += 1
	print("Game #{}".format(game_count))
	game()
	if input() == "x":
		print("")
		break
