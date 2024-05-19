import numpy as np


def random_search(objective_function, bounds, dimension, iterations):
    best_solution = np.random.uniform(bounds[0], bounds[1], dimension)
    best_value = objective_function(best_solution)
    outputs = []

    for _ in range(iterations):
        candidate = np.random.uniform(bounds[0], bounds[1], dimension)
        candidate_value = objective_function(candidate)

        if candidate_value < best_value:
            best_solution, best_value = candidate, candidate_value

        outputs.append(best_value)

    return best_solution, best_value, outputs


def simulated_annealing(objective_function, bounds, dimension, iterations,
                        temp_max=1000, temp_min=0.01, cooling_decr=0.994, metropolis_steps=20, step_size=0.1):
    current_solution = np.random.uniform(bounds[0], bounds[1], dimension)
    current_value = objective_function(current_solution)

    best_solution = current_solution.copy()
    best_value = current_value

    outputs = [best_value]

    def metropolis(curr_val, candidate_val, temp):
        delta = candidate_val - curr_val
        if delta < 0:
            return True
        else:
            probability = np.exp(-delta / temp)
            return np.random.rand() < probability

    def generate_neighbor(solution, step_size, neigh_bounds):
        neighbor = solution + np.random.uniform(-step_size, step_size, size=dimension)
        neighbor = np.clip(neighbor, neigh_bounds[0], neigh_bounds[1])
        return neighbor

    temperature = temp_max
    for _ in range(iterations):
        for _ in range(metropolis_steps):
            neighbor_solution = generate_neighbor(current_solution, step_size, bounds)
            neighbor_value = objective_function(neighbor_solution)

            if metropolis(current_value, neighbor_value, temperature):
                current_solution, current_value = neighbor_solution, neighbor_value

                if neighbor_value < best_value:
                    best_solution, best_value = neighbor_solution, neighbor_value

        temperature = max(temperature * cooling_decr, temp_min)
        outputs.append(best_value)

    return best_solution, best_value, outputs
