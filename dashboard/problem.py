import numpy as np
from pymoo.core.problem import ElementwiseProblem

class ModelingProblem(ElementwiseProblem):
    def __init__(self, target_lower, target_upper, xl_input, xu_input, frequencia, media_cenario):
        self.target_lower = target_lower
        self.target_upper = target_upper
        self.xl_input = xl_input
        self.xu_input = xu_input
        self.frequencia = frequencia
        self.media_cenario = media_cenario
        self.alpha = 1
    
        super().__init__(
            n_var = 7, 
            n_obj = 2,
            n_constr = 2, 
            xl = self.xl_input, 
            xu = self.xu_input
        )
    
    def _evaluate(self, x, out, *args, **kwargs):
        f1 = sum((self.media_cenario - x) * self.frequencia)
        f2 = np.std(self.frequencia * x * self.alpha)
    
        g1 = self.target_lower - sum(x * self.frequencia)
        g2 = sum(x * self.frequencia) - self.target_upper
                                             
        out['F'] = [f1, f2]
        out['G'] = [g1, g2]

