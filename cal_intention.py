import numpy as np
import matplotlib.pyplot as plt

def softmax(z):

    new_z = np.zeros(z)

    total = 0

    for i in z:
        total += np.exp(i)

    for i in z:
        new_z[i] = np.exp(i) / total

    return new_z

def initialize(dim):

    alpha = np.zeros(shape = dim)
    alpha += np.random.normal(1, 0.3, (dim))
    return alpha

def propagate(X, alpha, P, num_iterations , learning_rate):

    y = X.shape[0]
    Pi = P[1]
    #正向传播
    W = alpha[0] + np.multiply(alpha[1],np.log(Pi[0])) + np.multiply(alpha[2],np.log(Pi[1])) + np.multiply(alpha[3],np.log(Pi[2]))
    A = np.sum(np.dot(np.dot(P[0], W.T), X),axis=1)
    loss = (- 1 / (3*y)) * np.sum((X[0] - A)**2)

    #反向传播
    dalpha0 = 2/(3*len(X))*(X[0] - A)*Pi[0]*X*(W**2)*(1-W)
    dalpha1 = 2/(3*len(X))*(X[0] - A)*Pi[0]*X*(W**2)*(1-W)*np.log(Pi[0])
    dalpha2 = 2/(3*len(X))*(X[0] - A)*Pi[0]*X*(W**2)*(1-W)*np.log(Pi[1])
    dalpha3 = 2/(3*len(X))*(X[0] - A)*Pi[0]*X*(W**2)*(1-W)*np.log(Pi[2])

    #创建一个字典，把dalpha保存起来。
    grads = {
                "dalpha0": dalpha0,
                "dalpha1": dalpha1,
                "dalpha2": dalpha2,
                "dalpha3": dalpha3,
             }
    return (grads , loss)

def optimize(X_train, alpha, P, Pi, num_iterations , learning_rate):

    costs = []

    for i in range(num_iterations):

        grads, loss = propagate(X_train, alpha, Pi, num_iterations , learning_rate)

        dalpha0 = grads["dalpha0"]
        dalpha1 = grads["dalpha1"]
        dalpha2 = grads["dalpha2"]
        dalpha3 = grads["dalpha3"]

        alpha0 = alpha[0] - learning_rate * dalpha0
        alpha1 = alpha[1] - learning_rate * dalpha1
        alpha2 = alpha[2] - learning_rate * dalpha2
        alpha3 = alpha[3] - learning_rate * dalpha3

        #记录成本
        if i % 100 == 0:
            costs.append(loss)

    params  = {
                "alpha0" : alpha0,
                "alpha1" : alpha1,
                "alpha2" : alpha2,
                "alpha3" : alpha3, }
    return (params, costs)

def predict(alpha0, alpha1, alpha2, alpha3, X, Pi):
    W = alpha0 + np.multiply(alpha1,np.log(Pi[1][0])) + np.multiply(alpha2,np.log(Pi[1][1])) + np.multiply(alpha3,np.log(Pi[1][2]))
    A = np.dot(np.sum(Pi[0],axis=0).reshape(3,80),W.T)
    A = np.sum(A, axis=-1)
    A = np.sum(np.dot(X, A),axis=1)
    return A

def model(X_train , Pi_train, Y_train , X_test , Pi_test, Y_test, num_iterations = 2000 , learning_rate = 0.1 , print_cost = False):

    alpha = initialize((4, X_train.shape[1], 3))
    params, costs = optimize(X_train, alpha, Pi_train[0], Pi_train[1], num_iterations , learning_rate)

    #从字典“参数”中检索参数w和b
    alpha0, alpha1, alpha2, alpha3 = params["alpha0"] , params["alpha1"], params["alpha2"], params["alpha3"]

    #预测测试/训练集的例子
    Y_prediction_test = predict(alpha0, alpha1, alpha2, alpha3, X_test, Pi_test)
    Y_prediction_train = predict(alpha0, alpha1, alpha2, alpha3, X_train, Pi_train)

    #打印训练后的准确性
    print("训练集准确性："  , format(100 - np.mean(np.abs(Y_prediction_train - Y_train)) * 100) ,"%")
    print("测试集准确性："  , format(100 - np.mean(np.abs(Y_prediction_test - Y_test)) * 100) ,"%")

    return alpha

X_train = np.zeros(shape=[180, 80, 3])
Y_train = np.zeros(shape=[180, 3])
X_test = np.zeros(shape=[20, 80, 3])
Y_test = np.zeros(shape=[20, 3])
Pi_train = np.zeros(shape=[2, 4, X_train.shape[1], X_train.shape[2]])
Pi_test = np.zeros(shape=[2, 4, X_test.shape[1], X_test.shape[2]])
#数据集来自于中经数据，为保障数据来源方的隐私，这里去掉了敏感数据。

d = model(X_train , Pi_train, Y_train , X_test , Pi_test, Y_test, num_iterations = 2000, learning_rate = 0.1, print_cost = True)
