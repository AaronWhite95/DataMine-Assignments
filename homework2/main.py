from data import Data
from config import dataset_table_name

if __name__ == "__main__":
    data = Data()
    # 处理数据集的标称属性
    data.process_nom_features(data.dataset_nom_feature_list, dataset_table_name)