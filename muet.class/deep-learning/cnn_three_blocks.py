"""
CNN Assignment: 2-block demo model vs 3-block model.

Dataset: Fashion-MNIST (28x28 grayscale, 10 classes) — loaded straight from
keras.datasets so no external files are needed.
"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, callbacks

# ---------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------
(x_train, y_train), (x_test, y_test) = keras.datasets.fashion_mnist.load_data()

x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

early_stop = callbacks.EarlyStopping(
    monitor="val_loss", patience=3, restore_best_weights=True
)

# ---------------------------------------------------------------------------
# Demo model: 2x (Conv2D + MaxPooling2D) blocks
# ---------------------------------------------------------------------------
demo_model = keras.Sequential([
    layers.Input(shape=(28, 28, 1)),
    layers.Conv2D(32, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation="relu"),
    layers.Dense(10, activation="softmax"),
], name="demo_2block")

demo_model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
)

demo_model.summary()

demo_history = demo_model.fit(
    x_train, y_train,
    validation_split=0.1,
    epochs=20,
    batch_size=64,
    callbacks=[early_stop],
    verbose=2,
)

demo_loss, demo_acc = demo_model.evaluate(x_test, y_test, verbose=0)

# ---------------------------------------------------------------------------
# TODO 1: Add a third Conv2D + MaxPooling2D block.
# Same as the demo model, but with a THIRD Conv2D(128, (3,3), activation="relu")
# layer inserted just before Flatten (no MaxPooling after it, since the feature
# map is already small by that point).
# ---------------------------------------------------------------------------
three_block_model = keras.Sequential([
    layers.Input(shape=(28, 28, 1)),
    layers.Conv2D(32, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation="relu"),
    layers.Flatten(),
    layers.Dense(64, activation="relu"),
    layers.Dense(10, activation="softmax"),
], name="three_block")

three_block_model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
)

three_block_model.summary()

three_block_history = three_block_model.fit(
    x_train, y_train,
    validation_split=0.1,
    epochs=20,
    batch_size=64,
    callbacks=[early_stop],
    verbose=2,
)

three_block_loss, three_block_acc = three_block_model.evaluate(x_test, y_test, verbose=0)

# ---------------------------------------------------------------------------
# Comparison
# ---------------------------------------------------------------------------
print("\n===== Comparison =====")
print(f"Demo (2-block)  -> test accuracy: {demo_acc:.4f} | params: {demo_model.count_params():,}")
print(f"Three-block     -> test accuracy: {three_block_acc:.4f} | params: {three_block_model.count_params():,}")
