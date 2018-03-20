# -*- coding: UTF-8 -*-

# 使用图（graph）表示计算任务
# 在会话（Session）的上下文（context）中执行图
# 使用tensor表示数据
# 通过变量（Variable）维护状态
# 使用feed和fetch为任意操作赋值或从中获取数据

import tensorflow as tf

# 创建一个常量op，产生一个1x2矩阵
# 作为一个节点加到默认图
# 构造器的返回值代表该常量op的返回值
m1 = tf.constant([[3., 3.]])

# 创建另一个op，产生一个2x1矩阵
m2 = tf.constant([[2.], [2.]])

# 创建一个矩阵乘法
# 返回矩阵乘法结果
m = tf.matmul(m1, m2)

# 启用图并执行运算
with tf.Session() as sess:
    print('hello, tensorflow!')
    print(sess.run(m))
    

# 变量
state = tf.Variable(0, name='counter')

one = tf.constant(1)
new_value = tf.add(state, one)
update = tf.assign(state, new_value)

init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    print('hello, tensorflow!')
    sess.run(init_op)
    print(sess.run(state))
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))


# Fetch 取回操作
input1 = tf.constant(3.0)
input2 = tf.constant(2.0)
input3 = tf.constant(5.0)

inter = tf.add(input1, input3)
mul = tf.multiply(input2, inter)
with tf.Session() as sess:
    print('hello, tensorflow!')
    print(sess.run([mul, inter]))


# Feed 负值操作
input1 = tf.placeholder(tf.float32)
input2 == tf.placeholder(tf.float32)
output = tf.multiply(input1, input2)
with tf.Session() as sess:
    print('hello, tensorflow!')
    print(sess.run([output], feed_dict={input1:7., input2:2.}))

