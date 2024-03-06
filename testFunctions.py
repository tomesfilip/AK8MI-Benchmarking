import numpy as np

"""
Defined test function classes

source: https://github.com/AxelThevenot/Python_Benchmark_Test_Optimization_Function_Single_Objective
"""
class FirstDeJong:
    name = "First De Jong"
    latex_formula = r"f(x, y) = x^2 + y^2"
    latex_formula_dimension = r"x, y \in \mathbb{R}"
    latex_formula_input_domain = r"x, y \in (-\infty, +\infty)"
    continuous = True
    convex = True
    separable = True
    differentiable = True
    mutimodal = False
    randomized_term = False
    parametric = False

    @classmethod
    def is_dim_compatible(cls, d):
        return d == 2

    def __init__(self):
        self.input_domain = np.array([[-float('inf'), float('inf')], [-float('inf'), float('inf')]])

    def get_param(self):
        return {}

    def get_global_minimum(self):
        return (0, 0), 0

    def __call__(self, X):
        x, y = X
        res = x**2 + y**2
        return res


class SecondDeJong:
    name = "Second De Jong"
    latex_formula = r"f(x, y) = 3905.93 - 100\sqrt{x^2 + y^2} - \frac{sin(x^2 + y^2)}{x^2 + y^2}"
    latex_formula_dimension = r"x, y \in \mathbb{R}"
    latex_formula_input_domain = r"x, y \in (-\infty, +\infty)"
    continuous = True
    convex = False
    separable = True
    differentiable = False
    mutimodal = True
    randomized_term = False
    parametric = False

    @classmethod
    def is_dim_compatible(cls, d):
        return d == 2

    def __init__(self):
        self.input_domain = np.array([[-float('inf'), float('inf')], [-float('inf'), float('inf')]])

    def get_param(self):
        return {}

    def get_global_minimum(self):
        return (0, 0), 3905.93

    def __call__(self, X):
        x, y = X
        res = 3905.93 - 100 * np.sqrt(x**2 + y**2) - np.sin(x**2 + y**2) / (x**2 + y**2)
        return res


class Schwefel:
    name = "Schwefel"
    latex_formula = r"f(\mathbf{x})=418.9829d -{\sum_{i=1}^{d} x_i sin(\sqrt{|x_i|})}"
    latex_formula_dimension = r"d \in \mathbb{N}_{+}^{*}"
    latex_formula_input_domain = (
        r"x_i \in [-500, 500], \forall i \in \llbracket 1, d\rrbracket"
    )
    latex_formula_global_minimum = r"f(420.9687, ..., 420.9687)=0"
    continuous = True
    convex = False
    separable = True
    differentiable = False
    mutimodal = True
    randomized_term = False
    parametric = False

    @classmethod
    def is_dim_compatible(cls, d):
        assert (d is None) or (
            isinstance(d, int) and (not d < 0)
        ), "The dimension d must be None or a positive integer"
        return (d is None) or (d > 0)

    def __init__(
        self,
        d,
    ):
        self.d = d
        self.input_domain = np.array([[-500, 500] for _ in range(d)])

    def get_param(self):
        return {}

    def get_global_minimum(self, d):
        x = np.array([420.9687 for _ in range(d)])
        return x, self(x)

    def __call__(self, X):
        d = X.shape[0]
        res = 418.9829 * d - np.sum(X * np.sin(np.sqrt(np.abs(X))))
        return res
    