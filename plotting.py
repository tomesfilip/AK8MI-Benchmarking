import matplotlib.pyplot as plt


def plot_convergence_all(data, dimension, algo_name, test_function_name):
    _, ax = plt.subplots()

    for item in data:
        ax.plot(item)

    plt.title(f"All Runs: Dimension - {dimension}\nAlgorithm - {algo_name}, Test function - {test_function_name}")
    plt.xlabel("Generations")
    plt.ylabel("CF Value")
    plt.show()


def plot_average_convergence(data, dimension, algo_name, test_function_name):
    _, ax = plt.subplots()
    ax.plot(data)
    plt.title(f"Average Best Result: Dimension - {dimension}\nAlgorithm - {algo_name}, Test function - {test_function_name}")
    plt.xlabel("Generations")
    plt.ylabel("CF Value")
    plt.show()


def plot_average_convergence_comparison(data, dimension, test_function_name):
    _, ax = plt.subplots()

    for algo_name, data in data.items():
        print("Algo: ", algo_name)
        ax.plot(data, label=algo_name)

    plt.title(f"Average Best Result Comparison\n Dimension - {dimension}, Test function - {test_function_name}")
    plt.xlabel("Generations")
    plt.ylabel("CF Value")
    plt.legend()
    plt.show()

