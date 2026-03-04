# Telefone sem fio

Toda criança já brincou de "telefone sem fio". Joãozinho inventou uma variação da brincadeira.

O grupo de crianças é dividido em dois times. Os times se organizam como na brincadeira original, em que cada um repete o que lhe foi falado para o seguinte, até que o último diz o que chegou até ele. No caso da brincadeira de Joãozinho será falada uma frase com n caracteres (contando letras, espaços, sinais de pontuação, etc). Todos sabem que a frase tem este comprimento. A frase é falada pelo juiz ao primeiro competidor de cada time que a repete para o segundo, e este para o terceiro e assim sucessivamente, até que o último competidor de cada time escreve a frase final (garantindo que n caracteres sejam escritos) e a entrega para o juiz.

A equipe vencedora é aquela cuja frase final seja mais próxima da frase original. Para calcular a semelhança entre duas frases de mesmo comprimento você deve contar o número de vezes em que o caractere da frase do time coincide com o caractere da frase original. Ganha o time para o qual o número de coincidências seja máximo. Se os dois times empataram neste critério, a primeira vez que um dos times acertou e o outro errou decide.

Exemplo: Se a frase original foi "O rato roeu a roupa do rei.", o primeiro time escreveu "O ator morreu, garoupa rei." e o segundo time escreveu "O pato moeu garoupa dorlei." O segundo time ganhou pois teve 21 coincidências contra 9 coincidências do primeiro:

Assim como os juízes da Maratona de Programação, estes juízes são muitos preguiçosos. Logo, pediram para você escrever um programa que resolve este problema.

###### Entrada

A entrada começa com um inteiro t, onde 1 ≤ t ≤ 1000, indicando o número de instâncias que seu programa deve analisar.

Cada instância é composta por três linhas, na primeira a frase correta, na segunda a frase do primeiro time e na terceira a frase do segundo time. Cada frase tem no máximo 100 caracteres, e as frases possuem sempre o mesmo tamanho.

###### Saída

Para cada instância, você deverá imprimir um identificador Instancia k, onde k é o número da instância atual. Na linha seguinte você deve imprimir qual dos times foi o vencedor ou se houve empate. Após cada instância, seu programa deve imprimir uma linha em branco.