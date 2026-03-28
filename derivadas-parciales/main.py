from manim import *
import numpy as np

AZUL   = "#4A90D9"
DORADO = "#FFD700"
VERDE  = "#32CD32"
GRIS   = "#888888"
BLANCO = "#FFFFFF"


class Scene1_Portada(Scene):
    def construct(self):
        titulo = Text("Derivadas Parciales", font_size=72, color=AZUL, weight=BOLD)
        subtitulo = Text(
            "Una exploración visual del cálculo multivariable",
            font_size=32, color=GRIS
        )
        integrantes = Text(
            "Franco Cirielli  ·  Felipe De La Cuadra Bacci  ·  Facundo Feliú",
            font_size=24, color=GRIS
        )

        subtitulo.next_to(titulo, DOWN, buff=0.5)
        integrantes.next_to(subtitulo, DOWN, buff=0.8)

        self.play(Write(titulo, run_time=1.5))
        self.play(FadeIn(subtitulo, shift=UP), run_time=0.8)
        self.play(FadeIn(integrantes, shift=UP), run_time=0.8)
        self.wait(2)


# Función libre fuera de la clase — evita capturar `self` en always_redraw
def _make_secante(ax, x0, h):
    if abs(h) < 1e-6:
        h = 1e-6
    slope = ((x0 + h)**2 - x0**2) / h
    return ax.plot(
        lambda x: slope * (x - x0) + x0**2,
        color=VERDE, stroke_width=2,
        x_range=[x0 - 0.5, x0 + max(h + 0.3, 0.3)]
    )


class Scene2_Derivada(Scene):
    def construct(self):
        ax = Axes(
            x_range=(-0.5, 2.5, 1),
            y_range=(-0.5, 5, 1),
            x_length=7,
            y_length=5,
            axis_config={"color": GRIS, "include_tip": True},
        )
        ax.to_edge(LEFT, buff=0.8)

        curva = ax.plot(lambda x: x**2, color=AZUL, stroke_width=3)
        label_f = MathTex(r"f(x) = x^2", font_size=28, color=AZUL)
        label_f.next_to(ax, UP, buff=0.1).to_edge(RIGHT, buff=1.5)

        x0 = 1.0
        h_tracker = ValueTracker(1.2)

        punto_p = Dot(ax.c2p(x0, x0**2), color=DORADO, radius=0.08)
        punto_q = always_redraw(
            lambda: Dot(ax.c2p(x0 + h_tracker.get_value(),
                               (x0 + h_tracker.get_value())**2),
                        color=VERDE, radius=0.07)
        )

        secante = always_redraw(lambda: _make_secante(ax, x0, h_tracker.get_value()))
        label_h = always_redraw(
            lambda: MathTex(
                r"h = " + f"{h_tracker.get_value():.2f}",
                font_size=28, color=VERDE
            ).next_to(punto_q, UR, buff=0.15)
        )

        tangente = ax.plot(lambda x: 2 * x0 * (x - x0) + x0**2,
                           color=DORADO, stroke_width=3,
                           x_range=[x0 - 1, x0 + 1])

        formula = MathTex(
            r"f'(x) = \lim_{h \to 0} \frac{f(x+h)-f(x)}{h}",
            font_size=30, color=BLANCO
        ).to_edge(RIGHT, buff=0.5).shift(DOWN * 0.5)

        self.play(Create(ax), Create(curva), run_time=1.5)
        self.play(Write(label_f), run_time=0.8)
        self.play(FadeIn(punto_p), FadeIn(punto_q), Create(secante), run_time=0.8)
        self.add(label_h)
        self.wait(0.5)
        self.play(h_tracker.animate.set_value(0.01), run_time=3)
        self.wait(0.5)
        self.play(
            FadeOut(secante), FadeOut(punto_q), FadeOut(label_h),
            Create(tangente), run_time=1
        )
        secante.clear_updaters()
        punto_q.clear_updaters()
        label_h.clear_updaters()
        self.play(Write(formula), run_time=1)
        self.wait(2)


