'''

'''


'''
ALGORITHM

Place Marbles
- 0 -> first marble at center

-placement: 
newIndex = between [currentIndex+1] and [currentIndex+2] ***use insertion***

-counting: 
wraps around (to zero and starts again)

-if multiple of 23: #special case
*currentPlayerScore += currentMarble 
(currentMarble not placed)
*currentPlayerScore += the marble 7 marbles counter-clockwise from the current marble
{ [indexof(currentMarble)-7] }
*the marble 7 marbles counter-clockwise from the current marble is removed from the circle
{ removeMarble[indexof(currentMarble) - 7] }
*The marble immediately clockwise of the marble that was removed becomes the new current marble.
{ newCurrentMarble[indexof(removedMarbleAbove)-1] }

What Is The Winning Elf's Score?
-game ends after last marble is placed
-sort scores of all players
-return last/highest score

'''


'''
PSEUDO CODE
***CONTINUE HERE***
FIRST
-continue writing code
-create working program, NOT including 23 exception
-use printouts
*track progress
-run for input up to 22
*use sample code on website
*output should be same as printout diagram

-use functions


SECOND
-add 23 exception

-5 test cases listed on website
*function runTests
*use input, should match output
*unit testing,
*assertion, raise exception if fails, if true does nothing (use for debugging, not in production code)
*run first
*then ren rest of code

#handy starting functions templates:
(eg imports, read in file, functions)
def rangeInclusive(start, stop, step=1):
	return range(start, stop+step, step)

#google research "python generators"
def rangeInclusiveChars(start, stop):
	for i in rangeInclusive(ord(start), ord(stop)):
		yield char(i)


PART TWO / STAR 2
-if stuck:
	teachable moment with Jason
'''


numPlayers = 0
lastMarblePoints = 5
currentMarbleIndex = 0
currentMarbleValue = 0
circle = [0]	#initial marble placed (index 0 with value 0)


while currentMarbleValue < lastMarblePoints:	#play game until last marble placed ***watch for 23 exception

        #place next marble nto circle
	currentMarbleValue += 1	#next marble number
	if currentMarbleIndex == len(circle)-1:                 #current = last index in list
		currentMarbleIndex = 1
		#circle.insert(1, currentMarbleValue)
	elif (len(circle)-1) - currentMarbleIndex == 1:         #current = 2nd to last
		currentMarbleIndex = len(circle)
		#circle.append(currentMarbleValue)
	else:                                                   #normal placement
		currentMarbleIndex += 2
		#circle.insert(currentMarbleIndex + 2, currentMarbleValue)	
	circle.insert(currentMarbleIndex, currentMarbleValue)
	print(circle)

        #Score Keeping


'''
	#***CONTINUE HERE***t
	-write code for score keeping
	-end of game evaluation
	-run sample code tests
'''




	#account for 23 exception
	
	



'''
OLD CODE NO USED


WHY WRONG: didn't update currentIndexValue after insertion
while currentMarbleValue < lastMarblePoints:	#play game until last marble placed ***watch for 23 exception
#place next marble
	if currentMarbleIndex + 2 > len(circle)-1:	#wrap around
		currentMarbleIndex = (currentMarbleIndex + 2) - (len(circle)-1)	#num spaces move past 0	
	currentMarbleIndex += 2	#next marble value
	currentMarbleValue += 1	#next marble index
	circle.insert(currentMarbleIndex, currentMarbleValue)	#insert next marble into circle	
'''

'''
while currentMarbleValue < lastMarblePoints:	#play game until last marble placed ***watch for 23 exception
#place next marble nto circle
	currentMarbleValue += 1	#next marble number
	if currentMarbleIndex == len(circle)-1:               #current = last index in list
		circle.insert(1, currentMarbleValue)
		print(circle)
	elif (len(circle)-1) - currentMarbleIndex == 1:     #current = 2nd to last 
		circle.append(currentMarbleValue)
		print(circle)
	else:
		circle.insert(currentMarbleIndex + 2, currentMarbleValue)	#normal placement
		print(circle)
print(circle)
'''




