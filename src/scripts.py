import numpy as np
import pandas as pd
import streamlit as st


def generete_df_solution(x):
    df = pd.DataFrame()
    for i in range(len(x)):
        df[f'solution_{i}'] = x[i]  
    return df


def upload_file():
    data_input = st.file_uploader("upload file", type={"csv", "txt"})
    if data_input is not None:
        return pd.read_csv(data_input).drop(columns=["freq"])
    

def smaller_sizes(df_solutions, portes=[7], total_solutions=30):
    df_solutions = df_solutions.drop(
        columns=[
            'frequencia', 
            'valor_pessimista', 
            'media',
            'valor_otimo',
            'valor_otimista',
        ])

    aux = df_solutions[df_solutions.porte.isin(portes)]
    df = pd.DataFrame()
    df['solutions'] = aux.columns[1:]
    
    if aux.shape[0] == 0:
        df[f'porte_{portes[0]}'] = aux.values[0][1:]
        df[f'porte_{portes[1]}'] = aux.values[1][1:]
    elif aux.shape[0] == 1:
        df[f'porte_{portes[0]}'] = aux.values[0][1:]
    else:
        return "error"    
    return df.nsmallest(total_solutions, columns=df.columns[1:], keep='first')

    
def receive_solutions(df_solutions, solutions_selected, frequencia, total_solutions=15):    
    receita = [sum(df_solutions[solutions_selected][s] * frequencia) for s in solutions_selected]
    df = pd.DataFrame(columns=['solutions', 'receita'])
    df['solutions'] = solutions_selected
    df['receita'] = receita  
    return df.sort_values(by=['receita'], ascending=False).head(total_solutions)


def dif_receita(max_receive, great_value, freq, n=5):
    max_receive['dif_receitas'] = max_receive.receita - sum(great_value * freq)
    return max_receive.nsmallest(n, columns='dif_receitas', keep='first')