class Scene3_DerivadaParcial(ThreeDScene):
    def construct(self):
        titulo = Text("Derivadas Parciales", font_size=38, color=AZUL, weight=BOLD)
        self.add_fixed_in_frame_mobjects(titulo)
        titulo.to_edge(UP)

        axes = ThreeDAxes(
            x_range=(-2.5, 2.5, 1), y_range=(-2.5, 2.5, 1), z_range=(0, 4, 1),
            x_length=5, y_length=5, z_length=4,
            axis_config={"include_tip": True, "color": GRIS},
        )

        def f(x, y):
            return (x**2 + y**2) / 3

        surf = Surface(
            lambda u, v: axes.c2p(u, v, f(u, v)),
            u_range=(-2, 2), v_range=(-2, 2),
            resolution=(20, 20), fill_opacity=0.5,
            fill_color=AZUL, stroke_color="#1a5fa3", stroke_width=0.3,
        )

        # Plano y=1: Surface plana (obligatorio — no Rectangle/Polygon3D)
        plano_y = Surface(
            lambda u, v: axes.c2p(u, 1, v),
            u_range=(-2, 2), v_range=(0, 3),
            resolution=(2, 2),
            fill_color=VERDE, fill_opacity=0.25, stroke_width=0,
        )

        # Curva C1: y=1 fija, x varía
        c1 = ParametricFunction(
            lambda t: axes.c2p(t, 1, f(t, 1)),
            t_range=[-2, 2], color=VERDE, stroke_width=5
        )

        # Plano x=1: Surface plana
        plano_x = Surface(
            lambda u, v: axes.c2p(1, u, v),
            u_range=(-2, 2), v_range=(0, 3),
            resolution=(2, 2),
            fill_color=DORADO, fill_opacity=0.25, stroke_width=0,
        )

        # Curva C2: x=1 fija, y varía
        c2 = ParametricFunction(
            lambda t: axes.c2p(1, t, f(1, t)),
            t_range=[-2, 2], color=DORADO, stroke_width=5
        )

        # Labels fijos en frame
        lbl_c1 = Text("y = cte  →  C1", font_size=22, color=VERDE)
        lbl_c2 = Text("x = cte  →  C2", font_size=22, color=DORADO)
        lbl_dx = MathTex(r"\frac{\partial f}{\partial x}", font_size=26, color=VERDE)
        lbl_dy = MathTex(r"\frac{\partial f}{\partial y}", font_size=26, color=DORADO)
        self.add_fixed_in_frame_mobjects(lbl_c1, lbl_c2, lbl_dx, lbl_dy)
        lbl_c1.to_corner(UL).shift(DOWN * 0.8)
        lbl_c2.next_to(lbl_c1, DOWN, buff=0.2)
        lbl_dx.to_corner(UR).shift(DOWN * 0.8)
        lbl_dy.next_to(lbl_dx, DOWN, buff=0.2)

        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)

        self.play(Write(titulo))
        self.play(Create(axes), run_time=1)
        self.play(Create(surf), run_time=2)
        self.wait(0.5)
        self.play(FadeIn(plano_y), run_time=1)
        self.play(Create(c1), run_time=1.2)
        self.wait(0.5)
        self.play(FadeIn(plano_x), run_time=1)
        self.play(Create(c2), run_time=1.2)
        self.begin_ambient_camera_rotation(rate=0.12)
        self.wait(3.5)
        self.stop_ambient_camera_rotation()


