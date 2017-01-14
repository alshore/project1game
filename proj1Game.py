# import random module
import random

# define main function
def main():
	# give user and computer random cards calling hand function
	userHand = hand()
	computerHand = hand()
	userHand += hand()
	computerHand += hand()
	# print user and computer hands
	print "Your hand: " + str(userHand)
	print "Computer hand: " + str(comp   uterHand)
	# get card totals
	userTotal = userHand[0] + userHand[2]
	computerTotal = computerHand[0] + computerHand[2]
	# print card totals
	print "Your total: " + str(userTotal)
	print "Computer total: " + str(computerTotal)
	# enter loop for hit, and initialize incrementer
	hit = raw_input("Do you want another card? (y for yes): ")
	count = 4
	while hit == 'y':
		userHand += hand()
		print userHand
		userTotal += userHand[count]
		print "Your total: " + str(userTotal)
		if userTotal > 21:
			print "You bust!"
			break
		hit = raw_input("Do you want another card? (y for yes): ")
		# increment counter for adding new card to total
		count += 2
	computerCount = 4
	# computer hits if 16 or under
	while computerTotal <= 16:
		computerHand += hand()
		print computerHand
		computerTotal += computerHand[computerCount]
		print "Computer total: " + str(computerTotal)
		if computerTotal > 21:
			print "Computer busts!"
			break
		computerCount += 2
	# if user is high and 21 or under, user wins
	if computerTotal > 21 >= userTotal or computerTotal < userTotal <= 21 :
		print "You win!"
	else:
		print "Computer wins!"

# define the hand function
def hand():
	# get random number for suit
	randSuit = random.randint(1, 4)
	if randSuit == 1:
		randSuit = "Spades"
	elif randSuit == 2:
		randSuit = "Clubs"
	elif randSuit == 3:
		randSuit = "Hearts"
	else:
		randSuit = "Diamonds"
	# get random number for card face value
	randFace = random.randint(1, 13)
	if randFace == 1:
		# error catching
		while True:
			# try except block for non numbers/non 1 or 11
			try:
				# give user/computer option of 1 or 11 for ace
				randFace = int(raw_input("Ace! Enter 1 or 11: "))
				if randFace != 11 and randFace != 1:
					print "Oops! Try again... "
					raise ValueError
				break
			except ValueError:
				print "Nope! 1 or 11!"
	# just gave facecards values of 10...
	elif randFace == 11:
		randFace = 10
	elif randFace == 12:
		randFace = 10
	elif randFace == 13:
		randFace = 10
	# return values as list (array)
	return randFace, randSuit
# call main function
main()