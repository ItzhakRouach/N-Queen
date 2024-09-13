import random
import math
#  Crunchy annealing formula
def Schedule(t):
    return 1 / t


class SimulatedAnnealing:
    def __init__(self, queens,current):
        if queens <= 3:
            raise ValueError("Cannot solve for queen <= 3 only for queens >= 4")
        else:
            self.queens = queens
            self.t = 1
            self.current = current

    # randomly chose a neighbor from current
    def get_neighbor(self):
        neighbor = self.current[:] #create a copy of the original state that way we dont change it accidentally
        index = random.randint(0, len(self.current) - 1) #chose a random column queen position
        neighbor[index] = random.randint(0, len(self.current)-1) #move the queen in the index-column position to new location in her row
        return neighbor #return the new current state with the change of one queen position


    #check how many collision we have between each queen , the goal is to have none in our current state
    def collisions(self, state):
        collision = 0
        for i in range(len(state)): #run on one queen and compare to the others
            for j in range(i + 1, len(state)):
                if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j): #check if there is conflict in the same row or on the same diagonal
                    collision += 1 #add 1 to our total collision
        return collision #return total collision

    #from here we run the algorithm
    def runAlgorithm(self):
        while True:
            t = Schedule(self.t)
            if t == 0:
                return self.current

            neighbor = self.get_neighbor() #return the new current state with the change of one queen position,
            current_value = self.collisions(self.current)  #check how many collision we have in our current state and return it
            neighbor_value = self.collisions(neighbor) #check how many collision we have with our neighbor that we chose and change and return the value
            delta_E = current_value - neighbor_value #calculate the difference between current to neighbor

            if delta_E > 0: #if delta e greater then 0
                self.current = neighbor #current will now be neighbor
            else:
                probability = math.exp(delta_E / t) #define probability where if it's greater than random number 0 to 1 then change current to neighbor
                if random.random() < probability:
                    self.current = neighbor

            self.t += 1

            if current_value == 0: #if we reach to 0 collision its means we reach our goal target , then break and return the result
                break
        return f"Final Solution: {self.current}"
