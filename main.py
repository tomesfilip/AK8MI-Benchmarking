import json

from numpy import asarray

from algorithms import *
from testFunctions import *

INPUT_DOMAIN = ([-100, 100], [-100, 100])  # Used for plotting
DIMENSIONS = 5  # Possible values: 5, 10
REPETITIONS = 30
FES_LIMIT = 10000

area = asarray([[-6.0, 6.0]])
temperature = 12
iterations = 1200
step_size = 0.1

bench_functions = [
    schweffel(DIMENSIONS),
    dejong_1st(DIMENSIONS),
    dejong_2nd(DIMENSIONS)
]

for func in bench_functions:
    data = []

    for _ in range(REPETITIONS):
        # Results from algorithms
        best_rs, best_val_rs, outputs_rs = random_search(
            objective_function=func,
            bounds=area,
            n_iterations=iterations,
            fes_limit=FES_LIMIT
        )
        best_sa, best_val_sa, outputs_sa = simulated_annealing(
            objective_function=func,
            bounds=area,
            n_iterations=iterations,
            step_size=step_size,
            temp=temperature,
            fes_limit=FES_LIMIT
        )

        data.append({
            "Algorithm": "Random Search",
            "Test Function": func.name,
            "Dimensions": DIMENSIONS,
            "Best Value": best_val_rs
        })
        data.append({
            "Algorithm": "Simulated Annealing",
            "Test Function": func.name,
            "Dimensions": DIMENSIONS,
            "Best Value": best_val_sa
        })

    data_sorted = sorted(data, key=lambda x: x["Best Value"])
    filename = f"{func.name}_{DIMENSIONS}D_results.json"

    with open(filename, 'w') as f:
        json.dump(data_sorted[:30], f, indent=4)

    print(f"Results saved to: {filename}")