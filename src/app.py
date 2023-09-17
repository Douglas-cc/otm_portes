import numpy as np
import pandas as pd
import streamlit as st
from algorithms import Algorithms
from scripts import(
    upload_file,
    smaller_sizes,
    receive_solutions,
    dif_receita,
    generete_df_solution
)


alg = Algorithms()


def main():
    st.title('Negociação de Portes Cirurgicos')
    st.subheader('Upload da base de dados')    
    input = upload_file()   

    st.subheader('Dados de entrada')   
    st.dataframe(input)
    
    target_lower = st.number_input('Valor minímo de Receita: ')
    target_upper = st.number_input('Valor maxímo de Receita: ')


    if target_lower > 0 and target_upper > 0:
        if st.button('otimizar'):
            output = alg.nsga2(
                target_lower, 
                target_upper, 
                input.valor_pessimista.values, 
                input.valor_otimista.values, 
                input.frequencia.values, 
                input.media_cenario.values
            )
            st.subheader('Soluções Otimas')    
            st.dataframe(generete_df_solution(output["res_x"]))

            # st.subheader('Valores das funções objetivas')
            # st.write(output["res_f"])

            graph = alg.frente_pareto(
                output["res_f"],
                input.media_cenario.values,
                input.media.values, 
                input.frequencia.values,
                input.valor_otimo.values
            )
            st.pyplot(graph)
            
            


if __name__ == '__main__':
    main()