def match(ElderInfo, HelperInfo):
    score= 0
    for x in range(len(ElderInfo)):
        if ElderInfo[x]==1 and HelperInfo[x]==1:
            score +=1 
    if (score >=2):
        return True
    else:
        return False
      
def findMatches(elder, database):
    matches=[]
    for x in database:
        if match(elder, database[x]) == True:
            matches.append(x)
    return matches



Gurtrude = [1,1,0,1]
database={"Sally":[0,1,1,0], "Chad":[0,1,1,0], "Lily":[0,1,0,1], "Omar":[1,1,1,1]}


print(findMatches(Gurtrude, database))
