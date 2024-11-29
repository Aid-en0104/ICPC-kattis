import random
from collections import defaultdict

def simulate_ball(pGrid, pStart, w, h, probPercent, max_steps=10000):
    ballDir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    pRange = [sum(probPercent[:i]) for i in range(1, 5)]
    x, y = 0, pStart
    for _ in range(max_steps):
        if pGrid[x][y] == 'T':
            return (x, y)
        
        randNum = random.uniform(0, 1)
        if randNum < pRange[0]:
            x2, y2 = ballDir[0]
        elif randNum < pRange[1]:
            x2, y2 = ballDir[1]
        elif randNum < pRange[2]:
            x2, y2 = ballDir[2]
        else:
            x2, y2 = ballDir[3]

        newX, newY = x + x2, y + y2
        if 0 <= newX < h and 0 <= newY < w and pGrid[newX][newY] != 'X':
            x, y = newX, newY

    return None

def calcProb(w, h, u, d, l, r, numSim, pGrid):
    total = u + d + l + r
    probPercent = [u / total, d / total, l / total, r / total]

    ValidPath = [col for col, cell in enumerate(pGrid[0]) if cell == '.']
    endTargets = [(x, y) for x in range(h) for y in range(w) if pGrid[x][y] == 'T']
    
    tHits = defaultdict(int)

    for _ in range(numSim):
        pStart = random.choice(ValidPath)
        BallToTarget = simulate_ball(pGrid, pStart, w, h, probPercent)
        if BallToTarget:
            tHits[BallToTarget] += 1

    pFinal = []
    for BallToTarget in endTargets:
        pFinal.append(tHits[BallToTarget] / numSim)

    return pFinal

#Get amount of simulations
numSim = int(input("Enter in the amount of simulations you want to run: "))

#Get values for width, height
w , h = map(int, input("Enter the value of w (width) then h (height): ").split())

#Get probability values for up, down, left, right
u , d , l , r = map(int, input("Enter in the probabilities:").split())

#Input for Grid
#I use _ because I dont need how many times the for loop is ran i just need it to be ran
pGrid = [list(input().strip()) for _ in range(h)]

#Check that all inputs are correct / visualize 
#print("Simulation check",numSim)
#print("Diemension check",w,h)
#print("Probability Check",u , d , l , r)
#print("Grid Check",pGrid)

probFinal = calcProb(w, h, u, d, l, r, numSim, pGrid)
for i in probFinal:
    print(f"{i:.9f}")