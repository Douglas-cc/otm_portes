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
            st.subheader('Todas as soluções')    
            st.dataframe(generete_df_solution(output["res_x"]))

            st.subheader('Valores das funções objetivas')
            st.write(output["res_f"])

            st.subheader('Frente de Pareto')    
            graph = alg.frente_pareto(
                output["res_f"],
                input.media_cenario.values,
                input.media.values, 
                input.frequencia.values,
                input.valor_otimo.values
            )
            st.pyplot(graph)

        if st.checkbox('30 soluções que mais diminuiram o porte 7'):
            output = alg.nsga2(
                target_lower, 
                target_upper, 
                input.valor_pessimista.values, 
                input.valor_otimista.values, 
                input.frequencia.values, 
                input.media_cenario.values
            )
            df = pd.concat([input, generete_df_solution(output[0])], axis=1)  
            st.dataframe(smaller_sizes(df))


        if st.checkbox('Pegue as 15 maiores receitas das 30 soluções onde o porte 7 mais diminuiu'):
            output = alg.nsga2(
                target_lower, 
                target_upper, 
                input.valor_pessimista.values, 
                input.valor_otimista.values, 
                input.frequencia.values, 
                input.media_cenario.values
            )
            df = pd.concat([input, generete_df_solution(output[0])], axis=1)  
            filtro = smaller_sizes(df)

            st.dataframe(receive_solutions(df, filtro.solutions, df.frequencia))


        if st.checkbox("Das 15 maiores receitas, pegue as 5 soluções com menores diferenças positivas em relação aos valores otimos"):
            output = alg.nsga2(
                target_lower, 
                target_upper, 
                input.valor_pessimista.values, 
                input.valor_otimista.values, 
                input.frequencia.values, 
                input.media_cenario.values
            )

            df = pd.concat([input, generete_df_solution(output[0])], axis=1)  
            filtro = smaller_sizes(df)
            maiores_receitas = receive_solutions(df, filtro.solutions, df.frequencia)

            filtro_dif_receita = dif_receita(maiores_receitas, df.valor_otimo, df.frequencia)
            st.dataframe(filtro_dif_receita)

if __name__ == '__main__':
    main()