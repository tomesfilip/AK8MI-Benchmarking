from numpy import exp
from numpy.random import randn
from numpy.random import rand

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


def random_search(objective_function, bounds, n_iterations, fes_limit):
    best = None
    best_eval = float('inf')
    fes_count = 0
    outputs = []

    for i in range(n_iterations):
        candidate = bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
        candidate_eval = objective_function(candidate)
        fes_count += 1

        if candidate_eval < best_eval:
            best, best_eval = candidate, candidate_eval
            outputs.append(best_eval)

        if fes_count >= fes_limit:
            break

    return best, best_eval, outputs


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

the rate at which we decrease t is called the algorithm's schedule. The longer we stretch out the schedule,
the longer the algorithm resembles a random walk and the more exploration it does    

"""


# simulated annealing algorithm
def simulated_annealing(objective_function, bounds, n_iterations, step_size, temp, fes_limit):
    # generate an initial point
    best = bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
    # evaluate the initial point
    best_eval = objective_function(best)
    # current working solution
    curr, curr_eval = best, best_eval
    fes_count = 0
    outputs = []

    for i in range(n_iterations):
        if fes_count >= fes_limit:
            break
        # take a step
        candidate = curr + randn(len(bounds)) * step_size
        # evaluate candidate point
        candidate_eval = objective_function(candidate)
        fes_count += 2
        # check for new best solution
        if candidate_eval < best_eval:
            outputs.append(best_eval)
            # store new best point
            best, best_eval = candidate, candidate_eval
            # difference between candidate and current point evaluation
            diff = candidate_eval - curr_eval
            # calculate temperature for current epoch
            t = temp / float(i + 1)
            # calculate metropolis acceptance criterion
            metropolis = exp(-diff / t)
            # check if we should keep the new point
            if diff < 0 or rand() < metropolis:
                fes_count += 1
                # store the new current point
                curr, curr_eval = candidate, candidate_eval
    return best, best_eval, outputs


