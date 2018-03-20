import numpy as np

num_points = 1000
vectors_set = []
for i in range(num_points):
    x1 = np.random.normal(0.0, 0.55)
    y1 = x1 * 0.1 + 0.3 + np.random.normal(0.0, 0.03)
    vectors_set.append([x1, y1])
    
x_data = [v[0]for v in vectors_set]
y_data = [v[1]for v in vectors_set]

import matplotlib.pyplot as plt

# Graphic display
fig = plt.figure()  
ax = fig.add_subplot(1, 1, 1)  
ax.scatter(x_data, y_data)  
plt.ion()  # 不让show() block  
plt.show()

import tensorflow as tf

W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))
y = W * x_data + b

loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init)
    for step in range(18):
        sess.run(train)
        print(step, sess.run(W), sess.run(b))
        print(step, sess.run(loss))
        
        # Graphic display
        try:  
            ax.lines.remove(lines[0])  # lines建一个抹除一个  
        except Exception:  
            pass
        
        lines = ax.plot(x_data, sess.run(W) * x_data + sess.run(b), 'r-', lw=5)  # x_data X轴，prediction_value Y轴，'r-'红线，lw=5线宽5  
        plt.pause(0.1)  # 暂停0.1秒  
    plt.pause(1)

