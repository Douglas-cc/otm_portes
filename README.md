# Proposta
Uma rede hospitalar deseja usar u algoritmo de otimização para minimizar perda a fim de aumentar o ganhos em negociação de portes cirurgicos com operadoras de planos de saúde, além disso sera preciso minimizar o desvio padrão da receita dos portes a fim de balancear os valores dos portes, para que resolver o problema onde uma porte com frequencia baixa tenha valores muito altos e vice e versa

# Variaveis
**x = valores de negociação**
**mc = media cenario dos valores de negociação**
**li = limite inferior**
**ls = limite superior**
**m = media da população**
**N = tamanho da população**


# Funções Objetivas
Função de perda de receita e desvio padrão da receita por porte:

$$
f_1 = \sum{(mc - x) * frequencia}
$$

$$
f_2 = \sqrt{\frac{\sum{(1/receita - m)^2}}{N}}
$$



# Algumas restrições
Como desejamos limitar as soluções entre um intervalo de receita total da negociação foi criado as restrições de limite inferior (lower) limite superior (upper) de receita respectivamente:

$$
g_1 = li - \sum({frequencia * x })
$$

$$
g_2 = \sum({frequencia * x }) - ls
$$


# Click no video abaixo e veja o MVP da solução

[![IMAGE ALT TEXT HERE](https://img.olhardigital.com.br/wp-content/uploads/2021/03/shutterstock_1488096026_Easy-Resize.com_.jpg)](https://youtu.be/-X2qao8SEPs)
