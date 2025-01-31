"""
Ledetekst: Jeg vil ha et nevralt nettverk som med 1 input-node, to i skjult lag og en output-node
Nettverket skal tilpasses et datasett som er slik at input er mellom 0 og 1 og output skal teoretisk sett være lik 4x(x-1). Jeg trenger et program der jeg kan finne vekter og bias og stille inn for denne situasjonen. Python, tensorflow
"""
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Generere datasett
def generate_data(samples=1000):
    X = np.linspace(0, 1, num=samples)  # Input mellom 0 og 1
    y = 4 * X * (X - 1)                 # Output = 4x(x-1)
    return X, y

# Lage treningsdata
X, y = generate_data()

# Bygge nevralt nettverk
model = keras.Sequential([
    layers.Input(shape=(1,)),                # 1 input-node
    layers.Dense(10, activation='relu'),      # Første skjulte lag med 10 noder
    layers.Dense(10, activation='relu'),      # Andre skjulte lag med 10 noder
    layers.Dense(1)                           # 1 output-node
])

# Kompilere modellen
model.compile(optimizer='adam', loss='mean_squared_error')

# Trene modellen
model.fit(X, y, epochs=1000, verbose=0)

# Forutsi verdier for å se hvordan modellen presterer
predictions = model.predict(X)

# Sammenligne med faktiske verdier
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.scatter(X, y, label='Faktiske verdier', color='red')
plt.scatter(X, predictions, label='Prediksjoner', color='blue', alpha=0.5)
plt.title('Nevralt Nettverk Prediksjoner')
plt.xlabel('Input (x)')
plt.ylabel('Output (4x(x-1))')
plt.legend()
plt.grid()
plt.show()