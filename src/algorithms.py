import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pymoo.factory import get_termination
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.optimize import minimize
from problem import ModelingProblem
from pymoo.visualization.scatter import Scatter


class Algorithms:
    def __init__(self):
        self.population = 100 
        self.descendants = 70
        self.termination = get_termination("n_gen", 200)
        self.seed = 1

    def nsga2(self, 
            target_lower,
            target_upper,
            xl_input,
            xu_input,
            frequencia,
            media_cenario
        ):
        
        algo = NSGA2(
            pop_size = self.population,
            n_offsprings = self.descendants,
            eliminate_duplicates = True
        )

        model = ModelingProblem(
            target_lower,
            target_upper,
            xl_input,
            xu_input,
            frequencia,
            media_cenario
        )
                
        res = minimize(
            model,
            algo,
            self.termination,
            seed = self.seed,
            save_history=True,
            verbose=False
        )
                
        return {"res_x":res.X, "res_f":res.F}
    
    
    def frente_pareto(self, f, media_cenario, media, frequencia, valor_otimo):
        f1_ordenado_decres = sorted(f[:,0], reverse=True) 
        f2_ordenado_cres = sorted(f[:,1])
        fig, ax = plt.subplots(figsize=[12, 4], dpi=100)
        ax.scatter(f1_ordenado_decres, f2_ordenado_cres, color="green")
        ax.set_title("Frente de Pareto")
        ax.set_ylabel("$f_2$")
        ax.set_xlabel("$f_1$")
        return fig