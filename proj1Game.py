# import random module
import random

# define main function
def main():
	# give user and computer random cards calling hand function
	userWinCount = 0
	user = raw_input("Enter your user name: ")
	again = 'y'
	while again == 'y':
		with open('Scores.txt', 'a+') as doc:
			content = doc.readlines()
			doc.close()
		content = [x.strip() for x in content]
		if user in content:
			print "Welcome back, " + user + "!"
		else:
			print "Nice to meet you, " + user
		userHand = hand()
		computerHand = hand()
		userHand += hand()
		computerHand += hand()
		# print user and computer hands
		print user + "'s hand: " + str(userHand)
		print "Computer hand: " + str(computerHand)
		# get card totals
		userTotal = userHand[0] + userHand[2]
		computerTotal = computerHand[0] + computerHand[2]
		# print card totals
		print user + "'s total: " + str(userTotal)
		print "Computer total: " + str(computerTotal)
		# enter loop for hit, and initialize incrementer
		hit = raw_input("Do you want another card, " + user + "? (y for yes): ")
		count = 4
		while hit == 'y':
			userHand += hand()
			print userHand
			userTotal += userHand[count]
			print user + "'s total: " + str(userTotal)
			if userTotal > 21:
				print user + " busts!"
				break
			hit = raw_input("Do you want another card, " + user + "? (y for yes): ")
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
			userWins = True
			print "You win, " + user + "!"
			userWinCount += 1
			if userWins:
				with open('Scores.txt', 'a+') as doc:
					doc.write(user + ": " + str(userWinCount) + "\n")
					doc.close()
		else:
			print "Computer wins!"
		again = raw_input("Do you want to play again? (y for yes): ")


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
	# just gave face cards values of 10...
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