import numpy as np
import pandas as pd

info = {
    "Model_Name": ["BART", "T5", "Pegasus", "DistilBART"],
    "Metric_A": [0.85, 0.88, 0.86, 0.83],
    "Metric_B": [120, 150, 110, 100],
    "Metric_C": [500, 400, 600, 350],
    "Metric_D": [0.87, 0.89, 0.88, 0.84]
}

data_frame = pd.DataFrame(info)
print("Initial Data:")
print(data_frame)

def scale_values(data, positive_criteria):
    adjusted_data = data.copy()
    for column in data.columns[1:]:
        if column in positive_criteria:
            adjusted_data[column] = data[column] / np.sqrt(np.sum(data[column] ** 2))
        else:
            adjusted_data[column] = np.sqrt(np.sum(data[column] ** 2)) / data[column]
    return adjusted_data

criteria_weights = np.array([0.4, 0.2, 0.2, 0.2])
positive_criteria = ["Metric_A", "Metric_D"]

adjusted_data = scale_values(data_frame.drop(columns=["Model_Name"]), positive_criteria)
print("\nScaled Data:")
print(adjusted_data)

weighted_data = adjusted_data * criteria_weights
print("\nWeighted Data:")
print(weighted_data)

optimal_best = weighted_data.max()
optimal_worst = weighted_data.min()

dist_best = np.sqrt(((weighted_data - optimal_best) ** 2).sum(axis=1))
dist_worst = np.sqrt(((weighted_data - optimal_worst) ** 2).sum(axis=1))

score = dist_worst / (dist_best + dist_worst)

data_frame["Final_Score"] = score
data_frame["Position"] = data_frame["Final_Score"].rank(ascending=False)

print("\nFinal Rankings:")
print(data_frame.sort_values("Position"))