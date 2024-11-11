import tensorflow as tf
import numpy as np

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train / 255.
x_test = x_test / 255.

y_train = tf.one_hot(y_train, depth=10)
y_test = tf.one_hot(y_test, depth=10)
mnist_train_dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train)).shuffle(217).batch(32)
mnist_test_dataset = tf.data.Dataset.from_tensor_slices((x_test, y_test)).shuffle(217).batch(32)


class MLP:
    def __init__(self):
        # 修正后的隐藏层和输出层
        self.dense_mlp = tf.keras.layers.Dense(256, activation=tf.nn.relu)
        self.dense_last = tf.keras.layers.Dense(10, activation=tf.nn.softmax)


def __call__(self, inputs):
    train_inputs = inputs

    train_embedding = tf.reshape(train_inputs, [-1, 784])
    embedding = self.dense_mlp(train_embedding)
    logits = self.dense_last(embedding)
    return logits


train_inputs = tf.keras.Input(shape=(28, 28))
logits = MLP()(train_inputs)
model = tf.keras.Model(train_inputs, logits)

model.compile("SGD", loss="categorical_crossentropy", metrics=["accuracy"])
model.fit(mnist_train_dataset, epochs=10, validation_data=mnist_test_dataset)
