"""
Presentación Manim Slides — Independencia Lineal
Matemática 4 — Álgebra Lineal

Temas:
  1. Motivación
  2. Definición de Dependencia Lineal
  3. Definición de Independencia Lineal
  4. Teoremas (vector nulo, unicidad, T1.20, T1.23)
  5. Ejercicio 6(b) — Conjunto LI
  6. Ejercicio 6(a) — Conjunto LD

Renderizar:  manim render -ql presentacion.py IndependenciaLinealSlides
Presentar:   manim-slides IndependenciaLinealSlides
"""

from manim import *
from manim_slides import Slide

# ── Paleta consistente con presentaciones previas ──────────────────
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


class IndependenciaLinealSlides(Slide):

    def setup(self):
        self.camera.background_color = ManimColor(BG)

    def play(self, *args, **kwargs):
        if "run_time" in kwargs:
            kwargs["run_time"] = kwargs["run_time"] * 0.66
        else:
            kwargs["run_time"] = 0.66
        super().play(*args, **kwargs)

    # ─── helpers ───────────────────────────────────────────────────
    def section_title(self, text, sub=None):
        t = Text(text, font_size=44, color=CYAN, weight=BOLD)
        group = VGroup(t)
        if sub:
            s = Text(sub, font_size=26, color=GRAY)
            s.next_to(t, DOWN, buff=0.3)
            group.add(s)
        group.move_to(ORIGIN)
        return group

    def header_text(self, text, font_size=34):
        h = Text(text, font_size=font_size, color=CYAN, weight=BOLD)
        h.to_edge(UP, buff=0.5)
        return h

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 1 — Título
    # ══════════════════════════════════════════════════════════════

    def slide_titulo(self):
        title = Text("Independencia Lineal", font_size=58, color=CYAN, weight=BOLD)
        subtitle = Text("Espacios Vectoriales", font_size=32, color=GRAY)
        subtitle.next_to(title, DOWN, buff=0.4)

        line = Line(LEFT * 3.5, RIGHT * 3.5, color=BLUE, stroke_width=2)
        line.next_to(subtitle, DOWN, buff=0.3)

        mat = Text("Matemática 4 — Álgebra Lineal", font_size=24, color=GRAY)
        mat.next_to(line, DOWN, buff=0.3)

        self.play(FadeIn(title, shift=DOWN * 0.3))
        self.play(FadeIn(subtitle, shift=UP * 0.2), GrowFromCenter(line))
        self.play(FadeIn(mat))
        self.next_slide()
        self.play(FadeOut(VGroup(title, subtitle, line, mat)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 2 — Motivación
    # ══════════════════════════════════════════════════════════════

    def slide_motivacion(self):
        section = self.section_title("Motivación", "La idea de redundancia")
        self.play(FadeIn(section, shift=DOWN * 0.3))
        self.next_slide()
        self.play(FadeOut(section))

        header = self.header_text("¿Cuándo un vector está \"de más\"?")
        self.play(FadeIn(header, shift=DOWN * 0.2))

        ejemplo = MathTex(
            r"S = \{(2,1),\ (1,-2),\ (1,3)\} \subset \mathbb{R}^2",
            font_size=36, color=WHITE_S,
        )
        ejemplo.next_to(header, DOWN, buff=0.7)
        self.play(Write(ejemplo))
        self.next_slide()

        observ = MathTex(
            r"(1,-2) + (1,3) = (2,1)",
            font_size=34, color=ORANGE,
        )
        observ.next_to(ejemplo, DOWN, buff=0.5)
        self.play(Write(observ))
        self.next_slide()

        conclu = Text(
            "(2,1) no aporta nada nuevo: es redundante.",
            font_size=26, color=GREEN_A,
        )
        conclu.next_to(observ, DOWN, buff=0.5)
        self.play(FadeIn(conclu, shift=UP * 0.2))
        self.next_slide()

        pivote = Text(
            "¿Cómo formalizamos esto?",
            font_size=28, color=YELLOW_A, weight=BOLD,
        )
        pivote.next_to(conclu, DOWN, buff=0.7)
        self.play(FadeIn(pivote))
        self.next_slide()

        self.play(FadeOut(VGroup(header, ejemplo, observ, conclu, pivote)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 3 — La combinación lineal nula (concepto bisagra)
    # ══════════════════════════════════════════════════════════════

    def slide_concepto_nula(self):
        section = self.section_title("La combinación lineal nula", "El concepto clave")
        self.play(FadeIn(section, shift=DOWN * 0.3))
        self.next_slide()
        self.play(FadeOut(section))

        header = self.header_text("¿Cuándo una combinación da el vector nulo?")
        self.play(FadeIn(header, shift=DOWN * 0.2))

        setup = MathTex(
            r"v_1, v_2, \ldots, v_r \in V \quad \text{y escalares} \quad c_1, c_2, \ldots, c_r",
            font_size=30, color=WHITE_S,
        )
        setup.next_to(header, DOWN, buff=0.6)
        self.play(FadeIn(setup))
        self.next_slide()

        formula = MathTex(
            r"c_1 v_1 + c_2 v_2 + \cdots + c_r v_r = 0",
            font_size=38, color=CYAN,
        )
        formula.next_to(setup, DOWN, buff=0.5)
        self.play(Write(formula))
        self.next_slide()

        trivial_label = Text("Solución trivial:", font_size=24, color=GRAY)
        trivial_eq = MathTex(
            r"c_1 = c_2 = \cdots = c_r = 0",
            font_size=30, color=GRAY,
        )
        trivial_note = Text(
            "(siempre funciona — no dice nada del conjunto)",
            font_size=20, color=GRAY,
        )
        trivial_group = VGroup(trivial_label, trivial_eq, trivial_note).arrange(DOWN, buff=0.15)
        trivial_group.next_to(formula, DOWN, buff=0.5)
        self.play(FadeIn(trivial_group, shift=UP * 0.2))
        self.next_slide()

        pregunta = Text(
            "Pregunta clave: ¿existe alguna solución NO trivial?",
            font_size=26, color=YELLOW_A, weight=BOLD,
        )
        pregunta.next_to(trivial_group, DOWN, buff=0.5)
        self.play(FadeIn(pregunta))
        self.next_slide()

        self.play(FadeOut(VGroup(header, setup, formula, trivial_group, pregunta)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 4 — LD vs LI: el contraste
    # ══════════════════════════════════════════════════════════════

    def slide_ld_li_contraste(self):
        section = self.section_title(
            "Dependencia vs Independencia Lineal",
            "Dos respuestas a la misma pregunta",
        )
        self.play(FadeIn(section, shift=DOWN * 0.3))
        self.next_slide()
        self.play(FadeOut(section))

        header = self.header_text("¿Existe combinación nula no trivial?")
        self.play(FadeIn(header, shift=DOWN * 0.2))

        divider = Line(UP * 2.5, DOWN * 2.5, color=GRAY, stroke_width=1)
        divider.set_y(-0.3)

        # ── Columna izquierda: LD ─────────────────────────────────
        ld_title = Text("SÍ", font_size=40, color=ORANGE, weight=BOLD)
        ld_label = Text("Linealmente Dependientes", font_size=22, color=ORANGE, weight=BOLD)
        ld_formula = MathTex(
            r"\exists\, c_i\ \text{no todos } 0\, :",
            r"\sum c_i v_i = 0",
            font_size=26, color=WHITE_S,
        )
        ld_formula.arrange(DOWN, buff=0.2)
        ld_meaning = Text("hay redundancia", font_size=22, color=ORANGE)

        ld_col = VGroup(ld_title, ld_label, ld_formula, ld_meaning).arrange(DOWN, buff=0.35)
        ld_col.move_to(LEFT * 3.3 + DOWN * 0.3)

        # ── Columna derecha: LI ───────────────────────────────────
        li_title = Text("NO", font_size=40, color=GREEN_A, weight=BOLD)
        li_label = Text("Linealmente Independientes", font_size=22, color=GREEN_A, weight=BOLD)
        li_formula = MathTex(
            r"\sum c_i v_i = 0",
            r"\Longrightarrow\ \text{todos } c_i = 0",
            font_size=26, color=WHITE_S,
        )
        li_formula.arrange(DOWN, buff=0.2)
        li_meaning = Text("ningún redundante", font_size=22, color=GREEN_A)

        li_col = VGroup(li_title, li_label, li_formula, li_meaning).arrange(DOWN, buff=0.35)
        li_col.move_to(RIGHT * 3.3 + DOWN * 0.3)

        self.play(Create(divider))
        self.play(FadeIn(ld_col, shift=RIGHT * 0.2), FadeIn(li_col, shift=LEFT * 0.2))
        self.next_slide()

        self.play(FadeOut(VGroup(header, divider, ld_col, li_col)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 5 — Teorema: vector nulo → LD
    # ══════════════════════════════════════════════════════════════

    def slide_teo_nulo(self):
        section = self.section_title("Teorema 1", "Conjuntos con el vector nulo")
        self.play(FadeIn(section, shift=DOWN * 0.3))
        self.next_slide()
        self.play(FadeOut(section))

        header = self.header_text("Si 0 ∈ S, entonces S es Linealmente Dependiente")
        self.play(FadeIn(header, shift=DOWN * 0.2))

        enunciado = Text(
            "Todo conjunto que contiene al vector nulo es Linealmente Dependiente.",
            font_size=24, color=WHITE_S,
        )
        enunciado.next_to(header, DOWN, buff=0.5).set_x(0)
        self.play(FadeIn(enunciado))
        self.next_slide()

        prueba_titulo = Text("Idea:", font_size=24, color=CYAN, weight=BOLD)
        prueba_titulo.next_to(enunciado, DOWN, buff=0.5).set_x(0)
        self.play(FadeIn(prueba_titulo))

        prueba = MathTex(
            r"S = \{0,\ v_1,\ v_2,\ \ldots,\ v_r\}",
            font_size=32, color=WHITE_S,
        )
        prueba.next_to(prueba_titulo, DOWN, buff=0.3).set_x(0)
        self.play(Write(prueba))
        self.next_slide()

        comb = MathTex(
            r"5 \cdot 0 + 0 \cdot v_1 + \cdots + 0 \cdot v_r = 0",
            font_size=32, color=YELLOW_A,
        )
        comb.next_to(prueba, DOWN, buff=0.4).set_x(0)
        self.play(Write(comb))
        self.next_slide()

        conclu = Text(
            "Coeficiente no nulo (5) → combinación nula no trivial → Linealmente Dependiente",
            font_size=22, color=ORANGE, weight=BOLD,
        )
        conclu.next_to(comb, DOWN, buff=0.5).set_x(0)
        self.play(FadeIn(conclu, shift=UP * 0.2))
        self.next_slide()

        self.play(FadeOut(VGroup(header, enunciado, prueba_titulo, prueba, comb, conclu)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 6 — Teorema: unicidad
    # ══════════════════════════════════════════════════════════════

    def slide_teo_unicidad(self):
        section = self.section_title("Teorema 2", "Unicidad de la combinación")
        self.play(FadeIn(section, shift=DOWN * 0.3))
        self.next_slide()
        self.play(FadeOut(section))

        header = self.header_text("Combinación lineal única")
        self.play(FadeIn(header, shift=DOWN * 0.2))

        enunciado = VGroup(
            Text("Si S es Linealmente Independiente, todo vector de gen(S)", font_size=24, color=WHITE_S),
            Text("se expresa de UNA sola forma como combinación lineal de S.", font_size=24, color=WHITE_S),
        ).arrange(DOWN, buff=0.2)
        enunciado.next_to(header, DOWN, buff=0.5)
        self.play(FadeIn(enunciado))
        self.next_slide()

        suponer = Text("Supongamos dos representaciones:", font_size=24, color=CYAN)
        suponer.next_to(enunciado, DOWN, buff=0.5)
        self.play(FadeIn(suponer))

        repr1 = MathTex(
            r"v = a_1 v_1 + \cdots + a_r v_r",
            r"\quad\text{y}\quad",
            r"v = b_1 v_1 + \cdots + b_r v_r",
            font_size=30, color=WHITE_S,
        )
        repr1.next_to(suponer, DOWN, buff=0.3)
        self.play(Write(repr1))
        self.next_slide()

        resta = MathTex(
            r"0 = (a_1 - b_1) v_1 + \cdots + (a_r - b_r) v_r",
            font_size=32, color=YELLOW_A,
        )
        resta.next_to(repr1, DOWN, buff=0.3)
        self.play(Write(resta))
        self.next_slide()

        conclu = MathTex(
            r"\text{Linealmente Independiente} \Rightarrow a_i - b_i = 0 \Rightarrow a_i = b_i \quad \blacksquare",
            font_size=26, color=GREEN_A,
        )
        conclu.next_to(resta, DOWN, buff=0.3)
        self.play(Write(conclu))
        self.next_slide()

        self.play(FadeOut(VGroup(header, enunciado, suponer, repr1, resta, conclu)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 7 — Teorema 1.20
    # ══════════════════════════════════════════════════════════════

    def slide_teo_120(self):
        section = self.section_title("Teorema 3", "Más vectores que la dimensión")
        self.play(FadeIn(section, shift=DOWN * 0.3))
        self.next_slide()
        self.play(FadeOut(section))

        header = self.header_text("Si m > n, entonces son Linealmente Dependientes")
        self.play(FadeIn(header, shift=DOWN * 0.2))

        enunciado = VGroup(
            Text("Sea V un espacio vectorial con base de n vectores.", font_size=24, color=WHITE_S),
            Text("Todo conjunto de m > n vectores de V es Linealmente Dependiente.", font_size=24, color=WHITE_S),
        ).arrange(DOWN, buff=0.2)
        enunciado.next_to(header, DOWN, buff=0.5)
        self.play(FadeIn(enunciado))
        self.next_slide()

        # Visualización: 3 vectores en R²
        ejes = NumberPlane(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1],
            background_line_style={"stroke_color": GRAY, "stroke_opacity": 0.3, "stroke_width": 1},
            x_length=4.5, y_length=4.5,
        )
        ejes.next_to(enunciado, DOWN, buff=0.4).shift(LEFT * 2.5)

        v1 = Arrow(ejes.c2p(0, 0), ejes.c2p(2, 0), color=CYAN, buff=0)
        v2 = Arrow(ejes.c2p(0, 0), ejes.c2p(0, 2), color=BLUE, buff=0)
        v3 = Arrow(ejes.c2p(0, 0), ejes.c2p(1.5, 1.5), color=YELLOW_A, buff=0)

        l1 = MathTex(r"v_1", font_size=24, color=CYAN).next_to(v1.get_end(), DOWN, buff=0.1)
        l2 = MathTex(r"v_2", font_size=24, color=BLUE).next_to(v2.get_end(), LEFT, buff=0.1)
        l3 = MathTex(r"v_3", font_size=24, color=YELLOW_A).next_to(v3.get_end(), UR, buff=0.1)

        nota = VGroup(
            Text("3 vectores en R² (n=2)", font_size=22, color=WHITE_S),
            Text("→ Linealmente", font_size=22, color=ORANGE, weight=BOLD),
            Text("Dependientes", font_size=22, color=ORANGE, weight=BOLD),
        ).arrange(DOWN, buff=0.15)
        nota.next_to(ejes, RIGHT, buff=0.6)

        self.play(Create(ejes))
        self.play(GrowArrow(v1), GrowArrow(v2), FadeIn(l1, l2))
        self.next_slide()
        self.play(GrowArrow(v3), FadeIn(l3))
        self.play(FadeIn(nota))
        self.next_slide()

        self.play(FadeOut(VGroup(header, enunciado, ejes, v1, v2, v3, l1, l2, l3, nota)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 8 — Teorema 1.23
    # ══════════════════════════════════════════════════════════════

    def slide_teo_123(self):
        section = self.section_title("Teorema 4", "n vectores Linealmente Independientes en dimensión n")
        self.play(FadeIn(section, shift=DOWN * 0.3))
        self.next_slide()
        self.play(FadeOut(section))

        header = self.header_text("n vectores Linealmente Independientes forman base")
        self.play(FadeIn(header, shift=DOWN * 0.2))

        enunciado = VGroup(
            Text("Si dim(V) = n, entonces:", font_size=26, color=WHITE_S),
        )
        enunciado.next_to(header, DOWN, buff=0.5)
        self.play(FadeIn(enunciado))

        items = VGroup(
            Text("• n vectores Linealmente Independientes generan V (forman base).", font_size=22, color=GREEN_A),
            Text("• n vectores que generan V son Linealmente Independientes (forman base).", font_size=22, color=GREEN_A),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        items.next_to(enunciado, DOWN, buff=0.4)
        self.play(FadeIn(items, shift=UP * 0.2))
        self.next_slide()

        utilidad = Text(
            "Útil: con la cantidad justa, basta probar UNA condición.",
            font_size=24, color=YELLOW_A, weight=BOLD,
        )
        utilidad.next_to(items, DOWN, buff=0.5)
        self.play(FadeIn(utilidad, shift=UP * 0.2))
        self.next_slide()

        self.play(FadeOut(VGroup(header, enunciado, items, utilidad)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 9 — Ejercicio 6(b): LI
    # ══════════════════════════════════════════════════════════════

    def slide_ej_li(self):
        section = self.section_title("Ejercicio 6(b)", "Caso Linealmente Independiente")
        self.play(FadeIn(section, shift=DOWN * 0.3))
        self.next_slide()
        self.play(FadeOut(section))

        header = self.header_text("S = {(1,0,0); (0,1,0); (0,0,1)}")
        self.play(FadeIn(header, shift=DOWN * 0.2))

        planteo = Text("Planteamos la combinación lineal nula:", font_size=24, color=WHITE_S)
        planteo.next_to(header, DOWN, buff=0.5).align_to(header, LEFT).shift(RIGHT * 0.5)
        self.play(FadeIn(planteo))

        eq1 = MathTex(
            r"c_1 (1,0,0) + c_2 (0,1,0) + c_3 (0,0,1) = (0,0,0)",
            font_size=30, color=WHITE_S,
        )
        eq1.next_to(planteo, DOWN, buff=0.3)
        self.play(Write(eq1))
        self.next_slide()

        eq2 = MathTex(
            r"(c_1, c_2, c_3) = (0, 0, 0)",
            font_size=32, color=YELLOW_A,
        )
        eq2.next_to(eq1, DOWN, buff=0.3)
        self.play(Write(eq2))
        self.next_slide()

        sistema = MathTex(
            r"\Rightarrow\ c_1 = 0,\ c_2 = 0,\ c_3 = 0",
            font_size=32, color=GREEN_A,
        )
        sistema.next_to(eq2, DOWN, buff=0.3)
        self.play(Write(sistema))
        self.next_slide()

        conclu = Text(
            "Única solución: la trivial → S es Linealmente Independiente",
            font_size=24, color=GREEN_A, weight=BOLD,
        )
        conclu.next_to(sistema, DOWN, buff=0.5)
        self.play(FadeIn(conclu, shift=UP * 0.2))
        self.next_slide()

        bonus = Text(
            "Además: 3 vectores Linealmente Independientes en R³ (dim=3) → S es base canónica.",
            font_size=20, color=PURPLE,
        )
        bonus.next_to(conclu, DOWN, buff=0.3)
        self.play(FadeIn(bonus))
        self.next_slide()

        self.play(FadeOut(VGroup(header, planteo, eq1, eq2, sistema, conclu, bonus)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 10 — Ejercicio 6(a): LD
    # ══════════════════════════════════════════════════════════════

    def slide_ej_ld(self):
        section = self.section_title("Ejercicio 6(a)", "Caso Linealmente Dependiente")
        self.play(FadeIn(section, shift=DOWN * 0.3))
        self.next_slide()
        self.play(FadeOut(section))

        header = self.header_text("S = {(1,0,0); (0,1,0); (0,0,1); (1,2,3)}")
        self.play(FadeIn(header, shift=DOWN * 0.2))

        observ = Text(
            "4 vectores en R³ (dim = 3). Por el Teorema 3:",
            font_size=24, color=YELLOW_A,
        )
        observ.next_to(header, DOWN, buff=0.5)
        self.play(FadeIn(observ))
        self.next_slide()

        teo = Text("m > n  →  Linealmente Dependientes", font_size=28, color=ORANGE, weight=BOLD)
        teo.next_to(observ, DOWN, buff=0.3)
        self.play(Write(teo))
        self.next_slide()

        verif = Text("Verificación explícita:", font_size=24, color=CYAN, weight=BOLD)
        verif.next_to(teo, DOWN, buff=0.5)
        self.play(FadeIn(verif))

        eq = MathTex(
            r"(1,2,3) = 1\cdot(1,0,0) + 2\cdot(0,1,0) + 3\cdot(0,0,1)",
            font_size=28, color=WHITE_S,
        )
        eq.next_to(verif, DOWN, buff=0.3)
        self.play(Write(eq))
        self.next_slide()

        comb = MathTex(
            r"1\cdot(1,0,0) + 2\cdot(0,1,0) + 3\cdot(0,0,1) + (-1)\cdot(1,2,3) = 0",
            font_size=26, color=YELLOW_A,
        )
        comb.next_to(eq, DOWN, buff=0.3)
        self.play(Write(comb))
        self.next_slide()

        conclu = Text(
            "Coeficientes no todos nulos → S es Linealmente Dependiente",
            font_size=24, color=RED_A, weight=BOLD,
        )
        conclu.next_to(comb, DOWN, buff=0.4)
        self.play(FadeIn(conclu, shift=UP * 0.2))
        self.next_slide()

        self.play(FadeOut(VGroup(header, observ, teo, verif, eq, comb, conclu)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 11 — Cierre
    # ══════════════════════════════════════════════════════════════

    def slide_cierre(self):
        title = Text("Independencia Lineal", font_size=52, color=CYAN, weight=BOLD)
        sub = Text("¿Preguntas?", font_size=32, color=GRAY)
        sub.next_to(title, DOWN, buff=0.4)

        line = Line(LEFT * 3, RIGHT * 3, color=BLUE, stroke_width=2)
        line.next_to(sub, DOWN, buff=0.3)

        self.play(FadeIn(title, shift=DOWN * 0.3))
        self.play(FadeIn(sub), GrowFromCenter(line))
        self.next_slide()

    # ══════════════════════════════════════════════════════════════
    #  CONSTRUCT
    # ══════════════════════════════════════════════════════════════

    def construct(self):
        self.slide_titulo()
        self.slide_motivacion()
        self.slide_concepto_nula()
        self.slide_ld_li_contraste()
        self.slide_teo_nulo()
        self.slide_teo_unicidad()
        self.slide_teo_120()
        self.slide_teo_123()
        self.slide_ej_li()
        self.slide_ej_ld()
        self.slide_cierre()
