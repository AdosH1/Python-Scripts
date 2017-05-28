#Election Night Revisited - The Real Deal
# By Aden Huen 21329102

#importing ceil function just for convienience
from math import ceil
#using regex for ease of matching formal votes
from re import search

#Extract candidates data from file
#Provide error if unable to
def getCandidates(file):
    
    candidatesCount = {}
    try:
        f = open(file, "r")
    except:
        print("\nError loading from %s" % file)
        quit()
        
    for line in f:
        line = line.strip('\n')
        candidatesCount[line] = []

    f.close()
    
    return candidatesCount

#Extract ballot data from file
#Provide error if unable to
def getBallots(file):

    votes = []
    voteCount = 0
    try:
        f = open(file, "r")
    except:
        print("\nError loading from %s" % file)
        quit()
        
    for line in f:
        line = line.strip('\n').split(",")
        votes.append(line)
        voteCount += 1
        
    f.close()
    
    return (votes, voteCount)
    
#Converts each vote from string to int
#Also checks for illegal characters
def parseVotesStrToInt(votes):
    newVotes = []
    #A list of votes is checked on a vote by vote basis
    for i in range(len(votes)):
        formal = True
        #If each element in a single vote is legal, continue
        for j in range(len(votes[i])):
            votes[i][j] = votes[i][j].strip()
            if votes[i][j] == '':
                votes[i][j] = 0
            elif search('^[0-9]+$', votes[i][j]):
                votes[i][j] = int(votes[i][j])
            else:
                formal = False
        #A new list of formal votes are returned as ints        
        if formal == True:
            newVotes.append(votes[i])
                
    return newVotes

#This function is used to return an 'n' long set for comparison for formal votes
# eg. n = 3 -> returns ([3,2,1])    
def returnSet(ls):
    n = max(ls)
    setList = []
    
    for i in range(n,0,-1):
        setList.append(i)
    
    return set(setList)
    
#Return all formal votes depending on optional preference
def parseToFormalVotes(votes, optional, candidatesCount):
    #we create a new list to return
    formalVotes = []
    #we can't guarantee there will always be 5 candidates, thus we have a variable
    candLength = len(candidatesCount)
    
    #turn votes into integers, discard informal votes regarding illegal elements in each vote
    votes = parseVotesStrToInt(votes)
    
    if optional == False:
        #return a set of numbers equal to how many candidates competing
        # eg. 5 candidates return -> ([5,4,3,2,1])
        formalSet = returnSet([candLength])
        for vote in votes:
            #If our vote is equal in length to no. of Candidates, and formalSet is a subset of our vote
            # we guarantee that our vote is legal and has no repeat numbers
            if len(vote) == candLength and formalSet.issubset(vote):
                formalVotes.append(vote)
    elif optional == True:
        for vote in votes:
            #for each vote we need a new formalSet due to variance in length
            formalSet = returnSet(vote)
            
            #Here we check the len(formalSet) == len(vote) -> there are no repeat numbers
            #                  len(vote) == candLength -> for our best case scenario
            #                  formalSet is a subset of vote -> ensure numbers are ordered with no gaps eg. [1,2,4] disregarded
            if len(formalSet) == len(vote) and len(vote) == candLength and formalSet.issubset(vote):
                formalVotes.append(vote)
            #Same as above, but allows 3 <= len(vote) < candLength
            elif len(formalSet) == len(vote) and len(vote) >= 3 and len(vote) < candLength and formalSet.issubset(vote):
                #Appends 0's at the end of the vote until it hits our required length
                while len(vote) < candLength:
                    vote.append(0)
                formalVotes.append(vote)
            else:
                #disregard all other votes as informal if these tests aren't passed
                pass
    
    return formalVotes
    
#Parse the first round of voting
# The first round of voting does not eliminate competitors, we make use this function
# we'll use the iterateRound function for subsequence rounds
def parseVotingRoundOne(candidatesCount, votes):
    candidates = list(candidatesCount.keys())
    for vote in votes:
        for i in range(len(candidates)):
            if vote[i] == 1:
                candidatesCount[candidates[i]].append(vote)
                
