import tensorflow as tf
import numpy as np

# 生成训练数据 + 噪声，下面为了拟合 $$ Y = 2X $$ 
trX = np.linspace(-1, 1, 101)
trY = 2 * trX + np.random.randn(*trX.shape) * 0.33  # y=2x，但是加入了噪声

X = tf.placeholder("float")  # 输入输出符号变量
Y = tf.placeholder("float")

# 定义模型
def model(X, w):
    return tf.multiply(X, w)  # 线性回归只需要调用乘法操作即可。

# 模型权重 W 用变量表示
w = tf.Variable(0.0, name="weights")  # 共享变量
y_model = model(X, w)

# 定义损失函数
cost = (tf.pow(Y - y_model, 2))  # 平方损失函数

# 构建优化器，最小化损失函数。
train_op = tf.train.GradientDescentOptimizer(0.01).minimize(cost)

# 构建会话
sess = tf.Session()

# 初始化所有的符号共享变量
init = tf.global_variables_initializer()

# 运行会话
sess.run(init)

# 迭代训练
for i in range(100):
    for (x, y) in zip(trX, trY):
        sess.run(train_op, feed_dict={X: x, Y: y})
# 打印权重w
print(sess.run(w))
