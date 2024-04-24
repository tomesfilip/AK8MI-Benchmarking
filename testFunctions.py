import numpy as np

"""
Defined test function classes

source: https://github.com/AxelThevenot/Python_Benchmark_Test_Optimization_Function_Single_Objective
"""


class dejong_1st:
    name = "First De Jong"
    latex_formula = r"f(\mathbf{x}) = \sum_{i=1}^{d} x_i^2"
    latex_formula_dimension = r"d \in \mathbb{N}_{+}^{*}"
    latex_formula_input_domain = r"x_i \in (-\infty, +\infty), \forall i \in \llbracket 1, d\rrbracket"
    continuous = True
    convex = True
    separable = True
    differentiable = True
    mutimodal = False
    randomized_term = False
    parametric = False

    @classmethod
    def is_dim_compatible(cls, d):
        return d > 0

    def __init__(self, d: int):
        self.d = d
        self.input_domain = np.array([[-float('inf'), float('inf')] for _ in range(d)])

    def get_param(self):
        return {}

    def get_global_minimum(self):
        return np.zeros(self.d), 0

    def __call__(self, X):
        return np.sum(X ** 2)


class dejong_2nd:
    name = "Second De Jong"
    latex_formula = r"f(\mathbf{x}) = \sum_{i=1}^{d} |x_i|"
    latex_formula_dimension = r"d \in \mathbb{N}_{+}^{*}"
    latex_formula_input_domain = r"x_i \in (-\infty, +\infty), \forall i \in \llbracket 1, d\rrbracket"
    continuous = True
    convex = False
    separable = True
    differentiable = False
    mutimodal = True
    randomized_term = False
    parametric = False

    @classmethod
    def is_dim_compatible(cls, d):
        return d > 0

    def __init__(self, d: int):
        self.d = d
        self.input_domain = np.array([[-float('inf'), float('inf')] for _ in range(d)])

    def get_param(self):
        return {}

    def get_global_minimum(self):
        return np.zeros(self.d), 0

    def __call__(self, X):
        return np.sum(np.abs(X))


class schweffel:
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
            d: int,
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
