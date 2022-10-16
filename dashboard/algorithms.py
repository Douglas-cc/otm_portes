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

    def nsga2(self, target_lower, target_upper, xl_input,
              xu_input, frequencia, media_cenario):
        
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
                
        return [res.X, res.F]
    
    def frente_pareto(self, f, media_cenario, media, frequencia, valor_otimo):
        # Calculando f1 e f2 para o valor otimo
        f1_valor_otimo = sum((media_cenario - valor_otimo) * frequencia)
        f2_valor_otimo = np.std(1/frequencia * valor_otimo * 1)

        # Calculando f1 e f2 para o valor media
        f1_valor_media = sum((media_cenario -  media) * frequencia)
        f2_valor_media = np.std(1/frequencia * media * 1)

        fig, ax = plt.subplots(figsize=[12, 10], dpi=100)
        ax.scatter(f[:,0], f[:,1], color="firebrick", label="Soluções NSGA-II")
        ax.scatter(f1_valor_otimo, f2_valor_otimo, color="blue", label="Valor otimo")
        ax.scatter(f1_valor_media, f2_valor_media, color="green", label="Valor media")

        ax.set_ylabel("$f_2$")
        ax.set_xlabel("$f_1$")
        ax.legend()
        return fig 

