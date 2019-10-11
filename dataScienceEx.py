from matplotlib import pyplot as plt
from collections import Counter 

# Exercicio 2 08/outubro
#1. Construa um gráfico de linha que mostra o número de amigos por usuário.
num_amigos_por_id = [(0, 2), (1, 3), (2, 3), (3, 3), (4, 2), (5, 3), (6, 2), (7, 2), (8, 3), (9, 1)]
l1 = [ i[0] for i in num_amigos_por_id] 
l2 = [ i[1] for i in num_amigos_por_id] 
#plt.plot (l1, l2, color='green', marker='o', linestyle='solid') 
#plt.title ("Id Usuário X Num Amigos")   
#plt.xlabel ("Id do Usuário")
#plt.xticks ([i for i in range (11)])
#plt.ylabel ("Qtde Amigos")
#plt.yticks ([i for i in range (5)])
#plt.show()

# 2 Construa um gráfico de linha que mostra o número médio de amigos por usuário.

# 3 Construa um gráfico de dispersão envolvendo salário e tempo de experiência.
salarios_experiencia = [
    (83000, 8.7), (88000, 8.1),
    (48000, 0.7), (76000, 6),
    (69000, 6.5), (76000, 7.5),
    (60000, 2.5), (83000, 10),
    (48000, 1.9), (63000, 4.2)
]
l1 = [ i[0]/1000 for i in salarios_experiencia]
l2 = [ i[1] for i in salarios_experiencia]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#plt.scatter (l1, l2)
#for label, l1_count, l2_count in zip(labels, l1, l2):
#    plt.annotate(
#        label,
#        xy = (l1_count,l2_count),
#        xytext = (-5, 5),
#        textcoords = 'offset points'
#    )
#plt.title ("Salário X Tempo de Experiência")
#plt.xlabel ("Salário em R$ mil")
#plt.ylabel ("Tempo de Experiência")
#plt.show()

# 4 Construa um histograma envolvendo dados de pagantes e não pagantes.
experiencia_tipo_conta = [
    (0.7, 'paga'),
    (1.9,'não_paga'),
    (2.5,'paga'),
    (4.2,'não_paga'),
    (6,'não_paga'),
    (6.5,'não_paga'),
    (7.5,'não_paga'),
    (8.1,'não_paga'),
    (8.7,'paga'),
    (10,'paga')
]
l1 = [i[0] for i in experiencia_tipo_conta if (i[1] == "paga")]
#quartil = lambda grade: grade // 2.5001
#histograma = Counter(quartil (grade) for grade in l1 )
#plt.bar (
#    [
#        x for x in histograma.keys()
#    ],
#    histograma.values(),
#    .7
#)
#plt.title ("Usuário Pagantes")
#plt.xlabel ("Quartil")
#plt.axis ([-1, 5, 0, 4])
#plt.xticks ([i for i in range (5)])
#plt.ylabel ("Número de Pagantes")
#plt.show()

#  5 Construa um histograma de palavras em interesses. Por exemplo, a palavra 
# learning pode aparecer em machine learning e em deep learning. Quebre cada 
# interesse em palavras para fazer a contagem e montar o histograma.
interesses = [
(0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"), (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
(1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"), (1, "Postgres"), 
(2, "Python"), (2, "scikit-learn"), (2, "scipy"), (2, "numpy"), (2, "statsmodel"), (2, "pandas"), 
(3, "R"), (3, "Python"), (3, "statistics"), (3, "regression"), (3, "probability"),
(4, "machine learning"), (4, "regression"), (4, "decision trees"), (4, "libsvm"), 
(5, "Python"), (5, "R"),(5, "Java"), (5, "C++"), (5, "Haskell"), (5, "programming languages"), 
(6, "theory"),
(7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),(7, "neural networks"), 
(8, "neural networks"), (8, "deep learning"), (8, "Big Data"), (8, "artificial intelligence"), (8, "Hadoop"),
(9, "Java"), (9, "MapReduce"), (9, "Big Data"),
]
frequencia_palavras = Counter (
    palavra
    for usuario, assunto in interesses
    for palavra in assunto.lower().split()
)

d1 = [ e for e in frequencia_palavras.items() if e[1] > 1 ]

plt.bar (
    [
        palavra[0] for palavra in d1
    ],
    [
        palavra[1] for palavra in d1
    ],
    .8
)
plt.title ("Tecnologias com mais citações")
plt.axis ([-0.5, 13.5, 1, 4])
plt.xticks ([i for i in range(14)])
plt.xlabel ("Tecnologia")
plt.yticks ([i for i in range(4)])
plt.ylabel ("Número de citações")
plt.show()

