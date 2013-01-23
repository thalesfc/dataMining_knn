dataMining_knn
==============

A Python implementation of the KNN algorithm proposed for the course of Data Mining @ UFMG.

=============

* Executando o código:

$ cd src/

$ python knn.py -i ../data/imdb_train -t ../data/imdb_test -k 7


* Parâmetros:

  -i <arquivo de treino>

  -t <arquivo de teste>

  -k <numero de vizinhos>

  -s <stopwords> : caminho para o arquivo com as stopwords, se não passar não há remoção de stopwords

  -d <distância>  : euclidean, cosine, jaccard, hamming, manhattan, correlation

  -m <percentage> : porcentagem do treino a ser utilizada, e. g., -m 0.1 usa 10% do treino
