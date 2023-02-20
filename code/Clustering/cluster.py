import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import pandas as pd
from statistics import mode

#get the class name of a given object class id
def get_class_name(class_id, annotation_file):
    
    import json
    with open(annotation_file, 'r') as file:
        _data = json.load(file)
        _classes = _data["categories"]

        for category in _classes:
            if(category["id"] == class_id):
                return category["name"]

#get a dictionary with all object class ids and their names
def get_all_class_names(class_arr, annotation_file):

    classes = set(class_arr)
    all_class_names = {}

    for i in list(classes):
        cls_name = get_class_name(i, annotation_file)
        all_class_names[i] = cls_name
    return all_class_names


#get cluster names for the predicted kmeans cluster labels
def get_cluster_names(class_arr, label, all_class_names):
    clusters = {}
    for i in range(len(label)):
        cluster_id = label[i]
        cluster_name = all_class_names[class_arr[i]]
        
        if cluster_id not in clusters.keys():
            clusters[cluster_id] = []
            pass
        clusters[cluster_id].append(cluster_name)

    cluster_names = {}
    for i in clusters.keys():
        cluster_names[i] = mode(clusters[i])
    return cluster_names


#predict clusters for given objects
def pred_clusters(annotation_file, objects_arr, class_arr, pca_dim, k):
    data = np.array([x.numpy() for x in objects_arr], dtype=np.float32)
    pca = PCA(pca_dim)
    df = pca.fit_transform(data)
    kmeans = KMeans(n_clusters= k)
    label = kmeans.fit_predict(df)

    all_class_names = get_all_class_names(class_arr, annotation_file)
    cluster_names = get_cluster_names(class_arr, label, all_class_names)
    pred_clusters = {'true_cls_id' : [], 'true_cls_name' : [], 'pred_cluster_id' : [], 'pred_cluster_name' : []}

    for i in range(len(class_arr)):
        pred_clusters['true_cls_id'].append(class_arr[i])
        pred_clusters['true_cls_name'].append(all_class_names[class_arr[i]])
        pred_clusters['pred_cluster_id'].append('c' + str(label[i]))
        pred_clusters['pred_cluster_name'].append(cluster_names[label[i]])

    pred_cluster_df = pd.DataFrame(pred_clusters)
    return pred_cluster_df