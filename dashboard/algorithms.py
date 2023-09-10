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
        # ordenar f1 e f2 das soluções
        f1_ordenado_decres = sorted(f[:,0], reverse=True) 
        f2_ordenado_cres = sorted(f[:,1])

        fig, ax = plt.subplots(figsize=[8, 4], dpi=100)
        ax.scatter(f1_ordenado_decres, f2_ordenado_cres, color="firebrick", label="Soluções NSGA-II")

        ax.set_ylabel("$f_2$")
        ax.set_xlabel("$f_1$")
            
        # Calcule os valores mínimos e máximos de f2, f1, e otimo
        min_f2 = min(f2_ordenado_cres)
        max_f2 = max(f2_ordenado_cres)

        min_f1 = min(f1_ordenado_decres)
        max_f1 = max(f1_ordenado_decres)

        ax.set_ylim(min_f2, max_f2)
        ax.set_xlim(min_f1, max_f1)

        ax.legend()
        return fig
        
