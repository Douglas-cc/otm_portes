# Proposta
Uma rede hospitalar deseja otimização para maximizar ganhos em negociação de portes cirurgicos com operadoras de planos de saúde, além disso, será necessario minimizar o desvio padrão da receita do porte da negociação com operadora para que conseguentemente os portes com valores de negociação baixos e frequencias (ou seja numero de vendas) altas possam aumentar um pouco e portes com valores altos e frequencia baixa possa diminuir. Por fim, mas não menos importante foi preciso criar duas restrições para pegar intervalos de receita total esperado para a negociação dos portes como podemos ver a baixo:

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
