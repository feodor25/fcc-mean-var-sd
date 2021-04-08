import numpy as np

def calculate(list):
    try:
        matrix = np.array(list).reshape(3,3)

    except :
      raise ValueError("List must contain nine numbers!")
    
    sum_row = np.sum(matrix, axis = 0).tolist()
    sum_column = np.sum(matrix, axis = 1).tolist()
    sum_all = np.sum(matrix).tolist()

    mean_row = np.mean(matrix, axis = 0).tolist()
    mean_column = np.mean(matrix, axis = 1).tolist()
    mean_all = np.mean(matrix).tolist()

    var_row = np.var(matrix, axis = 0).tolist()
    var_column = np.var(matrix, axis = 1).tolist()
    var_all = np.var(matrix).tolist()

    std_row = np.std(matrix, axis = 0).tolist()
    std_column = np.std(matrix, axis = 1).tolist()
    std_all = np.std(matrix).tolist()

    max_row = np.max(matrix, axis = 0).tolist()
    max_column = np.max(matrix, axis = 1).tolist()
    max_all = np.max(matrix).tolist()

    min_row = np.min(matrix, axis = 0).tolist()
    min_column = np.min(matrix, axis = 1).tolist()
    min_all = np.min(matrix).tolist()

    calculations = {
      'mean': [mean_row, mean_column, mean_all],
      'variance': [var_row, var_column, var_all],
      'standard deviation': [std_row, std_column, std_all],
      'max': [max_row, max_column, max_all],
      'min': [min_row, min_column, min_all],
      'sum': [sum_row, sum_column, sum_all]
    }
    return calculations
calculate([24,75,3,56,87,649,2,76,78])

