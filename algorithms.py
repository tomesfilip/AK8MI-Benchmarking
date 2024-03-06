"""
Pseudocode for random search:

Best -> some initial random candidate solution
repeat
    S -> a random candidate solution
    if Quality(S) > Quality(Best) then
        Best -> S
until Best is the ideal solution or we have run out of time
return Best

"""


def random_search():
    print("Random Search")


"""
Pseudocode for simulated annealing
t -> temperature, initially a high number
S -> some initial candidate solution
Best -> S

repeat
    R -> Tweak(Copy(S))
    if Quality(R) > Quality(S) or if a random number chosen from 0 to 1 < e^(Quality(R)-Quality(S) / t) then
        S -> R
    Decrease t
    if Quality(S) > Quality(Best) then
        Best -> S
until Best is the ideal solution, we have run out of time, or t <= 0
return Best

the rate at which we decreate t is called the algorithm's schedule. The longer we stretch out the schedule,
the longer the algorithm resembles a random walk and the more exploration it does    

"""


def simulated_annealing():
    print("Simulated Annealing")
