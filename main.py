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

def scale_lookup():
	print ('Scale lookup tool. Enter q to quit at any time.')
	choice_key = ''
	choice_pos = ''
	choice_key = input('First, enter a minor key in the format A or A#: ')
	while choice_key != 'q' and choice_pos != 'q':
		if choice_key == 'E#':
			print('The key of E# exists in theory, but for our purposes, is equivalent to F')
			choice_key = 'F'
		elif choice_key == 'B#':
			print('The key of B# exists in theory, but for our purposes, is equivalent to F')
			choice_key = 'C'
		choice_pos = input('Enter the number of the position you want (1-5), or enter a for all positions: ')
		if choice_pos == 'a':
			guitar.print_all_scales(choice_key)
		else:
			guitar.print_scale_verbose(choice_key, choice_pos)
		choice_key = input('Another? Enter another key or q to quit: ')

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


#main
while hammer_time != 'q':
	print ('Welcome to the Aperture Science Guitar Practice Module.')
	print ('Please enter a number to select from the list, type q to quit.')
	print (options)

	hammer_time = input('Enter a selection: ')

	if hammer_time == '1':
		scale_lookup()
	elif hammer_time == '2':
		print('Practice mode')
	elif hammer_time == '3':
		faq()
	elif hammer_time == 'q':
		print ('Thanks for your time. Please grab a slice of cake on the way out.')
	else:
		print('I do not understand. Please try again')
