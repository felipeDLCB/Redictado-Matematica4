"""
Presentación Manim Slides — Regresión Lineal Simple (Ejercicio 3)
Matemática 4 - TP2 - 2025

Renderizar:  manim render -qh presentacion.py RegresionLinealSlides
Presentar:   manim-slides RegresionLinealSlides
"""

from manim import *
from manim_slides import Slide
import numpy as np

# ── Paleta de colores ──────────────────────────────────────────────
BG       = "#0d1117"
CYAN     = "#00d4ff"
BLUE     = "#58a6ff"
WHITE_S  = "#f0f6fc"
RED_A    = "#f85149"
GREEN_A  = "#3fb950"
YELLOW_A = "#e3b341"
GRAY     = "#8b949e"

# ── Datos del ejercicio ────────────────────────────────────────────
X_DATA = np.array([100, 110, 120, 150, 190, 200, 225, 265, 280, 300], dtype=float)
Y_DATA = np.array([52, 75, 62, 61, 84, 98, 110, 94, 100, 135], dtype=float)
N = len(X_DATA)

X_BAR = X_DATA.mean()          # 194
Y_BAR = Y_DATA.mean()          # 87.1
SXX   = np.sum(X_DATA**2) - (np.sum(X_DATA)**2) / N   # 47990
SXY   = np.sum(X_DATA * Y_DATA) - np.sum(X_DATA) * np.sum(Y_DATA) / N  # 14786
BETA1 = SXY / SXX              # 0.3081
BETA0 = Y_BAR - BETA1 * X_BAR  # 27.3275


def reg_line(x):
    return BETA0 + BETA1 * x


