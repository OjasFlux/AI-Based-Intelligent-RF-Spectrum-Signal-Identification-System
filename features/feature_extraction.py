"""
AI Based Intelligent RF Spectrum Signal Identification System

File:
    features/feature_extraction.py

Purpose:
    Generate supporting RF signal representations for analysis
    and visualization.

Representations:
    1. FFT Spectrum
    2. Constellation Diagram Data
    3. Spectrogram

Note:
    These functions are supporting signal-analysis utilities.
    The primary CNN input remains the preprocessed I/Q signal.
"""

import numpy as np
from scipy import signal


def validate_iq_signal(iq_signal):
    """
    Validate an IQ signal.

    Expected shape:
        (2, N)

    Channel 0:
        I

    Channel 1:
        Q

    Parameters
    ----------
    iq_signal : np.ndarray
        IQ signal.

    Returns
    -------
    np.ndarray
        Validated IQ signal.
    """

    iq_signal = np.asarray(iq_signal)

    if iq_signal.ndim != 2:
        raise ValueError(
            f"Expected 2D IQ signal, got shape {iq_signal.shape}"
        )

    if iq_signal.shape[0] != 2:
        raise ValueError(
            f"Expected IQ shape (2, N), got {iq_signal.shape}"
        )

    if iq_signal.shape[1] == 0:
        raise ValueError(
            "IQ signal contains no samples."
        )

    return iq_signal


def create_complex_iq(iq_signal):
    """
    Convert separate I/Q channels into a complex IQ signal.

    Parameters
    ----------
    iq_signal : np.ndarray
        IQ signal with shape (2, N).

    Returns
    -------
    np.ndarray
        Complex IQ signal with shape (N,).
    """

    iq_signal = validate_iq_signal(iq_signal)

    i_signal = iq_signal[0]
    q_signal = iq_signal[1]

    complex_iq = i_signal + 1j * q_signal

    return complex_iq


def compute_fft(
    iq_signal,
    sample_rate=1.0,
    fft_shift=True
):
    """
    Compute the FFT spectrum of an IQ signal.

    Parameters
    ----------
    iq_signal : np.ndarray
        IQ signal with shape (2, N).

    sample_rate : float
        Sampling rate in samples per second.

    fft_shift : bool
        Shift zero frequency to the center.

    Returns
    -------
    frequencies : np.ndarray
        Frequency axis.

    magnitude : np.ndarray
        FFT magnitude.
    """

    complex_iq = create_complex_iq(
        iq_signal
    )

    number_of_samples = len(
        complex_iq
    )

    spectrum = np.fft.fft(
        complex_iq
    )

    frequencies = np.fft.fftfreq(
        number_of_samples,
        d=1.0 / sample_rate
    )

    magnitude = np.abs(
        spectrum
    )

    if fft_shift:

        frequencies = np.fft.fftshift(
            frequencies
        )

        magnitude = np.fft.fftshift(
            magnitude
        )

    return frequencies, magnitude


def compute_fft_db(
    iq_signal,
    sample_rate=1.0,
    fft_shift=True
):
    """
    Compute FFT magnitude in decibels.

    Parameters
    ----------
    iq_signal : np.ndarray
        IQ signal with shape (2, N).

    sample_rate : float
        Sampling rate.

    fft_shift : bool
        Shift zero frequency to center.

    Returns
    -------
    frequencies : np.ndarray
        Frequency axis.

    magnitude_db : np.ndarray
        FFT magnitude in dB.
    """

    frequencies, magnitude = compute_fft(
        iq_signal,
        sample_rate=sample_rate,
        fft_shift=fft_shift
    )

    epsilon = 1e-12

    magnitude_db = 20 * np.log10(
        magnitude + epsilon
    )

    return frequencies, magnitude_db


def create_constellation(
    iq_signal
):
    """
    Generate I/Q constellation data.

    Parameters
    ----------
    iq_signal : np.ndarray
        IQ signal with shape (2, N).

    Returns
    -------
    i_values : np.ndarray
        In-phase values.

    q_values : np.ndarray
        Quadrature values.
    """

    iq_signal = validate_iq_signal(
        iq_signal
    )

    i_values = iq_signal[0]
    q_values = iq_signal[1]

    return i_values, q_values


def compute_amplitude(
    iq_signal
):
    """
    Compute instantaneous IQ signal amplitude.

    Formula:

        amplitude = sqrt(I^2 + Q^2)

    Parameters
    ----------
    iq_signal : np.ndarray
        IQ signal with shape (2, N).

    Returns
    -------
    np.ndarray
        Signal amplitude.
    """

    iq_signal = validate_iq_signal(
        iq_signal
    )

    i_signal = iq_signal[0]
    q_signal = iq_signal[1]

    amplitude = np.sqrt(
        i_signal ** 2 +
        q_signal ** 2
    )

    return amplitude


def compute_phase(
    iq_signal
):
    """
    Compute instantaneous phase of the IQ signal.

    Parameters
    ----------
    iq_signal : np.ndarray
        IQ signal with shape (2, N).

    Returns
    -------
    np.ndarray
        Unwrapped phase.
    """

    complex_iq = create_complex_iq(
        iq_signal
    )

    phase = np.angle(
        complex_iq
    )

    phase = np.unwrap(
        phase
    )

    return phase


