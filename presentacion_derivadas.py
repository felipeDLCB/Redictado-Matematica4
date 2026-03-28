#!/usr/bin/env python3
"""
Presentación de Derivadas Parciales usando Matplotlib
Genera frames como imágenes que pueden convertirse en video
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch
import os

# Crear directorio para frames
output_dir = "presentacion_frames"
os.makedirs(output_dir, exist_ok=True)

# Configuración de estilo
plt.style.use("dark_background")
plt.rcParams["font.family"] = "sans-serif"


def frame_titulo(n):
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.axis("off")

    ax.text(
        8,
        6,
        "Derivadas Parciales",
        fontsize=60,
        ha="center",
        va="center",
        color="#4A90D9",
        fontweight="bold",
    )
    ax.text(
        8,
        4,
        "Visualización Geométrica",
        fontsize=36,
        ha="center",
        va="center",
        color="#888888",
    )

    plt.tight_layout()
    plt.savefig(f"{output_dir}/frame_{n:03d}.png", dpi=100, facecolor="black")
    plt.close()


def frame_definicion(n):
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.axis("off")

    ax.text(
        8,
        7.5,
        "Definición",
        fontsize=40,
        ha="center",
        va="center",
        color="#4A90D9",
        fontweight="bold",
    )
    ax.text(
        8,
        5.5,
        "df/dx = lim [f(x+h,y) - f(x,y)] / h",
        fontsize=28,
        ha="center",
        va="center",
        color="white",
    )
    ax.text(
        8, 4, "y = constante", fontsize=32, ha="center", va="center", color="#FFD700"
    )
    ax.text(
        8,
        2.5,
        "Se congela la variable 'y'",
        fontsize=22,
        ha="center",
        va="center",
        color="#32CD32",
    )

    plt.tight_layout()
    plt.savefig(f"{output_dir}/frame_{n:03d}.png", dpi=100, facecolor="black")
    plt.close()


def frame_geometrica(n):
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.set_xlim(-3, 3)
    ax.set_ylim(-1, 9)
    ax.set_aspect("equal")

    # Ejes
    ax.axhline(y=0, color="gray", linewidth=1)
    ax.axvline(x=0, color="gray", linewidth=1)

    # Etiquetas
    ax.text(2.7, 0.3, "x", fontsize=20, color="white")
    ax.text(0.3, 8.5, "f(x,y)", fontsize=20, color="white")

    # Parábola
    x = np.linspace(-2.5, 2.5, 100)
    y = x**2
    ax.plot(x, y, "b-", linewidth=3, label="f(x,y) = x²")

    # Punto
    ax.plot(1, 1, "wo", markersize=10)
    ax.annotate(
        "(a,b,f(a,b))",
        xy=(1, 1),
        xytext=(1.3, 2),
        fontsize=16,
        color="white",
        arrowprops=dict(arrowstyle="->", color="white"),
    )

    # Tangente
    x_tan = np.linspace(0, 2, 50)
    y_tan = 2 * x_tan - 1
    ax.plot(x_tan, y_tan, "g-", linewidth=2, label="Tangente")

    ax.text(
        -2,
        7,
        "Interpretación Geométrica",
        fontsize=32,
        color="#4A90D9",
        fontweight="bold",
    )
    ax.text(-2, 6, "Pendiente = df/dx", fontsize=20, color="#32CD32")
    ax.legend(loc="upper right", fontsize=14)

    plt.tight_layout()
    plt.savefig(f"{output_dir}/frame_{n:03d}.png", dpi=100, facecolor="black")
    plt.close()


def frame_notacion(n):
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.axis("off")

    ax.text(
        8,
        7.5,
        "Notación",
        fontsize=48,
        ha="center",
        va="center",
        color="#4A90D9",
        fontweight="bold",
    )
    ax.text(8, 5.5, "df/dx = f_x", fontsize=36, ha="center", va="center", color="white")
    ax.text(8, 4, "df/dy = f_y", fontsize=36, ha="center", va="center", color="white")
    ax.text(
        8,
        2.5,
        "f_x(a,b) = df/dx evaluado en (a,b)",
        fontsize=24,
        ha="center",
        va="center",
        color="#AAAAAA",
    )

    plt.tight_layout()
    plt.savefig(f"{output_dir}/frame_{n:03d}.png", dpi=100, facecolor="black")
    plt.close()


def frame_ejemplo(n):
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.axis("off")

    ax.text(
        8,
        7.5,
        "Ejemplo",
        fontsize=48,
        ha="center",
        va="center",
        color="#4A90D9",
        fontweight="bold",
    )
    ax.text(
        8, 5.5, "f(x,y) = x² · y", fontsize=36, ha="center", va="center", color="white"
    )
    ax.text(8, 4, "f_x = 2xy", fontsize=36, ha="center", va="center", color="#FFD700")
    ax.text(8, 2.5, "f_y = x²", fontsize=36, ha="center", va="center", color="#32CD32")

    plt.tight_layout()
    plt.savefig(f"{output_dir}/frame_{n:03d}.png", dpi=100, facecolor="black")
    plt.close()


def frame_resumen(n):
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.axis("off")

    ax.text(
        8,
        7.5,
        "Resumen",
        fontsize=48,
        ha="center",
        va="center",
        color="#4A90D9",
        fontweight="bold",
    )
    ax.text(
        4,
        5.5,
        "• Derivada parcial = derivada univariable",
        fontsize=24,
        ha="left",
        va="center",
        color="white",
    )
    ax.text(
        4,
        4.5,
        "• Se congela otra(s) variable(s)",
        fontsize=24,
        ha="left",
        va="center",
        color="white",
    )
    ax.text(
        4,
        3.5,
        "• Pendiente de traza en superficie",
        fontsize=24,
        ha="left",
        va="center",
        color="white",
    )
    ax.text(
        4,
        2.5,
        "• Notación: símbolo ∂ (partial)",
        fontsize=24,
        ha="left",
        va="center",
        color="white",
    )

    plt.tight_layout()
    plt.savefig(f"{output_dir}/frame_{n:03d}.png", dpi=100, facecolor="black")
    plt.close()


# Generar todos los frames
frames = [
    (frame_titulo, "Frame 1: Título"),
    (frame_definicion, "Frame 2: Definición"),
    (frame_geometrica, "Frame 3: Interpretación Geométrica"),
    (frame_notacion, "Frame 4: Notación"),
    (frame_ejemplo, "Frame 5: Ejemplo"),
    (frame_resumen, "Frame 6: Resumen"),
]

for i, (func, desc) in enumerate(frames):
    func(i + 1)
    print(f"Generado: {desc}")

print(f"\nFrames guardados en: {output_dir}/")
print(
    "Para crear video: ffmpeg -r 2 -i presentacion_frames/frame_%03d.png -c:v libx264 -pix_fmt yuv420p presentacion.mp4"
)
