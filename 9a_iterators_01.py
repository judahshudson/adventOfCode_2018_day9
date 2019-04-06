'''

PART TWO / STAR 2
-if stuck:
        teachable moment with Jason
'''


def rangeInclusive(start, stop, step=1):
        return range(start, stop+step, step)

def findWinner(numOfPlayers, theScore):
        winner = -1
        highScore = 0
        for p in rangeInclusive(1, numOfPlayers):
                if theScore[p] > highScore:
                        highScore = theScore[p]
                        winner = p
        print("Player ", winner, " is the winner with a score of: ", highScore)
 

numPlayers = 10
lastMarblePoints = 1618
currentMarbleIndex = 0
currentMarbleValue = 0
circle = [0]    #initial marble placed (index 0 with value 0)
score = {}      #player:score
scoreIterator = iter(score)     #***NEW ITERATOR CODE***


#initialize player scores (so all represented, and prevent error using += to creat scores in 23 exception(cant += if not initialized))
for p in rangeInclusive(1, numPlayers):
        score[p] = 0

#play game until last marble placed ***watch for 23 exception
while currentMarbleValue < lastMarblePoints:    

        #keep track of players & turns
        for player in range(1, numPlayers+1):    #current player == i  
                #next marble number
                currentMarbleValue += 1
                if currentMarbleValue <= lastMarblePoints:      
                        #23 exception
                        if currentMarbleValue % 23 == 0:        #multiple of 23
                                #score[player] += currentMarbleValue  #value of marble added to current player's score
#***NEW ITERATOR CODE***        -doesnt' work; i don't get concept
                                next(scoreIterator) += currentMarbleValue



                                #7th marble counter-clockwise from current marble
                                if currentMarbleIndex < 7:            #wrap around case
                                        excptnIndex = (len(circle)) - (7-currentMarbleIndex)
                                else:
                                        excptnIndex = currentMarbleIndex-7       #regular case
                                        '''
                                print("\nexcptnIndex: ",  excptnIndex)
                                print("length of circle: ", len(circle))
                                print("currentMarbleValue: ", currentMarbleValue)
                                print("currentMarbleIndex: ", currentMarbleIndex)
                                '''     
                                score[player] += circle[excptnIndex]    # -> added to current player's score...
                                del circle[excptnIndex]                 #...and is removed from circle

                                currentMarbleIndex = excptnIndex #- 1    #current marble = marble located immediately clockwise of the marble that was removed
                                #break                                   #do not place %23 marble into circle (skips code below)

                                #print("[{}]  {}".format(player, circle))                #prints display like AOC example page
        
                        else:
                                #place next marble into circle
                                if currentMarbleIndex == len(circle)-1:                 #current = last index in list
                                        currentMarbleIndex = 1
                                elif (len(circle)-1) - currentMarbleIndex == 1:         #current = 2nd to last
                                        currentMarbleIndex = len(circle)
                                else:                                                   #normal placement
                                        currentMarbleIndex += 2 
                                circle.insert(currentMarbleIndex, currentMarbleValue)
                                #print("[{}]  {}".format(player, circle))                #prints display like AOC example page


                
#end of game evaluation

'''
#find highest score
winner = -1
highScore = 0
for p in rangeInclusive(1, numPlayers):
        if score[p] > highScore:
                highScore = score[p]
                winner = p
        
print("Player ", winner, " is the winner with a score of: ", highScore)
'''
findWinner(numPlayers, score)



#***CONTINUE HERE NEXT***
'''
try incorporating iterators into
-Find Highest Score
*doesn't fit example, bottom page
https://www.datacamp.com/community/tutorials/python-iterator-tutorial

rather than function,
try using iterators in body of code, such as:
a_set = {1, 2, 3}
b_iterator = iter(a_set)
next(b_iterator)
1) find eterables (eg lists, dictionaries)
2) try apply iterator

CONTINUE HERE
-didn't work
-i don't get concept

NEXT STEP
-learn better grasp of iterators
*easy practice exercises
-come back later,
attempt to apply new knowledge to this problem


               



'''