class Scene4_Geometrica(ThreeDScene):
    def construct(self):
        titulo = Text("Interpretación Geométrica", font_size=38, color=AZUL, weight=BOLD)
        self.add_fixed_in_frame_mobjects(titulo)
        titulo.to_edge(UP)

        axes = ThreeDAxes(
            x_range=(-2.5, 2.5, 1), y_range=(-2.5, 2.5, 1), z_range=(0, 4, 1),
            x_length=5, y_length=5, z_length=4,
            axis_config={"include_tip": True, "color": GRIS},
        )

        def f(x, y):
            return (x**2 + y**2) / 3

        surf = Surface(
            lambda u, v: axes.c2p(u, v, f(u, v)),
            u_range=(-2, 2), v_range=(-2, 2),
            resolution=(20, 20), fill_opacity=0.6,
            fill_color=AZUL, stroke_color="#1a5fa3", stroke_width=0.5,
        )

        # Point P(1, 1, 2/3)
        a, b, z0 = 1, 1, f(1, 1)
        punto = Dot3D(point=axes.c2p(a, b, z0), color=DORADO, radius=0.08)

        # Curve C1: y=1 fixed, x varies → (t, 1, (t²+1)/3)
        c1 = ParametricFunction(
            lambda t: axes.c2p(t, b, f(t, b)),
            t_range=[-2, 2], color=VERDE, stroke_width=4
        )

        # Curve C2: x=1 fixed, y varies → (1, t, (1+t²)/3)
        c2 = ParametricFunction(
            lambda t: axes.c2p(a, t, f(a, t)),
            t_range=[-2, 2], color=DORADO, stroke_width=4
        )

        # Tangent T1 at P: direction (1, 0, ∂f/∂x|(1,1)) = (1, 0, 2/3)
        # ∂f/∂x = 2x/3 → at (1,1): 2/3
        df_dx_at_p = 2 * a / 3
        t1_start = axes.c2p(a - 0.8, b, z0 - 0.8 * df_dx_at_p)
        t1_end   = axes.c2p(a + 0.8, b, z0 + 0.8 * df_dx_at_p)
        t1 = Line3D(t1_start, t1_end, color=VERDE, thickness=0.04)

        # Tangent T2 at P: direction (0, 1, ∂f/∂y|(1,1)) = (0, 1, 2/3)
        # ∂f/∂y = 2y/3 → at (1,1): 2/3
        df_dy_at_p = 2 * b / 3
        t2_start = axes.c2p(a, b - 0.8, z0 - 0.8 * df_dy_at_p)
        t2_end   = axes.c2p(a, b + 0.8, z0 + 0.8 * df_dy_at_p)
        t2 = Line3D(t2_start, t2_end, color=DORADO, thickness=0.04)

        # Fixed frame labels
        label_c1 = Text("C1 (y=1 fija)", font_size=22, color=VERDE)
        label_c2 = Text("C2 (x=1 fija)", font_size=22, color=DORADO)
        label_p  = Text("P(1, 1, 2/3)", font_size=22, color=DORADO)
        label_z  = Text("z = (x²+y²)/3", font_size=22, color=BLANCO)
        self.add_fixed_in_frame_mobjects(label_c1, label_c2, label_p, label_z)
        label_c1.to_corner(UL).shift(DOWN * 0.8)
        label_c2.next_to(label_c1, DOWN, buff=0.2)
        label_p.to_corner(UR).shift(DOWN * 0.8)
        label_z.next_to(label_p, DOWN, buff=0.2)

        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)

        self.play(Write(titulo))
        self.play(Create(axes), run_time=1)
        self.play(Create(surf), run_time=2)
        self.play(FadeIn(punto), run_time=0.5)
        self.play(Create(c1), run_time=1)
        self.play(Create(c2), run_time=1)
        self.play(Create(t1), Create(t2), run_time=1)
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(4)
        self.stop_ambient_camera_rotation()


