"""
Clasificación usando k-NN
-----------------------------------------------------------------------------------------


"""
import pandas as pd


def pregunta_01():
    """
    Complete el código presentado a continuación.

    """
    # Lea el archivo de datos
    df = pd.read_csv("house-votes-84.csv", sep=",")

    # Cree un vector con la variable de respuesta ('party')
    y = df['party'].copy()

    # Extraiga las variables de entrada
    X = df.drop('party', axis=1).values

    # Importe el transformador OrdinalEncoder
    from sklearn.preprocessing import OrdinalEncoder

    # Transforme las variables de entrada usando fit_transform
    X = OrdinalEncoder().fit_transform(X)

    # Importe KNeighborsClassifier de sklearn.neighbors
    from sklearn.neighbors import KNeighborsClassifier
    
    # Cree un un clasificador k-NN con 6 vecinos
    knn = KNeighborsClassifier(n_neighbors=6)

    # Entrene el clasificador con el conjunto de entrenamiento
    knn.fit(X, y)

    # Retorne el score del clasificador
    return knn.score(X, y)


def pregunta_02():
    """
    Complete el código presentado a continuación.

    """
    # Lea el archivo de datos
    df = pd.read_csv("house-votes-84.csv", sep=",")

    # Cree un vector con la variable de respuesta ('party')
    y = ____

    # Extraiga las variables de entrada
    X = ____

    # Importe el transformador OrdinalEncoder
    from ____ import ____

    # Transforme las variables de entrada usando fit_transform
    X = ____().____(____)

    # Importe KNeighborsClassifier de sklearn.neighbors
    from ____ import ____
    

    # Cree un un clasificador k-NN con 6 vecinos
    knn = ____(____=____)

    # Entrene el clasificador con el conjunto de entrenamiento
    knn.____(____, ____)

    # Pronostique el resultado para el conjunto de entrenamiento
    y_pred = ____.____(____)

    # Importe la función confusion_matrix de sklearn.metrics
    from ____ import ____

    # Retorne la matriz de confusión
    return ____(____, ____)
