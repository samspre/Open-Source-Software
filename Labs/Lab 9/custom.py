from __future__ import absolute_import, division, print_function

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
from PIL import Image
from PIL import ImageOps

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
import glob, os

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

# plt.figure()
# plt.imshow(train_images[0])
# plt.colorbar()
# plt.grid(False)
# plt.show()

# train_images = train_images / 255.0
# test_images = test_images / 255.0

size = 28, 28

im1 = Image.open("images/shirt1.jpg")
im2 = Image.open("images/shirt2.jpg")
im3 = Image.open("images/shoes.jpg")

im1.thumbnail(size)
im2.thumbnail(size)
im3.thumbnail(size)

shirt1Processed = ImageOps.grayscale(im1)
shirt1Processed = ImageOps.invert(shirt1Processed)

shirt2Processed = ImageOps.grayscale(im2)
shirt2Processed = ImageOps.invert(shirt2Processed)

shoesProcessed = ImageOps.grayscale(im3)
shoesProcessed = ImageOps.invert(shoesProcessed)

images = []
images.append(shirt1Processed)
images.append(shirt2Processed)
images.append(shoesProcessed)

# for img in images:
#     plt.imshow(img, cmap=plt.cm.binary)

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# model.fit(train_images, train_labels, epochs=5)

# test_loss, test_acc = model.evaluate(test_images, test_labels)
# print('Test accuracy:', test_acc)

predictions = model.predict(test_images)
np.argmax(predictions[0])

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

for i in range(0, len(images)):
    plt.figure(figsize=(6,3))
    plt.subplot(1,2,1)
    plot_image(i, predictions, test_labels, images)
    plt.subplot(1,2,2)
    plot_value_array(i, predictions, test_labels)
    plt.show()


# Plot the first X test images, their predicted label, and the true label
# Color correct predictions in blue, incorrect predictions in red
num_rows = 1
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
  plt.subplot(num_rows, 2*num_cols, 2*i+1)
  plot_image(9000+i, predictions, test_labels, test_images)
  plt.subplot(num_rows, 2*num_cols, 2*i+2)
  plot_value_array(9000+i, predictions, test_labels)
plt.show()

# # Grab an image from the test dataset
img = images[0]
print(img.shape)

# Add the image to a batch where it's the only member.
img = (np.expand_dims(img,0))
print(img.shape)


predictions_single = model.predict(img)
print(predictions_single)

plot_value_array(0, predictions_single, test_labels)
plt.xticks(range(10), class_names, rotation=45)
plt.show()

prediction_result = np.argmax(predictions_single[0])
print(prediction_result)