def compute_spectrogram(
    iq_signal,
    sample_rate=1.0,
    nperseg=None,
    noverlap=None
):
    """
    Generate a spectrogram from the complex IQ signal.

    Parameters
    ----------
    iq_signal : np.ndarray
        IQ signal with shape (2, N).

    sample_rate : float
        Sampling rate.

    nperseg : int or None
        Number of samples per segment.

    noverlap : int or None
        Number of overlapping samples.

    Returns
    -------
    frequencies : np.ndarray
        Frequency values.

    times : np.ndarray
        Time values.

    spectrogram : np.ndarray
        Spectrogram power values.
    """

    complex_iq = create_complex_iq(
        iq_signal
    )

    if nperseg is None:

        nperseg = min(
            64,
            len(complex_iq)
        )

    if nperseg < 2:

        raise ValueError(
            "Signal is too short for spectrogram calculation."
        )

    if noverlap is None:

        noverlap = nperseg // 2

    frequencies, times, spectrum = (
        signal.stft(
            complex_iq,
            fs=sample_rate,
            nperseg=nperseg,
            noverlap=noverlap
        )
    )

    power = np.abs(
        spectrum
    ) ** 2

    return (
        frequencies,
        times,
        power
    )


def compute_spectrogram_db(
    iq_signal,
    sample_rate=1.0,
    nperseg=None,
    noverlap=None
):
    """
    Generate spectrogram power in decibels.

    Returns
    -------
    frequencies : np.ndarray
        Frequency values.

    times : np.ndarray
        Time values.

    power_db : np.ndarray
        Spectrogram power in dB.
    """

    frequencies, times, power = (
        compute_spectrogram(
            iq_signal,
            sample_rate=sample_rate,
            nperseg=nperseg,
            noverlap=noverlap
        )
    )

    epsilon = 1e-12

    power_db = 10 * np.log10(
        power + epsilon
    )

    return (
        frequencies,
        times,
        power_db
    )


def extract_signal_features(
    iq_signal,
    sample_rate=1.0
):
    """
    Generate the main supporting signal representations.

    Parameters
    ----------
    iq_signal : np.ndarray
        IQ signal with shape (2, N).

    sample_rate : float
        Sampling rate.

    Returns
    -------
    dict
        Dictionary containing:

        fft_frequency
        fft_magnitude
        constellation_i
        constellation_q
        amplitude
        phase
        spectrogram_frequency
        spectrogram_time
        spectrogram_power
    """

    fft_frequency, fft_magnitude = (
        compute_fft(
            iq_signal,
            sample_rate=sample_rate
        )
    )

    constellation_i, constellation_q = (
        create_constellation(
            iq_signal
        )
    )

    amplitude = compute_amplitude(
        iq_signal
    )

    phase = compute_phase(
        iq_signal
    )

    (
        spectrogram_frequency,
        spectrogram_time,
        spectrogram_power
    ) = compute_spectrogram(
        iq_signal,
        sample_rate=sample_rate
    )

    return {
        "fft_frequency": fft_frequency,
        "fft_magnitude": fft_magnitude,

        "constellation_i":
            constellation_i,

        "constellation_q":
            constellation_q,

        "amplitude": amplitude,

        "phase": phase,

        "spectrogram_frequency":
            spectrogram_frequency,

        "spectrogram_time":
            spectrogram_time,

        "spectrogram_power":
            spectrogram_power
    }


if __name__ == "__main__":

    print("=" * 60)
    print("FEATURE EXTRACTION TEST")
    print("=" * 60)

    # Generate a small example IQ signal
    number_of_samples = 128

    time = np.arange(
        number_of_samples
    )

    i_signal = np.cos(
        2 * np.pi * 0.1 * time
    )

    q_signal = np.sin(
        2 * np.pi * 0.1 * time
    )

    example_iq = np.array([
        i_signal,
        q_signal
    ])

    print(
        "\nInput IQ shape:",
        example_iq.shape
    )

    # FFT
    frequencies, magnitude = compute_fft(
        example_iq
    )

    print(
        "FFT output shape:",
        magnitude.shape
    )

    # Constellation
    i_values, q_values = (
        create_constellation(
            example_iq
        )
    )

    print(
        "Constellation points:",
        len(i_values)
    )

    # Amplitude
    amplitude = compute_amplitude(
        example_iq
    )

    print(
        "Amplitude shape:",
        amplitude.shape
    )

    # Phase
    phase = compute_phase(
        example_iq
    )

    print(
        "Phase shape:",
        phase.shape
    )

    # Spectrogram
    (
        spec_frequency,
        spec_time,
        spec_power
    ) = compute_spectrogram(
        example_iq
    )

    print(
        "Spectrogram shape:",
        spec_power.shape
    )

    print("\n" + "=" * 60)
    print("FEATURE EXTRACTION TEST COMPLETED")
    print("=" * 60)
