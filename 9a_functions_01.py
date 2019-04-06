'''
1) where in code to use iterators?
    a) incorporate functions
    b) use iterators in function
    https://www.datacamp.com/community/tutorials/python-iterator-tutorial


NEXT STEP
-add end of game denoument block


FUTURE STEPS
-more functions?
-test processing speeds


'''

def rangeInclusive(start, stop, step=1):
    return range(start, stop+step, step)

def playGame(player, lastMarblePoints, currentMarbleIndex, currentMarbleValue, circle, score):
    if currentMarbleValue <= lastMarblePoints:
        #23 exception
        if currentMarbleValue % 23 == 0:        #multiple of 23
                score[player] += currentMarbleValue  #value of marble added to current player's score
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
    return (marbleIndex, marbleValue, circle, score)

def findWinner(numOfPlayers, theScore):
    winner = -1
    highScore = 0
    for p in rangeInclusive(1, numOfPlayers):
            if theScore[p] > highScore:
                    highScore = theScore[p]     
                    winner = p    
    print("Player ", winner, " is the winner with a score of: ", highScore)

                    
numPlayers = 10
lastMarble = 1618
marbleIndex = 0
marbleValue = 0 #explicit, so it can exist outside of function
circle = [0]    #initial marble placed (index 0 with value 0)
score = {}      

#initialize player scores (so all represented, and prevent error using += to creat scores in 23 exception(cant += if not initialized))
for p in rangeInclusive(1, numPlayers):
        score[p] = 0
        

#play game until last marble placed ***watch for 23 exception
while marbleValue < lastMarble:
    #keep track of players & turns
    for player in range(1, numPlayers+1):    #current player == i
        #next marble number
        marbleValue += 1
        marbleIndex, marbleValue, circle, score = playGame(player, lastMarble, marbleIndex, marbleValue, circle, score)


findWinner(numPlayers, score)
print(score[10])
