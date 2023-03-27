[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10637529&assignment_repo_type=AssignmentRepo)
# Lista de Exercícios 00 - Lembra De Python?

## Objetivos:

Lembrar de alguns conceitos básicos da linguagem *Python*, com o foco nos requisitos da disciplina de Estrutura de Dados e Algoritmos. Sejam eles:

* Vetores,
* Funções e passagem de parâmetros.

## Exercícios:

1. Codifique um programa em *Python* que gere um vetor com valores inteiros, preenchido em ordem crescente, e imprima seu conteúdo. O numero de valores e seu intervalo devem ser fornecidos pelo usuário, via linha de comando. Por exemplo:

	<prompt>$ programa01 20 10 100

chama na linha de comando o seu programa (no exemplo chamado `programa01`) indicando que o vetor a ser gerado deve conter 20 valores dentro do intervalo `[10, 100]`.

Caso os parâmetros não sejam fornecidos seu programa deve gerar valores *default* (a sua escolha).  Além disso os valores fornecidos devem ser verificados se são válidos, por exemplo não faz sentido a quantidade de elementos ser 0 ou um valor negativo. 

2. Modifique o programa do exercício anterior para que outra opção de preenchimento do vetor seja aceita: ordem decrescente. Sendo outra possibilidade, o usuário também poderá, via linha de comando, indicar qual a opção de preechimento será usada. Nesse caso a chamada do programa passa a ser, por exemplo: 

	<prompt>$ programa02 C 20 10 100

onde o primeiro parâmetro pode ser `C` ou `D` para, respectivamente, indicar ordem crescente ou decrescente de preenchimento. 

3. Extenda o programa do exercício 2 adicionando mais uma outra opção de preenchimento: valores aleatórios. Use o identificador `R` para essa opção. 

4. Usando o programa criado no exercício 3, estenda-o incluindo funções para:

	a. Calcular a média dos elementos do vetor;

	b. Calcular a variância do vetor;

	c. Calcular o desvio padrão do vetor;

	d. Calcular a soma dos seus elementos, estabelecendo um valor de salto entre eles. Ou seja, se o salto for de 2, sua função deve somar o primeiro, terceiro, quinto,... elementos do vetor;

	e. Inverter os elementos do vetor, ou seja, o primeiro troca de lugar com o último, o segundo com o ante-penultimo, e assim por diante;

	f. Modificar os elementos do vetor da seguinte forma: todo elemento de indice par, e que contenha um numero par, deve ser substituido por -1, enquanto que elementos de indice impar, que contenham numeros ímpares, devem ser substituidos por 1. 

## Observações Gerais:

- Não utilize pacotes externos ou métodos prontos da classe vetor. Tente elaborar os algoritmos usando as estruturas de controle da própria linguagem *Python* [^1];
- Procure utilizar ao máximo funções, com a escolha adequada de parametros de entrada e saída para torna-las o mais reutilizáveis possível. 

## Referências Bibliográficas:

- Canning, J., Broder, A., Lafore, R., **Data Structures & Algorithms in Python**. Addison-Wesley. 2022. 
- Karumanchi, N. , **Data Structures And Algorithmic - Thinking With Python**. CareerMonk Publications. 2020.
- Goodrich,M.T., Tamassia, R., Goldwasser, M.H.. **Data Structures and Algorithms in Python**. John Wiley & Sons, Inc. 2012.
- John Sturtz, [**Defining Your Own Python Function**](https://realpython.com/defining-your-own-python-function/).

[^1]: As operações de entrada e saída e geração de numeros aleatórios são exceção.