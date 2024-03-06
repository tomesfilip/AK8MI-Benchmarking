import testFunctions
from algorithms import *
from testFunctions import *

# Algorithms
random_search()
simulated_annealing()

x = np.array([1, 3])

# Test functions
schwefel = Schwefel(2)
de_jong = FirstDeJong()
de_jong_2 = SecondDeJong()


print("Schwefel: ", schwefel(x))
print("First de jong: ", de_jong(x))
print("Second de jong: ", de_jong_2(x))
