import tensorflow as tf
tf.enable_eager_execution()
print(tf.__version__)
print("EE enabled?", tf.executing_eagerly())