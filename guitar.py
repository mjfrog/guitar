#guitar practice program
"""ideas
-practice mode, give you a random key and pos, maybe changes every ten seconds
-lookup mode, lets you print a key and position
-FAQ mode
"""
import random

keys = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

key = random.choice(keys)
pos = random.randint(1,5)

pos1 = """
|-m-|---|---|-M-|
|-o-|---|---|-o-|
|-M-|---|-o-|---|
|-o-|---|-m-|---|
|-o-|---|-o-|---|
|-m-|---|---|-M-|"""

pos2 = """
|---|-M-|---|-o-|
|---|-o-|---|-m-|
|-o-|---|-o-|---|
|-m-|---|---|-M-|
|-o-|---|---|-o-|
|---|-M-|---|-o-|"""

pos3 = """
|---|-o-|---|-o-|---|
|---|-m-|---|---|-M-|
|-o-|---|---|-o-|---|
|---|-M-|---|-o-|---|
|---|-o-|---|-m-|---|
|---|-o-|---|-o-|---|"""

pos4 = """
|-o-|---|---|-o-|
|---|-M-|---|-o-|
|-o-|---|-m-|---|
|-o-|---|-o-|---|
|-m-|---|---|-M-|
|-o-|---|---|-o-|"""

pos5 = """
|---|-o-|---|-m-|
|---|-o-|---|-o-|
|-m-|---|---|-M-|
|-o-|---|---|-o-|
|---|-M-|---|-o-|
|---|-o-|---|-m-|"""

positions = [pos1, pos2, pos3, pos4, pos5]


def print_scale(key, pos):
	#accept a key and position and print it out
	
	print '\n' + key + ' minor pentatonic, position ' + str(pos)
	print positions[pos-1]
	print str(starting_fret(key,pos)) + 'fr.'

def starting_fret(key, pos):
	#calculate the starting fret based on the key and position
	frets = ['E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
	start = [0,2,4,7,10]
	ans = frets.index(key) + start[pos-1]
	if pos == 5:
		ans = '     ' + str(ans)

	return ans

print_scale('B', 1)