import tensorflow as tf
input = tf.Variable(tf.random.normal([1, 3, 3, 1]))
conv = tf.keras.layers.Conv2D(1,2)(input)
print(conv)
