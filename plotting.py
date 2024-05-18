import matplotlib.pyplot as plt


def plot_convergence_all(data, algo_name, test_function_name):
    _, ax = plt.subplots()

    for item in data:
        ax.plot(item)

    plt.title(f"All Runs Convergence: Algorithm - {algo_name}, Test function - {test_function_name}")
    plt.xlabel("Generations")
    plt.ylabel("CF Value")
    plt.show()


def plot_average_convergence(data, algo_name, test_function_name):
    _, ax = plt.subplots()
    ax.plot(data)
    plt.title(f"Average Best Result Convergence: Algorithm - {algo_name}, Test function - {test_function_name}")
    plt.xlabel("Generations")
    plt.ylabel("CF Value")
    plt.show()


def plot_average_convergence_comparison(data, test_function_name):
    _, ax = plt.subplots()

    for algo_name, data in data.items():
        print("Algo: ", algo_name)
        ax.plot(data, label=algo_name)

    plt.title(f"Average Best Result Convergence Comparison: Test function - {test_function_name}")
    plt.xlabel("Generations")
    plt.ylabel("CF Value")
    plt.legend()
    plt.show()

