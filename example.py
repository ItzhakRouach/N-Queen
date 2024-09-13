from simulatedAnnealing import  *
#Example of n-queen problem (in this example for 8 - queen) solve with Simulated Annealing

#First set randomly initial state
initial_state = [random.randint(0,7) for _ in range(8)]

#Create an instance of SimulatedAnnealing with the initial state and number of queens 8
example = SimulatedAnnealing(queens=8 ,current=initial_state)

#Use the main algorithm on the initial state
sol_example = example.runAlgorithm()

#Print the solution the algorithm found
print(sol_example)