class Scene5_EjemploDefinicion(Scene):
    def construct(self):
        titulo = MathTex(r"f(x,y) = xy", font_size=52, color=BLANCO)
        titulo.to_edge(UP, buff=0.5)

        # Colorear f(x,y)=xy: x en AZUL, y en DORADO
        funcion = MathTex(r"f(x,y) = ", r"x", r"y", font_size=48)
        funcion[1].set_color(AZUL)
        funcion[2].set_color(DORADO)
        funcion.next_to(titulo, DOWN, buff=0.3)

        self.play(Write(titulo, run_time=1))
        self.play(Write(funcion, run_time=0.8))
        self.wait(0.4)

        # ---- Bloque ∂f/∂x ----
        lbl_dx = MathTex(r"\frac{\partial f}{\partial x} =", font_size=38, color=BLANCO)
        lbl_dx.next_to(funcion, DOWN, buff=0.6).to_edge(LEFT, buff=1)

        # Paso 1: lim [(x+h)y - xy] / h  — "y" en DORADO
        p1 = MathTex(r"\lim_{h \to 0} \frac{(x+h)", r"y", r"- x", r"y", r"}{h}",
                     font_size=32)
        p1[1].set_color(DORADO)
        p1[3].set_color(DORADO)
        p1.next_to(lbl_dx, DOWN, buff=0.3).align_to(lbl_dx, LEFT)

        # Paso 2: lim [hy] / h — separar "h" de \lim para colorear correctamente
        p2 = MathTex(r"\lim_{h \to 0} \frac{", r"h", r"y", r"}{h}", font_size=32)
        p2[1].set_color(VERDE)   # h numerador en VERDE
        p2[2].set_color(DORADO)  # y constante en DORADO
        p2.next_to(p1, DOWN, buff=0.25).align_to(lbl_dx, LEFT)

        # Paso 3: lim y
        p3 = MathTex(r"\lim_{h \to 0} ", r"y", font_size=32)
        p3[1].set_color(DORADO)
        p3.next_to(p2, DOWN, buff=0.25).align_to(lbl_dx, LEFT)

        # Resultado ∂f/∂x = y
        res_dx = MathTex(r"\frac{\partial f}{\partial x} = ", r"y", font_size=40)
        res_dx[0].set_color(BLANCO)
        res_dx[1].set_color(DORADO)
        res_dx.next_to(p3, DOWN, buff=0.3).align_to(lbl_dx, LEFT)
        rect_dx = SurroundingRectangle(res_dx, color=DORADO, buff=0.15)

        self.play(Write(lbl_dx))
        self.play(Write(p1, run_time=0.8)); self.wait(0.2)
        self.play(Write(p2, run_time=0.8)); self.wait(0.2)
        self.play(Write(p3, run_time=0.8)); self.wait(0.2)
        self.play(Write(res_dx, run_time=0.8))
        self.play(Create(rect_dx), run_time=0.5)
        self.wait(0.8)

        # ---- Bloque ∂f/∂y (reemplaza bloque ∂x) ----
        bloque_dx = VGroup(lbl_dx, p1, p2, p3, res_dx, rect_dx)
        self.play(FadeOut(bloque_dx), run_time=0.5)

        lbl_dy = MathTex(r"\frac{\partial f}{\partial y} =", font_size=38, color=BLANCO)
        lbl_dy.next_to(funcion, DOWN, buff=0.6).to_edge(LEFT, buff=1)

        # Paso 1: lim [x(y+k) - xy] / k — "x" en DORADO
        q1 = MathTex(r"\lim_{k \to 0} \frac{", r"x", r"(y+k) - ", r"x", r"y}{k}",
                     font_size=32)
        q1[1].set_color(DORADO)
        q1[3].set_color(DORADO)
        q1.next_to(lbl_dy, DOWN, buff=0.3).align_to(lbl_dy, LEFT)

        # Paso 2: lim [xk] / k — "k" en VERDE
        q2 = MathTex(r"\lim_{k \to 0} \frac{", r"x", r"k", r"}{k}", font_size=32)
        q2[1].set_color(DORADO)
        q2[2].set_color(VERDE)
        q2.next_to(q1, DOWN, buff=0.25).align_to(lbl_dy, LEFT)

        # Paso 3: lim x
        q3 = MathTex(r"\lim_{k \to 0} ", r"x", font_size=32)
        q3[1].set_color(DORADO)
        q3.next_to(q2, DOWN, buff=0.25).align_to(lbl_dy, LEFT)

        res_dy = MathTex(r"\frac{\partial f}{\partial y} = ", r"x", font_size=40)
        res_dy[0].set_color(BLANCO)
        res_dy[1].set_color(DORADO)
        res_dy.next_to(q3, DOWN, buff=0.3).align_to(lbl_dy, LEFT)
        rect_dy = SurroundingRectangle(res_dy, color=DORADO, buff=0.15)

        self.play(Write(lbl_dy))
        self.play(Write(q1, run_time=0.8)); self.wait(0.2)
        self.play(Write(q2, run_time=0.8)); self.wait(0.2)
        self.play(Write(q3, run_time=0.8)); self.wait(0.2)
        self.play(Write(res_dy, run_time=0.8))
        self.play(Create(rect_dy), run_time=0.5)
        self.wait(2.5)