class RegresionLinealSlides(Slide):

    def setup(self):
        self.camera.background_color = ManimColor(BG)

    # ─── helpers ───────────────────────────────────────────────────
    def section_title(self, text, sub=None):
        t = Text(text, font_size=40, color=CYAN, weight=BOLD)
        group = VGroup(t)
        if sub:
            s = Text(sub, font_size=24, color=GRAY)
            s.next_to(t, DOWN, buff=0.3)
            group.add(s)
        group.move_to(ORIGIN)
        return group

    def show_overlay(self):
        """Muestra un rectángulo negro que tapa todo el gráfico de fondo."""
        self.overlay = Rectangle(
            width=config.frame_width + 1, height=config.frame_height + 1,
            fill_color=BG, fill_opacity=1, stroke_width=0,
        )
        self.overlay.set_z_index(10)
        self.play(FadeIn(self.overlay), run_time=0.5)

    def hide_overlay(self):
        """Quita el rectángulo negro para mostrar el gráfico otra vez."""
        self.play(FadeOut(self.overlay), run_time=0.5)

    def build_axes(self, x_range=None, y_range=None, x_len=9, y_len=5.5,
                   x_label="x \\text{ (bytes)}", y_label="y \\text{ (ms)}"):
        if x_range is None:
            x_range = [0, 350, 50]
        if y_range is None:
            y_range = [0, 160, 20]
        axes = Axes(
            x_range=x_range,
            y_range=y_range,
            x_length=x_len,
            y_length=y_len,
            axis_config={"color": WHITE_S, "include_numbers": True,
                         "font_size": 20, "tip_width": 0.15, "tip_height": 0.15},
            tips=True,
        )
        labels = axes.get_axis_labels(
            MathTex(x_label, font_size=24, color=GRAY),
            MathTex(y_label, font_size=24, color=GRAY),
        )
        axes.shift(DOWN * 0.3)
        labels.shift(DOWN * 0.3)
        return axes, labels

    def data_dots(self, axes, color=WHITE_S, radius=0.06):
        dots = VGroup()
        for xi, yi in zip(X_DATA, Y_DATA):
            dot = Dot(axes.c2p(xi, yi), radius=radius, color=color)
            dots.add(dot)
        return dots

    # ══════════════════════════════════════════════════════════════
    #  INTRO — Fundamentos teóricos
    # ══════════════════════════════════════════════════════════════

    def slide_titulo(self):
        title = Text("Regresión Lineal Simple", font_size=52, color=CYAN, weight=BOLD)
        subtitle = Text("Ejercicio 3 — Transmisión en Redes", font_size=28, color=GRAY)
        subtitle.next_to(title, DOWN, buff=0.4)

        line = Line(LEFT * 3, RIGHT * 3, color=BLUE, stroke_width=2)
        line.next_to(subtitle, DOWN, buff=0.3)

        mat = Text("Matemática 4 — TP N°2 — 2025", font_size=20, color=GRAY)
        mat.next_to(line, DOWN, buff=0.3)

        self.play(FadeIn(title, shift=DOWN * 0.3))
        self.play(FadeIn(subtitle, shift=UP * 0.2), GrowFromCenter(line))
        self.play(FadeIn(mat))
        self.next_slide()

        self.play(FadeOut(VGroup(title, subtitle, line, mat)))

    def slide_que_es_regresion(self):
        header = Text("¿Qué es la Regresión Lineal?", font_size=36, color=CYAN, weight=BOLD)
        header.to_edge(UP, buff=0.5)

        defn = Text(
            "Método estadístico que modela la relación\n"
            "lineal entre una variable dependiente (Y)\n"
            "y una variable independiente (x).",
            font_size=24, color=WHITE_S, line_spacing=1.4,
        )
        defn.next_to(header, DOWN, buff=0.5)

        # Mini scatter plot ilustrativo
        ax_mini = Axes(
            x_range=[0, 6, 1], y_range=[0, 6, 1],
            x_length=4, y_length=3,
            axis_config={"color": GRAY, "include_numbers": False, "tip_width": 0.1, "tip_height": 0.1},
            tips=True,
        ).shift(DOWN * 1.5)

        np.random.seed(42)
        pts_x = np.array([0.5, 1.2, 1.8, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5])
        pts_y = 0.8 * pts_x + 0.5 + np.random.normal(0, 0.4, len(pts_x))
        mini_dots = VGroup(*[
            Dot(ax_mini.c2p(px, py), radius=0.05, color=BLUE)
            for px, py in zip(pts_x, pts_y)
        ])

        line_mini = ax_mini.plot(lambda x: 0.8 * x + 0.5, x_range=[0.2, 5.8], color=CYAN, stroke_width=3)

        lbl_x = MathTex("x", font_size=22, color=GRAY).next_to(ax_mini, DR, buff=0.1)
        lbl_y = MathTex("Y", font_size=22, color=GRAY).next_to(ax_mini, UL, buff=0.1)

        self.play(Write(header))
        self.play(FadeIn(defn, shift=UP * 0.2))
        self.next_slide()

        self.play(Create(ax_mini), FadeIn(lbl_x), FadeIn(lbl_y))
        self.play(LaggedStart(*[GrowFromCenter(d) for d in mini_dots], lag_ratio=0.08))
        self.play(Create(line_mini), run_time=1.5)
        self.next_slide()

        self.play(FadeOut(VGroup(header, defn, ax_mini, mini_dots, line_mini, lbl_x, lbl_y)))

    def slide_modelo(self):
        header = Text("El Modelo de Regresión Lineal Simple", font_size=34, color=CYAN, weight=BOLD)
        header.to_edge(UP, buff=0.5)

        modelo = MathTex(
            "Y", "=", r"\beta_0", "+", r"\beta_1", "x", "+", r"\varepsilon",
            font_size=52,
        )
        modelo.set_color(WHITE_S)
        modelo[0].set_color(CYAN)       # Y
        modelo[2].set_color(YELLOW_A)   # β₀
        modelo[4].set_color(GREEN_A)    # β₁
        modelo[5].set_color(BLUE)       # x
        modelo[7].set_color(RED_A)      # ε

        # Etiquetas distribuidas: unas arriba, otras abajo, bien separadas
        # (target, label_text, color, vertical_direction, horizontal_shift)
        labels_data = [
            (modelo[0], r"Y : \text{Variable dependiente}", CYAN, UP, LEFT * 1.5),
            (modelo[2], r"\beta_0 : \text{Ordenada al origen}", YELLOW_A, DOWN, LEFT * 0.5),
            (modelo[4], r"\beta_1 : \text{Pendiente}", GREEN_A, UP, RIGHT * 0.5),
            (modelo[5], r"x : \text{Variable independiente}", BLUE, DOWN, RIGHT * 1.5),
            (modelo[7], r"\varepsilon : \text{Error aleatorio}", RED_A, UP, RIGHT * 2.5),
        ]

        self.play(Write(header))
        self.play(Write(modelo), run_time=2)
        self.next_slide()

        arrows_labels = VGroup()
        for target, lbl_text, color, vert_dir, h_shift in labels_data:
            lbl = MathTex(lbl_text, font_size=22, color=color)
            # Posicionar la etiqueta arriba o abajo con offset horizontal
            lbl.next_to(target, vert_dir, buff=1.2)
            lbl.shift(h_shift)
            # Flecha desde la etiqueta hacia el símbolo
            if vert_dir is UP:
                arrow = Arrow(
                    lbl.get_bottom(), target.get_top(),
                    buff=0.08, color=color, stroke_width=2, max_tip_length_to_length_ratio=0.15,
                )
            else:
                arrow = Arrow(
                    lbl.get_top(), target.get_bottom(),
                    buff=0.08, color=color, stroke_width=2, max_tip_length_to_length_ratio=0.15,
                )
            arrows_labels.add(lbl, arrow)
            self.play(FadeIn(lbl), GrowArrow(arrow), run_time=0.6)

        self.next_slide()
        self.play(FadeOut(VGroup(header, modelo, arrows_labels)))

    def slide_minimos_cuadrados(self):
        header = Text("Método de Mínimos Cuadrados", font_size=34, color=CYAN, weight=BOLD)
        header.to_edge(UP, buff=0.5)

        ax = Axes(
            x_range=[0, 6, 1], y_range=[0, 6, 1],
            x_length=5, y_length=3.5,
            axis_config={"color": GRAY, "include_numbers": False, "tip_width": 0.1, "tip_height": 0.1},
            tips=True,
        ).shift(LEFT * 2.5 + DOWN * 0.5)

        np.random.seed(7)
        pts_x = np.array([0.8, 1.5, 2.0, 2.8, 3.5, 4.0, 4.8, 5.2])
        pts_y = 0.7 * pts_x + 0.8 + np.random.normal(0, 0.5, len(pts_x))
        dots = VGroup(*[Dot(ax.c2p(px, py), radius=0.06, color=BLUE) for px, py in zip(pts_x, pts_y)])

        line_func = lambda x: 0.7 * x + 0.8
        reg = ax.plot(line_func, x_range=[0.3, 5.5], color=CYAN, stroke_width=3)

        # Residuos (líneas verticales)
        residuals = VGroup()
        for px, py in zip(pts_x, pts_y):
            y_hat = line_func(px)
            res_line = DashedLine(
                ax.c2p(px, py), ax.c2p(px, y_hat),
                color=RED_A, stroke_width=2, dash_length=0.05,
            )
            residuals.add(res_line)

        # Cuadrados visuales de los residuos
        squares = VGroup()
        for px, py in zip(pts_x, pts_y):
            y_hat = line_func(px)
            side = abs(py - y_hat)
            if side < 0.05:
                continue
            sq = Square(side_length=side * (5 / 6))  # escalar al tamaño del eje
            p1 = ax.c2p(px, min(py, y_hat))
            sq.move_to(p1, aligned_edge=DL if py > y_hat else UL)
            sq.set_fill(RED_A, opacity=0.25)
            sq.set_stroke(RED_A, width=1)
            squares.add(sq)

        formula = MathTex(
            r"f(\beta_0, \beta_1) = \sum_{i=1}^{n}",
            r"(y_i - \beta_0 - \beta_1 x_i)^2",
            font_size=28, color=WHITE_S,
        ).shift(RIGHT * 3 + UP * 0.5)

        goal = Text(
            "Buscamos β₀ y β₁ que\nminimicen esta suma",
            font_size=22, color=GRAY, line_spacing=1.3,
        ).next_to(formula, DOWN, buff=0.5)

        self.play(Write(header))
        self.play(Create(ax))
        self.play(LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.06))
        self.play(Create(reg))
        self.next_slide()

        self.play(LaggedStart(*[Create(r) for r in residuals], lag_ratio=0.08))
        self.next_slide()

        self.play(
            LaggedStart(*[FadeIn(sq) for sq in squares], lag_ratio=0.08),
            Write(formula),
        )
        self.play(FadeIn(goal, shift=UP * 0.2))
        self.next_slide()

        self.play(FadeOut(VGroup(header, ax, dots, reg, residuals, squares, formula, goal)))

    def slide_contexto_ejercicio(self):
        header = Text("Contexto del Ejercicio", font_size=34, color=CYAN, weight=BOLD)
        header.to_edge(UP, buff=0.5)

        enunciado = Text(
            "Un grupo de investigación estudia la relación entre\n"
            "la longitud de un paquete de red (bytes) y el tiempo\n"
            "de transmisión (milisegundos).",
            font_size=22, color=WHITE_S, line_spacing=1.3,
        )
        enunciado.next_to(header, DOWN, buff=0.4)

        self.play(Write(header))
        self.play(FadeIn(enunciado, shift=UP * 0.2))
        self.next_slide()

        # ── Tabla de datos ──
        x_vals = [str(int(v)) for v in X_DATA]
        y_vals = [str(int(v)) for v in Y_DATA]

        table_data = [
            [r"\mathbf{x}" + r"\text{ (bytes)}"] + x_vals,
            [r"\mathbf{y}" + r"\text{ (ms)}"]     + y_vals,
        ]

        table = MobjectTable(
            [[MathTex(cell, font_size=18, color=WHITE_S) for cell in row] for row in table_data],
            include_outer_lines=True,
            line_config={"color": GRAY, "stroke_width": 1},
            h_buff=0.4, v_buff=0.35,
        ).scale(0.85)
        table.next_to(enunciado, DOWN, buff=0.4)

        # Colorear encabezados
        for entry in table.get_rows()[0]:
            entry.set_color(CYAN)
        for entry in table.get_rows()[1]:
            entry.set_color(CYAN)
        # Los datos en blanco
        for i in range(2):
            for j in range(1, 11):
                table.get_entries((i + 1, j + 1)).set_color(WHITE_S)

        self.play(FadeIn(table, shift=UP * 0.2))
        self.next_slide()

        # ── Transición a scatter plot ──
        self.play(FadeOut(enunciado), FadeOut(header), table.animate.scale(0.6).to_edge(UR, buff=0.3))

        axes, labels = self.build_axes()
        axes.shift(LEFT * 0.5)
        labels.shift(LEFT * 0.5)
        dots = self.data_dots(axes, color=BLUE, radius=0.07)

        self.play(Create(axes), FadeIn(labels))
        self.play(LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.08), run_time=1.5)
        self.next_slide()

        # Guardar para reusar
        self.axes_main = axes
        self.labels_main = labels
        self.dots_main = dots
        self.table_small = table

    # ══════════════════════════════════════════════════════════════
    #  INCISO a) — Construcción del modelo
    # ══════════════════════════════════════════════════════════════

    def slide_que_buscamos(self):
        header = Text("a) Estimación de la recta de regresión", font_size=30, color=CYAN, weight=BOLD)
        header.to_edge(UP, buff=0.4)

        # Recta animada que rota buscando ajuste
        slopes = [0.1, 0.5, 0.15, 0.45, 0.25, BETA1]
        intercepts = [40, 10, 60, 5, 50, BETA0]

        current_line = self.axes_main.plot(
            lambda x: intercepts[0] + slopes[0] * x,
            x_range=[60, 330], color=YELLOW_A, stroke_width=3,
        )

        busca = Text("Buscamos la recta que mejor se ajuste...", font_size=20, color=GRAY)
        busca.to_edge(DOWN, buff=0.5)

        self.play(Write(header), FadeIn(busca))
        self.play(Create(current_line))

        for sl, ic in zip(slopes[1:], intercepts[1:]):
            new_line = self.axes_main.plot(
                lambda x, s=sl, i=ic: i + s * x,
                x_range=[60, 330], color=YELLOW_A, stroke_width=3,
            )
            self.play(Transform(current_line, new_line), run_time=0.7)

        # Cambiar color a cyan cuando encuentra la correcta
        final_line = self.axes_main.plot(
            lambda x: reg_line(x),
            x_range=[60, 330], color=CYAN, stroke_width=3,
        )
        self.play(Transform(current_line, final_line), FadeOut(busca))
        self.next_slide()

        self.play(FadeOut(current_line), FadeOut(header))

    def slide_formulas_estimadores(self):
        header = Text("Fórmulas de los Estimadores", font_size=30, color=CYAN, weight=BOLD)
        header.to_edge(UP, buff=0.4)

        f_beta1 = MathTex(
            r"\hat{\beta}_1", "=", r"\frac{S_{xy}}{S_{xx}}",
            font_size=40, color=WHITE_S,
        )
        f_beta1[0].set_color(GREEN_A)

        f_beta0 = MathTex(
            r"\hat{\beta}_0", "=", r"\bar{y}", "-", r"\hat{\beta}_1", r"\bar{x}",
            font_size=40, color=WHITE_S,
        )
        f_beta0[0].set_color(YELLOW_A)
        f_beta0[4].set_color(GREEN_A)

        donde = MathTex(
            r"S_{xx} = \sum(x_i - \bar{x})^2 \qquad S_{xy} = \sum(x_i - \bar{x})(y_i - \bar{y})",
            font_size=26, color=GRAY,
        )

        formulas = VGroup(f_beta1, f_beta0, donde).arrange(DOWN, buff=0.5)
        formulas.move_to(ORIGIN)

        self.show_overlay()
        for obj in [header, f_beta1, f_beta0, donde]:
            obj.set_z_index(20)

        self.play(Write(header))
        self.play(Write(f_beta1), run_time=1.2)
        self.play(Write(f_beta0), run_time=1.2)
        self.play(FadeIn(donde, shift=UP * 0.2))
        self.next_slide()

        self.play(FadeOut(VGroup(header, formulas)))
        self.hide_overlay()

    def slide_medias(self):
        header = Text("Cálculo de las medias", font_size=30, color=CYAN, weight=BOLD)
        header.to_edge(UP, buff=0.4)

        calc_x = MathTex(
            r"\bar{x}", "=", r"\frac{\sum x_i}{n}", "=",
            r"\frac{1940}{10}", "=", "194",
            font_size=34, color=WHITE_S,
        )
        calc_x[0].set_color(BLUE)
        calc_x[-1].set_color(CYAN)

        calc_y = MathTex(
            r"\bar{y}", "=", r"\frac{\sum y_i}{n}", "=",
            r"\frac{871}{10}", "=", "87{,}1",
            font_size=34, color=WHITE_S,
        )
        calc_y[0].set_color(BLUE)
        calc_y[-1].set_color(CYAN)

        calcs = VGroup(calc_x, calc_y).arrange(DOWN, buff=0.6).move_to(ORIGIN)

        self.play(Write(header))
        self.play(Write(calc_x), run_time=1.5)
        self.play(Write(calc_y), run_time=1.5)
        self.next_slide()

        # Mostrar medias en el gráfico
        self.play(FadeOut(VGroup(header, calcs)))

        h_line = DashedLine(
            self.axes_main.c2p(0, Y_BAR), self.axes_main.c2p(330, Y_BAR),
            color=YELLOW_A, stroke_width=1.5, dash_length=0.08,
        )
        v_line = DashedLine(
            self.axes_main.c2p(X_BAR, 0), self.axes_main.c2p(X_BAR, 150),
            color=YELLOW_A, stroke_width=1.5, dash_length=0.08,
        )
        mean_dot = Dot(self.axes_main.c2p(X_BAR, Y_BAR), radius=0.1, color=YELLOW_A)
        mean_label = MathTex(r"(\bar{x}, \bar{y})", font_size=22, color=YELLOW_A)
        mean_label.next_to(mean_dot, UR, buff=0.15)

        self.play(Create(h_line), Create(v_line))
        self.play(GrowFromCenter(mean_dot), FadeIn(mean_label))
        self.next_slide()

        self.mean_lines = VGroup(h_line, v_line, mean_dot, mean_label)

    def slide_sxx_sxy(self):
        header = Text("Cálculo de Sxx y Sxy", font_size=30, color=CYAN, weight=BOLD)
        header.to_edge(UP, buff=0.4)

        self.show_overlay()

        sxx = MathTex(
            r"S_{xx}", "=", r"\sum x_i^2", "-", r"\frac{(\sum x_i)^2}{n}",
            "=", "424350", "-", r"\frac{(1940)^2}{10}", "=", r"\mathbf{47990}",
            font_size=30, color=WHITE_S,
        )
        sxx[0].set_color(BLUE)
        sxx[-1].set_color(CYAN)

        sxy = MathTex(
            r"S_{xy}", "=", r"\sum x_i y_i", "-", r"\frac{\sum x_i \sum y_i}{n}",
            "=", "183760", "-", r"\frac{(1940)(871)}{10}", "=", r"\mathbf{14786}",
            font_size=30, color=WHITE_S,
        )
        sxy[0].set_color(BLUE)
        sxy[-1].set_color(CYAN)

        formulas = VGroup(sxx, sxy).arrange(DOWN, buff=0.7).move_to(ORIGIN)
        for obj in [header, sxx, sxy]:
            obj.set_z_index(20)

        self.play(Write(header))
        self.play(Write(sxx), run_time=2)
        self.play(Write(sxy), run_time=2)
        self.next_slide()

        self.play(FadeOut(VGroup(header, sxx, sxy)))
        self.hide_overlay()

    def slide_beta1(self):
        header = Text("Cálculo de β̂₁ (pendiente)", font_size=30, color=CYAN, weight=BOLD)
        header.to_edge(UP, buff=0.4)

        self.show_overlay()

        step1 = MathTex(
            r"\hat{\beta}_1", "=", r"\frac{S_{xy}}{S_{xx}}",
            font_size=44, color=WHITE_S,
        )
        step1[0].set_color(GREEN_A)

        step2 = MathTex(
            r"\hat{\beta}_1", "=", r"\frac{14786}{47990}",
            font_size=44, color=WHITE_S,
        )
        step2[0].set_color(GREEN_A)

        step3 = MathTex(
            r"\hat{\beta}_1", "=", r"0{,}3081",
            font_size=52, color=WHITE_S,
        )
        step3[0].set_color(GREEN_A)
        step3[2].set_color(CYAN)

        for s in [header, step1, step2, step3]:
            s.set_z_index(20)
        for s in [step1, step2, step3]:
            s.move_to(ORIGIN)

        self.play(Write(header))
        self.play(Write(step1), run_time=1.2)
        self.next_slide()

        self.play(TransformMatchingTex(step1, step2), run_time=1.2)
        self.next_slide()

        self.play(TransformMatchingTex(step2, step3), run_time=1.2)
        self.next_slide()

        self.play(FadeOut(VGroup(header, step3)))
        self.hide_overlay()

    def slide_beta0_recta(self):
        header = Text("Cálculo de β̂₀ y recta final", font_size=30, color=CYAN, weight=BOLD)
        header.to_edge(UP, buff=0.4)

        self.show_overlay()

        calc_b0 = MathTex(
            r"\hat{\beta}_0", "=", r"\bar{y}", "-", r"\hat{\beta}_1", r"\bar{x}",
            font_size=38, color=WHITE_S,
        )
        calc_b0[0].set_color(YELLOW_A)
        calc_b0[4].set_color(GREEN_A)

        calc_b0_num = MathTex(
            r"\hat{\beta}_0", "=", "87{,}1", "-", "0{,}3081", r"\cdot", "194",
            font_size=38, color=WHITE_S,
        )
        calc_b0_num[0].set_color(YELLOW_A)

        calc_b0_res = MathTex(
            r"\hat{\beta}_0", "=", "27{,}3275",
            font_size=44, color=WHITE_S,
        )
        calc_b0_res[0].set_color(YELLOW_A)
        calc_b0_res[2].set_color(CYAN)

        for c in [header, calc_b0, calc_b0_num, calc_b0_res]:
            c.set_z_index(20)
        for c in [calc_b0, calc_b0_num, calc_b0_res]:
            c.move_to(UP * 0.5)

        self.play(Write(header))
        self.play(Write(calc_b0), run_time=1.2)
        self.next_slide()

        self.play(TransformMatchingTex(calc_b0, calc_b0_num), run_time=1)
        self.play(TransformMatchingTex(calc_b0_num, calc_b0_res), run_time=1)
        self.next_slide()

        # Recta final
        recta_eq = MathTex(
            r"\hat{y}", "=", "0{,}3081", "x", "+", "27{,}3275",
            font_size=48,
        )
        recta_eq[0].set_color(CYAN)
        recta_eq[2].set_color(GREEN_A)
        recta_eq[5].set_color(YELLOW_A)
        recta_eq.move_to(DOWN * 1)
        recta_eq.set_z_index(20)

        box = SurroundingRectangle(recta_eq, color=CYAN, buff=0.2, corner_radius=0.1)
        box.set_z_index(20)

        self.play(Write(recta_eq))
        self.play(Create(box))
        self.next_slide()

        self.play(FadeOut(VGroup(header, calc_b0_res, recta_eq, box)))
        self.hide_overlay()

        reg_graph = self.axes_main.plot(
            lambda x: reg_line(x), x_range=[60, 330],
            color=CYAN, stroke_width=3,
        )
        reg_label = MathTex(
            r"\hat{y} = 0{,}3081x + 27{,}3275",
            font_size=22, color=CYAN,
        )
        reg_label.next_to(reg_graph, UR, buff=0.1).shift(LEFT * 2 + DOWN * 0.3)

        self.play(Create(reg_graph), run_time=2)
        self.play(FadeIn(reg_label))
        self.next_slide()

        self.reg_graph = reg_graph
        self.reg_label = reg_label

    # ══════════════════════════════════════════════════════════════
    #  INCISO b) — Predicción x=170
    # ══════════════════════════════════════════════════════════════

    def slide_prediccion_170(self):
        header = Text("b) Predicción para x = 170", font_size=30, color=CYAN, weight=BOLD)
        header.to_edge(UP, buff=0.4)

        y_pred = reg_line(170)  # ~79.7055

        v_line = DashedLine(
            self.axes_main.c2p(170, 0), self.axes_main.c2p(170, y_pred),
            color=GREEN_A, stroke_width=2, dash_length=0.08,
        )
        h_line = DashedLine(
            self.axes_main.c2p(0, y_pred), self.axes_main.c2p(170, y_pred),
            color=GREEN_A, stroke_width=2, dash_length=0.08,
        )
        pred_dot = Dot(self.axes_main.c2p(170, y_pred), radius=0.1, color=GREEN_A)

        x_label = MathTex("170", font_size=20, color=GREEN_A)
        x_label.next_to(self.axes_main.c2p(170, 0), DOWN, buff=0.15)

        self.play(Write(header))
        self.play(Create(v_line), FadeIn(x_label))
        self.play(Create(h_line), GrowFromCenter(pred_dot))
        self.next_slide()

        # Cálculo
        # Atenuar gráfico un poco
        calc = MathTex(
            r"\hat{y}", "=", "0{,}3081", r"\cdot", "170", "+", "27{,}3275",
            font_size=32, color=WHITE_S,
        )
        calc[4].set_color(GREEN_A)
        result = MathTex(
            r"\hat{y}", "=", r"\mathbf{79{,}7055 \text{ ms}}",
            font_size=38, color=WHITE_S,
        )
        result[2].set_color(GREEN_A)

        calc_group = VGroup(calc, result).arrange(DOWN, buff=0.4)
        calc_group.to_edge(LEFT, buff=0.8).shift(DOWN * 1.5)

        bg_rect = BackgroundRectangle(calc_group, color=BG, fill_opacity=0.85, buff=0.2)

        self.play(FadeIn(bg_rect), Write(calc))
        self.play(Write(result))

        nota = Text("170 ∈ (100, 300) → Interpolación válida", font_size=18, color=GREEN_A)
        nota.next_to(result, DOWN, buff=0.3)
        nota_bg = BackgroundRectangle(nota, color=BG, fill_opacity=0.85, buff=0.1)
        self.play(FadeIn(nota_bg), FadeIn(nota))
        self.next_slide()

        self.play(FadeOut(VGroup(
            header, v_line, h_line, pred_dot, x_label,
            bg_rect, calc, result, nota_bg, nota,
        )))

    # ══════════════════════════════════════════════════════════════
    #  INCISO d) — Interpretación de la pendiente
    # ══════════════════════════════════════════════════════════════

    def slide_pendiente(self):
        header = Text("d) Interpretación de la pendiente", font_size=30, color=CYAN, weight=BOLD)
        header.to_edge(UP, buff=0.4)

        # Escalón visual sobre la recta
        x_start = 180
        y_start = reg_line(x_start)
        x_end = x_start + 50  # Δx visual exagerado para que se vea
        y_end = reg_line(x_end)

        p1 = self.axes_main.c2p(x_start, y_start)
        p2 = self.axes_main.c2p(x_end, y_start)    # horizontal
        p3 = self.axes_main.c2p(x_end, y_end)       # vertical

        h_seg = Line(p1, p2, color=BLUE, stroke_width=3)
        v_seg = Line(p2, p3, color=GREEN_A, stroke_width=3)

        dx_label = MathTex(r"\Delta x", font_size=22, color=BLUE)
        dx_label.next_to(h_seg, DOWN, buff=0.15)
        dy_label = MathTex(r"\Delta y", font_size=22, color=GREEN_A)
        dy_label.next_to(v_seg, RIGHT, buff=0.15)

        self.play(Write(header))
        self.play(Create(h_seg), Create(v_seg))
        self.play(FadeIn(dx_label), FadeIn(dy_label))
        self.next_slide()

        interp = MathTex(
            r"\hat{\beta}_1 = 0{,}3081 \; \frac{\text{ms}}{\text{byte}}",
            font_size=36, color=GREEN_A,
        )
        interp.to_edge(DOWN, buff=0.8)
        interp_bg = BackgroundRectangle(interp, color=BG, fill_opacity=0.85, buff=0.15)

        texto = Text(
            "Por cada byte adicional, el tiempo\nde transmisión aumenta 0,3081 ms",
            font_size=22, color=WHITE_S, line_spacing=1.3,
        )
        texto.next_to(interp, UP, buff=0.3)
        texto_bg = BackgroundRectangle(texto, color=BG, fill_opacity=0.85, buff=0.1)

        self.play(FadeIn(interp_bg), Write(interp))
        self.play(FadeIn(texto_bg), FadeIn(texto))
        self.next_slide()

        self.play(FadeOut(VGroup(
            header, h_seg, v_seg, dx_label, dy_label,
            interp_bg, interp, texto_bg, texto,
        )))

    # ══════════════════════════════════════════════════════════════
    #  INCISO c) — Extrapolación
    # ══════════════════════════════════════════════════════════════

    def slide_extrapolacion(self):
        header = Text("c) ¿Podemos predecir para x = 500?", font_size=30, color=CYAN, weight=BOLD)
        header.to_edge(UP, buff=0.4)

        self.play(Write(header))

        # Limpiar elementos anteriores del gráfico
        self.play(FadeOut(VGroup(
            self.mean_lines, self.reg_graph, self.reg_label, self.table_small,
        )))

        # Crear nuevos ejes extendidos
        axes_ext, labels_ext = self.build_axes(
            x_range=[0, 550, 50], y_range=[0, 200, 25],
            x_len=11, y_len=5,
        )
        axes_ext.shift(DOWN * 0.3)
        labels_ext.shift(DOWN * 0.3)

        # Mover puntos al nuevo sistema
        new_dots = self.data_dots(axes_ext, color=BLUE, radius=0.07)

        self.play(
            ReplacementTransform(self.axes_main, axes_ext),
            ReplacementTransform(self.labels_main, labels_ext),
            ReplacementTransform(self.dots_main, new_dots),
        )

        # Recta dentro del rango
        reg_solid = axes_ext.plot(
            lambda x: reg_line(x), x_range=[60, 300],
            color=CYAN, stroke_width=3,
        )
        # Recta extendida (punteada)
        reg_dashed_pts = [
            axes_ext.c2p(x, reg_line(x)) for x in np.linspace(300, 530, 50)
        ]
        reg_dashed = DashedVMobject(
            VMobject().set_points_smoothly(reg_dashed_pts),
            num_dashes=30,
        )
        reg_dashed.set_color(RED_A).set_stroke(width=2)

        self.play(Create(reg_solid))
        self.play(Create(reg_dashed), run_time=1.5)
        self.next_slide()

        # Zonas
        safe_zone = Rectangle(
            width=axes_ext.c2p(300, 0)[0] - axes_ext.c2p(100, 0)[0],
            height=axes_ext.c2p(0, 180)[1] - axes_ext.c2p(0, 0)[1],
        )
        safe_zone.set_fill(GREEN_A, opacity=0.08).set_stroke(GREEN_A, width=1, opacity=0.5)
        safe_zone.move_to(axes_ext.c2p(200, 90))

        danger_zone = Rectangle(
            width=axes_ext.c2p(540, 0)[0] - axes_ext.c2p(300, 0)[0],
            height=axes_ext.c2p(0, 180)[1] - axes_ext.c2p(0, 0)[1],
        )
        danger_zone.set_fill(RED_A, opacity=0.08).set_stroke(RED_A, width=1, opacity=0.5)
        danger_zone.move_to(axes_ext.c2p(420, 90))

        safe_label = Text("Interpolación", font_size=18, color=GREEN_A)
        safe_label.move_to(axes_ext.c2p(200, 170))
        safe_bg = BackgroundRectangle(safe_label, color=BG, fill_opacity=0.7, buff=0.05)

        danger_label = Text("Extrapolación", font_size=18, color=RED_A)
        danger_label.move_to(axes_ext.c2p(420, 170))
        danger_bg = BackgroundRectangle(danger_label, color=BG, fill_opacity=0.7, buff=0.05)

        x500_mark = Cross(
            Dot(axes_ext.c2p(500, reg_line(500)), radius=0.01),
            stroke_color=RED_A, stroke_width=4,
        ).scale(0.3)
        x500_label = MathTex("x = 500", font_size=22, color=RED_A)
        x500_label.next_to(x500_mark, UP, buff=0.2)

        self.play(FadeIn(safe_zone), FadeIn(danger_zone))
        self.play(
            FadeIn(safe_bg), FadeIn(safe_label),
            FadeIn(danger_bg), FadeIn(danger_label),
        )
        self.play(Create(x500_mark), FadeIn(x500_label))
        self.next_slide()

        # Explicación
        expl = Text(
            "500 ∉ (100, 300)\n"
            "No se puede utilizar la recta para\n"
            "predecir fuera del rango observado.",
            font_size=22, color=WHITE_S, line_spacing=1.3,
        )
        expl.to_edge(LEFT, buff=0.5).shift(DOWN * 1)
        expl_bg = BackgroundRectangle(expl, color=BG, fill_opacity=0.85, buff=0.15)

        self.play(FadeIn(expl_bg), FadeIn(expl))
        self.next_slide()

        self.play(FadeOut(VGroup(
            header, axes_ext, labels_ext, new_dots,
            reg_solid, reg_dashed,
            safe_zone, danger_zone,
            safe_bg, safe_label, danger_bg, danger_label,
            x500_mark, x500_label, expl_bg, expl,
        )))

    # ══════════════════════════════════════════════════════════════
    #  CONCLUSIÓN
    # ══════════════════════════════════════════════════════════════

    def slide_conclusion(self):
        header = Text("Conclusión", font_size=40, color=CYAN, weight=BOLD)
        header.to_edge(UP, buff=0.6)

        points = [
            "La regresión lineal modela relaciones lineales entre variables",
            "Los estimadores β̂₀ y β̂₁ minimizan la suma de residuos al cuadrado",
            "La recta obtenida: ŷ = 0,3081x + 27,3275",
            "Solo es válido predecir dentro del rango de datos (100-300 bytes)",
            "β̂₁ = 0,3081 ms/byte: aumento del tiempo por cada byte adicional",
        ]

        bullets = VGroup()
        for p in points:
            dot = Dot(radius=0.04, color=CYAN).shift(LEFT * 5.5)
            txt = Text(p, font_size=20, color=WHITE_S)
            txt.next_to(dot, RIGHT, buff=0.2)
            row = VGroup(dot, txt)
            bullets.add(row)

        bullets.arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        bullets.next_to(header, DOWN, buff=0.6)

        self.play(Write(header))
        for bullet in bullets:
            self.play(FadeIn(bullet, shift=RIGHT * 0.3), run_time=0.6)
        self.next_slide()

        # Cierre
        thanks = Text("¡Gracias!", font_size=52, color=CYAN, weight=BOLD)
        thanks.move_to(ORIGIN)

        self.play(FadeOut(VGroup(header, bullets)))
        self.play(FadeIn(thanks, scale=1.5))
        self.next_slide()

    # ══════════════════════════════════════════════════════════════
    #  CONSTRUCT — Flujo principal
    # ══════════════════════════════════════════════════════════════

    def construct(self):
        # Intro
        self.slide_titulo()
        self.slide_que_es_regresion()
        self.slide_modelo()
        self.slide_minimos_cuadrados()
        self.slide_contexto_ejercicio()

        # Inciso a)
        self.slide_que_buscamos()
        self.slide_formulas_estimadores()
        self.slide_medias()
        self.slide_sxx_sxy()
        self.slide_beta1()
        self.slide_beta0_recta()

        # Inciso b)
        self.slide_prediccion_170()

        # Inciso d)
        self.slide_pendiente()

        # Inciso c)
        self.slide_extrapolacion()

        # Conclusión
        self.slide_conclusion()
