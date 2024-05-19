import numpy as np
from algorithms import random_search, simulated_annealing
from testFunctions import dejong1, dejong2, schweffel
from comparison import construct_stats, compare_stats
from plotting import plot_convergence_all, plot_average_convergence, plot_average_convergence_comparison


def run_experiment(algorithm, objective_function, dimension, bounds, iterations, runs):
    print(
        "Experiment\nAlgorithm: " + algorithm[
            "title"] + "\nObjective function" + objective_function.__name__ + "\nDimension: " + str(
            dimension))

    results = []
    for _ in range(runs):
        _, _, outputs = algorithm["algo_func"](objective_function=objective_function,
                                               bounds=bounds,
                                               dimension=dimension,
                                               iterations=iterations)

        results.append(outputs)

    average_convergence = np.mean(results, axis=0)

    plot_convergence_all(data=results,
                         dimension=dimension,
                         algo_name=algorithm["title"],
                         test_function_name=objective_function.__name__)
    plot_average_convergence(data=average_convergence,
                             dimension=dimension,
                             algo_name=algorithm["title"],
                             test_function_name=objective_function.__name__)

    return results, average_convergence


def main():
    algorithms = [
        {"title": "Random Search", "algo_func": random_search},
        {"title": "Simulated Annealing", "algo_func": simulated_annealing}]
    objective_functions = [
        {"func": dejong1, "bounds": (-5, 5)},
        {"func": dejong2, "bounds": (-5, 5)},
        {"func": schweffel, "bounds": (-500, 500)}]
    dimensions = [5, 10]
    max_fes = 10000
    runs = 30

    for dimension in dimensions:
        for objective_function in objective_functions:
            avg_convergences = {}
            all_results = []
            stats_list = []
            for algorithm in algorithms:
                results, avg_convergence = run_experiment(algorithm=algorithm,
                                                          objective_function=objective_function["func"],
                                                          bounds=objective_function["bounds"],
                                                          dimension=dimension,
                                                          iterations=max_fes,
                                                          runs=runs)
                avg_convergences[algorithm["title"]] = avg_convergence
                all_results.append((algorithm["title"], results))

                stats = construct_stats(np.concatenate(results), algorithm["title"], objective_function["func"].__name__)
                stats_list.append(stats)

            plot_average_convergence_comparison(data=avg_convergences,
                                                dimension=dimension,
                                                test_function_name=objective_function["func"].__name__)
            compare_stats(stats_list)


if __name__ == "__main__":
    main()
