import os
import sys

import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import tensorflow as tf
from scipy import signal


# ============================================================
# PROJECT PATH
# ============================================================

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, PROJECT_ROOT)


# ============================================================
# PATHS
# ============================================================

MODEL_PATH = os.path.join(
    PROJECT_ROOT,
    "saved_models",
    "best_improved_cnn_classifier.keras"
)

DATA_DIR = os.path.join(
    PROJECT_ROOT,
    "data",
    "processed"
)

X_TEST_PATH = os.path.join(DATA_DIR, "X_test.npy")
Y_TEST_PATH = os.path.join(DATA_DIR, "y_test.npy")
SNR_TEST_PATH = os.path.join(DATA_DIR, "snr_test.npy")
CLASSES_PATH = os.path.join(DATA_DIR, "modulation_classes.npy")


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI RF Signal Identification",
    page_icon="📡",
    layout="wide"
)


# ============================================================
# TITLE
# ============================================================

st.title("📡 AI Based Intelligent RF Spectrum Signal Identification System")

st.markdown(
    "### Improved CNN Based RF Modulation Classification"
)

st.divider()


# ============================================================
# CHECK REQUIRED FILES
# ============================================================

required_files = {
    "Improved CNN Model": MODEL_PATH,
    "Test IQ Data": X_TEST_PATH,
    "Test Labels": Y_TEST_PATH,
    "SNR Data": SNR_TEST_PATH,
    "Modulation Classes": CLASSES_PATH,
}

missing_files = [
    name
    for name, path in required_files.items()
    if not os.path.exists(path)
]

if missing_files:

    st.error("Required project files are missing:")

    for item in missing_files:
        st.write(f"- {item}")

    st.stop()


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():

    return tf.keras.models.load_model(
        MODEL_PATH,
        compile=False
    )


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_test_data():

    X_test = np.load(X_TEST_PATH)
    y_test = np.load(Y_TEST_PATH)
    snr_test = np.load(SNR_TEST_PATH)
    classes = np.load(CLASSES_PATH, allow_pickle=True)

    return X_test, y_test, snr_test, classes


try:

    model = load_model()

    X_test, y_test, snr_test, classes = load_test_data()

except Exception as e:

    st.error("Unable to load model or test data.")
    st.exception(e)
    st.stop()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.header("Signal Selection")

sample_index = st.sidebar.number_input(
    "Test Signal Index",
    min_value=0,
    max_value=len(X_test) - 1,
    value=0,
    step=1
)


# ============================================================
# SELECT SIGNAL
# ============================================================

sample = X_test[sample_index]

true_label_index = int(y_test[sample_index])
true_label = str(classes[true_label_index])

snr_value = snr_test[sample_index]


# ============================================================
# PREPARE MODEL INPUT
# ============================================================

# Stored data:
# (2, 128)
#
# CNN input:
# (128, 2)

model_input = np.transpose(sample, (1, 0))

model_input = np.expand_dims(
    model_input,
    axis=0
)


# ============================================================
# PREDICTION
# ============================================================

prediction = model.predict(
    model_input,
    verbose=0
)

probabilities = prediction[0]

predicted_index = int(
    np.argmax(probabilities)
)

predicted_label = str(
    classes[predicted_index]
)

confidence = float(
    probabilities[predicted_index]
) * 100


# ============================================================
# TOP METRICS
# ============================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Predicted Modulation",
        predicted_label
    )

with col2:
    st.metric(
        "Confidence",
        f"{confidence:.2f}%"
    )

with col3:
    st.metric(
        "Actual Modulation",
        true_label
    )

with col4:
    st.metric(
        "SNR",
        f"{snr_value} dB"
    )


st.divider()


# ============================================================
# IQ SIGNAL
# ============================================================

I = sample[0]
Q = sample[1]

magnitude = np.sqrt(
    I ** 2 + Q ** 2
)

phase = np.unwrap(
    np.arctan2(Q, I)
)


# ============================================================
# VISUALIZATION ROW 1
# ============================================================

col1, col2 = st.columns(2)


# ------------------------------------------------------------
# I/Q WAVEFORM
# ------------------------------------------------------------

