from __future__ import print_function, division
import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
from sklearn.cross_validation import train_test_split
import random

# 读取数据
data = pd.read_csv("datatraining.txt")
# 拆分数据
X_train, X_test, y_train, y_test = train_test_split(data[["Temperature", "Humidity", "Light", "CO2", "HumidityRatio"]].values, data["Occupancy"].values.reshape(-1, 1), random_state=42)
# one-hot 编码
y_train = tf.concat(1, [1 - y_train, y_train])
y_test = tf.concat(1, [1 - y_test, y_test])

# 设置模型
learning_rate = 0.001
training_epochs = 50
batch_size = 100
display_step = 1

n_samples = X_train.shape[0]
n_features = 5
n_class = 2
x = tf.placeholder(tf.float32, [None, n_features])
y = tf.placeholder(tf.float32, [None, n_class])

# 模型参数
W = tf.Variable(tf.zeros([n_features, n_class]))
b = tf.Variable(tf.zeros([n_class]))
# W = tf.Variable(tf.truncated_normal([n_features, n_class-1]))
# b = tf.Variable(tf.truncated_normal([n_class]))

# 定义模型，此处使用与线性回归一样的定义
# 因为在后面定义损失的时候会加上映射
pred = tf.matmul(x, W) + b

# 定义损失函数
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(pred, y))
# cost = tf.nn.sigmoid_cross_entropy_with_logits(pred, y)

# 梯度下降
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# 准确率
correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# 初始化所有变量
init = tf.initialize_all_variables()

# 训练模型
with tf.Session() as sess:
    sess.run(init)
    for epoch in range(training_epochs):
        avg_cost = 0
        total_batch = int(n_samples / batch_size)
        for i in range(total_batch):
            _, c = sess.run([optimizer, cost], 
                            feed_dict={x: X_train[i * batch_size : (i+1) * batch_size], 
                                      y: y_train[i * batch_size : (i+1) * batch_size, :].eval()})
            avg_cost = c / total_batch
        plt.plot(epoch+1, avg_cost, 'co')

        if (epoch+1) % display_step == 0:
            print("Epoch:", "%04d" % (epoch+1), "cost=", avg_cost)

    print("Optimization Finished!")

    print("Testing Accuracy:", accuracy.eval({x: X_train, y:y_train.eval()}))
    plt.xlabel("Epoch")
    plt.ylabel("Cost")
    plt.show()