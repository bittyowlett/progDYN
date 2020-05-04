import numpy as np
import matplotlib.pyplot as plt

def drawArrow(A, B):
    plt.arrow(A[0], A[1], B[0] - A[0], B[1] - A[1], head_width=1, length_includes_head=True)

A1=np.array([10,23])
A2=np.array([20,30])
A3=np.array([45,78])
drawArrow(A1,A2);
drawArrow(A2,A3);
plt.xlim([0, 100])
plt.ylim([0, 100])
plt.show();

