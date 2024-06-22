# -*- coding: utf-8 -*-
from tkinter import messagebox

import cv2
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
from keras.src.saving import load_model


import tkinter as tk
import cv2
import numpy as np
from keras.models import load_model


def tahmin_harf():
    model = load_model('my_model.h5')

    image = cv2.imread('oo_harf.png', cv2.IMREAD_GRAYSCALE)  # Load image in grayscale
    image = cv2.resize(image, (32, 32))  # Resize image
    inputdata = image.reshape(-1, 32, 32, 1).astype('float32') / 255.0  # Normalize etme

    predictions = model.predict(inputdata)
    predicted_class_index = np.argmax(predictions)

    labels = ['A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'Ğ', 'H', 'I', 'İ', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'P',
              'R',
              'S', 'Ş', 'T', 'U', 'Ü', 'V', 'Y', 'Z']
    predicted_class = labels[predicted_class_index]
    etiket.config(text=predicted_class)


root = tk.Tk()
root.title("Harf Tahmin Projesi")


button = tk.Button(root, text="Tahmin Et", command=tahmin_harf)
button.pack(pady=10)
etiket = tk.Label(root, text="")
etiket.pack()

label_sonuc = tk.Label(root, text="")
label_sonuc.pack()


root.mainloop()