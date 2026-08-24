"""
AI Based Intelligent RF Spectrum Signal Identification System

File:
    visualization/visualize_signal.py

Purpose:
    Generate visual representations of RF/IQ signals.

Visualizations:
    - I/Q waveform
    - FFT spectrum
    - Constellation diagram
    - Spectrogram
    - Amplitude
    - Phase
"""

import os
import argparse

import numpy as np
import matplotlib.pyplot as plt

from features.feature_extraction import (
    compute_fft,
    create_constellation,
    compute_amplitude,
    compute_phase,
    compute_spectrogram_db,
)


def load_iq_signal(file_path):
    """
    Load an IQ signal from a NumPy file.

    Supported shapes:
        (2, 128)
        (128, 2)
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"IQ file not found:\n"
            f"{os.path.abspath(file_path)}"
        )

    iq_signal = np.load(file_path)

    if iq_signal.shape == (128, 2):
        iq_signal = iq_signal.T

    if iq_signal.shape != (2, 128):
        raise ValueError(
            "Expected IQ signal shape "
            "(2,128) or (128,2), "
            f"got {iq_signal.shape}"
        )

    return iq_signal


def plot_iq_waveform(
    iq_signal,
    output_dir,
    sample_name="iq_signal"
):
    """
    Plot I and Q waveform.
    """

    samples = np.arange(
        iq_signal.shape[1]
    )

    plt.figure(figsize=(10, 5))

    plt.plot(
        samples,
        iq_signal[0],
        label="I"
    )

    plt.plot(
        samples,
        iq_signal[1],
        label="Q"
    )

    plt.xlabel("Sample")
    plt.ylabel("Amplitude")
    plt.title("I/Q Signal Waveform")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    path = os.path.join(
        output_dir,
        f"{sample_name}_iq_waveform.png"
    )

    plt.savefig(
        path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    return path


def plot_fft(
    iq_signal,
    output_dir,
    sample_name="iq_signal",
    sample_rate=1.0
):
    """
    Plot FFT magnitude spectrum.
    """

    frequencies, magnitude = compute_fft(
        iq_signal,
        sample_rate=sample_rate
    )

    plt.figure(figsize=(10, 5))

    plt.plot(
        frequencies,
        magnitude
    )

    plt.xlabel("Frequency")
    plt.ylabel("Magnitude")
    plt.title("FFT Spectrum")
    plt.grid(True)
    plt.tight_layout()

    path = os.path.join(
        output_dir,
        f"{sample_name}_fft.png"
    )

    plt.savefig(
        path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    return path


def plot_constellation(
    iq_signal,
    output_dir,
    sample_name="iq_signal"
):
    """
    Plot I/Q constellation.
    """

    i_values, q_values = (
        create_constellation(
            iq_signal
        )
    )

    plt.figure(figsize=(7, 7))

    plt.scatter(
        i_values,
        q_values,
        s=15
    )

    plt.xlabel("In-Phase (I)")
    plt.ylabel("Quadrature (Q)")
    plt.title("IQ Constellation")
    plt.grid(True)
    plt.axis("equal")
    plt.tight_layout()

    path = os.path.join(
        output_dir,
        f"{sample_name}_constellation.png"
    )

    plt.savefig(
        path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    return path


def plot_spectrogram(
    iq_signal,
    output_dir,
    sample_name="iq_signal",
    sample_rate=1.0
):
    """
    Plot time-frequency spectrogram.
    """

    (
        frequencies,
        times,
        power_db
    ) = compute_spectrogram_db(
        iq_signal,
        sample_rate=sample_rate
    )

    plt.figure(figsize=(10, 6))

    plt.pcolormesh(
        times,
        frequencies,
        power_db,
        shading="auto"
    )

    plt.xlabel("Time")
    plt.ylabel("Frequency")
    plt.title("IQ Signal Spectrogram")

    plt.colorbar(
        label="Power (dB)"
    )

    plt.tight_layout()

    path = os.path.join(
        output_dir,
        f"{sample_name}_spectrogram.png"
    )

    plt.savefig(
        path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    return path


def plot_amplitude(
    iq_signal,
    output_dir,
    sample_name="iq_signal"
):
    """
    Plot instantaneous signal amplitude.
    """

    amplitude = compute_amplitude(
        iq_signal
    )

    samples = np.arange(
        len(amplitude)
    )

    plt.figure(figsize=(10, 5))

    plt.plot(
        samples,
        amplitude
    )

    plt.xlabel("Sample")
    plt.ylabel("Amplitude")
    plt.title("IQ Signal Amplitude")
    plt.grid(True)
    plt.tight_layout()

    path = os.path.join(
        output_dir,
        f"{sample_name}_amplitude.png"
    )

    plt.savefig(
        path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    return path


def plot_phase(
    iq_signal,
    output_dir,
    sample_name="iq_signal"
):
    """
    Plot unwrapped signal phase.
    """

    phase = compute_phase(
        iq_signal
    )

    samples = np.arange(
        len(phase)
    )

    plt.figure(figsize=(10, 5))

    plt.plot(
        samples,
        phase
    )

    plt.xlabel("Sample")
    plt.ylabel("Phase (radians)")
    plt.title("IQ Signal Phase")
    plt.grid(True)
    plt.tight_layout()

    path = os.path.join(
        output_dir,
        f"{sample_name}_phase.png"
    )

    plt.savefig(
        path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    return path


def visualize_signal(
    iq_signal,
    output_dir,
    sample_name="iq_signal",
    sample_rate=1.0
):
    """
    Generate all signal visualizations.
    """

    os.makedirs(
        output_dir,
        exist_ok=True
    )

    output_files = {}

    output_files["iq_waveform"] = (
        plot_iq_waveform(
            iq_signal,
            output_dir,
            sample_name
        )
    )

    output_files["fft"] = plot_fft(
        iq_signal,
        output_dir,
        sample_name,
        sample_rate
    )

    output_files["constellation"] = (
        plot_constellation(
            iq_signal,
            output_dir,
            sample_name
        )
    )

    output_files["spectrogram"] = (
        plot_spectrogram(
            iq_signal,
            output_dir,
            sample_name,
            sample_rate
        )
    )

    output_files["amplitude"] = (
        plot_amplitude(
            iq_signal,
            output_dir,
            sample_name
        )
    )

    output_files["phase"] = (
        plot_phase(
            iq_signal,
            output_dir,
            sample_name
        )
    )

    return output_files


def create_demo_signal():
    """
    Create a simple IQ signal for testing.
    """

    samples = np.arange(128)

    i_signal = np.cos(
        2 * np.pi * 0.1 * samples
    )

    q_signal = np.sin(
        2 * np.pi * 0.1 * samples
    )

    return np.array(
        [i_signal, q_signal],
        dtype=np.float32
    )


def main():

    parser = argparse.ArgumentParser(
        description=(
            "Visualize an RF/IQ signal."
        )
    )

    parser.add_argument(
        "--input",
        type=str,
        default=None,
        help="Path to IQ .npy file."
    )

    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Output directory."
    )

    args = parser.parse_args()

    project_root = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )

    if args.output is None:
        output_dir = os.path.join(
            project_root,
            "visualization",
            "results"
        )
    else:
        output_dir = args.output

    if args.input is None:

        print(
            "No IQ file supplied."
        )

        print(
            "Using demo IQ signal "
            "for visualization test."
        )

        iq_signal = create_demo_signal()

        sample_name = "demo"

    else:

        iq_signal = load_iq_signal(
            args.input
        )

        sample_name = os.path.splitext(
            os.path.basename(args.input)
        )[0]

    print(
        "\nInput IQ shape:",
        iq_signal.shape
    )

    print(
        "\nGenerating visualizations..."
    )

    output_files = visualize_signal(
        iq_signal,
        output_dir,
        sample_name
    )

    print(
        "\nGenerated files:"
    )

    for name, path in output_files.items():

        print(
            f"- {name}: {path}"
        )

    print(
        "\nVisualization completed successfully."
    )


if __name__ == "__main__":
    main()
