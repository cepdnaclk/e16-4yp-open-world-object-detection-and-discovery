from crop_features import crop_features
from cluster import pred_clusters
from sklearn.metrics import accuracy_score
from sklearn.metrics import adjusted_rand_score as ari_score
from sklearn.metrics import rand_score
from sklearn.metrics.cluster import normalized_mutual_info_score as nmi_score


annotation_file = './datasets/t1_train/t1_train_coco.json'
image_dir = './data/coco/images'
objects_arr, class_arr, img_id_arr, bbox_arr = crop_features(annotation_file, image_dir, FH = 384, FW = 600)

pred_cluster_df = pred_clusters(annotation_file, objects_arr, class_arr, pca_dim=2, k = 45)
print("cluster prediction accuracy :", accuracy_score(pred_cluster_df['true_cls_name'], pred_cluster_df['pred_cluster_name']))
print("rand_score :", rand_score(pred_cluster_df['true_cls_name'], pred_cluster_df['pred_cluster_name']))
print("adjusted_rand_score :", ari_score(pred_cluster_df['true_cls_name'], pred_cluster_df['pred_cluster_name']))
print("normalized_mutual_info_score :", nmi_score(pred_cluster_df['true_cls_name'], pred_cluster_df['pred_cluster_name']))