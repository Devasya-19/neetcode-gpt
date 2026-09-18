import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        pass
        # maxi=np.max(z)
        # sum=0
        # for i in range(len(z)):
        #     sum+=np.exp(z[i]-maxi)
        # y=np.exp(z-maxi)/sum
        # return np.round(y,4)
        maxi=np.max(z)
        exp_z=np.exp(z-maxi)
        s_max=exp_z/np.sum(exp_z)
        return np.round(s_max,4)

