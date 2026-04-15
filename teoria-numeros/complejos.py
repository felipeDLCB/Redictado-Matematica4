"""
Presentación Manim Slides — Números Complejos (Teoría de Números)
Matemática 4 - TP3 - 2025

Temas:
  1. Definición de números complejos
  2. Producto en forma binómica
  3. Cociente en forma binómica
  4. Módulo y conjugado
  5. Ejemplo resuelto de producto y cociente

Renderizar:  manim render -qh complejos.py NumerosComplejosSlides
Presentar:   manim-slides NumerosComplejosSlides
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


class NumerosComplejosSlides(Slide):

    def setup(self):
        self.camera.background_color = ManimColor(BG)

    def play(self, *args, **kwargs):
        """Todas las animaciones corren a 1.5× velocidad (run_time × 0.66)."""
        if "run_time" in kwargs:
            kwargs["run_time"] = kwargs["run_time"] * 0.66
        else:
            kwargs["run_time"] = 0.66
        super().play(*args, **kwargs)

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
        title = Text("Números Complejos", font_size=52, color=CYAN, weight=BOLD)
        subtitle = Text("Forma Binómica — Operaciones", font_size=28, color=GRAY)
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
    #  SLIDE 2 — Definición de número complejo
    # ══════════════════════════════════════════════════════════════

    def slide_definicion(self):
        header = self.header_text("¿Qué es un número complejo?")

        # Motivación: no existe raíz de -1 en los reales
        motiv = Text(
            "En los reales, no existe ningún número\n"
            "cuyo cuadrado sea negativo.",
            font_size=24, color=WHITE_S, line_spacing=1.4,
        )
        motiv.next_to(header, DOWN, buff=0.5)

        no_sol = MathTex(
            r"x^2 = -1", r"\quad \Longrightarrow \quad",
            r"\nexists \; x \in \mathbb{R}",
            font_size=38, color=WHITE_S,
        )
        no_sol[0].set_color(RED_A)
        no_sol[2].set_color(RED_A)
        no_sol.next_to(motiv, DOWN, buff=0.4)

        self.play(Write(header))
        self.play(FadeIn(motiv, shift=UP * 0.2))
        self.play(Write(no_sol), run_time=1.5)
        self.next_slide()

        # Definimos i
        self.play(FadeOut(VGroup(motiv, no_sol)))

        defn_i_label = Text(
            "Definimos la unidad imaginaria:",
            font_size=24, color=WHITE_S,
        )
        defn_i_label.next_to(header, DOWN, buff=0.5)

        defn_i = MathTex(
            r"i^2 = -1", r"\quad \Longleftrightarrow \quad",
            r"i = \sqrt{-1}",
            font_size=44, color=WHITE_S,
        )
        defn_i[0].set_color(PURPLE)
        defn_i[2].set_color(PURPLE)
        defn_i.next_to(defn_i_label, DOWN, buff=0.4)

        self.play(FadeIn(defn_i_label, shift=UP * 0.2))
        self.play(Write(defn_i), run_time=1.5)
        self.next_slide()

        # Forma binómica
        self.play(FadeOut(VGroup(defn_i_label, defn_i)))

        form_label = Text("Forma binómica:", font_size=24, color=GREEN_A, weight=BOLD)
        form_label.next_to(header, DOWN, buff=0.5)

        form = MathTex(
            r"z", "=", "a", "+", "b", r"\,i",
            font_size=52,
        )
        form[0].set_color(CYAN)
        form[2].set_color(YELLOW_A)
        form[4].set_color(ORANGE)
        form[5].set_color(PURPLE)
        form.next_to(form_label, DOWN, buff=0.4)

        parts = VGroup(
            MathTex(r"a", r"\;=\;\text{parte real } (\text{Re}(z))",
                    font_size=28, color=WHITE_S),
            MathTex(r"b", r"\;=\;\text{parte imaginaria } (\text{Im}(z))",
                    font_size=28, color=WHITE_S),
            MathTex(r"a, b \in \mathbb{R}",
                    font_size=28, color=WHITE_S),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        parts[0][0].set_color(YELLOW_A)
        parts[1][0].set_color(ORANGE)
        parts[2].set_color(GRAY)
        parts.next_to(form, DOWN, buff=0.5)

        # Conjunto C
        conj = MathTex(
            r"\mathbb{C}", "=",
            r"\left\{", "a", "+", "b", r"\,i",
            r"\;:\;", "a", ",", "b",
            r"\in", r"\mathbb{R}", r"\right\}",
            font_size=38, color=WHITE_S,
        )
        conj[0].set_color(CYAN)
        conj[3].set_color(YELLOW_A)
        conj[5].set_color(ORANGE)
        conj[6].set_color(PURPLE)
        conj[8].set_color(YELLOW_A)
        conj[10].set_color(ORANGE)
        conj[12].set_color(BLUE)
        conj.next_to(parts, DOWN, buff=0.5)

        self.play(FadeIn(form_label))
        self.play(Write(form), run_time=1.5)
        self.next_slide()

        self.play(FadeIn(parts, shift=UP * 0.2))
        self.next_slide()

        self.play(Write(conj), run_time=1.5)
        self.next_slide()

        # Ejemplos
        ex_title = Text("Ejemplos:", font_size=24, color=GREEN_A, weight=BOLD)
        ex_title.next_to(header, DOWN, buff=0.5)

        examples = VGroup(
            MathTex(r"3 + 2i", font_size=36, color=WHITE_S),
            MathTex(r"-1 + 4i", font_size=36, color=WHITE_S),
            MathTex(r"5 + 0i = 5", font_size=36, color=WHITE_S),
            MathTex(r"0 + 3i = 3i", font_size=36, color=WHITE_S),
        ).arrange(RIGHT, buff=1.0)
        examples.next_to(ex_title, DOWN, buff=0.3)

        note = Text(
            "Los reales son complejos con parte imaginaria 0",
            font_size=20, color=GRAY,
        )
        note.next_to(examples, DOWN, buff=0.4)

        self.play(FadeOut(VGroup(form_label, form, parts, conj)))
        self.play(FadeIn(ex_title))
        self.play(LaggedStart(*[FadeIn(e, shift=UP * 0.2) for e in examples], lag_ratio=0.2))
        self.play(FadeIn(note, shift=UP * 0.1))
        self.next_slide()

        self.play(FadeOut(VGroup(header, ex_title, examples, note)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 3 — Plano complejo (representación visual)
    # ══════════════════════════════════════════════════════════════

    def slide_plano_complejo(self):
        header = self.header_text("Plano Complejo (Gauss-Argand)")

        # Ejes
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            x_length=6,
            y_length=4.5,
            tips=True,
            axis_config={"color": GRAY, "stroke_width": 1.5},
        )
        axes.shift(DOWN * 0.3)

        x_label = MathTex(r"\text{Re}", font_size=24, color=YELLOW_A)
        x_label.next_to(axes.x_axis.get_end(), RIGHT, buff=0.15)
        y_label = MathTex(r"\text{Im}", font_size=24, color=ORANGE)
        y_label.next_to(axes.y_axis.get_end(), UP, buff=0.15)

        # Punto z = 3 + 2i
        dot = Dot(axes.c2p(3, 2), color=CYAN, radius=0.08)
        label_z = MathTex(r"z = 3 + 2i", font_size=24, color=CYAN)
        label_z.next_to(dot, UR, buff=0.15)

        # Líneas punteadas
        h_line = DashedLine(axes.c2p(0, 0), axes.c2p(3, 0), color=YELLOW_A, stroke_width=1.5)
        v_line = DashedLine(axes.c2p(3, 0), axes.c2p(3, 2), color=ORANGE, stroke_width=1.5)

        brace_re = Brace(h_line, DOWN, buff=0.1, color=YELLOW_A)
        brace_re_label = MathTex("3", font_size=22, color=YELLOW_A)
        brace_re_label.next_to(brace_re, DOWN, buff=0.1)

        brace_im = Brace(v_line, RIGHT, buff=0.1, color=ORANGE)
        brace_im_label = MathTex("2", font_size=22, color=ORANGE)
        brace_im_label.next_to(brace_im, RIGHT, buff=0.1)

        self.play(Write(header))
        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label), run_time=1.5)
        self.next_slide()

        self.play(Create(h_line), Create(v_line))
        self.play(
            FadeIn(brace_re), FadeIn(brace_re_label),
            FadeIn(brace_im), FadeIn(brace_im_label),
        )
        self.play(FadeIn(dot, scale=1.5), Write(label_z))
        self.next_slide()

        self.play(FadeOut(VGroup(
            header, axes, x_label, y_label, dot, label_z,
            h_line, v_line, brace_re, brace_re_label,
            brace_im, brace_im_label,
        )))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 4 — Producto en forma binómica
    # ══════════════════════════════════════════════════════════════

    def slide_producto(self):
        section = self.section_title(
            "Producto de Complejos",
            "Forma Binómica",
        )
        self.play(FadeIn(section, shift=DOWN * 0.3))
        self.next_slide()
        self.play(FadeOut(section))

        header = self.header_text("Producto en forma binómica", font_size=32)

        # Sean z1 y z2
        sean = MathTex(
            r"\text{Sean } z_1 = a + bi",
            r"\text{ y } z_2 = c + di",
            font_size=30, color=WHITE_S,
        )
        sean.next_to(header, DOWN, buff=0.5)

        self.play(Write(header))
        self.play(FadeIn(sean, shift=UP * 0.2))
        self.next_slide()

        # Paso 1: distributiva
        step1_label = Text("Aplicamos distributiva:", font_size=22, color=GREEN_A)
        step1_label.next_to(sean, DOWN, buff=0.4)

        dist = MathTex(
            r"z_1 \cdot z_2", "=",
            "(a + bi)", r"\cdot", "(c + di)",
            font_size=34, color=WHITE_S,
        )
        dist[2].set_color(CYAN)
        dist[4].set_color(PURPLE)
        dist.next_to(step1_label, DOWN, buff=0.25)

        expanded = MathTex(
            "=", "ac", "+", "adi", "+", "bci", "+", "bdi^2",
            font_size=34, color=WHITE_S,
        )
        expanded.next_to(dist, DOWN, buff=0.25)

        self.play(FadeIn(step1_label))
        self.play(Write(dist), run_time=1.5)
        self.play(Write(expanded), run_time=1.5)
        self.next_slide()

        # Paso 2: i² = -1
        step2_label = Text("Usamos i² = −1:", font_size=22, color=GREEN_A)
        step2_label.next_to(expanded, DOWN, buff=0.35)

        simplified = MathTex(
            "=", "ac", "+", "adi", "+", "bci", "+", "bd", r"(-1)",
            font_size=34, color=WHITE_S,
        )
        simplified[8].set_color(RED_A)
        simplified.next_to(step2_label, DOWN, buff=0.25)

        self.play(FadeIn(step2_label))
        self.play(Write(simplified), run_time=1.5)
        self.next_slide()

        # Paso 3: agrupar
        self.play(FadeOut(VGroup(
            sean, step1_label, dist, expanded, step2_label, simplified,
        )))

        step3_label = Text("Agrupamos parte real e imaginaria:", font_size=22, color=GREEN_A)
        step3_label.next_to(header, DOWN, buff=0.5)

        result = MathTex(
            r"z_1 \cdot z_2", "=",
            r"\underbrace{(ac - bd)}_{\text{Re}}",
            "+",
            r"\underbrace{(ad + bc)}_{\text{Im}}",
            r"\,i",
            font_size=36, color=WHITE_S,
        )
        result[2].set_color(YELLOW_A)
        result[4].set_color(ORANGE)
        result[5].set_color(PURPLE)
        result.next_to(step3_label, DOWN, buff=0.5)

        # Fórmula destacada
        formula_box = self.step_box(
            r"(a+bi)(c+di) = (ac-bd) + (ad+bc)\,i",
            color=CYAN,
        )
        formula_box.next_to(result, DOWN, buff=0.6)

        self.play(FadeIn(step3_label))
        self.play(Write(result), run_time=2)
        self.next_slide()

        self.play(FadeIn(formula_box, shift=UP * 0.2))
        self.next_slide()

        self.play(FadeOut(VGroup(header, step3_label, result, formula_box)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 5 — Módulo y Conjugado
    # ══════════════════════════════════════════════════════════════

    def slide_modulo_conjugado(self):
        section = self.section_title(
            "Módulo y Conjugado",
            "Propiedades fundamentales",
        )
        self.play(FadeIn(section, shift=DOWN * 0.3))
        self.next_slide()
        self.play(FadeOut(section))

        header = self.header_text("Conjugado de un complejo", font_size=32)

        # Conjugado
        sean = MathTex(
            r"\text{Si } z = a + bi",
            font_size=32, color=WHITE_S,
        )
        sean.next_to(header, DOWN, buff=0.5)

        conj_def = MathTex(
            r"\bar{z}", "=", "a", "-", "b", r"\,i",
            font_size=48,
        )
        conj_def[0].set_color(CYAN)
        conj_def[2].set_color(YELLOW_A)
        conj_def[4].set_color(ORANGE)
        conj_def[5].set_color(PURPLE)
        conj_def.next_to(sean, DOWN, buff=0.4)

        conj_explain = Text(
            "Se cambia el signo de la parte imaginaria.",
            font_size=22, color=GRAY,
        )
        conj_explain.next_to(conj_def, DOWN, buff=0.3)

        # Propiedad clave: z · z̄
        prop_label = Text("Propiedad clave:", font_size=22, color=GREEN_A, weight=BOLD)
        prop_label.next_to(conj_explain, DOWN, buff=0.4)

        prop = MathTex(
            r"z \cdot \bar{z}", "=",
            "(a+bi)(a-bi)", "=",
            r"a^2 + b^2",
            font_size=34, color=WHITE_S,
        )
        prop[0].set_color(CYAN)
        prop[4].set_color(GREEN_A)
        prop.next_to(prop_label, DOWN, buff=0.25)

        prop_note = Text(
            "¡Siempre da un número real no negativo!",
            font_size=20, color=YELLOW_A,
        )
        prop_note.next_to(prop, DOWN, buff=0.25)

        self.play(Write(header))
        self.play(FadeIn(sean, shift=UP * 0.2))
        self.play(Write(conj_def), run_time=1.5)
        self.play(FadeIn(conj_explain, shift=UP * 0.1))
        self.next_slide()

        self.play(FadeIn(prop_label))
        self.play(Write(prop), run_time=1.5)
        self.play(FadeIn(prop_note, shift=UP * 0.1))
        self.next_slide()

        self.play(FadeOut(VGroup(
            header, sean, conj_def, conj_explain,
            prop_label, prop, prop_note,
        )))

        # ── Módulo ──
        header2 = self.header_text("Módulo de un complejo", font_size=32)

        mod_def_label = MathTex(
            r"\text{Si } z = a + bi",
            font_size=32, color=WHITE_S,
        )
        mod_def_label.next_to(header2, DOWN, buff=0.5)

        mod_def = MathTex(
            r"|z|", "=", r"\sqrt{a^2 + b^2}",
            font_size=48,
        )
        mod_def[0].set_color(GREEN_A)
        mod_def[2].set_color(GREEN_A)
        mod_def.next_to(mod_def_label, DOWN, buff=0.4)

        mod_explain = Text(
            "Es la distancia del punto z al origen\n"
            "en el plano complejo.",
            font_size=22, color=GRAY, line_spacing=1.3,
        )
        mod_explain.next_to(mod_def, DOWN, buff=0.3)

        # Relación módulo-conjugado
        rel_label = Text("Relación con el conjugado:", font_size=22, color=GREEN_A, weight=BOLD)
        rel_label.next_to(mod_explain, DOWN, buff=0.4)

        rel = MathTex(
            r"|z|^2", "=", r"z \cdot \bar{z}", "=", r"a^2 + b^2",
            font_size=36, color=WHITE_S,
        )
        rel[0].set_color(GREEN_A)
        rel[2].set_color(CYAN)
        rel.next_to(rel_label, DOWN, buff=0.25)

        # Plano con módulo visual
        self.play(Write(header2))
        self.play(FadeIn(mod_def_label, shift=UP * 0.2))
        self.play(Write(mod_def), run_time=1.5)
        self.play(FadeIn(mod_explain, shift=UP * 0.1))
        self.next_slide()

        self.play(FadeIn(rel_label))
        self.play(Write(rel), run_time=1.5)
        self.next_slide()

        # Visualización en plano
        self.play(FadeOut(VGroup(
            mod_def_label, mod_def, mod_explain, rel_label, rel,
        )))

        axes = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 4, 1],
            x_length=5,
            y_length=4,
            tips=True,
            axis_config={"color": GRAY, "stroke_width": 1.5},
        )
        axes.shift(DOWN * 0.3)

        dot = Dot(axes.c2p(3, 2), color=CYAN, radius=0.08)
        label_z = MathTex(r"z = 3 + 2i", font_size=22, color=CYAN)
        label_z.next_to(dot, UR, buff=0.1)

        # Vector desde origen al punto
        arrow = Arrow(
            axes.c2p(0, 0), axes.c2p(3, 2),
            color=GREEN_A, stroke_width=3, buff=0,
        )
        mod_label = MathTex(
            r"|z| = \sqrt{13}",
            font_size=24, color=GREEN_A,
        )
        mod_label.next_to(arrow.get_center(), UL, buff=0.15)

        self.play(Create(axes), run_time=1.5)
        self.play(FadeIn(dot, scale=1.5), Write(label_z))
        self.play(GrowArrow(arrow), FadeIn(mod_label))
        self.next_slide()

        self.play(FadeOut(VGroup(header2, axes, dot, label_z, arrow, mod_label)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 6 — Cociente en forma binómica
    # ══════════════════════════════════════════════════════════════

    def slide_cociente(self):
        section = self.section_title(
            "Cociente de Complejos",
            "Forma Binómica",
        )
        self.play(FadeIn(section, shift=DOWN * 0.3))
        self.next_slide()
        self.play(FadeOut(section))

        header = self.header_text("Cociente en forma binómica", font_size=32)

        # Idea clave
        idea = Text(
            "Idea: multiplicar y dividir por el conjugado\n"
            "del denominador para eliminar la i del denominador.",
            font_size=22, color=WHITE_S, line_spacing=1.4,
        )
        idea.next_to(header, DOWN, buff=0.5)

        self.play(Write(header))
        self.play(FadeIn(idea, shift=UP * 0.2))
        self.next_slide()

        # Desarrollo paso a paso
        self.play(FadeOut(idea))

        step1_label = Text("Paso 1: multiplicamos por el conjugado", font_size=22, color=GREEN_A)
        step1_label.next_to(header, DOWN, buff=0.5)

        frac1 = MathTex(
            r"\frac{z_1}{z_2}", "=",
            r"\frac{a+bi}{c+di}", r"\cdot",
            r"\frac{c-di}{c-di}",
            font_size=36, color=WHITE_S,
        )
        frac1[4].set_color(PURPLE)
        frac1.next_to(step1_label, DOWN, buff=0.3)

        self.play(FadeIn(step1_label))
        self.play(Write(frac1), run_time=2)
        self.next_slide()

        # Paso 2: denominador
        step2_label = Text("Paso 2: el denominador queda real", font_size=22, color=GREEN_A)
        step2_label.next_to(frac1, DOWN, buff=0.35)

        denom = MathTex(
            r"(c+di)(c-di)", "=", r"c^2 + d^2",
            font_size=34, color=WHITE_S,
        )
        denom[2].set_color(GREEN_A)
        denom.next_to(step2_label, DOWN, buff=0.25)

        self.play(FadeIn(step2_label))
        self.play(Write(denom), run_time=1.5)
        self.next_slide()

        # Paso 3: resultado final
        self.play(FadeOut(VGroup(step1_label, frac1, step2_label, denom)))

        step3_label = Text("Resultado final:", font_size=22, color=GREEN_A, weight=BOLD)
        step3_label.next_to(header, DOWN, buff=0.5)

        result = MathTex(
            r"\frac{a+bi}{c+di}", "=",
            r"\frac{(ac+bd)}{c^2+d^2}", "+",
            r"\frac{(bc-ad)}{c^2+d^2}", r"\,i",
            font_size=36, color=WHITE_S,
        )
        result[2].set_color(YELLOW_A)
        result[4].set_color(ORANGE)
        result[5].set_color(PURPLE)
        result.next_to(step3_label, DOWN, buff=0.4)

        formula_box = self.step_box(
            r"\frac{z_1}{z_2} = \frac{z_1 \cdot \bar{z_2}}{|z_2|^2}",
            color=CYAN,
        )
        formula_box.next_to(result, DOWN, buff=0.5)

        tip = Text(
            "Recordá: multiplicar por el conjugado del denominador",
            font_size=20, color=GRAY,
        )
        tip.next_to(formula_box, DOWN, buff=0.3)

        self.play(FadeIn(step3_label))
        self.play(Write(result), run_time=2)
        self.next_slide()

        self.play(FadeIn(formula_box, shift=UP * 0.2))
        self.play(FadeIn(tip, shift=UP * 0.1))
        self.next_slide()

        self.play(FadeOut(VGroup(header, step3_label, result, formula_box, tip)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 7 — Ejemplo resuelto: Producto
    # ══════════════════════════════════════════════════════════════

    def slide_ejemplo_producto(self):
        section = self.section_title(
            "Ejemplo Resuelto",
            "Producto de complejos",
        )
        self.play(FadeIn(section, shift=DOWN * 0.3))
        self.next_slide()
        self.play(FadeOut(section))

        header = self.header_text("Ejemplo: Producto", font_size=32)

        # Enunciado
        enunc = MathTex(
            r"\text{Calcular } (3 + 2i) \cdot (1 - 4i)",
            font_size=34, color=WHITE_S,
        )
        enunc.next_to(header, DOWN, buff=0.5)

        self.play(Write(header))
        self.play(FadeIn(enunc, shift=UP * 0.2))
        self.next_slide()

        # Paso 1: distributiva
        p1 = Text("Paso 1: Distributiva", font_size=20, color=GREEN_A)
        p1.next_to(enunc, DOWN, buff=0.35)

        dist = MathTex(
            "=", r"3 \cdot 1", "+", r"3 \cdot (-4i)", "+",
            r"2i \cdot 1", "+", r"2i \cdot (-4i)",
            font_size=30, color=WHITE_S,
        )
        dist.next_to(p1, DOWN, buff=0.2)

        self.play(FadeIn(p1))
        self.play(Write(dist), run_time=1.5)
        self.next_slide()

        # Paso 2: operar
        p2 = Text("Paso 2: Operamos", font_size=20, color=GREEN_A)
        p2.next_to(dist, DOWN, buff=0.3)

        oper = MathTex(
            "=", "3", "-", "12i", "+", "2i", "-", "8i^2",
            font_size=30, color=WHITE_S,
        )
        oper.next_to(p2, DOWN, buff=0.2)

        self.play(FadeIn(p2))
        self.play(Write(oper), run_time=1.5)
        self.next_slide()

        # Paso 3: i² = -1
        p3 = Text("Paso 3: Reemplazamos i² = −1", font_size=20, color=GREEN_A)
        p3.next_to(oper, DOWN, buff=0.3)

        repl = MathTex(
            "=", "3", "-", "12i", "+", "2i", "-", "8(-1)",
            font_size=30, color=WHITE_S,
        )
        repl[7].set_color(RED_A)
        repl.next_to(p3, DOWN, buff=0.2)

        self.play(FadeIn(p3))
        self.play(Write(repl), run_time=1.5)
        self.next_slide()

        # Paso 4: agrupar
        self.play(FadeOut(VGroup(enunc, p1, dist, p2, oper, p3, repl)))

        p4 = Text("Paso 4: Agrupamos", font_size=20, color=GREEN_A)
        p4.next_to(header, DOWN, buff=0.5)

        group1 = MathTex(
            "=", r"(3 + 8)", "+", r"(-12 + 2)i",
            font_size=34, color=WHITE_S,
        )
        group1[1].set_color(YELLOW_A)
        group1[3].set_color(ORANGE)
        group1.next_to(p4, DOWN, buff=0.3)

        final = MathTex(
            "=", r"11", "-", r"10i",
            font_size=44, color=WHITE_S,
        )
        final[1].set_color(YELLOW_A)
        final[3].set_color(ORANGE)
        final.next_to(group1, DOWN, buff=0.4)

        result_box = SurroundingRectangle(final, color=CYAN, buff=0.25, corner_radius=0.1)

        self.play(FadeIn(p4))
        self.play(Write(group1), run_time=1.5)
        self.next_slide()

        self.play(Write(final), run_time=1.5)
        self.play(Create(result_box))
        self.next_slide()

        self.play(FadeOut(VGroup(header, p4, group1, final, result_box)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 8 — Ejemplo resuelto: Cociente
    # ══════════════════════════════════════════════════════════════

    def slide_ejemplo_cociente(self):
        section = self.section_title(
            "Ejemplo Resuelto",
            "Cociente de complejos",
        )
        self.play(FadeIn(section, shift=DOWN * 0.3))
        self.next_slide()
        self.play(FadeOut(section))

        header = self.header_text("Ejemplo: Cociente", font_size=32)

        # Enunciado
        enunc = MathTex(
            r"\text{Calcular } \frac{3 + 2i}{1 - 4i}",
            font_size=36, color=WHITE_S,
        )
        enunc.next_to(header, DOWN, buff=0.5)

        self.play(Write(header))
        self.play(FadeIn(enunc, shift=UP * 0.2))
        self.next_slide()

        # Paso 1: multiplicar por conjugado
        p1 = Text("Paso 1: Multiplicamos por el conjugado del denominador",
                   font_size=20, color=GREEN_A)
        p1.next_to(enunc, DOWN, buff=0.35)

        conj_step = MathTex(
            r"\frac{3+2i}{1-4i}", r"\cdot",
            r"\frac{1+4i}{1+4i}",
            font_size=34, color=WHITE_S,
        )
        conj_step[2].set_color(PURPLE)
        conj_step.next_to(p1, DOWN, buff=0.25)

        self.play(FadeIn(p1))
        self.play(Write(conj_step), run_time=1.5)
        self.next_slide()

        # Paso 2: numerador
        self.play(FadeOut(VGroup(enunc, p1, conj_step)))

        p2 = Text("Paso 2: Operamos el numerador", font_size=20, color=GREEN_A)
        p2.next_to(header, DOWN, buff=0.5)

        num = MathTex(
            r"(3+2i)(1+4i)", "=",
            r"3 + 12i + 2i + 8i^2",
            font_size=32, color=WHITE_S,
        )
        num.next_to(p2, DOWN, buff=0.25)

        num2 = MathTex(
            "=", r"3 + 14i + 8(-1)", "=",
            r"3 + 14i - 8",
            font_size=32, color=WHITE_S,
        )
        num2.next_to(num, DOWN, buff=0.2)

        num3 = MathTex(
            "=", r"-5 + 14i",
            font_size=36, color=CYAN,
        )
        num3.next_to(num2, DOWN, buff=0.2)

        self.play(FadeIn(p2))
        self.play(Write(num), run_time=1.5)
        self.play(Write(num2), run_time=1.5)
        self.play(Write(num3), run_time=1)
        self.next_slide()

        # Paso 3: denominador
        self.play(FadeOut(VGroup(p2, num, num2, num3)))

        p3 = Text("Paso 3: Operamos el denominador", font_size=20, color=GREEN_A)
        p3.next_to(header, DOWN, buff=0.5)

        den = MathTex(
            r"(1-4i)(1+4i)", "=",
            r"1^2 + 4^2", "=", "17",
            font_size=34, color=WHITE_S,
        )
        den[4].set_color(GREEN_A)
        den.next_to(p3, DOWN, buff=0.25)

        self.play(FadeIn(p3))
        self.play(Write(den), run_time=1.5)
        self.next_slide()

        # Paso 4: resultado
        p4 = Text("Resultado:", font_size=22, color=GREEN_A, weight=BOLD)
        p4.next_to(den, DOWN, buff=0.4)

        final = MathTex(
            r"\frac{3+2i}{1-4i}", "=",
            r"\frac{-5 + 14i}{17}", "=",
            r"-\frac{5}{17}", "+",
            r"\frac{14}{17}", r"\,i",
            font_size=36, color=WHITE_S,
        )
        final[4].set_color(YELLOW_A)
        final[6].set_color(ORANGE)
        final[7].set_color(PURPLE)
        final.next_to(p4, DOWN, buff=0.3)

        result_box = SurroundingRectangle(final[4:], color=CYAN, buff=0.2, corner_radius=0.1)

        self.play(FadeIn(p4))
        self.play(Write(final), run_time=2)
        self.play(Create(result_box))
        self.next_slide()

        self.play(FadeOut(VGroup(header, p3, den, p4, final, result_box)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 9 — Resumen de propiedades
    # ══════════════════════════════════════════════════════════════

    def slide_resumen(self):
        header = self.header_text("Resumen de Propiedades")

        props = VGroup(
            VGroup(
                Text("Conjugado", font_size=22, color=CYAN, weight=BOLD),
                MathTex(r"\overline{a+bi} = a - bi", font_size=30, color=WHITE_S),
            ).arrange(DOWN, buff=0.15),
            VGroup(
                Text("Módulo", font_size=22, color=GREEN_A, weight=BOLD),
                MathTex(r"|a+bi| = \sqrt{a^2+b^2}", font_size=30, color=WHITE_S),
            ).arrange(DOWN, buff=0.15),
            VGroup(
                Text("Producto", font_size=22, color=YELLOW_A, weight=BOLD),
                MathTex(
                    r"(a+bi)(c+di) = (ac-bd)+(ad+bc)i",
                    font_size=28, color=WHITE_S,
                ),
            ).arrange(DOWN, buff=0.15),
            VGroup(
                Text("Cociente", font_size=22, color=PURPLE, weight=BOLD),
                MathTex(
                    r"\frac{z_1}{z_2} = \frac{z_1 \cdot \bar{z_2}}{|z_2|^2}",
                    font_size=30, color=WHITE_S,
                ),
            ).arrange(DOWN, buff=0.15),
            VGroup(
                Text("Relación clave", font_size=22, color=ORANGE, weight=BOLD),
                MathTex(r"z \cdot \bar{z} = |z|^2", font_size=30, color=WHITE_S),
            ).arrange(DOWN, buff=0.15),
        )
        props.arrange_in_grid(rows=3, cols=2, buff=(2.0, 0.6))
        props.next_to(header, DOWN, buff=0.5)

        self.play(Write(header))
        self.play(
            LaggedStart(*[FadeIn(p, shift=UP * 0.3) for p in props], lag_ratio=0.25),
            run_time=3,
        )
        self.next_slide()

        self.play(FadeOut(VGroup(header, props)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 10 — Cierre
    # ══════════════════════════════════════════════════════════════

    def slide_cierre(self):
        title = Text("Números Complejos", font_size=44, color=CYAN, weight=BOLD)
        thanks = Text("¡Gracias!", font_size=36, color=WHITE_S)
        thanks.next_to(title, DOWN, buff=0.5)

        line = Line(LEFT * 2.5, RIGHT * 2.5, color=BLUE, stroke_width=2)
        line.next_to(thanks, DOWN, buff=0.3)

        self.play(FadeIn(title, shift=DOWN * 0.3))
        self.play(GrowFromCenter(line), FadeIn(thanks, shift=UP * 0.2))
        self.next_slide()

    # ══════════════════════════════════════════════════════════════
    #  CONSTRUCT — Hilo principal
    # ══════════════════════════════════════════════════════════════

    def construct(self):
        # Intro
        self.slide_titulo()
        self.slide_definicion()
        self.slide_plano_complejo()

        # Operaciones
        self.slide_producto()
        self.slide_modulo_conjugado()
        self.slide_cociente()

        # Ejemplos
        self.slide_ejemplo_producto()
        self.slide_ejemplo_cociente()

        # Cierre
        self.slide_resumen()
        self.slide_cierre()
