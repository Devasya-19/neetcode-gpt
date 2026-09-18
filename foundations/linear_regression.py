import numpy as np
from numpy.typing import NDArray

class Solution:

    def get_model_prediction(self, X: NDArray[np.float64], weights: NDArray[np.float64]) -> NDArray[np.float64]:
        # X is (n, m), weights is (m,) -> return (n,) predictions
        # Round to 5 decimal places
        pass
        y_pred=np.dot(X,weights)
        return np.round(y_pred,5)

    def get_error(self, model_prediction: NDArray[np.float64], ground_truth: NDArray[np.float64]) -> float:
        # Compute mean squared error between predictions and ground truth
        # Round to 5 decimal places
        pass
        y_pred=model_prediction.copy()
        y_true=ground_truth.copy()
        error=(np.sum(np.pow((y_pred-y_true),2)))/len(y_true)
        return np.round(error,5)
