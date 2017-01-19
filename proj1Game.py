# import modules
import random
import datetime


def blackjack():
	# give user and computer random cards calling card function
	userWinCount = 0
	again = 'y'
	user = input("Enter your user name: ")
	with open('Scores.txt', 'r') as doc:
		content = doc.readlines()
		doc.close()
	if user in content:
		print("Welcome back, " + user + "!")
	else:
		print("Nice to meet you, " + user)
	while again == 'y':
		userHand = card()
		computerHand = card()
		userHand += card()
		computerHand += card()
		# print(user and computer cards)
		get_user_hand(user, userHand)
		get_comp_hand(computerHand)
		# get card totals
		userTotal = userHand[0] + userHand[2]
		computerTotal = computerHand[0] + computerHand[2]
		# print(card totals)
		print(user + "'s total: " + str(userTotal))
		print("Computer total: " + str(computerTotal))
		# enter loop for hit, and initialize incrementer
		hit = input("Do you want another card, " + user + "? (y for yes): ")
		count = 4
		userBust = False
		while hit == 'y':
			userHand += card()
			print(userHand)
			userTotal += userHand[count]
			print(user + "'s total: " + str(userTotal))
			if userTotal > 21:
				print(user + " busts!")
				userBust = True
				break
			hit = input("Do you want another card, " + user + "? (y for yes): ")
			# increment counter for adding new card to total
			count += 2
		computerCount = 4
		# computer hits if 16 or under
		while computerTotal <= 16 and not userBust:
			computerHand += card()
			print(computerHand)
			computerTotal += computerHand[computerCount]
			print("Computer total: " + str(computerTotal))
			if computerTotal > 21:
				print("Computer busts!")
				break
			computerCount += 2
		# if user is high and 21 or under, user wins
		if computerTotal > 21 >= userTotal or computerTotal < userTotal <= 21 :
			userWins = True
			print("You win, " + user + "!")
			userWinCount += 1
			if userWins:
				with open('Scores.txt', 'a+') as doc:
					doc.write(user + ": " + str(userWinCount) + "\t" + str(datetime.date.today()) + "\n")
					doc.close()
		else:
			print("Computer wins!")
		again = input("Do you want to play again? (y for yes): ")

# define the card drawing function
def card():
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
		randFace = get_ace(randFace)
	elif randFace == 11:
		randFace = 10
	elif randFace == 12:
		randFace = 10
	elif randFace == 13:
		randFace = 10
	# return values as list (array)
	return randFace, randSuit


# define the get ace function
def get_ace(ace):
	while True:
		# try except block for non numbers/non 1 or 11
		try:
			# give user/computer option of 1 or 11 for ace
			ace = int(input("Ace! Enter 1 or 11: "))
			if ace != 11 and ace != 1:
				print("Oops! Try again... ")
				raise ValueError
			break
		except ValueError:
			print("Nope! 1 or 11!")
	return ace


def get_user_hand(user, hand):
		print(user + "'s hand: " + str(hand))


def get_comp_hand(hand):
		print("Computer hand: " + str(hand))

# call main function
blackjack()