with col1:

    st.subheader("I/Q Waveform")

    fig, ax = plt.subplots()

    ax.plot(I, label="I")
    ax.plot(Q, label="Q")

    ax.set_xlabel("Sample")
    ax.set_ylabel("Amplitude")
    ax.set_title("In-phase and Quadrature Components")
    ax.legend()
    ax.grid(True)

    st.pyplot(
        fig,
        clear_figure=True
    )


# ------------------------------------------------------------
# FFT
# ------------------------------------------------------------

with col2:

    st.subheader("FFT Spectrum")

    complex_signal = I + 1j * Q

    fft_result = np.fft.fftshift(
        np.fft.fft(complex_signal)
    )

    frequency = np.fft.fftshift(
        np.fft.fftfreq(len(complex_signal))
    )

    magnitude_fft = np.abs(fft_result)

    fig, ax = plt.subplots()

    ax.plot(
        frequency,
        magnitude_fft
    )

    ax.set_xlabel("Normalized Frequency")
    ax.set_ylabel("Magnitude")
    ax.set_title("Frequency Spectrum")
    ax.grid(True)

    st.pyplot(
        fig,
        clear_figure=True
    )


# ============================================================
# VISUALIZATION ROW 2
# ============================================================

col1, col2 = st.columns(2)


# ------------------------------------------------------------
# CONSTELLATION
# ------------------------------------------------------------

with col1:

    st.subheader("Constellation Diagram")

    fig, ax = plt.subplots()

    ax.scatter(
        I,
        Q,
        s=12,
        alpha=0.7
    )

    ax.set_xlabel("In-phase (I)")
    ax.set_ylabel("Quadrature (Q)")
    ax.set_title("I-Q Constellation")
    ax.grid(True)

    st.pyplot(
        fig,
        clear_figure=True
    )


# ------------------------------------------------------------
# SPECTROGRAM
# ------------------------------------------------------------

with col2:

    st.subheader("Spectrogram")

    frequencies, times, Zxx = signal.stft(
        complex_signal
    )

    magnitude_spectrogram = np.abs(Zxx)

    fig, ax = plt.subplots()

    image = ax.pcolormesh(
        times,
        frequencies,
        magnitude_spectrogram,
        shading="auto"
    )

    ax.set_xlabel("Time")
    ax.set_ylabel("Normalized Frequency")
    ax.set_title("Signal Spectrogram")

    fig.colorbar(
        image,
        ax=ax
    )

    st.pyplot(
        fig,
        clear_figure=True
    )


# ============================================================
# ROW 3
# ============================================================

col1, col2 = st.columns(2)


# ------------------------------------------------------------
# AMPLITUDE
# ------------------------------------------------------------

with col1:

    st.subheader("Signal Amplitude")

    fig, ax = plt.subplots()

    ax.plot(
        magnitude
    )

    ax.set_xlabel("Sample")
    ax.set_ylabel("Magnitude")
    ax.set_title("Instantaneous Signal Magnitude")
    ax.grid(True)

    st.pyplot(
        fig,
        clear_figure=True
    )


# ------------------------------------------------------------
# PHASE
# ------------------------------------------------------------

with col2:

    st.subheader("Signal Phase")

    fig, ax = plt.subplots()

    ax.plot(
        phase
    )

    ax.set_xlabel("Sample")
    ax.set_ylabel("Phase (radians)")
    ax.set_title("Signal Phase")
    ax.grid(True)

    st.pyplot(
        fig,
        clear_figure=True
    )


# ============================================================
# CLASS PROBABILITIES
# ============================================================

st.divider()

st.subheader("Modulation Class Probabilities")

probability_values = probabilities * 100

for class_name, probability in zip(
    classes,
    probability_values
):

    st.write(
        f"**{class_name}** — {probability:.2f}%"
    )

    st.progress(
        float(probability / 100)
    )


# ============================================================
# FINAL RESULT
# ============================================================

st.divider()

if predicted_index == true_label_index:

    st.success(
        f"Correct Prediction: {predicted_label}"
    )

else:

    st.warning(
        f"Prediction: {predicted_label} | "
        f"Actual: {true_label}"
    )


st.caption(
    "Model: Improved CNN | "
    "Dataset: RadioML 2016.10a"
)

