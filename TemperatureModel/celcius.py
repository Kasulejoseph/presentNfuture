from __future__ import absolute_import, division, print_function
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
#logging errors
tf.logging.set_verbosity(tf.logging.ERROR)
# features/inputs
celsius_q = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
#labels/outputs
fahrenheit_a = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)
for i, c in enumerate(celsius_q):
    print("{} degrees Celsius = {} degrees Fahrenheit".format(c, fahrenheit_a[i]))

#input_shape=[1] --> input layer in a single value
#units=1 --> number of neurons in the layer
IO = tf.keras.layers.Dense(units=1, input_shape=[1])

#assemble layer into a model
model = tf.keras.Sequential([IO])

#Loss function - A way of measuring how far off preditions are from the desired outcome.
#optimizer function - Away of adjusting internal values in order to reduce the loss.
model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.1))
#train the model
history = model.fit(celsius_q, fahrenheit_a, epochs=600, verbose=False)
print('Finished training model')
# plot
plt.xlabel('Rpoch  Number')
plt.ylabel('Loss Magnitude')
plt.plot(history.history['loss'])
print(model.predict([1000.0]))
plt.show()