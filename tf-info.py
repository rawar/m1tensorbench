import tensorflow as tf
tf.debugging.set_log_device_placement(True)
print('tensorflow version:',tf.__version__)
tf.config.run_functions_eagerly(False)
print(tf.executing_eagerly())
