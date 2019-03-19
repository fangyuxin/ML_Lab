import numpy as np

def train(theta, x, y):
    NotFinish = True
    while NotFinish:
        m = 0
        for i in range(len(x)):
            if y[i]*np.dot(theta, x[i]) <= 0:
                theta = theta + y[i]*x[i]
                m = m + 1
        if m == 0: NotFinish = False

    return theta


def predit(theta, x, y):
    print(theta)
    for i in range(len(x)):
        print(np.dot(theta, x[i]))


x = np.array([[1,1],
            [1, 1.1],
            [1, 1.2],
            [-1, -1]])

y = np.array([1, 1, 1, -1])

theta = np.array([0, 0])

theta = train(theta, x, y)
predit(theta, x, y)





