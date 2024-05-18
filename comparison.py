import numpy as np


def construct_stats(data, algo_name, function_name):
    return {
        "algorithm": algo_name,
        "function": function_name,
        "min": np.min(data),
        "max": np.max(data),
        "mean": np.mean(data),
        "median": np.median(data),
        "std": np.std(data)
    }


def compare_stats(stats_list):
    for stats in stats_list:
        print(f"Algorithm: {stats['algorithm']} ({stats['function']})")
        print(f"  Min: {stats['min']}")
        print(f"  Max: {stats['max']}")
        print(f"  Mean: {stats['mean']}")
        print(f"  Median: {stats['median']}")
        print(f"  Std: {stats['std']}")
        print()
