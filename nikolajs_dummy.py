#TODO: Create your own subfile (e.g. "group0.py"), with a class ('Group0IsAwesome()')
class NikolajsDummyCalculator:
    """
    The class must have an attribute name (e.g. self.name = "Group 0s calculator")
    and a method Z which takes as input an integer n and parameter w, and returns
    Z(n,w) := sum_{x1, ..., xn} P(x1, ..., xn), where P is the joint probability
    of the Ising model with graph X1 - X2 - ... - Xn and energy function
    epsilon(xi, xj) = - w*xi*xj.
    """
    def __init__(self): self.name = "Nikolajs dummy calculator"

    def Z(self, n, w):
        """Compute the normalization constant for a choice of n and w"""
        return 5
