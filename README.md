# ModKomp
Git repository for the class Models for Complex Systems

## Exercise 6: 
Create your own subfile (e.g. `group0.py`), with a class (`Group0IsAwesome`). The class must have an attribute `name` (e.g. `self.name = "Group 0s calculator"`) and a method `Z` which takes as input an integer `n` and parameter `w`, and returns the normalization constant `Z(n,w) := sum_{x1, ..., xn} P(x1, ..., xn)`, where P is the joint probability of the Ising model with graph `X1 - X2 - ... - Xn` and energy function `epsilon(xi, xj) = - w*xi*xj`.

Once you have added your Z function to a class, go to the file `arena.py` and register it, by importing it (`from group0 import Group0IsAwesome`) and adding it to the list of models in the Engine. 

