"""
Presentación Manim Slides — Relaciones de Equivalencia
Matemática 4 — Relaciones entre conjuntos

Temas:
  1. Definición de relación de equivalencia
  2. Ejemplos
  3. Clases de equivalencia y conjunto cociente
  4. Particiones y su relación con equivalencia
  5. Ejercicio 29 resuelto (TP4)
  6. Ejercicio 32 resuelto (TP4) — Construcción de los racionales

Renderizar:  manim render -qh presentacion.py RelacionesEquivalenciaSlides
Presentar:   manim-slides RelacionesEquivalenciaSlides
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


class RelacionesEquivalenciaSlides(Slide):

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
        title = Text("Relaciones de Equivalencia", font_size=48, color=CYAN, weight=BOLD)
        subtitle = Text(
            "Clases de equivalencia y Particiones",
            font_size=26, color=GRAY,
        )
        subtitle.next_to(title, DOWN, buff=0.4)

        line = Line(LEFT * 3.5, RIGHT * 3.5, color=BLUE, stroke_width=2)
        line.next_to(subtitle, DOWN, buff=0.3)

        mat = Text("Matemática 4 — Relaciones entre conjuntos", font_size=20, color=GRAY)
        mat.next_to(line, DOWN, buff=0.3)

        self.play(FadeIn(title, shift=DOWN * 0.3))
        self.play(FadeIn(subtitle, shift=UP * 0.2), GrowFromCenter(line))
        self.play(FadeIn(mat))
        self.next_slide()

        self.play(FadeOut(VGroup(title, subtitle, line, mat)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 2 — Repaso: Propiedades de relaciones binarias
    # ══════════════════════════════════════════════════════════════

    def slide_propiedades_repaso(self):
        header = self.header_text("Repaso: Propiedades de Relaciones", font_size=32)

        intro = Text(
            "Antes de definir equivalencia, recordemos\n"
            "las tres propiedades que la componen:",
            font_size=22, color=WHITE_S, line_spacing=1.4,
        )
        intro.next_to(header, DOWN, buff=0.4)

        props = VGroup(
            VGroup(
                Text("Reflexividad", font_size=24, color=YELLOW_A, weight=BOLD),
                MathTex(
                    r"\forall\, x \in A: \; x\,R\,x",
                    font_size=30, color=WHITE_S,
                ),
                Text(
                    "Todo elemento se relaciona consigo mismo.",
                    font_size=18, color=GRAY,
                ),
            ).arrange(DOWN, buff=0.12),
            VGroup(
                Text("Simetría", font_size=24, color=ORANGE, weight=BOLD),
                MathTex(
                    r"\forall\, x, y \in A: \; x\,R\,y \Rightarrow y\,R\,x",
                    font_size=30, color=WHITE_S,
                ),
                Text(
                    "Si x se relaciona con y, entonces y se relaciona con x.",
                    font_size=18, color=GRAY,
                ),
            ).arrange(DOWN, buff=0.12),
            VGroup(
                Text("Transitividad", font_size=24, color=PURPLE, weight=BOLD),
                MathTex(
                    r"\forall\, x, y, z \in A: \; x\,R\,y \;\land\; y\,R\,z \Rightarrow x\,R\,z",
                    font_size=30, color=WHITE_S,
                ),
                Text(
                    "Si x→y e y→z, entonces x→z.",
                    font_size=18, color=GRAY,
                ),
            ).arrange(DOWN, buff=0.12),
        )
        props.arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        props.next_to(intro, DOWN, buff=0.35)

        self.play(Write(header))
        self.play(FadeIn(intro, shift=UP * 0.2))
        self.next_slide()

        for p in props:
            self.play(FadeIn(p, shift=UP * 0.2))
            self.next_slide()

        self.play(FadeOut(VGroup(header, intro, props)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 3 — Definición de relación de equivalencia
    # ══════════════════════════════════════════════════════════════

    def slide_definicion(self):
        section = self.section_title(
            "Relación de Equivalencia",
            "Definición formal",
        )
        self.play(FadeIn(section, shift=DOWN * 0.3))
        self.next_slide()
        self.play(FadeOut(section))

        header = self.header_text("¿Qué es una relación de equivalencia?", font_size=30)

        defn_text = Text(
            "Una relación R definida sobre un conjunto A\n"
            "es una relación de equivalencia si y sólo si\n"
            "es reflexiva, simétrica y transitiva.",
            font_size=22, color=WHITE_S, line_spacing=1.5,
        )
        defn_text.next_to(header, DOWN, buff=0.45)

        # Las tres propiedades en una fórmula compacta
        formula = MathTex(
            r"R \text{ es equivalencia en } A",
            r"\;\Longleftrightarrow\;",
            r"\begin{cases}"
            r"\text{Reflexiva: } \forall\,x \in A,\; xRx \\"
            r"\text{Simétrica: } xRy \Rightarrow yRx \\"
            r"\text{Transitiva: } xRy \land yRz \Rightarrow xRz"
            r"\end{cases}",
            font_size=26, color=WHITE_S,
        )
        formula[0].set_color(CYAN)
        formula.next_to(defn_text, DOWN, buff=0.45)

        nota = MathTex(
            r"\text{Notación: } R \text{ se denota } \sim,\; \approx \;\text{ ó }\; \equiv",
            font_size=22, color=GRAY,
        )
        nota.next_to(formula, DOWN, buff=0.4)

        self.play(Write(header))
        self.play(FadeIn(defn_text, shift=UP * 0.2))
        self.next_slide()

        self.play(Write(formula), run_time=2)
        self.next_slide()

        self.play(FadeIn(nota, shift=UP * 0.1))
        self.next_slide()

        self.play(FadeOut(VGroup(header, defn_text, formula, nota)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 4 — Ejemplos de relaciones de equivalencia
    # ══════════════════════════════════════════════════════════════

    def slide_ejemplos(self):
        section = self.section_title("Ejemplos", "Relaciones de equivalencia")
        self.play(FadeIn(section, shift=DOWN * 0.3))
        self.next_slide()
        self.play(FadeOut(section))

        header = self.header_text("Ejemplo 1: La igualdad", font_size=32)

        ex1 = VGroup(
            Text(
                "La igualdad matemática (=) es trivialmente\n"
                "una relación de equivalencia en cualquier conjunto.",
                font_size=22, color=WHITE_S, line_spacing=1.4,
            ),
            VGroup(
                MathTex(r"\text{Reflexiva: } a = a \;\checkmark", font_size=26, color=WHITE_S),
                MathTex(r"\text{Simétrica: } a = b \Rightarrow b = a \;\checkmark", font_size=26, color=WHITE_S),
                MathTex(r"\text{Transitiva: } a = b \land b = c \Rightarrow a = c \;\checkmark", font_size=26, color=WHITE_S),
            ).arrange(DOWN, buff=0.2, aligned_edge=LEFT),
        )
        ex1[0].next_to(header, DOWN, buff=0.4)
        ex1[1].next_to(ex1[0], DOWN, buff=0.35)

        self.play(Write(header))
        self.play(FadeIn(ex1[0], shift=UP * 0.2))
        self.next_slide()
        self.play(FadeIn(ex1[1], shift=UP * 0.2))
        self.next_slide()

        self.play(FadeOut(VGroup(header, ex1)))

        # ── Ejemplo 2: rectas paralelas ──
        header2 = self.header_text("Ejemplo 2: Rectas paralelas", font_size=32)

        ex2_desc = Text(
            "En el conjunto de las rectas del plano, la relación\n"
            "\"L es paralela a M\" es de equivalencia.",
            font_size=22, color=WHITE_S, line_spacing=1.4,
        )
        ex2_desc.next_to(header2, DOWN, buff=0.4)

        ex2_props = VGroup(
            MathTex(r"\text{Reflexiva: toda recta es paralela a sí misma}", font_size=24, color=WHITE_S),
            MathTex(r"\text{Simétrica: si } L \parallel M \text{ entonces } M \parallel L", font_size=24, color=WHITE_S),
            MathTex(r"\text{Transitiva: si } L \parallel M \text{ y } M \parallel N \text{ entonces } L \parallel N", font_size=24, color=WHITE_S),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        ex2_props.next_to(ex2_desc, DOWN, buff=0.35)

        nota2 = Text(
            "Dos rectas son paralelas si tienen igual pendiente.",
            font_size=18, color=GRAY,
        )
        nota2.next_to(ex2_props, DOWN, buff=0.3)

        self.play(Write(header2))
        self.play(FadeIn(ex2_desc, shift=UP * 0.2))
        self.next_slide()
        self.play(FadeIn(ex2_props, shift=UP * 0.2))
        self.play(FadeIn(nota2, shift=UP * 0.1))
        self.next_slide()

        self.play(FadeOut(VGroup(header2, ex2_desc, ex2_props, nota2)))

        # ── Ejemplo 3: la identidad ──
        header3 = self.header_text("Ejemplo 3: La relación Identidad", font_size=32)

        ex3_desc = VGroup(
            Text(
                "La relación Identidad sobre un conjunto A:",
                font_size=22, color=WHITE_S,
            ),
            MathTex(
                r"\Delta_A = \{(x, x) : x \in A\}",
                font_size=34, color=CYAN,
            ),
            Text(
                "Es reflexiva, simétrica, antisimétrica y transitiva.\n"
                "Por lo tanto, es una relación de equivalencia\n"
                "(y también de orden).",
                font_size=22, color=WHITE_S, line_spacing=1.4,
            ),
        ).arrange(DOWN, buff=0.3)
        ex3_desc.next_to(header3, DOWN, buff=0.4)

        self.play(Write(header3))
        self.play(FadeIn(ex3_desc, shift=UP * 0.2))
        self.next_slide()

        self.play(FadeOut(VGroup(header3, ex3_desc)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 5 — Clases de equivalencia
    # ══════════════════════════════════════════════════════════════

    def slide_clases(self):
        section = self.section_title(
            "Clases de Equivalencia",
            "Agrupando elementos relacionados",
        )
        self.play(FadeIn(section, shift=DOWN * 0.3))
        self.next_slide()
        self.play(FadeOut(section))

        header = self.header_text("¿Qué es una clase de equivalencia?", font_size=30)

        defn = VGroup(
            Text(
                "Dada una relación de equivalencia R sobre A\n"
                "y un elemento a ∈ A:",
                font_size=22, color=WHITE_S, line_spacing=1.4,
            ),
            MathTex(
                r"\bar{a}", "=", r"\text{cl}(a)", "=",
                r"\{x \in A : x\,R\,a\}",
                font_size=36, color=WHITE_S,
            ),
            Text(
                "Es el conjunto de TODOS los elementos de A\n"
                "que están relacionados con a por R.",
                font_size=22, color=WHITE_S, line_spacing=1.4,
            ),
        ).arrange(DOWN, buff=0.3)
        defn[1][0].set_color(CYAN)
        defn[1][2].set_color(CYAN)
        defn[1][4].set_color(GREEN_A)
        defn.next_to(header, DOWN, buff=0.4)

        self.play(Write(header))
        self.play(FadeIn(defn[0], shift=UP * 0.2))
        self.next_slide()
        self.play(Write(defn[1]), run_time=1.5)
        self.play(FadeIn(defn[2], shift=UP * 0.2))
        self.next_slide()

        self.play(FadeOut(VGroup(defn)))

        # Representante
        rep_label = Text("Representante de una clase", font_size=24, color=GREEN_A, weight=BOLD)
        rep_label.next_to(header, DOWN, buff=0.5)

        rep_text = VGroup(
            Text(
                "Cualquier elemento de la clase se llama representante.",
                font_size=22, color=WHITE_S,
            ),
            Text(
                "Como R es reflexiva, a ∈ cl(a), entonces\n"
                "a es siempre representante de su propia clase.",
                font_size=22, color=WHITE_S, line_spacing=1.4,
            ),
        ).arrange(DOWN, buff=0.25)
        rep_text.next_to(rep_label, DOWN, buff=0.3)

        # Propiedad clave
        prop_key = VGroup(
            Text("Propiedad clave:", font_size=22, color=YELLOW_A, weight=BOLD),
            MathTex(
                r"\bar{a} = \bar{b} \;\Longleftrightarrow\; a\,R\,b",
                font_size=36, color=WHITE_S,
            ),
            Text(
                "Dos clases son iguales si y sólo si\n"
                "sus representantes están relacionados.",
                font_size=20, color=GRAY, line_spacing=1.3,
            ),
        ).arrange(DOWN, buff=0.15)
        prop_key.next_to(rep_text, DOWN, buff=0.35)

        self.play(FadeIn(rep_label))
        self.play(FadeIn(rep_text, shift=UP * 0.2))
        self.next_slide()

        self.play(FadeIn(prop_key, shift=UP * 0.2))
        self.next_slide()

        self.play(FadeOut(VGroup(header, rep_label, rep_text, prop_key)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 6 — Conjunto cociente
    # ══════════════════════════════════════════════════════════════

    def slide_cociente(self):
        header = self.header_text("Conjunto Cociente", font_size=34)

        defn = VGroup(
            Text(
                "El conjunto formado por TODAS las clases\n"
                "de equivalencia se llama conjunto cociente:",
                font_size=22, color=WHITE_S, line_spacing=1.4,
            ),
            MathTex(
                r"A/R", "=", r"\{\bar{a} : a \in A\}",
                font_size=40,
            ),
            Text(
                "Es un conjunto de conjuntos: cada elemento\n"
                "del cociente es una clase de equivalencia.",
                font_size=20, color=GRAY, line_spacing=1.3,
            ),
        ).arrange(DOWN, buff=0.3)
        defn[1][0].set_color(CYAN)
        defn[1][2].set_color(GREEN_A)
        defn.next_to(header, DOWN, buff=0.45)

        # Ejemplo concreto
        ej_label = Text("Ejemplo:", font_size=22, color=GREEN_A, weight=BOLD)
        ej_label.next_to(defn, DOWN, buff=0.35)

        ej = VGroup(
            MathTex(
                r"A = \{1,2,3,4\}, \quad R = \{(1,1),(1,2),(2,1),(2,2),(3,3),(4,4)\}",
                font_size=24, color=WHITE_S,
            ),
            MathTex(
                r"\bar{1} = \bar{2} = \{1,2\}, \quad \bar{3} = \{3\}, \quad \bar{4} = \{4\}",
                font_size=26, color=WHITE_S,
            ),
            MathTex(
                r"A/R = \big\{\{1,2\},\;\{3\},\;\{4\}\big\}",
                font_size=28, color=CYAN,
            ),
        ).arrange(DOWN, buff=0.2)
        ej.next_to(ej_label, DOWN, buff=0.2)

        self.play(Write(header))
        self.play(FadeIn(defn, shift=UP * 0.2))
        self.next_slide()

        self.play(FadeIn(ej_label))
        for e in ej:
            self.play(FadeIn(e, shift=UP * 0.2))
        self.next_slide()

        self.play(FadeOut(VGroup(header, defn, ej_label, ej)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 7 — Particiones
    # ══════════════════════════════════════════════════════════════

    def slide_particiones(self):
        section = self.section_title(
            "Particiones",
            "Dividiendo un conjunto en partes",
        )
        self.play(FadeIn(section, shift=DOWN * 0.3))
        self.next_slide()
        self.play(FadeOut(section))

        header = self.header_text("¿Qué es una partición?", font_size=32)

        defn = VGroup(
            Text(
                "Una partición de un conjunto A es una familia\n"
                "de subconjuntos no vacíos de A que cumple:",
                font_size=22, color=WHITE_S, line_spacing=1.4,
            ),
        )
        defn.next_to(header, DOWN, buff=0.4)

        conds = VGroup(
            VGroup(
                Text("1.", font_size=22, color=YELLOW_A, weight=BOLD),
                MathTex(
                    r"A_i \in P \Rightarrow A_i \neq \emptyset",
                    font_size=28, color=WHITE_S,
                ),
                Text("Cada parte es no vacía", font_size=18, color=GRAY),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("2.", font_size=22, color=ORANGE, weight=BOLD),
                MathTex(
                    r"A_i, A_j \in P,\; i \neq j \Rightarrow A_i \cap A_j = \emptyset",
                    font_size=28, color=WHITE_S,
                ),
                Text("Son disjuntas dos a dos", font_size=18, color=GRAY),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("3.", font_size=22, color=PURPLE, weight=BOLD),
                MathTex(
                    r"\bigcup_{i \in I} A_i = A",
                    font_size=28, color=WHITE_S,
                ),
                Text("Su unión cubre todo A", font_size=18, color=GRAY),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        conds.next_to(defn, DOWN, buff=0.35)

        self.play(Write(header))
        self.play(FadeIn(defn, shift=UP * 0.2))
        self.next_slide()

        for c in conds:
            self.play(FadeIn(c, shift=UP * 0.2))
        self.next_slide()

        self.play(FadeOut(VGroup(defn, conds)))

        # Ejemplo visual
        ej_label = Text("Ejemplo:", font_size=22, color=GREEN_A, weight=BOLD)
        ej_label.next_to(header, DOWN, buff=0.5)

        ej = VGroup(
            MathTex(
                r"\mathbb{N} = \text{Pares} \cup \text{Impares}",
                font_size=32, color=WHITE_S,
            ),
            MathTex(
                r"\text{Pares} \cap \text{Impares} = \emptyset",
                font_size=28, color=WHITE_S,
            ),
            Text(
                "Los pares e impares forman una partición de ℕ",
                font_size=22, color=GRAY,
            ),
        ).arrange(DOWN, buff=0.25)
        ej.next_to(ej_label, DOWN, buff=0.3)

        self.play(FadeIn(ej_label))
        self.play(FadeIn(ej, shift=UP * 0.2))
        self.next_slide()

        self.play(FadeOut(VGroup(ej_label, ej)))

        # Teorema fundamental
        teo_label = Text("Teorema Fundamental", font_size=24, color=CYAN, weight=BOLD)
        teo_label.next_to(header, DOWN, buff=0.5)

        teo = VGroup(
            Text(
                "Si R es una relación de equivalencia en A,",
                font_size=22, color=WHITE_S,
            ),
            Text(
                "entonces el conjunto cociente A/R",
                font_size=22, color=WHITE_S,
            ),
            Text(
                "es una partición de A.",
                font_size=24, color=CYAN, weight=BOLD,
            ),
        ).arrange(DOWN, buff=0.15)
        teo.next_to(teo_label, DOWN, buff=0.35)

        teo_box = SurroundingRectangle(teo, color=CYAN, buff=0.3, corner_radius=0.1)

        reciproco = VGroup(
            Text("Y recíprocamente:", font_size=22, color=WHITE_S),
            Text(
                "Toda partición de A induce una relación\n"
                "de equivalencia en A.",
                font_size=22, color=WHITE_S, line_spacing=1.3,
            ),
            Text(
                "aRb ⟺ a y b pertenecen al mismo subconjunto de P",
                font_size=20, color=GRAY,
            ),
        ).arrange(DOWN, buff=0.15)
        reciproco.next_to(teo_box, DOWN, buff=0.35)

        self.play(FadeIn(teo_label))
        self.play(FadeIn(teo, shift=UP * 0.2))
        self.play(Create(teo_box))
        self.next_slide()

        self.play(FadeIn(reciproco, shift=UP * 0.2))
        self.next_slide()

        self.play(FadeOut(VGroup(header, teo_label, teo, teo_box, reciproco)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 8 — Ejercicio 29 (TP4)
    # ══════════════════════════════════════════════════════════════

    def slide_ejercicio_29(self):
        section = self.section_title(
            "Ejercicio 29",
            "Trabajo Práctico 4",
        )
        self.play(FadeIn(section, shift=DOWN * 0.3))
        self.next_slide()
        self.play(FadeOut(section))

        header = self.header_text("Ejercicio 29 — Enunciado", font_size=30)

        enunc = VGroup(
            MathTex(
                r"A = \{1, 2, 3, 4\}",
                font_size=30, color=WHITE_S,
            ),
            MathTex(
                r"R = \{(1,1),(1,2),(2,1),(2,2),(3,3),(3,4),(4,3),(4,4)\}",
                font_size=26, color=WHITE_S,
            ),
            Text(
                "Mostrar que R es de equivalencia,\n"
                "hallar las clases y la partición que induce.",
                font_size=22, color=GRAY, line_spacing=1.3,
            ),
        ).arrange(DOWN, buff=0.25)
        enunc.next_to(header, DOWN, buff=0.4)

        self.play(Write(header))
        self.play(FadeIn(enunc, shift=UP * 0.2))
        self.next_slide()

        self.play(FadeOut(VGroup(enunc)))

        # ── Reflexividad ──
        self.play(header.animate.become(
            self.header_text("Ej. 29 — Reflexividad", font_size=30)
        ))

        ref = VGroup(
            Text("¿Todos los elementos se relacionan consigo mismos?", font_size=22, color=WHITE_S),
            MathTex(r"(1,1) \in R \;\checkmark", font_size=28, color=GREEN_A),
            MathTex(r"(2,2) \in R \;\checkmark", font_size=28, color=GREEN_A),
            MathTex(r"(3,3) \in R \;\checkmark", font_size=28, color=GREEN_A),
            MathTex(r"(4,4) \in R \;\checkmark", font_size=28, color=GREEN_A),
            Text("R es reflexiva ✓", font_size=24, color=GREEN_A, weight=BOLD),
        ).arrange(DOWN, buff=0.2)
        ref.next_to(header, DOWN, buff=0.4)

        self.play(FadeIn(ref, shift=UP * 0.2))
        self.next_slide()

        self.play(FadeOut(ref))

        # ── Simetría ──
        self.play(header.animate.become(
            self.header_text("Ej. 29 — Simetría", font_size=30)
        ))

        sim = VGroup(
            Text("¿Para cada (x,y) ∈ R, también (y,x) ∈ R?", font_size=22, color=WHITE_S),
            MathTex(r"(1,2) \in R \;\land\; (2,1) \in R \;\checkmark", font_size=26, color=WHITE_S),
            MathTex(r"(3,4) \in R \;\land\; (4,3) \in R \;\checkmark", font_size=26, color=WHITE_S),
            Text("Los pares (x,x) son trivialmente simétricos.", font_size=20, color=GRAY),
            Text("R es simétrica ✓", font_size=24, color=GREEN_A, weight=BOLD),
        ).arrange(DOWN, buff=0.2)
        sim.next_to(header, DOWN, buff=0.4)

        self.play(FadeIn(sim, shift=UP * 0.2))
        self.next_slide()

        self.play(FadeOut(sim))

        # ── Transitividad ──
        self.play(header.animate.become(
            self.header_text("Ej. 29 — Transitividad", font_size=30)
        ))

        trans = VGroup(
            Text("¿Si (x,y) ∈ R y (y,z) ∈ R, entonces (x,z) ∈ R?", font_size=22, color=WHITE_S),
            MathTex(r"(1,2) \in R \;\land\; (2,1) \in R \Rightarrow (1,1) \in R \;\checkmark", font_size=24, color=WHITE_S),
            MathTex(r"(3,4) \in R \;\land\; (4,3) \in R \Rightarrow (3,3) \in R \;\checkmark", font_size=24, color=WHITE_S),
            MathTex(r"(4,3) \in R \;\land\; (3,4) \in R \Rightarrow (4,4) \in R \;\checkmark", font_size=24, color=WHITE_S),
            Text(
                "Todos los pares componibles tienen su compuesto en R.",
                font_size=20, color=GRAY,
            ),
            Text("R es transitiva ✓", font_size=24, color=GREEN_A, weight=BOLD),
        ).arrange(DOWN, buff=0.18)
        trans.next_to(header, DOWN, buff=0.4)

        self.play(FadeIn(trans, shift=UP * 0.2))
        self.next_slide()

        self.play(FadeOut(trans))

        # ── Conclusión: es equivalencia ──
        self.play(header.animate.become(
            self.header_text("Ej. 29 — R es de equivalencia", font_size=30)
        ))

        concl = VGroup(
            MathTex(
                r"\text{Reflexiva } \checkmark \quad "
                r"\text{Simétrica } \checkmark \quad "
                r"\text{Transitiva } \checkmark",
                font_size=28, color=GREEN_A,
            ),
            MathTex(
                r"\Longrightarrow R \text{ es relación de equivalencia en } A",
                font_size=28, color=CYAN,
            ),
        ).arrange(DOWN, buff=0.3)
        concl.next_to(header, DOWN, buff=0.5)

        concl_box = SurroundingRectangle(concl, color=CYAN, buff=0.25, corner_radius=0.1)

        self.play(FadeIn(concl, shift=UP * 0.2))
        self.play(Create(concl_box))
        self.next_slide()

        self.play(FadeOut(VGroup(concl, concl_box)))

        # ── Clases de equivalencia ──
        self.play(header.animate.become(
            self.header_text("Ej. 29 — Clases de equivalencia", font_size=30)
        ))

        clases = VGroup(
            Text("Agrupamos los elementos relacionados entre sí:", font_size=22, color=WHITE_S),
            VGroup(
                MathTex(r"\bar{1} = \{x \in A : x\,R\,1\} = \{1, 2\}", font_size=28, color=WHITE_S),
                MathTex(r"\bar{2} = \{x \in A : x\,R\,2\} = \{1, 2\}", font_size=28, color=GRAY),
            ).arrange(DOWN, buff=0.15),
            MathTex(r"\Rightarrow \bar{1} = \bar{2} = \{1, 2\}", font_size=30, color=CYAN),
            VGroup(
                MathTex(r"\bar{3} = \{x \in A : x\,R\,3\} = \{3, 4\}", font_size=28, color=WHITE_S),
                MathTex(r"\bar{4} = \{x \in A : x\,R\,4\} = \{3, 4\}", font_size=28, color=GRAY),
            ).arrange(DOWN, buff=0.15),
            MathTex(r"\Rightarrow \bar{3} = \bar{4} = \{3, 4\}", font_size=30, color=CYAN),
        ).arrange(DOWN, buff=0.25)
        clases.next_to(header, DOWN, buff=0.35)

        self.play(FadeIn(clases, shift=UP * 0.2))
        self.next_slide()

        self.play(FadeOut(clases))

        # ── Partición ──
        self.play(header.animate.become(
            self.header_text("Ej. 29 — Partición inducida", font_size=30)
        ))

        part = VGroup(
            Text("El conjunto cociente:", font_size=22, color=WHITE_S),
            MathTex(
                r"A/R = \big\{\{1,2\},\;\{3,4\}\big\}",
                font_size=36, color=CYAN,
            ),
            Text("Verificamos que es partición:", font_size=22, color=WHITE_S),
            MathTex(r"\{1,2\} \neq \emptyset \;\land\; \{3,4\} \neq \emptyset \;\checkmark",
                    font_size=26, color=GREEN_A),
            MathTex(r"\{1,2\} \cap \{3,4\} = \emptyset \;\checkmark",
                    font_size=26, color=GREEN_A),
            MathTex(r"\{1,2\} \cup \{3,4\} = \{1,2,3,4\} = A \;\checkmark",
                    font_size=26, color=GREEN_A),
        ).arrange(DOWN, buff=0.2)
        part.next_to(header, DOWN, buff=0.35)

        part_box = SurroundingRectangle(part[1], color=CYAN, buff=0.2, corner_radius=0.1)

        self.play(FadeIn(part, shift=UP * 0.2))
        self.play(Create(part_box))
        self.next_slide()

        self.play(FadeOut(VGroup(header, part, part_box)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 9 — Ejercicio 32 (TP4) — Construcción de los racionales
    # ══════════════════════════════════════════════════════════════

    def slide_ejercicio_32(self):
        section = self.section_title(
            "Ejercicio 32",
            "Trabajo Práctico 4",
        )
        self.play(FadeIn(section, shift=DOWN * 0.3))
        self.next_slide()
        self.play(FadeOut(section))

        # ── Enunciado ──
        header = self.header_text("Ejercicio 32 — Enunciado", font_size=32)

        enunc = VGroup(
            Text(
                "Sea ~ una relación definida en",
                font_size=26, color=WHITE_S,
            ),
            MathTex(
                r"\mathbb{Z} \times \mathbb{Z}_0",
                font_size=40, color=CYAN,
            ),
            Text("dada por:", font_size=26, color=WHITE_S),
            MathTex(
                r"(x, y) \sim (z, w) \;\Longleftrightarrow\; x \cdot w = y \cdot z",
                font_size=38, color=WHITE_S,
            ),
            Text(
                "Probar que ~ es de equivalencia.\n"
                "Hallar la clase del elemento (-1, 4).\n"
                "Mostrar que cada clase se identifica con un racional.",
                font_size=22, color=GRAY, line_spacing=1.4,
            ),
        ).arrange(DOWN, buff=0.2)
        enunc.next_to(header, DOWN, buff=0.35)

        self.play(Write(header))
        self.play(FadeIn(enunc, shift=UP * 0.2))
        self.next_slide()

        self.play(FadeOut(enunc))

        # ── Intuición ──
        self.play(header.animate.become(
            self.header_text("Ej. 32 — Intuición", font_size=32)
        ))

        intuicion = VGroup(
            Text(
                "¿Qué significa xw = yz?",
                font_size=28, color=YELLOW_A, weight=BOLD,
            ),
            Text(
                "Si pensamos al par (x, y) como la fracción x/y,\n"
                "entonces xw = yz es lo mismo que:",
                font_size=26, color=WHITE_S, line_spacing=1.4,
            ),
            MathTex(
                r"\frac{x}{y} = \frac{z}{w}",
                font_size=48, color=CYAN,
            ),
            Text(
                "Dos pares son equivalentes si representan\n"
                "la misma fracción.",
                font_size=26, color=WHITE_S, line_spacing=1.3,
            ),
            Text(
                "Ejemplo: (1,2) ~ (2,4) ~ (3,6) ~ ...  son todos  1/2",
                font_size=22, color=GRAY,
            ),
        ).arrange(DOWN, buff=0.25)
        intuicion.next_to(header, DOWN, buff=0.35)

        self.play(FadeIn(intuicion, shift=UP * 0.2))
        self.next_slide()

        self.play(FadeOut(intuicion))

        # ── Reflexividad ──
        self.play(header.animate.become(
            self.header_text("Ej. 32 — Reflexividad", font_size=32)
        ))

        ref = VGroup(
            MathTex(
                r"\forall\,(x,y) \in \mathbb{Z} \times \mathbb{Z}_0,"
                r"\;\text{¿vale } (x,y) \sim (x,y)\text{ ?}",
                font_size=32, color=WHITE_S,
            ),
            MathTex(
                r"(x,y) \sim (x,y) \;\Longleftrightarrow\; x \cdot y = y \cdot x",
                font_size=34, color=WHITE_S,
            ),
            Text(
                "Se cumple siempre por la conmutatividad\n"
                "del producto en los enteros.",
                font_size=26, color=WHITE_S, line_spacing=1.3,
            ),
            Text("~ es reflexiva ✓", font_size=28, color=GREEN_A, weight=BOLD),
        ).arrange(DOWN, buff=0.3)
        ref.next_to(header, DOWN, buff=0.4)

        self.play(FadeIn(ref, shift=UP * 0.2))
        self.next_slide()

        self.play(FadeOut(ref))

        # ── Simetría ──
        self.play(header.animate.become(
            self.header_text("Ej. 32 — Simetría", font_size=32)
        ))

        sim = VGroup(
            MathTex(
                r"\forall\,(x,y),(z,w) \in \mathbb{Z} \times \mathbb{Z}_0:",
                font_size=30, color=WHITE_S,
            ),
            MathTex(
                r"\text{¿}(x,y) \sim (z,w) \;\Rightarrow\; (z,w) \sim (x,y)\text{ ?}",
                font_size=30, color=WHITE_S,
            ),
            MathTex(
                r"\text{1. Si } (x,y) \sim (z,w) \;\Rightarrow\; xw = yz",
                font_size=30, color=WHITE_S,
            ),
            MathTex(
                r"\text{2. } yz = zy \;\text{(conmut.)} \;\land\; xw = wx \;\text{(conmut.)}",
                font_size=30, color=WHITE_S,
            ),
            MathTex(
                r"\text{3. Entonces } zy = wx \;\Rightarrow\; (z,w) \sim (x,y) \;\checkmark",
                font_size=30, color=GREEN_A,
            ),
            Text("~ es simétrica ✓", font_size=28, color=GREEN_A, weight=BOLD),
        ).arrange(DOWN, buff=0.22)
        sim.next_to(header, DOWN, buff=0.35)

        self.play(FadeIn(sim, shift=UP * 0.2))
        self.next_slide()

        self.play(FadeOut(sim))

        # ── Transitividad ──
        self.play(header.animate.become(
            self.header_text("Ej. 32 — Transitividad", font_size=32)
        ))

        trans = VGroup(
            MathTex(
                r"\forall\,(x,y),(z,w),(k,h) \in \mathbb{Z} \times \mathbb{Z}_0:",
                font_size=28, color=WHITE_S,
            ),
            MathTex(
                r"(x,y) \sim (z,w) \;\land\; (z,w) \sim (k,h)"
                r"\;\Rightarrow\; (x,y) \sim (k,h) \text{ ?}",
                font_size=28, color=WHITE_S,
            ),
            MathTex(
                r"\text{1. Suponemos } (x,y) \sim (z,w) \;\land\; (z,w) \sim (k,h)",
                font_size=28, color=WHITE_S,
            ),
            MathTex(
                r"\text{2. Sabemos: } xw = yz \quad \text{y} \quad zh = wk",
                font_size=28, color=WHITE_S,
            ),
        ).arrange(DOWN, buff=0.25)
        trans.next_to(header, DOWN, buff=0.4)

        self.play(FadeIn(trans, shift=UP * 0.2))
        self.next_slide()

        self.play(FadeOut(trans))

        # ── Transitividad (continuación) ──

        demo = VGroup(
            MathTex(
                r"\text{3. Multiplicamos } xw = yz \text{ por } h:",
                font_size=30, color=WHITE_S,
            ),
            MathTex(
                r"xwh = yzh",
                font_size=34, color=WHITE_S,
            ),
            MathTex(
                r"\text{4. Reemplazamos } zh = wk:",
                font_size=30, color=WHITE_S,
            ),
            MathTex(
                r"xwh = y \cdot wk",
                font_size=34, color=WHITE_S,
            ),
            MathTex(
                r"\text{5. Como } w \neq 0 \text{, simplificamos } w:",
                font_size=30, color=WHITE_S,
            ),
            MathTex(
                r"xh = yk \;\Rightarrow\; (x,y) \sim (k,h) \;\checkmark",
                font_size=34, color=GREEN_A,
            ),
            Text("~ es transitiva ✓", font_size=28, color=GREEN_A, weight=BOLD),
        ).arrange(DOWN, buff=0.2)
        demo.next_to(header, DOWN, buff=0.35)

        self.play(FadeIn(demo, shift=UP * 0.2))
        self.next_slide()

        self.play(FadeOut(demo))

        # ── Conclusión: es equivalencia ──
        self.play(header.animate.become(
            self.header_text("Ej. 32 — ~ es de equivalencia", font_size=32)
        ))

        concl = VGroup(
            MathTex(
                r"\text{Reflexiva } \checkmark \quad "
                r"\text{Simétrica } \checkmark \quad "
                r"\text{Transitiva } \checkmark",
                font_size=32, color=GREEN_A,
            ),
            MathTex(
                r"\therefore \;\sim\; \text{ es relación de equivalencia en } "
                r"\mathbb{Z} \times \mathbb{Z}_0",
                font_size=30, color=CYAN,
            ),
        ).arrange(DOWN, buff=0.3)
        concl.next_to(header, DOWN, buff=0.5)

        concl_box = SurroundingRectangle(concl, color=CYAN, buff=0.25, corner_radius=0.1)

        self.play(FadeIn(concl, shift=UP * 0.2))
        self.play(Create(concl_box))
        self.next_slide()

        self.play(FadeOut(VGroup(concl, concl_box)))

        # ── Clase de (-1, 4) ──
        self.play(header.animate.become(
            self.header_text("Ej. 32 — Clase de (-1, 4)", font_size=32)
        ))

        clase = VGroup(
            MathTex(
                r"\overline{(-1,4)}", "=",
                r"\{(x,y) \in \mathbb{Z} \times \mathbb{Z}_0 : (-1) \cdot y = 4 \cdot x\}",
                font_size=30, color=WHITE_S,
            ),
            Text("Es decir,  y = -4x  con  y ≠ 0  y  x ≠ 0", font_size=26, color=WHITE_S),
            MathTex(
                r"\therefore\;\overline{(-1,4)} = \{(x, -4x) : x \in \mathbb{Z}_0\}",
                font_size=34, color=CYAN,
            ),
            Text("Algunos elementos:", font_size=26, color=WHITE_S),
            MathTex(
                r"\ldots,\; (-2, 8),\; (-1, 4),\; (1, -4),\; (2, -8),\; \ldots",
                font_size=30, color=WHITE_S,
            ),
            Text(
                "Todos representan la fracción  -1/4",
                font_size=26, color=YELLOW_A,
            ),
        ).arrange(DOWN, buff=0.2)
        clase[0][0].set_color(CYAN)
        clase.next_to(header, DOWN, buff=0.35)

        clase_box = SurroundingRectangle(clase[2], color=CYAN, buff=0.2, corner_radius=0.1)

        self.play(FadeIn(clase, shift=UP * 0.2))
        self.play(Create(clase_box))
        self.next_slide()

        self.play(FadeOut(VGroup(clase, clase_box)))

        # ── Identificación con los racionales ──
        self.play(header.animate.become(
            self.header_text("Ej. 32 — Los racionales como cociente", font_size=30)
        ))

        racional = VGroup(
            Text(
                "Si (x,y) ~ (z,w) entonces xw = yz, lo que implica:",
                font_size=26, color=WHITE_S,
            ),
            MathTex(
                r"\frac{x}{y} = \frac{z}{w}",
                r"\quad \text{con } y \neq 0 \;\land\; w \neq 0",
                font_size=38, color=WHITE_S,
            ),
            Text(
                "Cada clase de equivalencia [(x,y)] corresponde\n"
                "al número racional  x/y",
                font_size=26, color=WHITE_S, line_spacing=1.3,
            ),
            MathTex(
                r"\overline{(x,y)} \;\longleftrightarrow\; \frac{x}{y} \in \mathbb{Q}",
                font_size=42, color=CYAN,
            ),
        ).arrange(DOWN, buff=0.25)
        racional.next_to(header, DOWN, buff=0.4)

        self.play(FadeIn(racional, shift=UP * 0.2))
        self.next_slide()

        self.play(FadeOut(racional))

        # ── Conclusión final ──
        final = VGroup(
            Text(
                "El conjunto cociente es exactamente",
                font_size=28, color=WHITE_S,
            ),
            MathTex(
                r"\frac{\mathbb{Z} \times \mathbb{Z}_0}{\sim}",
                r"\;=\;",
                r"\mathbb{Q}",
                font_size=52,
            ),
            Text(
                "Esta es la construcción formal de los racionales\n"
                "como conjunto cociente a partir de los enteros.",
                font_size=26, color=WHITE_S, line_spacing=1.3,
            ),
        ).arrange(DOWN, buff=0.3)
        final[1][0].set_color(WHITE_S)
        final[1][2].set_color(CYAN)
        final.next_to(header, DOWN, buff=0.4)

        final_box = SurroundingRectangle(final[1], color=CYAN, buff=0.3, corner_radius=0.1)

        self.play(FadeIn(final, shift=UP * 0.2))
        self.play(Create(final_box))
        self.next_slide()

        self.play(FadeOut(VGroup(header, final, final_box)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 10 — Resumen
    # ══════════════════════════════════════════════════════════════

    def slide_resumen(self):
        header = self.header_text("Resumen")

        props = VGroup(
            VGroup(
                Text("Equivalencia", font_size=22, color=CYAN, weight=BOLD),
                MathTex(
                    r"\text{Reflexiva + Simétrica + Transitiva}",
                    font_size=24, color=WHITE_S,
                ),
            ).arrange(DOWN, buff=0.12),
            VGroup(
                Text("Clase de equivalencia", font_size=22, color=GREEN_A, weight=BOLD),
                MathTex(
                    r"\bar{a} = \{x \in A : xRa\}",
                    font_size=26, color=WHITE_S,
                ),
            ).arrange(DOWN, buff=0.12),
            VGroup(
                Text("Conjunto cociente", font_size=22, color=YELLOW_A, weight=BOLD),
                MathTex(
                    r"A/R = \{\bar{a} : a \in A\}",
                    font_size=26, color=WHITE_S,
                ),
            ).arrange(DOWN, buff=0.12),
            VGroup(
                Text("Partición", font_size=22, color=PURPLE, weight=BOLD),
                MathTex(
                    r"\text{Partes no vacías, disjuntas, cuya unión es } A",
                    font_size=22, color=WHITE_S,
                ),
            ).arrange(DOWN, buff=0.12),
            VGroup(
                Text("Teorema clave", font_size=22, color=ORANGE, weight=BOLD),
                MathTex(
                    r"A/R \text{ es partición de } A \;\longleftrightarrow\; "
                    r"R \text{ es equivalencia}",
                    font_size=22, color=WHITE_S,
                ),
            ).arrange(DOWN, buff=0.12),
        )
        props.arrange_in_grid(rows=3, cols=2, buff=(1.5, 0.5))
        props.next_to(header, DOWN, buff=0.4)

        self.play(Write(header))
        self.play(
            LaggedStart(*[FadeIn(p, shift=UP * 0.3) for p in props], lag_ratio=0.25),
            run_time=3,
        )
        self.next_slide()

        self.play(FadeOut(VGroup(header, props)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 11 — Cierre
    # ══════════════════════════════════════════════════════════════

    def slide_cierre(self):
        title = Text("Relaciones de Equivalencia", font_size=40, color=CYAN, weight=BOLD)
        thanks = Text("¡Gracias!", font_size=36, color=WHITE_S)
        thanks.next_to(title, DOWN, buff=0.5)

        line = Line(LEFT * 3, RIGHT * 3, color=BLUE, stroke_width=2)
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
        self.slide_propiedades_repaso()
        self.slide_definicion()

        # Ejemplos
        self.slide_ejemplos()

        # Teoría: clases, cociente, particiones
        self.slide_clases()
        self.slide_cociente()
        self.slide_particiones()

        # Ejercicios resueltos
        self.slide_ejercicio_29()
        self.slide_ejercicio_32()

        # Cierre
        self.slide_resumen()
        self.slide_cierre()