class Scene6_ReglaDerivacion(Scene):
    def construct(self):
        titulo = Text("Reglas de Derivación", font_size=44, color=AZUL, weight=BOLD)
        titulo.to_edge(UP, buff=0.4)
        self.play(Write(titulo, run_time=1))
        self.wait(0.3)

        # ---- Regla 1: Potencia x^n → n·x^(n-1) ----
        # ReplacementTransform (NO TransformMatchingTex — token n es ambiguo)
        r1_label = Text("Potencia:", font_size=28, color=GRIS)
        r1_label.next_to(titulo, DOWN, buff=0.6).to_edge(LEFT, buff=1)

        r1_antes = MathTex(r"\frac{\partial}{\partial x}", r"x^n",
                           font_size=44)
        r1_antes[1].set_color(AZUL)
        r1_antes.next_to(r1_label, RIGHT, buff=0.4)

        r1_despues = MathTex(r"n \cdot x^{n-1}", font_size=44, color=DORADO)
        r1_despues.move_to(r1_antes[1].get_center())

        self.play(FadeIn(r1_label), Write(r1_antes, run_time=0.8))
        self.wait(0.3)
        # FadeOut del operador ∂/∂x (r1_antes[0]) para que no quede huérfano
        self.play(
            ReplacementTransform(r1_antes[1], r1_despues),
            FadeOut(r1_antes[0]),
            run_time=1
        )
        self.wait(0.5)

        # ---- Regla 2: Producto u(x)·v → u'(x)·v ----
        r2_label = Text("Producto:", font_size=28, color=GRIS)
        r2_label.next_to(r1_label, DOWN, buff=0.7)

        r2_antes = MathTex(r"\frac{\partial}{\partial x}\bigl[",
                           r"u(x)", r"\cdot", r"v", r"\bigr]", font_size=40)
        r2_antes[1].set_color(VERDE)
        r2_antes[3].set_color(DORADO)
        r2_antes.next_to(r2_label, RIGHT, buff=0.4)

        r2_despues = MathTex(r"\frac{\partial}{\partial x}\bigl[",
                             r"u(x)", r"\cdot", r"v", r"\bigr]",
                             r"= u'(x) \cdot", r"v", font_size=40)
        r2_despues[1].set_color(VERDE)
        r2_despues[3].set_color(DORADO)
        r2_despues[5].set_color(VERDE)
        r2_despues[6].set_color(DORADO)
        r2_despues.next_to(r2_label, RIGHT, buff=0.4)

        self.play(FadeIn(r2_label), Write(r2_antes, run_time=0.8))
        self.wait(0.3)
        self.play(TransformMatchingTex(r2_antes, r2_despues), run_time=1.2)
        self.wait(0.5)

        # ---- Regla 3: Cadena g(h(x)) → g'(h(x))·h'(x) ----
        r3_label = Text("Cadena:", font_size=28, color=GRIS)
        r3_label.next_to(r2_label, DOWN, buff=0.7)

        r3_antes = MathTex(r"\frac{\partial}{\partial x}",
                           r"g(h(x))", font_size=40)
        r3_antes[1].set_color(AZUL)
        r3_antes.next_to(r3_label, RIGHT, buff=0.4)

        r3_despues = MathTex(r"g'(h(x))", r"\cdot", r"h'(x)",
                             font_size=40)
        r3_despues[0].set_color(VERDE)
        r3_despues[2].set_color(DORADO)
        r3_despues.next_to(r3_label, RIGHT, buff=0.4).shift(RIGHT * 1.2)

        self.play(FadeIn(r3_label), Write(r3_antes, run_time=0.8))
        self.wait(0.3)
        self.play(
            ReplacementTransform(r3_antes[1], r3_despues),
            FadeOut(r3_antes[0]),
            run_time=1.2
        )
        self.wait(2.5)


class Scene7_EjemploRegla(Scene):
    def construct(self):
        titulo = Text("Ejemplo: Usando Reglas", font_size=44, color=AZUL, weight=BOLD)
        titulo.to_edge(UP, buff=0.4)

        funcion = MathTex(
            r"f(x,y) = -3x^2 + 2(y-3)^2",
            font_size=44, color=BLANCO
        )
        funcion.next_to(titulo, DOWN, buff=0.5)

        self.play(Write(titulo, run_time=1.5))
        self.play(Write(funcion, run_time=1))
        self.wait(0.5)

        # ---- ∂f/∂x ----
        lbl_dx = Text("Respecto a x  (tratar 2(y-3)² como constante):",
                       font_size=26, color=GRIS)
        lbl_dx.next_to(funcion, DOWN, buff=0.55).to_edge(LEFT, buff=0.8)

        step_dx1 = MathTex(
            r"\frac{\partial f}{\partial x} = \frac{\partial}{\partial x}(-3x^2) + \frac{\partial}{\partial x}\bigl[2(y-3)^2\bigr]",
            font_size=36, color=VERDE
        )
        step_dx1.next_to(lbl_dx, DOWN, buff=0.3).to_edge(LEFT, buff=0.8)

        step_dx2 = MathTex(
            r"= -6x + 0",
            font_size=36, color=VERDE
        )
        step_dx2.next_to(step_dx1, DOWN, buff=0.25).to_edge(LEFT, buff=0.8)

        res_dx = MathTex(r"\frac{\partial f}{\partial x} = -6x", font_size=40, color=DORADO)
        res_dx.next_to(step_dx2, DOWN, buff=0.25).to_edge(LEFT, buff=0.8)

        self.play(FadeIn(lbl_dx, shift=UP), run_time=0.6)
        self.play(Write(step_dx1, run_time=1))
        self.play(Write(step_dx2, run_time=0.8))
        self.play(Write(res_dx, run_time=0.8))
        self.wait(0.5)

        # ---- ∂f/∂y ----
        lbl_dy = Text("Respecto a y  (tratar -3x² como constante):",
                       font_size=26, color=GRIS)
        lbl_dy.next_to(res_dx, DOWN, buff=0.55).to_edge(LEFT, buff=0.8)

        step_dy1 = MathTex(
            r"\frac{\partial f}{\partial y} = \frac{\partial}{\partial y}(-3x^2) + \frac{\partial}{\partial y}\bigl[2(y-3)^2\bigr]",
            font_size=36, color=VERDE
        )
        step_dy1.next_to(lbl_dy, DOWN, buff=0.3).to_edge(LEFT, buff=0.8)

        step_dy2 = MathTex(
            r"= 0 + 2 \cdot 2(y-3) \cdot 1",
            font_size=36, color=VERDE
        )
        step_dy2.next_to(step_dy1, DOWN, buff=0.25).to_edge(LEFT, buff=0.8)

        res_dy = MathTex(r"\frac{\partial f}{\partial y} = 4(y-3)", font_size=40, color=DORADO)
        res_dy.next_to(step_dy2, DOWN, buff=0.25).to_edge(LEFT, buff=0.8)

        self.play(FadeIn(lbl_dy, shift=UP), run_time=0.6)
        self.play(Write(step_dy1, run_time=1))
        self.play(Write(step_dy2, run_time=0.8))
        self.play(Write(res_dy, run_time=0.8))
        self.wait(2.5)


