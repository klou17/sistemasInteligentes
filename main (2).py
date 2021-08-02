import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

if __name__ == '__main__':
    data = pd.read_csv("Wholesale customers data.csv")
    # print(data.shape)
    # print(data.isnull().sum())
    # print(data.dtypes)
    indices = [22, 222, 253]
    samples = pd.DataFrame(data.loc[indices],
                           columns=data.keys()).reset_index(drop=True)
    data = data.drop(indices, axis=0)
    data = data.drop(['Fresh', 'Milk'], axis=1, )
    samples = samples.drop(['Fresh', 'Milk'], axis=1, )
    data_scaled = preprocessing.Normalizer().fit_transform(data)
    sample_scaled = preprocessing.Normalizer().fit_transform(samples)
    inercia = []
    x = data_scaled
    for i in range(2, 100):
        algoritmo = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10)
        algoritmo.fit(x)
        inercia.append(algoritmo.inertia_)
    # plt.figure(figsize=[10, 6])
    # plt.title('Metodo del Codo')
    # plt.xlabel('N. de clusters')
    # plt.ylabel('Inercia')
    # plt.plot(list(range(1, 20)), inercia, marker='o')
    # plt.show()
    algoritmo = KMeans(n_clusters=6, init='k-means++',
                       max_iter=300, n_init=10)
    algoritmo.fit(x)

    centroides, etiquetas = algoritmo.cluster_centers_, algoritmo.labels_

    muestra_prediccion = algoritmo.predict(sample_scaled)

    for i, pred in enumerate(muestra_prediccion):
        print("Muestra ", i, " se encuentra en el cluster: ", pred)

    modelo_pca = PCA(n_components=2)
    modelo_pca.fit(x)
    pca = modelo_pca.transform(x)
    centroides_pca = modelo_pca.transform(centroides)
    colores = ['blue', 'red', 'green', 'orange', 'gray', 'brown']
    colores_cluster = [colores[etiquetas[i]] for i in range(len(pca))]
    plt.scatter(pca[:, 0], pca[:, 1], c=colores_cluster,
                marker='o', alpha=0.4)
    plt.scatter(centroides_pca[:, 0], centroides_pca[:, 1],
                marker='x', s=100, linewidths=3, c=colores)
    xvector = modelo_pca.components_[0] * max(pca[:, 0])
    yvector = modelo_pca.components_[1] * max(pca[:, 1])
    columnas = data.columns
    for i in range(len(columnas)):
        plt.arrow(0, 0, xvector[i], yvector[i], color='black',
                  width=0.0005, head_width=0.02, alpha=0.75)
        plt.text(xvector[i], yvector[i], list(columnas)[i], color='black',
                 alpha=0.75)
    plt.show()