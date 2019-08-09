from __future__ import absolute_import, division, print_function

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
from PIL import Image
from PIL import ImageOps

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
import glob, os, cv2

print(tf.__version__)

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images.shape
len(train_labels)
train_labels
test_images.shape
len(test_labels)

im1 = Image.open("images/shirt1.jpg")
im2 = Image.open("images/shirt2.jpg")
im3 = Image.open("images/shoes.jpg")

im1 = im1.convert(mode = 'L')
im1 = im1.resize((28, 28))
im1 = ImageOps.invert(im1)

im2 = im2.convert(mode = 'L')
im2 = im2.resize((28, 28))
im2 = ImageOps.invert(im2)

im3 = im3.convert(mode = 'L')
im3 = im3.resize((28, 28))
im3 = ImageOps.invert(im3)

im1.save("images/shirt1Processed.jpg")
im2.save("images/shirt2Processed.jpg")
im3.save("images/shoesProcessed.jpg")

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

def plot_image(i, predictions_array, true_label, img):
  predictions_array, true_label, img = predictions_array[i], true_label[i], images[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])

  plt.imshow(img, cmap=plt.cm.binary)

  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'

  plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)

def plot_value_array(i, predictions_array, true_label):
  predictions_array, true_label = predictions_array[i], true_label[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])
  thisplot = plt.bar(range(10), predictions_array, color="#777777")
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')


im1 = np.array(im1)
im2 = np.array(im2)
im3 = np.array(im3)

im1 = (np.expand_dims(im1, 0))
im2 = (np.expand_dims(im2, 0))
im3 = (np.expand_dims(im3, 0))

images = np.empty((1,3))

images = np.append(images, im1)
images = np.append(images, im2)
images = np.append(images, im3)

pred1 = model.predict(im1)
pred2 = model.predict(im2)
pred3 = model.predict(im3)

predictions = []
predictions.append(pred1)
predictions.append(pred2)
predictions.append(pred3)


print("\nPredictions")

print(np.argmax(pred1), class_names[np.argmax(pred1)], end = '\n')
print(pred1, end = '\n')
plot_value_array(0, pred1, test_labels)
plt.xticks(range(10), class_names, rotation=45)

print(np.argmax(pred2), class_names[np.argmax(pred2)], end = '\n')
print(pred2, end = '\n')
plot_value_array(0, pred2, test_labels)
plt.xticks(range(10), class_names, rotation=45)

print(np.argmax(pred3), class_names[np.argmax(pred3)], end = '\n')
print(pred3, end = '\n')
plot_value_array(0, pred3, test_labels)
plt.xticks(range(10), class_names, rotation=45)

# Plot the first X test images, their predicted label, and the true label
# Color correct predictions in blue, incorrect predictions in red
# num_rows = 1
# num_cols = 3
# num_images = num_rows*num_cols
# plt.figure(figsize=(2*2*num_cols, 2*num_rows))
# for i in range(0, len(images)):
#   plt.subplot(num_rows, 2*num_cols, 2*i+1)
#   plot_image(i, predictions, test_labels, images[i])
#   plt.subplot(num_rows, 2*num_cols, 2*i+2)
#   plot_value_array(i, predictions, test_labels)
# plt.show()
