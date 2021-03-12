"""
main file to drive the guitar program
as opposed to doing it all in one file
i'm trying to be a good programmer here
"""
import guitar

#guitar.print_all_scales('A')


options = """
1) Scale lookup
2) Practice mode
3) FAQ
"""
hammer_time = ''

#maybe move these fuctions to another file to clean up main?
#that's what i would do if i was a good programmer

def validate_key(key):
	#this function checks if the entered key is valid

	if key == 'E#':
		print('The key of E# exists in theory, but for our purposes, is equivalent to F')
		return 'F'
	elif key == 'B#':
		print('The key of B# exists in theory, but for our purposes, is equivalent to C')
		return 'C'
	else:
		try:
			key_index = guitar.keys.index(key)
		except ValueError:
			key_index = -1

		if key_index > -1:
			return key
		else: 
			print('Invalid key.')
			return 'q'

def scale_lookup():
	print ('Scale lookup tool. Enter q to quit at any time.')
	choice_key = ''
	choice_pos = ''
	choice_key = input('First, enter a minor key in the format A or A#: ')
	choice_key = validate_key(choice_key)
	if choice_key == 'q':
		choice_key = input('Try another? Enter a minor key in the format A or A#: ')
		choice_key = validate_key(choice_key)
	while choice_key != 'q' and choice_pos != 'q':
		choice_pos = input('Enter the number of the position you want (1-5), or enter a for all positions: ')
		if choice_pos == 'a':
			guitar.print_all_scales(choice_key)
		else:
			guitar.print_scale_verbose(choice_key, choice_pos)
		choice_key = input('Another? Enter another key or q to quit: ')
		choice_key = validate_key(choice_key)

def faq():
	print ('Frequently axed questions. Enter a numner for an answer, or q to quit.')
	for x in guitar.qs:
		print (x)
	choice = ''
	choice = input('Selection: ')
	while choice != 'q':
		if choice == 'a':
			for x in guitar.qs:
				print (x)
		elif int(choice) > 0 and int(choice) < 6:
			choice = int(choice)
			print (guitar.qs[(choice - 1) % 5])
			print ('\n' + guitar.ans[(choice - 1) % 5] + '\n')
		else:
			print('We both know that is not a valid input.')
		choice = input('Another? Enter another number, a to see the list agian, q to quit: ')

practice_options = """
1) Pure random mode: you'll be given a series of random keys and positions
2) Random in-key: pick a key, get a random series of positions
"""

def practice_mode():
	#this mode allows you to practice the scale patterns
	print ('Welcome to practice mode. Please note that minor burns are a normal part of the experience.')
	choice_mode = ''
	print (practice_options)
	choice_mode = input('Select an option by entering a number. Enter q to exit: ')
	

	while choice_mode != 'q':
		if choice_mode == '2':
			choice_key = input('Enter a key in the format A or A#: ')
		hard_mode = False
		mode = input('Optional hard mode. Do you want to hide the scale diagrams? y/n: ')
		if mode == 'y':
			hard_mode = True
		print ("Starting practice mode. Enter q to quit, or any other key to fetch the next item.")
		practice_choice = ''
		while practice_choice != 'q':
			if choice_mode == '1':
				choice_key = guitar.random_key()
			choice_pos = guitar.random_pos(choice_key)
			if hard_mode:
				print('Key: ' + choice_key + ' Position: ' + str(choice_pos))
			else:
				guitar.print_scale_verbose(choice_key, choice_pos)
			practice_choice = input('Enter q to quit, or hit enter for another: ')
		print (practice_options)
		choice_mode = input('Select an option to keep practicing. Enter q to exit: ')
		



#main
while hammer_time != 'q':
	print ('Welcome to the Aperture Science Guitar Practice Module.')
	print ('Please enter a number to select from the list, type q to quit.')
	print (options)

	hammer_time = input('Enter a selection: ')

	if hammer_time == '1':
		scale_lookup()
	elif hammer_time == '2':
		practice_mode()
	elif hammer_time == '3':
		faq()
	elif hammer_time == 'q':
		print ('Thanks for your time. Please grab a slice of cake on the way out.')
	else:
		print('I do not understand. Please try again')