# Función libre — evita capturar `self` en always_redraw
def _make_secante_3d(axes, f, x0, y0, h):
    if abs(h) < 1e-6:
        h = 1e-6
    m = (f(x0 + h, y0) - f(x0, y0)) / h
    z0 = f(x0, y0)
    start = axes.c2p(x0 - 0.8, y0, z0 - 0.8 * m)
    end   = axes.c2p(x0 + 0.8, y0, z0 + 0.8 * m)
    return Line3D(start, end, color=VERDE, thickness=0.03)


class SceneA_LimiteEnAccion(ThreeDScene):
    def construct(self):
        self.camera.background_color = WHITE

        titulo = Text("El Límite en Acción", font_size=36, color=AZUL, weight=BOLD)
        self.add_fixed_in_frame_mobjects(titulo)
        titulo.to_edge(UP)

        axes = ThreeDAxes(
            x_range=(-2.5, 2.5, 1), y_range=(-2.5, 2.5, 1), z_range=(0, 4, 1),
            x_length=5, y_length=5, z_length=4,
            axis_config={"include_tip": True, "color": BLACK},
        )

        def f(x, y):
            return (x**2 + y**2) / 3

        surf = Surface(
            lambda u, v: axes.c2p(u, v, f(u, v)),
            u_range=(-2, 2), v_range=(-2, 2),
            resolution=(20, 20), fill_opacity=0.5,
            fill_color=AZUL, stroke_color="#1a5fa3", stroke_width=0.3,
        )

        plano_y = Surface(
            lambda u, v: axes.c2p(u, 1, v),
            u_range=(-2, 2), v_range=(0, 3),
            resolution=(2, 2),
            fill_color=VERDE, fill_opacity=0.25, stroke_width=0,
        )

        c1 = ParametricFunction(
            lambda t: axes.c2p(t, 1, f(t, 1)),
            t_range=[-2, 2], color=VERDE, stroke_width=4,
        )

        x0, y0 = 1.0, 1.0
        punto_p = Dot3D(point=axes.c2p(x0, y0, f(x0, y0)), color="#B8860B", radius=0.08)

        h_tracker = ValueTracker(1.5)

        punto_q = always_redraw(
            lambda: Dot3D(
                point=axes.c2p(x0 + h_tracker.get_value(), y0,
                               f(x0 + h_tracker.get_value(), y0)),
                color=VERDE, radius=0.07,
            )
        )

        secante = always_redraw(
            lambda: _make_secante_3d(axes, f, x0, y0, h_tracker.get_value())
        )

        label_h = MathTex(r"h = 1.50", font_size=28, color=VERDE)
        label_h.to_corner(UR).shift(DOWN * 0.8)
        self.add_fixed_in_frame_mobjects(label_h)
        label_h.add_updater(lambda m: m.become(
            MathTex(r"h = " + f"{h_tracker.get_value():.2f}", font_size=28, color=VERDE)
            .to_corner(UR).shift(DOWN * 0.8)
        ))

        df_dx = 2 * x0 / 3
        z0_val = f(x0, y0)
        tang_start = axes.c2p(x0 - 1.0, y0, z0_val - 1.0 * df_dx)
        tang_end   = axes.c2p(x0 + 1.0, y0, z0_val + 1.0 * df_dx)
        tangente = Line3D(tang_start, tang_end, color="#B8860B", thickness=0.04)

        formula = MathTex(
            r"\frac{\partial f}{\partial x} = \lim_{h \to 0}"
            r"\frac{f(x+h,y)-f(x,y)}{h}",
            font_size=26, color=BLACK,
        ).to_corner(DR).shift(UP * 0.3)
        self.add_fixed_in_frame_mobjects(formula)

        self.set_camera_orientation(phi=70 * DEGREES, theta=90* DEGREES)

        self.play(Write(titulo))
        self.play(Create(axes), run_time=1)
        self.play(Create(surf), run_time=2)
        self.play(FadeIn(plano_y), run_time=1)
        self.play(Create(c1), run_time=1.2)
        self.play(FadeIn(punto_p), FadeIn(punto_q), Create(secante), run_time=0.8)
        self.wait(0.5)
        self.play(h_tracker.animate.set_value(0.01), run_time=3.5)
        self.wait(0.3)
        # Llamadas directas Python — NO dentro de self.play()
        secante.clear_updaters()
        punto_q.clear_updaters()
        label_h.clear_updaters()
        self.play(
            FadeOut(secante), FadeOut(punto_q), FadeOut(label_h),
            Create(tangente), run_time=1,
        )
        self.play(Write(formula), run_time=1)
        self.wait(2)


