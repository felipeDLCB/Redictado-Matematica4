"""
Presentación Manim Slides — Números Racionales (Teoría de Números)
Matemática 4 - TP3 - 2025

Ejercicios:
  - Ejercicio 9 (adicionales): Clausura de Q bajo +, -, ·, inverso
  - Ejercicio 10: Densidad de Q (propiedad arquimediana)

Renderizar:  manim render -qh presentacion.py NumerosRacionalesSlides
Presentar:   manim-slides NumerosRacionalesSlides
"""

from manim import *
from manim_slides import Slide

# ── Paleta de colores (consistente con las otras presentaciones) ───
BG       = "#0d1117"
CYAN     = "#00d4ff"
BLUE     = "#58a6ff"
WHITE_S  = "#f0f6fc"
RED_A    = "#f85149"
GREEN_A  = "#3fb950"
YELLOW_A = "#e3b341"
GRAY     = "#8b949e"
PURPLE   = "#bc8cff"
ORANGE   = "#f0883e"


class NumerosRacionalesSlides(Slide):

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

    def header_text(self, text, font_size=36):
        h = Text(text, font_size=font_size, color=CYAN, weight=BOLD)
        h.to_edge(UP, buff=0.5)
        return h

    def step_box(self, tex_string, color=BLUE):
        """Crea un recuadro con una ecuación destacada."""
        tex = MathTex(tex_string, font_size=44, color=WHITE_S)
        box = SurroundingRectangle(tex, color=color, buff=0.25, corner_radius=0.1)
        return VGroup(box, tex)

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 1 — Título
    # ══════════════════════════════════════════════════════════════

    def slide_titulo(self):
        title = Text("Números Racionales", font_size=52, color=CYAN, weight=BOLD)
        subtitle = Text("Propiedades y Demostraciones", font_size=28, color=GRAY)
        subtitle.next_to(title, DOWN, buff=0.4)

        line = Line(LEFT * 3, RIGHT * 3, color=BLUE, stroke_width=2)
        line.next_to(subtitle, DOWN, buff=0.3)

        mat = Text("Matemática 4 — Teoría de Números — 2025", font_size=20, color=GRAY)
        mat.next_to(line, DOWN, buff=0.3)

        self.play(FadeIn(title, shift=DOWN * 0.3))
        self.play(FadeIn(subtitle, shift=UP * 0.2), GrowFromCenter(line))
        self.play(FadeIn(mat))
        self.next_slide()

        self.play(FadeOut(VGroup(title, subtitle, line, mat)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 2 — Definición de número racional
    # ══════════════════════════════════════════════════════════════

    def slide_definicion(self):
        header = self.header_text("¿Qué es un número racional?")

        # Definición formal
        defn = MathTex(
            r"\mathbb{Q}", "=", r"\left\{", r"\frac{a}{b}",
            r"\;:\;", "a", r"\in", r"\mathbb{Z}", ",\;",
            "b", r"\in", r"\mathbb{Z}", ",\;", "b", r"\neq", "0",
            r"\right\}",
            font_size=42,
        )
        defn.set_color(WHITE_S)
        defn.next_to(header, DOWN, buff=0.5)
        defn[0].set_color(CYAN)        # Q
        defn[3].set_color(YELLOW_A)    # a/b
        defn[5].set_color(YELLOW_A)    # a
        defn[7].set_color(BLUE)        # Z
        defn[9].set_color(YELLOW_A)    # b
        defn[11].set_color(BLUE)       # Z
        defn[13].set_color(RED_A)      # b
        defn[14].set_color(RED_A)      # ≠
        defn[15].set_color(RED_A)      # 0

        # Texto explicativo
        explain = Text(
            "Un número racional es todo número que puede\n"
            "representarse como el cociente de dos enteros,\n"
            "con denominador distinto de cero.",
            font_size=22, color=WHITE_S, line_spacing=1.4,
        )
        explain.next_to(defn, DOWN, buff=0.4)

        # Ejemplos visuales
        examples_title = Text("Ejemplos:", font_size=24, color=GREEN_A, weight=BOLD)
        examples_title.next_to(explain, DOWN, buff=0.35)

        exs = VGroup(
            MathTex(r"\frac{3}{4}", font_size=36, color=WHITE_S),
            MathTex(r"-\frac{7}{2}", font_size=36, color=WHITE_S),
            MathTex(r"\frac{0}{5} = 0", font_size=36, color=WHITE_S),
            MathTex(r"\frac{8}{1} = 8", font_size=36, color=WHITE_S),
        ).arrange(RIGHT, buff=1.0)
        exs.next_to(examples_title, DOWN, buff=0.25)

        self.play(Write(header))
        self.play(Write(defn), run_time=2)
        self.next_slide()

        self.play(FadeIn(explain, shift=UP * 0.2))
        self.next_slide()

        self.play(FadeIn(examples_title))
        self.play(LaggedStart(*[FadeIn(e, shift=UP * 0.2) for e in exs], lag_ratio=0.2))
        self.next_slide()

        self.play(FadeOut(VGroup(header, defn, explain, examples_title, exs)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 3 — Z ⊂ Q
    # ══════════════════════════════════════════════════════════════

    def slide_z_subset_q(self):
        header = self.header_text("Los enteros están contenidos en Q")

        # Mostrar la inclusión
        inclusion = MathTex(
            r"\mathbb{Z}", r"\subset", r"\mathbb{Q}",
            font_size=56,
        )
        inclusion[0].set_color(BLUE)
        inclusion[1].set_color(WHITE_S)
        inclusion[2].set_color(CYAN)

        reason = MathTex(
            r"\text{Todo entero } n \text{ se puede escribir como } \frac{n}{1}",
            font_size=30, color=WHITE_S,
        )
        reason.next_to(inclusion, DOWN, buff=0.6)

        # Ejemplos animados: entero → fracción
        conversions = VGroup(
            MathTex("5", r"\;=\;", r"\frac{5}{1}", font_size=36),
            MathTex("-3", r"\;=\;", r"\frac{-3}{1}", font_size=36),
            MathTex("0", r"\;=\;", r"\frac{0}{1}", font_size=36),
        ).arrange(RIGHT, buff=1.5)
        conversions.next_to(reason, DOWN, buff=0.6)

        for conv in conversions:
            conv[0].set_color(BLUE)
            conv[2].set_color(CYAN)

        # Diagrama de Venn simple
        circle_z = Circle(radius=1.0, color=BLUE, stroke_width=2)
        circle_q = Circle(radius=1.8, color=CYAN, stroke_width=2)
        venn = VGroup(circle_z, circle_q).move_to(DOWN * 0.5)

        lbl_z = MathTex(r"\mathbb{Z}", font_size=30, color=BLUE)
        lbl_z.move_to(circle_z.get_center() + DOWN * 0.3)
        lbl_q = MathTex(r"\mathbb{Q}", font_size=30, color=CYAN)
        lbl_q.move_to(circle_q.get_center() + UP * 1.3)

        self.play(Write(header))
        self.play(Write(inclusion), run_time=1.5)
        self.next_slide()

        self.play(FadeIn(reason, shift=UP * 0.2))
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.2) for c in conversions], lag_ratio=0.3))
        self.next_slide()

        # Transicionar a Venn
        self.play(
            FadeOut(VGroup(inclusion, reason, conversions)),
        )
        self.play(
            Create(circle_q),
            Create(circle_z),
            FadeIn(lbl_z),
            FadeIn(lbl_q),
        )
        self.next_slide()

        self.play(FadeOut(VGroup(header, circle_z, circle_q, lbl_z, lbl_q)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 4 — Operaciones en Q (repaso rápido)
    # ══════════════════════════════════════════════════════════════

    def slide_operaciones_repaso(self):
        header = self.header_text("Operaciones entre Racionales")

        ops = VGroup(
            VGroup(
                Text("Suma", font_size=24, color=GREEN_A, weight=BOLD),
                MathTex(
                    r"\frac{a}{b} + \frac{c}{d} = \frac{ad + bc}{bd}",
                    font_size=32, color=WHITE_S,
                ),
            ).arrange(DOWN, buff=0.2),
            VGroup(
                Text("Resta", font_size=24, color=YELLOW_A, weight=BOLD),
                MathTex(
                    r"\frac{a}{b} - \frac{c}{d} = \frac{ad - bc}{bd}",
                    font_size=32, color=WHITE_S,
                ),
            ).arrange(DOWN, buff=0.2),
            VGroup(
                Text("Producto", font_size=24, color=BLUE, weight=BOLD),
                MathTex(
                    r"\frac{a}{b} \cdot \frac{c}{d} = \frac{ac}{bd}",
                    font_size=32, color=WHITE_S,
                ),
            ).arrange(DOWN, buff=0.2),
            VGroup(
                Text("Inverso", font_size=24, color=PURPLE, weight=BOLD),
                MathTex(
                    r"\left(\frac{a}{b}\right)^{-1} = \frac{b}{a}, \quad a \neq 0",
                    font_size=32, color=WHITE_S,
                ),
            ).arrange(DOWN, buff=0.2),
        )

        ops.arrange_in_grid(rows=2, cols=2, buff=(1.5, 0.8))
        ops.next_to(header, DOWN, buff=0.6)

        self.play(Write(header))
        self.play(
            LaggedStart(*[FadeIn(op, shift=UP * 0.3) for op in ops], lag_ratio=0.3),
            run_time=2.5,
        )
        self.next_slide()

        # Destacar la clave
        key = Text(
            "Clave: el resultado siempre es cociente de enteros\n"
            "→ las operaciones son cerradas en Q",
            font_size=22, color=YELLOW_A, line_spacing=1.3,
        )
        key.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(key, shift=UP * 0.2))
        self.next_slide()

        self.play(FadeOut(VGroup(header, ops, key)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 5 — Ejercicio 9: Enunciado
    # ══════════════════════════════════════════════════════════════

    def slide_ej9_enunciado(self):
        section = self.section_title(
            "Ejercicio 9 — Adicionales",
            "Clausura de operaciones en Q",
        )
        self.play(FadeIn(section, shift=DOWN * 0.3))
        self.next_slide()
        self.play(FadeOut(section))

        header = self.header_text("Ejercicio 9: Enunciado", font_size=32)

        enunciado = Text(
            "Sean u y v números racionales. Probar que:",
            font_size=26, color=WHITE_S,
        )
        enunciado.next_to(header, DOWN, buff=0.5)

        items = VGroup(
            MathTex(r"\text{(a)}\quad u + v \in \mathbb{Q} \;\text{ y }\; u - v \in \mathbb{Q}",
                    font_size=32, color=WHITE_S),
            MathTex(r"\text{(b)}\quad u \cdot v \in \mathbb{Q}",
                    font_size=32, color=WHITE_S),
            MathTex(r"\text{(c)}\quad \text{Si } u \neq 0, \;\; u^{-1} \in \mathbb{Q}",
                    font_size=32, color=WHITE_S),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        items.next_to(enunciado, DOWN, buff=0.5)

        self.play(Write(header))
        self.play(FadeIn(enunciado, shift=UP * 0.2))
        self.play(LaggedStart(*[FadeIn(it, shift=LEFT * 0.3) for it in items], lag_ratio=0.3))
        self.next_slide()

        self.play(FadeOut(VGroup(header, enunciado, items)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 6 — Ejercicio 9a: u+v ∈ Q y u-v ∈ Q
    # ══════════════════════════════════════════════════════════════

    def slide_ej9a(self):
        header = self.header_text("Ejercicio 9 (a): u + v ∈ Q  y  u − v ∈ Q", font_size=30)

        # Paso 1: Hipótesis
        step1_title = Text("Paso 1: Hipótesis", font_size=24, color=GREEN_A, weight=BOLD)
        step1_title.next_to(header, DOWN, buff=0.5).to_edge(LEFT, buff=1.0)

        hyp = MathTex(
            r"u = \frac{a}{b}", r",\quad", r"v = \frac{c}{d}",
            r",\quad", r"a,c \in \mathbb{Z}", r",\;", r"b,d \in \mathbb{Z}", r",\;",
            r"b \neq 0", r",\;", r"d \neq 0",
            font_size=28, color=WHITE_S,
        )
        hyp[0].set_color(CYAN)
        hyp[2].set_color(CYAN)
        hyp[8].set_color(RED_A)
        hyp[10].set_color(RED_A)
        hyp.next_to(step1_title, DOWN, buff=0.3).to_edge(LEFT, buff=1.0)

        self.play(Write(header))
        self.play(FadeIn(step1_title), Write(hyp))
        self.next_slide()

        # Paso 2: Suma
        step2_title = Text("Paso 2: Calculamos u + v", font_size=24, color=GREEN_A, weight=BOLD)
        step2_title.next_to(hyp, DOWN, buff=0.4).to_edge(LEFT, buff=1.0)

        suma_eq = MathTex(
            r"u + v", "=", r"\frac{a}{b}", "+", r"\frac{c}{d}",
            "=", r"\frac{ad + bc}{bd}",
            font_size=32, color=WHITE_S,
        )
        suma_eq[6].set_color(YELLOW_A)
        suma_eq.next_to(step2_title, DOWN, buff=0.3)

        self.play(FadeIn(step2_title), Write(suma_eq), run_time=2)
        self.next_slide()

        # Paso 3: Verificación
        step3_title = Text("Paso 3: Verificamos que es racional",
                           font_size=24, color=GREEN_A, weight=BOLD)
        step3_title.next_to(suma_eq, DOWN, buff=0.4).to_edge(LEFT, buff=1.0)

        verif = VGroup(
            MathTex(r"ad + bc \in \mathbb{Z}", r"\quad\text{(suma y producto de enteros)}",
                    font_size=26, color=WHITE_S),
            MathTex(r"bd \in \mathbb{Z}", r"\quad\text{(producto de enteros)}",
                    font_size=26, color=WHITE_S),
            MathTex(r"bd \neq 0", r"\quad\text{(pues } b \neq 0 \text{ y } d \neq 0\text{)}",
                    font_size=26, color=WHITE_S),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        verif[2][0].set_color(RED_A)
        verif.next_to(step3_title, DOWN, buff=0.3).to_edge(LEFT, buff=1.0)

        self.play(FadeIn(step3_title))
        self.play(LaggedStart(*[FadeIn(v, shift=LEFT * 0.2) for v in verif], lag_ratio=0.3))
        self.next_slide()

        # Conclusión suma
        concl_sum = MathTex(
            r"\therefore\; u + v = \frac{ad+bc}{bd} \in \mathbb{Q} \;\;\;\checkmark",
            font_size=30, color=GREEN_A,
        )
        concl_sum.next_to(verif, DOWN, buff=0.4)

        self.play(Write(concl_sum))
        self.next_slide()

        # Limpiar para la resta
        self.play(FadeOut(VGroup(
            step2_title, suma_eq, step3_title, verif, concl_sum,
        )))

        # Paso 4: Resta (análogo)
        step4_title = Text("Paso 4: Calculamos u − v (análogo)",
                           font_size=24, color=GREEN_A, weight=BOLD)
        step4_title.next_to(hyp, DOWN, buff=0.4).to_edge(LEFT, buff=1.0)

        resta_eq = MathTex(
            r"u - v", "=", r"\frac{a}{b}", "-", r"\frac{c}{d}",
            "=", r"\frac{ad - bc}{bd}",
            font_size=32, color=WHITE_S,
        )
        resta_eq[6].set_color(YELLOW_A)
        resta_eq.next_to(step4_title, DOWN, buff=0.3)

        verif_resta = VGroup(
            MathTex(r"ad - bc \in \mathbb{Z}", r"\quad\text{(resta de enteros)}",
                    font_size=26, color=WHITE_S),
            MathTex(r"bd \neq 0", r"\quad\text{(mismo argumento)}",
                    font_size=26, color=WHITE_S),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        verif_resta[1][0].set_color(RED_A)
        verif_resta.next_to(resta_eq, DOWN, buff=0.3).to_edge(LEFT, buff=1.0)

        concl_resta = MathTex(
            r"\therefore\; u - v = \frac{ad-bc}{bd} \in \mathbb{Q} \;\;\;\checkmark",
            font_size=30, color=GREEN_A,
        )
        concl_resta.next_to(verif_resta, DOWN, buff=0.4)

        self.play(FadeIn(step4_title), Write(resta_eq), run_time=1.5)
        self.next_slide()

        self.play(LaggedStart(*[FadeIn(v, shift=LEFT * 0.2) for v in verif_resta], lag_ratio=0.3))
        self.play(Write(concl_resta))
        self.next_slide()

        qed_box = self.step_box(r"u+v \in \mathbb{Q} \;\;\text{ y }\;\; u-v \in \mathbb{Q} \quad\quad\text{Q.E.D.}",
                                color=GREEN_A)
        qed_box.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(qed_box, shift=UP * 0.3))
        self.next_slide()

        self.play(FadeOut(VGroup(
            header, step1_title, hyp, step4_title, resta_eq,
            verif_resta, concl_resta, qed_box,
        )))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 7 — Ejercicio 9b: u·v ∈ Q
    # ══════════════════════════════════════════════════════════════

    def slide_ej9b(self):
        header = self.header_text("Ejercicio 9 (b): u · v ∈ Q", font_size=30)

        # Hipótesis (recordatorio compacto)
        hyp = MathTex(
            r"u = \frac{a}{b},\quad v = \frac{c}{d}",
            r",\quad a,c \in \mathbb{Z},\; b,d \in \mathbb{Z}^*",
            font_size=28, color=WHITE_S,
        )
        hyp[0].set_color(CYAN)
        hyp.next_to(header, DOWN, buff=0.5)

        self.play(Write(header), FadeIn(hyp))
        self.next_slide()

        # Cálculo
        step_title = Text("Calculamos el producto:", font_size=24, color=GREEN_A, weight=BOLD)
        step_title.next_to(hyp, DOWN, buff=0.5).to_edge(LEFT, buff=1.0)

        prod_eq = MathTex(
            r"u \cdot v", "=", r"\frac{a}{b}", r"\cdot", r"\frac{c}{d}",
            "=", r"\frac{a \cdot c}{b \cdot d}",
            "=", r"\frac{ac}{bd}",
            font_size=34, color=WHITE_S,
        )
        prod_eq[8].set_color(YELLOW_A)
        prod_eq.next_to(step_title, DOWN, buff=0.3)

        self.play(FadeIn(step_title))
        self.play(Write(prod_eq), run_time=2)
        self.next_slide()

        # Verificación
        verif_title = Text("Verificamos:", font_size=24, color=GREEN_A, weight=BOLD)
        verif_title.next_to(prod_eq, DOWN, buff=0.4).to_edge(LEFT, buff=1.0)

        verif = VGroup(
            MathTex(r"ac \in \mathbb{Z}",
                    r"\quad\text{(producto de enteros es cerrado en } \mathbb{Z}\text{)}",
                    font_size=26, color=WHITE_S),
            MathTex(r"bd \in \mathbb{Z}",
                    r"\quad\text{(producto de enteros es cerrado en } \mathbb{Z}\text{)}",
                    font_size=26, color=WHITE_S),
            MathTex(r"bd \neq 0",
                    r"\quad\text{(pues } b \neq 0 \text{ y } d \neq 0\text{)}",
                    font_size=26, color=WHITE_S),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        verif[2][0].set_color(RED_A)
        verif.next_to(verif_title, DOWN, buff=0.3).to_edge(LEFT, buff=1.0)

        self.play(FadeIn(verif_title))
        self.play(LaggedStart(*[FadeIn(v, shift=LEFT * 0.2) for v in verif], lag_ratio=0.3))
        self.next_slide()

        qed = MathTex(
            r"\therefore\; u \cdot v = \frac{ac}{bd} \in \mathbb{Q} \quad\quad\text{Q.E.D.}",
            font_size=32, color=GREEN_A,
        )
        qed.next_to(verif, DOWN, buff=0.5)
        self.play(Write(qed))
        self.next_slide()

        self.play(FadeOut(VGroup(header, hyp, step_title, prod_eq, verif_title, verif, qed)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 8 — Ejercicio 9c: u⁻¹ ∈ Q
    # ══════════════════════════════════════════════════════════════

    def slide_ej9c(self):
        header = self.header_text("Ejercicio 9 (c): Si u ≠ 0, u⁻¹ ∈ Q", font_size=30)

        # Hipótesis
        hyp = MathTex(
            r"u = \frac{a}{b}",
            r",\quad a \in \mathbb{Z},\; b \in \mathbb{Z}^*",
            r",\quad u \neq 0 \;\Rightarrow\; a \neq 0",
            font_size=28, color=WHITE_S,
        )
        hyp[0].set_color(CYAN)
        hyp[2].set_color(RED_A)
        hyp.next_to(header, DOWN, buff=0.5)

        self.play(Write(header), FadeIn(hyp))
        self.next_slide()

        # Cálculo del inverso
        step_title = Text("Calculamos el inverso multiplicativo:",
                          font_size=24, color=GREEN_A, weight=BOLD)
        step_title.next_to(hyp, DOWN, buff=0.5).to_edge(LEFT, buff=1.0)

        inv_eq = MathTex(
            r"u^{-1}", "=", r"\left(\frac{a}{b}\right)^{-1}",
            "=", r"\frac{b}{a}",
            font_size=36, color=WHITE_S,
        )
        inv_eq[4].set_color(YELLOW_A)
        inv_eq.next_to(step_title, DOWN, buff=0.3)

        self.play(FadeIn(step_title))
        self.play(Write(inv_eq), run_time=1.5)
        self.next_slide()

        # Verificación
        verif_title = Text("Verificamos que es racional:", font_size=24, color=GREEN_A, weight=BOLD)
        verif_title.next_to(inv_eq, DOWN, buff=0.4).to_edge(LEFT, buff=1.0)

        verif = VGroup(
            MathTex(r"b \in \mathbb{Z}",
                    r"\quad\text{(el numerador es entero)}",
                    font_size=26, color=WHITE_S),
            MathTex(r"a \in \mathbb{Z}",
                    r"\quad\text{(el denominador es entero)}",
                    font_size=26, color=WHITE_S),
            MathTex(r"a \neq 0",
                    r"\quad\text{(pues } u \neq 0 \text{, hipótesis clave)}",
                    font_size=26, color=WHITE_S),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        verif[2][0].set_color(RED_A)
        verif.next_to(verif_title, DOWN, buff=0.3).to_edge(LEFT, buff=1.0)

        self.play(FadeIn(verif_title))
        self.play(LaggedStart(*[FadeIn(v, shift=LEFT * 0.2) for v in verif], lag_ratio=0.3))
        self.next_slide()

        # Verificación del producto u · u⁻¹ = 1
        check_title = Text("Comprobación:", font_size=24, color=BLUE, weight=BOLD)
        check_title.next_to(verif, DOWN, buff=0.4).to_edge(LEFT, buff=1.0)

        check = MathTex(
            r"u \cdot u^{-1}", "=",
            r"\frac{a}{b} \cdot \frac{b}{a}",
            "=", r"\frac{ab}{ba}", "=", "1",
            font_size=30, color=WHITE_S,
        )
        check[6].set_color(GREEN_A)
        check.next_to(check_title, DOWN, buff=0.3)

        self.play(FadeIn(check_title), Write(check), run_time=1.5)
        self.next_slide()

        qed = MathTex(
            r"\therefore\; u^{-1} = \frac{b}{a} \in \mathbb{Q} \quad\quad\text{Q.E.D.}",
            font_size=32, color=GREEN_A,
        )
        qed.next_to(check, DOWN, buff=0.5)
        self.play(Write(qed))
        self.next_slide()

        self.play(FadeOut(VGroup(
            header, hyp, step_title, inv_eq, verif_title, verif,
            check_title, check, qed,
        )))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 9 — Resumen Ejercicio 9
    # ══════════════════════════════════════════════════════════════

    def slide_ej9_resumen(self):
        header = self.header_text("Ejercicio 9: Resumen")

        summary_title = Text(
            "Q es cerrado bajo las 4 operaciones fundamentales",
            font_size=26, color=WHITE_S,
        )
        summary_title.next_to(header, DOWN, buff=0.6)

        items = VGroup(
            MathTex(r"u + v \in \mathbb{Q}", font_size=36, color=GREEN_A),
            MathTex(r"u - v \in \mathbb{Q}", font_size=36, color=GREEN_A),
            MathTex(r"u \cdot v \in \mathbb{Q}", font_size=36, color=GREEN_A),
            MathTex(r"u^{-1} \in \mathbb{Q} \;\text{ (si } u \neq 0\text{)}",
                    font_size=36, color=GREEN_A),
        ).arrange(DOWN, buff=0.4)
        items.next_to(summary_title, DOWN, buff=0.5)

        # Checks animados
        checks = VGroup()
        for item in items:
            check = MathTex(r"\;\checkmark", font_size=36, color=CYAN)
            check.next_to(item, RIGHT, buff=0.5)
            checks.add(check)

        conclusion = Text(
            "→ Q tiene estructura de cuerpo",
            font_size=24, color=YELLOW_A,
        )
        conclusion.next_to(items, DOWN, buff=0.6)

        self.play(Write(header), FadeIn(summary_title))
        self.play(LaggedStart(*[FadeIn(it, shift=LEFT * 0.3) for it in items], lag_ratio=0.2))
        self.next_slide()

        self.play(LaggedStart(*[FadeIn(c, scale=1.5) for c in checks], lag_ratio=0.15))
        self.play(FadeIn(conclusion, shift=UP * 0.2))
        self.next_slide()

        self.play(FadeOut(VGroup(header, summary_title, items, checks, conclusion)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 10 — Ejercicio 10: Introducción densidad
    # ══════════════════════════════════════════════════════════════

    def slide_ej10_intro(self):
        section = self.section_title(
            "Ejercicio 10",
            "Densidad de los números racionales",
        )
        self.play(FadeIn(section, shift=DOWN * 0.3))
        self.next_slide()
        self.play(FadeOut(section))

        header = self.header_text("¿Qué es la densidad de Q?", font_size=32)

        explain = Text(
            "Entre cualquier par de números racionales\n"
            "siempre existe otro número racional.",
            font_size=24, color=WHITE_S, line_spacing=1.4,
        )
        explain.next_to(header, DOWN, buff=0.5)

        contrast = Text(
            "Esta propiedad NO la tienen los enteros:\n"
            "entre 3 y 4 no hay ningún entero.",
            font_size=22, color=GRAY, line_spacing=1.3,
        )
        contrast.next_to(explain, DOWN, buff=0.5)

        # Mini recta numérica de enteros
        nl_int = NumberLine(
            x_range=[0, 6, 1], length=8,
            color=GRAY,
            include_numbers=True,
            numbers_to_include=[0, 1, 2, 3, 4, 5, 6],
            font_size=24,
        ).shift(DOWN * 1.5)

        # Resaltar que entre 3 y 4 no hay nada
        brace_34 = BraceBetweenPoints(
            nl_int.n2p(3) + DOWN * 0.3,
            nl_int.n2p(4) + DOWN * 0.3,
            direction=DOWN, color=RED_A,
        )
        brace_label = MathTex(r"\text{¿?}", font_size=28, color=RED_A)
        brace_label.next_to(brace_34, DOWN, buff=0.15)

        self.play(Write(header))
        self.play(FadeIn(explain, shift=UP * 0.2))
        self.next_slide()

        self.play(FadeIn(contrast, shift=UP * 0.2))
        self.play(Create(nl_int))
        self.play(GrowFromCenter(brace_34), FadeIn(brace_label))
        self.next_slide()

        self.play(FadeOut(VGroup(header, explain, contrast, nl_int, brace_34, brace_label)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 11 — Ejercicio 10: Enunciado formal
    # ══════════════════════════════════════════════════════════════

    def slide_ej10_enunciado(self):
        header = self.header_text("Ejercicio 10: Enunciado", font_size=32)

        enunciado = MathTex(
            r"\text{Dados } a, b \in \mathbb{Q} \text{ con } a < b,",
            r"\text{ demostrar que existe } x \in \mathbb{Q}",
            r"\text{ tal que } a < x < b.",
            font_size=28, color=WHITE_S,
        )
        enunciado.arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        enunciado.next_to(header, DOWN, buff=0.6)

        # Idea visual — todo centrado
        idea_title = Text("Idea clave:", font_size=24, color=YELLOW_A, weight=BOLD)
        idea_title.next_to(enunciado, DOWN, buff=0.6)

        idea = MathTex(
            r"x = \frac{a + b}{2}",
            font_size=44, color=CYAN,
        )
        idea.next_to(idea_title, DOWN, buff=0.3)

        idea_sub = Text(
            "El promedio de dos racionales es racional\n"
            "y está entre ambos.",
            font_size=22, color=GRAY, line_spacing=1.3,
        )
        idea_sub.next_to(idea, DOWN, buff=0.4)

        # Centrar todo el bloque idea
        idea_group = VGroup(idea_title, idea, idea_sub)
        idea_group.move_to(ORIGIN).shift(DOWN * 0.8)

        self.play(Write(header))
        self.play(FadeIn(enunciado, shift=UP * 0.2))
        self.next_slide()

        self.play(FadeIn(idea_title), Write(idea), run_time=1.5)
        self.play(FadeIn(idea_sub, shift=UP * 0.2))
        self.next_slide()

        self.play(FadeOut(VGroup(header, enunciado, idea_title, idea, idea_sub)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 12 — Ejercicio 10: Demostración paso a paso
    # ══════════════════════════════════════════════════════════════

    def slide_ej10_demo(self):
        header = self.header_text("Ejercicio 10: Demostración", font_size=30)

        # Paso 1: Hipótesis
        p1_title = Text("Paso 1: Hipótesis", font_size=22, color=GREEN_A, weight=BOLD)
        p1_title.next_to(header, DOWN, buff=0.4).to_edge(LEFT, buff=0.8)
        p1 = MathTex(
            r"a, b \in \mathbb{Q},\quad a < b",
            font_size=28, color=WHITE_S,
        )
        p1.next_to(p1_title, DOWN, buff=0.2).to_edge(LEFT, buff=0.8)

        self.play(Write(header))
        self.play(FadeIn(p1_title), Write(p1))
        self.next_slide()

        # Paso 2: Definimos x
        p2_title = Text("Paso 2: Definimos el candidato",
                        font_size=22, color=GREEN_A, weight=BOLD)
        p2_title.next_to(p1, DOWN, buff=0.35).to_edge(LEFT, buff=0.8)
        p2 = MathTex(
            r"x = \frac{a + b}{2}",
            font_size=34, color=CYAN,
        )
        p2.next_to(p2_title, DOWN, buff=0.2)

        self.play(FadeIn(p2_title), Write(p2))
        self.next_slide()

        # Paso 3: x ∈ Q
        p3_title = Text("Paso 3: x ∈ Q (por ejercicio 9)",
                        font_size=22, color=GREEN_A, weight=BOLD)
        p3_title.next_to(p2, DOWN, buff=0.35).to_edge(LEFT, buff=0.8)

        p3_lines = VGroup(
            MathTex(r"a + b \in \mathbb{Q}", r"\quad\text{(clausura de la suma, ej. 9a)}",
                    font_size=24, color=WHITE_S),
            MathTex(r"\frac{a+b}{2} = (a+b) \cdot \frac{1}{2} \in \mathbb{Q}",
                    r"\quad\text{(clausura del producto, ej. 9b)}",
                    font_size=24, color=WHITE_S),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        p3_lines.next_to(p3_title, DOWN, buff=0.2).to_edge(LEFT, buff=0.8)

        self.play(FadeIn(p3_title))
        self.play(LaggedStart(*[FadeIn(l, shift=LEFT * 0.2) for l in p3_lines], lag_ratio=0.3))
        self.next_slide()

        # Paso 4: a < x < b
        p4_title = Text("Paso 4: Probamos a < x < b",
                        font_size=22, color=GREEN_A, weight=BOLD)
        p4_title.next_to(p3_lines, DOWN, buff=0.35).to_edge(LEFT, buff=0.8)

        # a < x
        p4a = VGroup(
            MathTex(r"a < b", r"\;\Rightarrow\;", r"2a < a + b",
                    r"\;\Rightarrow\;", r"a < \frac{a+b}{2} = x",
                    font_size=24, color=WHITE_S),
        )
        p4a[0][4].set_color(CYAN)

        # x < b
        p4b = VGroup(
            MathTex(r"a < b", r"\;\Rightarrow\;", r"a + b < 2b",
                    r"\;\Rightarrow\;", r"x = \frac{a+b}{2} < b",
                    font_size=24, color=WHITE_S),
        )
        p4b[0][4].set_color(CYAN)

        p4_group = VGroup(p4a, p4b).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        p4_group.next_to(p4_title, DOWN, buff=0.2).to_edge(LEFT, buff=0.8)

        self.play(FadeIn(p4_title))
        self.play(Write(p4a[0]), run_time=1.5)
        self.play(Write(p4b[0]), run_time=1.5)
        self.next_slide()

        # QED
        qed = MathTex(
            r"\therefore\; a < x = \frac{a+b}{2} < b,\quad x \in \mathbb{Q} \quad\quad\text{Q.E.D.}",
            font_size=30, color=GREEN_A,
        )
        qed.to_edge(DOWN, buff=0.5)
        self.play(Write(qed))
        self.next_slide()

        self.play(FadeOut(VGroup(
            header, p1_title, p1, p2_title, p2,
            p3_title, p3_lines, p4_title, p4_group, qed,
        )))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 13 — Ejercicio 10: Visualización en recta numérica
    # ══════════════════════════════════════════════════════════════

    def slide_ej10_recta(self):
        header = self.header_text("Visualización: Densidad de Q", font_size=30)

        self.play(Write(header))

        # Recta numérica
        nl = NumberLine(
            x_range=[0, 4, 0.5], length=10,
            color=WHITE_S,
            include_numbers=True,
            font_size=22,
        ).shift(DOWN * 0.5)

        self.play(Create(nl))

        # a y b
        a_val, b_val = 1.0, 3.0
        dot_a = Dot(nl.n2p(a_val), color=CYAN, radius=0.1)
        dot_b = Dot(nl.n2p(b_val), color=CYAN, radius=0.1)
        lbl_a = MathTex("a", font_size=28, color=CYAN).next_to(dot_a, UP, buff=0.2)
        lbl_b = MathTex("b", font_size=28, color=CYAN).next_to(dot_b, UP, buff=0.2)

        self.play(GrowFromCenter(dot_a), FadeIn(lbl_a))
        self.play(GrowFromCenter(dot_b), FadeIn(lbl_b))
        self.next_slide()

        # Primer punto medio
        mid1 = (a_val + b_val) / 2  # 2.0
        dot_x1 = Dot(nl.n2p(mid1), color=YELLOW_A, radius=0.1)
        lbl_x1 = MathTex(r"x_1 = \frac{a+b}{2}", font_size=22, color=YELLOW_A)
        lbl_x1.next_to(dot_x1, DOWN, buff=0.3)

        arrow1 = Arrow(
            start=lbl_x1.get_top(),
            end=dot_x1.get_bottom(),
            color=YELLOW_A, stroke_width=2, buff=0.05,
        )

        self.play(GrowFromCenter(dot_x1), FadeIn(lbl_x1), GrowArrow(arrow1))
        self.next_slide()

        # Segundo punto medio (entre a y x1)
        mid2 = (a_val + mid1) / 2  # 1.5
        dot_x2 = Dot(nl.n2p(mid2), color=GREEN_A, radius=0.08)
        lbl_x2 = MathTex(r"x_2", font_size=20, color=GREEN_A)
        lbl_x2.next_to(dot_x2, UP, buff=0.3)

        self.play(GrowFromCenter(dot_x2), FadeIn(lbl_x2))

        # Tercer punto medio (entre x1 y b)
        mid3 = (mid1 + b_val) / 2  # 2.5
        dot_x3 = Dot(nl.n2p(mid3), color=GREEN_A, radius=0.08)
        lbl_x3 = MathTex(r"x_3", font_size=20, color=GREEN_A)
        lbl_x3.next_to(dot_x3, UP, buff=0.3)

        self.play(GrowFromCenter(dot_x3), FadeIn(lbl_x3))
        self.next_slide()

        # Más puntos para mostrar la densidad
        extra_dots = VGroup()
        extra_mids = [
            (a_val + mid2) / 2,   # 1.25
            (mid2 + mid1) / 2,    # 1.75
            (mid1 + mid3) / 2,    # 2.25
            (mid3 + b_val) / 2,   # 2.75
        ]
        for m in extra_mids:
            d = Dot(nl.n2p(m), color=PURPLE, radius=0.06)
            extra_dots.add(d)

        self.play(LaggedStart(*[GrowFromCenter(d) for d in extra_dots], lag_ratio=0.1))

        # Aún más puntos
        many_dots = VGroup()
        import numpy as np
        np.random.seed(42)
        for _ in range(20):
            val = np.random.uniform(a_val + 0.05, b_val - 0.05)
            d = Dot(nl.n2p(val), color=ORANGE, radius=0.04, fill_opacity=0.7)
            many_dots.add(d)

        self.play(LaggedStart(*[FadeIn(d) for d in many_dots], lag_ratio=0.03))
        self.next_slide()

        # Texto final
        dense_text = Text(
            "Siempre podemos encontrar otro racional entre dos racionales.\n"
            "¡El proceso nunca termina!",
            font_size=22, color=YELLOW_A, line_spacing=1.3,
        )
        dense_text.to_edge(DOWN, buff=0.3)
        self.play(FadeIn(dense_text, shift=UP * 0.2))
        self.next_slide()

        self.play(FadeOut(VGroup(
            header, nl, dot_a, dot_b, lbl_a, lbl_b,
            dot_x1, lbl_x1, arrow1,
            dot_x2, lbl_x2, dot_x3, lbl_x3,
            extra_dots, many_dots, dense_text,
        )))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 15 — Cierre
    # ══════════════════════════════════════════════════════════════

    def slide_cierre(self):
        title = Text("Conclusiones", font_size=44, color=CYAN, weight=BOLD)

        bullets = VGroup(
            Text("• Q es cerrado bajo +, −, ×, y el inverso", font_size=24, color=WHITE_S),
            Text("  (Ejercicio 9: Q tiene estructura de cuerpo)", font_size=20, color=GRAY),
            Text("• Q es denso: entre dos racionales siempre hay otro", font_size=24, color=WHITE_S),
            Text("  (Ejercicio 10: propiedad arquimediana)", font_size=20, color=GRAY),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)

        group = VGroup(title, bullets).arrange(DOWN, buff=0.6)
        group.move_to(ORIGIN)

        line = Line(LEFT * 4, RIGHT * 4, color=BLUE, stroke_width=2)
        line.next_to(bullets, DOWN, buff=0.5)

        thanks = Text("¡Gracias!", font_size=36, color=CYAN, weight=BOLD)
        thanks.next_to(line, DOWN, buff=0.4)

        self.play(FadeIn(title, shift=DOWN * 0.3))
        self.play(LaggedStart(*[FadeIn(b, shift=LEFT * 0.3) for b in bullets], lag_ratio=0.2))
        self.next_slide()

        self.play(GrowFromCenter(line), FadeIn(thanks, shift=UP * 0.2))
        self.next_slide()

    # ══════════════════════════════════════════════════════════════
    #  CONSTRUCT — Hilo principal
    # ══════════════════════════════════════════════════════════════

    def construct(self):
        # Intro
        self.slide_titulo()
        self.slide_definicion()
        self.slide_z_subset_q()
        self.slide_operaciones_repaso()

        # Ejercicio 10
        self.slide_ej10_intro()
        self.slide_ej10_enunciado()
        self.slide_ej10_demo()
        self.slide_ej10_recta()

        # Ejercicio 9
        self.slide_ej9_enunciado()
        self.slide_ej9a()
        self.slide_ej9b()
        self.slide_ej9c()
        self.slide_ej9_resumen()

        # Cierre
        self.slide_cierre()
