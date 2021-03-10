#guitar practice program
"""ideas
-practice mode, give you a random key and pos, maybe changes every ten seconds
-lookup mode, lets you print a key and position
-FAQ mode
"""
import random

keys = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

#key = random.choice(keys)
#pos = random.randint(1,5)

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

about = 'This tool can be used as a reference for the minor pentatonic scales as well as to help practice these scales.'

q1 = '1) What is the minor pentatnic scale?'
q2 = "2) Why are there five positions?"
q3 = '3) Is the minor scale the same as its relative major?'
q4 = '4) What is beauty?'
q5 = '5) Who is better at guitar, Eathan or Ryden?'

qs = [q1, q2, q3, q4, q5]

a1 = """The minor pentatonic scale is like the normal minor scale, but with a couple fewer notes.\
With only 5 notes and a steady pattern, it's straighforward to learn and useful for lead guitar."""

a2 = """There are five notes in the pentatonic scale. Each position corresponds to the scale starting on one of those five notes.\
Learning all five positions is useful because it gives you access to the entire fretboard."""

a3 = """It depends what you mean by same. It has the same notes, which is useful for using scales interchangably while improvising. \
But they are different keys, and behave and feel differently. That's why I included the major and minor roots."""

a4 = """Look buddy, I'm an engineer. That means I solve problems, not problems like "What is beauty?",\
because that would fall within the purview of your conundrums of philosophy. I solve practical problems."""

a5 = """I think the sentiment of this question misses the point of what makes music menaningful. \
The learning of music is a highly individual experience. Teddy Roosevelt said "Comparison is the theif of joy", and pursuing music \
as a means to best someone else defeats the purpose of the exercise. Even if you did want to make a comparison, there are several \
avenues of guitar skill (rhythm, improvisation, fingerstyle, chord voicing, etc.), and it's meaningless to compress them all into a single \
metric for the sole purpose of comparison.

That being said, Eathan is better."""

ans = [a1, a2, a3, a4, a5]


def print_scale(key, pos):
	#accept a key and position and print it out
	pos = int(pos)
	#print '\n' + key + ' minor pentatonic, position ' + str(pos)
	print ('\n', 'position ' , str(pos))
	print (positions[pos-1])
	print (str(starting_fret(key,pos)) + 'fr.')

def print_scale_verbose(key, pos):
	#nearly identical to print_scale() but with more info
	pos = int(pos)
	#print '\n' + key + ' minor pentatonic, position ' + str(pos)
	print ('\n' + key + ' minor pentatonic, relative major ' + str(keys[(keys.index(key) + 3) % 12]))
	print ('m = minor root, M = major root')
	print ('\n', 'position ' , str(pos))
	print (positions[pos-1])
	print (str(starting_fret(key,pos)) + 'fr.')

def starting_fret(key, pos):
	#calculate the starting fret based on the key and position
	cutoff_fret = 16 #when a scale would start on this fret, instead wrap back around to the bottom of the fret board
	frets = ['E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
	start = [0,3,5,7,10]
	ans = frets.index(key) + start[pos-1]
	if ans > cutoff_fret:
		ans -= 12
	if pos == 5 or pos == 2 or pos == 3:
		ans = '     ' + str(ans)


	return ans

def print_all_scales(key):
	print ('\n' + key + ' minor pentatonic, relative major ' + str(keys[(keys.index(key) + 3) % 12]))
	print ('m = minor root, M = major root')
	for i in range(1,6):
		print_scale(key,i)



#print_all_scales('G')
#print_scale('A', 5)