# A function to check whether a majority vote has been achieved
# Returns (if a winner is found), (highest scoring candidate), (lowest scoring candidate)
# We use highest candidate for announcing winner, or lowest candidate for removing from the running 
def checkWinner(candidatesCount):
    highCand = ""
    lowCand = ""
    scores = []
    votes = 0
    candidates = list(candidatesCount.keys())
    
    for candidate in candidates:
        lv = len(candidatesCount[candidate])
        scores.append(lv)
        votes += lv
    
    if max(scores) > ceil( votes / 2 ):
        for candidate, noVotes in candidatesCount.items():
            if len(noVotes) == max(scores):
                highCand = candidate
        return (True, highCand, lowCand)
    else:     
        for candidate, noVotes in candidatesCount.items():
            if len(noVotes) == min(scores):
                lowCand = candidate
        return (False, highCand, lowCand)
 
# A function that helps print the current scoring of the votes without changing the order of our votes 
def printStatus(candidatesCount, count, isWinnerFound):
    candidates = list(candidatesCount.keys())
    printList = []
    
    print("\nCount " + str(count))
    for candidate in candidates:
        printList.append([len(candidatesCount[candidate]), candidate])
    
    printList.sort(reverse=True)
    
    for i in range(len(printList)):
        print(str(printList[i][0]) + "        " + str(printList[i][1]))
        
# A function that parses all of the lowest candidates votes to the next preference, then removes the candidate   
def iterateRound(candidatesCount, lowCand, failedCandidates): 
    candidates = list(candidatesCount.keys())
    for vote in candidatesCount[lowCand]:
        for i in range(len(candidatesCount)):
            vote[i] -= 1
            if vote[i] == 1:
                candidatesCount[candidates[i]].append(vote)
            
    for cand in failedCandidates:
        if cand in candidatesCount:
            del candidatesCount[cand]
            
def roundResultMsg(isWinnerFound, highCand, lowCand):
    if isWinnerFound == True:
        print("\nCandidate " + str(highCand) + " was elected.")
    else:
        print("\nCandidate " + str(lowCand) + " has the smallest number of votes and is eliminated from the count.")
    

def main(candidates_file_name, ballots_file_name, optional=False):
    #A set of candidates that are removed from competing used in the iterateRound function
    failedCandidates = set([])
    
    #Open files to get data
    candidatesCount = getCandidates(candidates_file_name)
    votes, voteCount = getBallots(ballots_file_name)

    #Return list of formal votes
    formalVotes = parseToFormalVotes(votes, optional, candidatesCount)
    #First round of voting
    parseVotingRoundOne(candidatesCount, formalVotes)
    #Check for winner
    isWinnerFound, highCand, lowCand = checkWinner(candidatesCount)
    #Add the lowest candidate to our failedCandidates set
    failedCandidates.add(lowCand)
    
    #Count variable used to keep track of how any cycles we've been through
    count = 1
    #Print status of our counting
    printStatus(candidatesCount, count, isWinnerFound)
    #Print the result of this round of counting
    roundResultMsg(isWinnerFound, highCand, lowCand)
    #Increase our round count
    count += 1
    
    #If no winner has been decided yet, continue our process while removing the lowest candidate
    while isWinnerFound == False:
        iterateRound(candidatesCount, lowCand, failedCandidates)
        isWinnerFound, highCand, lowCand = checkWinner(candidatesCount)
        failedCandidates.add(lowCand)
        printStatus(candidatesCount, count, isWinnerFound)
        
        roundResultMsg(isWinnerFound, highCand, lowCand)
        
        count += 1
    
    print("\n"+ str(voteCount) + " votes submitted with " + str(len(formalVotes)) + " formal votes and " + str(voteCount - len(formalVotes)) + " informal votes.\n")
    