class SceneB_EjemploXY(ThreeDScene):
    def construct(self):
        self.camera.background_color = WHITE

        # ---- Parte 1: Superficie 3D z=xy ----
        titulo_3d = Text("f(x,y) = xy", font_size=36, color=BLACK, weight=BOLD)
        self.add_fixed_in_frame_mobjects(titulo_3d)
        titulo_3d.to_edge(UP)

        axes = ThreeDAxes(
            x_range=(-2.5, 2.5, 1), y_range=(-2.5, 2.5, 1), z_range=(-4, 4, 2),
            x_length=5, y_length=5, z_length=5,
            axis_config={"include_tip": True, "color": BLACK},
        )

        def f(x, y):
            return x * y

        surf = Surface(
            lambda u, v: axes.c2p(u, v, f(u, v)),
            u_range=(-2, 2), v_range=(-2, 2),
            resolution=(20, 20), fill_opacity=0.5,
            fill_color=AZUL, stroke_color="#1a5fa3", stroke_width=0.3,
        )

        plano_y = Surface(
            lambda u, v: axes.c2p(u, 1, v),
            u_range=(-2, 2), v_range=(-4, 4),
            resolution=(2, 2),
            fill_color=VERDE, fill_opacity=0.25, stroke_width=0,
        )
        c1 = ParametricFunction(
            lambda t: axes.c2p(t, 1, f(t, 1)),
            t_range=[-2, 2], color=VERDE, stroke_width=5,
        )

        plano_x = Surface(
            lambda u, v: axes.c2p(1, u, v),
            u_range=(-2, 2), v_range=(-4, 4),
            resolution=(2, 2),
            fill_color=DORADO, fill_opacity=0.25, stroke_width=0,
        )
        c2 = ParametricFunction(
            lambda t: axes.c2p(1, t, f(1, t)),
            t_range=[-2, 2], color=DORADO, stroke_width=5,
        )

        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)
        self.play(Write(titulo_3d))
        self.play(Create(axes), run_time=1)
        self.play(Create(surf), run_time=2)
        self.play(FadeIn(plano_y), run_time=0.8)
        self.play(Create(c1), run_time=1)
        self.play(FadeIn(plano_x), run_time=0.8)
        self.play(Create(c2), run_time=1)
        self.begin_ambient_camera_rotation(rate=0.10)
        self.wait(2.5)
        self.stop_ambient_camera_rotation()

        # ---- Transición 3D → 2D ----
        todo_3d = VGroup(surf, axes, plano_y, c1, plano_x, c2)
        self.play(FadeOut(todo_3d), run_time=1)
        # titulo_3d es fixed-in-frame → FadeOut en llamada separada
        self.play(FadeOut(titulo_3d), run_time=0.4)
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, run_time=0.8)

        # ---- Parte 2: Dos columnas simultáneas ----
        funcion_base = MathTex(r"f(x,y) = ", r"x", r"y", font_size=44, color=BLACK)
        funcion_base[1].set_color(AZUL)
        funcion_base[2].set_color(AZUL)
        funcion_base.to_edge(UP, buff=0.5)

        # --- Columna izquierda: ∂f/∂x ---
        lbl_dx = MathTex(r"\frac{\partial f}{\partial x} =", font_size=36, color=BLACK)
        lbl_dx.next_to(funcion_base, DOWN, buff=0.6).to_edge(LEFT, buff=0.5)

        p1 = MathTex(r"\lim_{h \to 0} \frac{(x+h)", r"y", r"- x", r"y", r"}{h}",
                     font_size=30, color=BLACK)
        p1[1].set_color("#B8860B")
        p1[3].set_color("#B8860B")
        p1.next_to(lbl_dx, DOWN, buff=0.25).align_to(lbl_dx, LEFT)

        p2 = MathTex(r"\lim_{h \to 0} \frac{", r"h", r"y", r"}{h}", font_size=30, color=BLACK)
        p2[1].set_color(VERDE)       # h numerador en VERDE
        p2[2].set_color("#B8860B")   # y constante en dorado oscuro
        p2.next_to(p1, DOWN, buff=0.2).align_to(lbl_dx, LEFT)

        p3 = MathTex(r"\lim_{h \to 0} ", r"y", font_size=30, color=BLACK)
        p3[1].set_color("#B8860B")
        p3.next_to(p2, DOWN, buff=0.2).align_to(lbl_dx, LEFT)

        res_dx = MathTex(r"\frac{\partial f}{\partial x} = ", r"y", font_size=38)
        res_dx[0].set_color(BLACK)
        res_dx[1].set_color("#B8860B")
        res_dx.next_to(p3, DOWN, buff=0.25).align_to(lbl_dx, LEFT)
        rect_dx = SurroundingRectangle(res_dx, color="#B8860B", buff=0.15)

        # --- Columna derecha: ∂f/∂y ---
        lbl_dy = MathTex(r"\frac{\partial f}{\partial y} =", font_size=36, color=BLACK)
        lbl_dy.next_to(funcion_base, DOWN, buff=0.6).to_edge(RIGHT, buff=3.5)

        q1 = MathTex(r"\lim_{k \to 0} \frac{", r"x", r"(y+k) - ", r"x", r"y}{k}",
                     font_size=30, color=BLACK)
        q1[1].set_color("#B8860B")
        q1[3].set_color("#B8860B")
        q1.next_to(lbl_dy, DOWN, buff=0.25).align_to(lbl_dy, LEFT)

        q2 = MathTex(r"\lim_{k \to 0} \frac{", r"x", r"k", r"}{k}", font_size=30, color=BLACK)
        q2[1].set_color("#B8860B")
        q2[2].set_color(VERDE)
        q2.next_to(q1, DOWN, buff=0.2).align_to(lbl_dy, LEFT)

        q3 = MathTex(r"\lim_{k \to 0} ", r"x", font_size=30, color=BLACK)
        q3[1].set_color("#B8860B")
        q3.next_to(q2, DOWN, buff=0.2).align_to(lbl_dy, LEFT)

        res_dy = MathTex(r"\frac{\partial f}{\partial y} = ", r"x", font_size=38)
        res_dy[0].set_color(BLACK)
        res_dy[1].set_color("#B8860B")
        res_dy.next_to(q3, DOWN, buff=0.25).align_to(lbl_dy, LEFT)
        rect_dy = SurroundingRectangle(res_dy, color="#B8860B", buff=0.15)

        # Animación simultánea paso a paso
        self.play(Write(funcion_base), run_time=1)
        self.play(Write(lbl_dx), Write(lbl_dy), run_time=0.8)
        self.play(Write(p1), Write(q1), run_time=0.9); self.wait(0.2)
        self.play(Write(p2), Write(q2), run_time=0.9); self.wait(0.2)
        self.play(Write(p3), Write(q3), run_time=0.9); self.wait(0.2)
        self.play(Write(res_dx), Write(res_dy), run_time=0.9)
        self.play(Create(rect_dx), Create(rect_dy), run_time=0.5)
        self.wait(2.5)
