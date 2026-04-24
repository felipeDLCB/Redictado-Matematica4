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

    # ─── helpers visuales ──────────────────────────────────────────

    def self_loop(self, dot, color=None, size=0.22, angle=-TAU + 1.0):
        """Flecha circular que vuelve al mismo punto (self-loop)."""
        c = color if color is not None else YELLOW_A
        center = dot.get_center()
        start = center + UP * 0.10 + RIGHT * 0.08
        end = center + UP * 0.10 + LEFT * 0.08
        loop = CurvedArrow(
            start, end,
            angle=angle,
            color=c,
            tip_length=0.12,
            stroke_width=2.5,
        )
        return loop

    def dot_labeled(self, label, pos=ORIGIN, color=CYAN, radius=0.12,
                    label_dir=DOWN, font_size=22, label_color=None):
        """Un Dot con label."""
        d = Dot(pos, color=color, radius=radius)
        lc = label_color if label_color is not None else WHITE_S
        if isinstance(label, str) and label.startswith("$"):
            lbl = MathTex(label.strip("$"), font_size=font_size + 4, color=lc)
        else:
            lbl = Text(str(label), font_size=font_size, color=lc)
        lbl.next_to(d, label_dir, buff=0.12)
        return VGroup(d, lbl)

    def set_ellipse(self, group, color=BLUE, buff=0.45, stroke_width=2):
        """Elipse que envuelve a un grupo de mobjects (representando un conjunto)."""
        w = group.width + buff * 2
        h = group.height + buff * 2
        el = Ellipse(width=w, height=h, color=color, stroke_width=stroke_width)
        el.move_to(group.get_center())
        return el

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

        # ── Ejemplo 2: la identidad ──
        header_id = self.header_text("Ejemplo 2: La relación Identidad", font_size=32)

        ex_id = VGroup(
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
        ex_id.next_to(header_id, DOWN, buff=0.4)

        self.play(Write(header_id))
        self.play(FadeIn(ex_id, shift=UP * 0.2))
        self.next_slide()

        self.play(FadeOut(VGroup(header_id, ex_id)))

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

        # ── Definición compacta ──
        defn = MathTex(
            r"\bar{a}", "=", r"\{x \in A : x \sim a\}",
            font_size=40, color=WHITE_S,
        )
        defn[0].set_color(CYAN)
        defn[2].set_color(GREEN_A)
        defn.next_to(header, DOWN, buff=0.5)

        defn_sub = Text(
            "= todos los elementos de A relacionados con a",
            font_size=20, color=GRAY,
        )
        defn_sub.next_to(defn, DOWN, buff=0.2)

        self.play(Write(header))
        self.play(Write(defn), run_time=1.5)
        self.play(FadeIn(defn_sub))
        self.next_slide()

        self.play(FadeOut(VGroup(defn, defn_sub)))

        # ══ Visualización: conjunto A con 3 clases coloreadas ══
        # A = {1,2,3,4,5,6,7,8,9} con 3 clases:
        #   clase roja: {1, 4, 7}
        #   clase verde: {2, 5, 8}
        #   clase violeta: {3, 6, 9}

        class_red = [1, 4, 7]
        class_green = [2, 5, 8]
        class_purple = [3, 6, 9]

        # Posiciones acomodadas: cada clase en su zona
        layout = {
            1: LEFT * 3.2 + UP * 0.6,
            4: LEFT * 3.8 + DOWN * 0.3,
            7: LEFT * 2.5 + DOWN * 0.4,
            2: UP * 0.7,
            5: DOWN * 0.4,
            8: RIGHT * 0.7 + UP * 0.1,
            3: RIGHT * 2.7 + UP * 0.6,
            6: RIGHT * 3.5 + DOWN * 0.4,
            9: RIGHT * 2.4 + DOWN * 0.2,
        }

        color_map = {}
        for n in class_red: color_map[n] = RED_A
        for n in class_green: color_map[n] = GREEN_A
        for n in class_purple: color_map[n] = PURPLE

        dots = {}
        labels = {}
        for n, pos in layout.items():
            d = Dot(pos, color=color_map[n], radius=0.13)
            l = MathTex(str(n), font_size=22, color=WHITE_S).next_to(d, DOWN, buff=0.1)
            dots[n] = d
            labels[n] = l

        all_dots = VGroup(*dots.values())
        all_labels = VGroup(*labels.values())

        # Burbujas por clase
        def make_bubble(numbers, color):
            grp = VGroup(*[dots[n] for n in numbers], *[labels[n] for n in numbers])
            w = grp.width + 0.55
            h = grp.height + 0.45
            el = Ellipse(width=w, height=h, color=color, stroke_width=2.5,
                         fill_opacity=0.12, fill_color=color)
            el.move_to(grp.get_center())
            return el

        bubble_red = make_bubble(class_red, RED_A)
        bubble_green = make_bubble(class_green, GREEN_A)
        bubble_purple = make_bubble(class_purple, PURPLE)

        # Frontera del conjunto A
        whole = VGroup(bubble_red, bubble_green, bubble_purple, all_dots, all_labels)
        A_boundary = Ellipse(
            width=whole.width + 0.8, height=whole.height + 0.8,
            color=BLUE, stroke_width=2,
        ).move_to(whole.get_center())
        A_label = MathTex("A", font_size=30, color=BLUE).next_to(A_boundary, UL, buff=-0.25)

        # Etiquetas de clases
        lbl_red = MathTex(r"\bar{1} = \{1,4,7\}", font_size=24, color=RED_A)
        lbl_green = MathTex(r"\bar{2} = \{2,5,8\}", font_size=24, color=GREEN_A)
        lbl_purple = MathTex(r"\bar{3} = \{3,6,9\}", font_size=24, color=PURPLE)

        lbls_clases = VGroup(lbl_red, lbl_green, lbl_purple).arrange(RIGHT, buff=0.7)

        diagram_group = VGroup(A_boundary, A_label, bubble_red, bubble_green, bubble_purple,
                               all_dots, all_labels)
        diagram_group.move_to(ORIGIN).shift(UP * 0.4)
        lbls_clases.next_to(diagram_group, DOWN, buff=0.6)

        self.play(
            Create(A_boundary),
            FadeIn(A_label),
        )
        self.play(
            LaggedStart(*[FadeIn(d) for d in all_dots], lag_ratio=0.05),
            LaggedStart(*[FadeIn(l) for l in all_labels], lag_ratio=0.05),
            run_time=1.5,
        )
        self.next_slide()

        self.play(Create(bubble_red), FadeIn(lbl_red))
        self.next_slide()
        self.play(Create(bubble_green), FadeIn(lbl_green))
        self.next_slide()
        self.play(Create(bubble_purple), FadeIn(lbl_purple))
        self.next_slide()

        # Propiedad clave destacada
        prop_key = VGroup(
            MathTex(r"\bar{a} = \bar{b}", r"\iff", r"a \sim b",
                    font_size=38, color=WHITE_S),
            Text("Dos clases son iguales ⟺ sus representantes se relacionan",
                 font_size=18, color=GRAY),
        ).arrange(DOWN, buff=0.25)
        prop_key[0][0].set_color(CYAN)
        prop_key[0][2].set_color(CYAN)
        prop_key.next_to(lbls_clases, DOWN, buff=0.5)

        self.play(FadeIn(prop_key, shift=UP * 0.2))
        self.next_slide()

        self.play(FadeOut(VGroup(
            header, A_boundary, A_label, bubble_red, bubble_green, bubble_purple,
            all_dots, all_labels, lbls_clases, prop_key,
        )))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 6 — Conjunto cociente
    # ══════════════════════════════════════════════════════════════

    def slide_cociente(self):
        header = self.header_text("Conjunto Cociente", font_size=34)

        # Definición compacta
        defn = MathTex(
            r"A/R", r"=", r"\{\bar{a} : a \in A\}",
            font_size=42,
        )
        defn[0].set_color(CYAN)
        defn[2].set_color(GREEN_A)
        defn.next_to(header, DOWN, buff=0.5)

        defn_sub = Text(
            "= el conjunto de todas las clases de equivalencia",
            font_size=20, color=GRAY,
        )
        defn_sub.next_to(defn, DOWN, buff=0.2)

        self.play(Write(header))
        self.play(Write(defn), run_time=1.5)
        self.play(FadeIn(defn_sub))
        self.next_slide()

        self.play(FadeOut(VGroup(defn, defn_sub)))

        # ══ Animación de colapso: A con clases → A/R ══
        # Izquierda: A con 3 burbujas y sus puntos
        # Derecha: A/R con 3 puntos (uno por clase)

        # ── Lado izquierdo: conjunto A ──
        left_center = LEFT * 3.3
        layout_L = {
            1: left_center + LEFT * 0.55 + UP * 0.6,
            2: left_center + RIGHT * 0.55 + UP * 0.6,
            3: left_center + LEFT * 0.1 + DOWN * 0.0,
            4: left_center + LEFT * 0.55 + DOWN * 0.75,
            5: left_center + RIGHT * 0.55 + DOWN * 0.75,
        }
        color_L = {1: RED_A, 2: RED_A, 3: GREEN_A, 4: PURPLE, 5: PURPLE}

        L_dots = {}
        L_labels = {}
        for n, pos in layout_L.items():
            d = Dot(pos, color=color_L[n], radius=0.12)
            l = MathTex(str(n), font_size=20, color=WHITE_S).next_to(d, DOWN, buff=0.08)
            L_dots[n] = d
            L_labels[n] = l

        # Burbujas izquierda
        def bubble_around(numbers, color):
            grp = VGroup(*[L_dots[n] for n in numbers], *[L_labels[n] for n in numbers])
            w = max(grp.width + 0.5, 0.8)
            h = max(grp.height + 0.4, 0.8)
            el = Ellipse(width=w, height=h, color=color, stroke_width=2,
                         fill_opacity=0.15, fill_color=color)
            el.move_to(grp.get_center())
            return el

        bub_red_L = bubble_around([1, 2], RED_A)
        bub_green_L = bubble_around([3], GREEN_A)
        bub_purple_L = bubble_around([4, 5], PURPLE)

        L_all = VGroup(bub_red_L, bub_green_L, bub_purple_L,
                       *L_dots.values(), *L_labels.values())
        A_boundary = Ellipse(
            width=L_all.width + 0.7, height=L_all.height + 0.7,
            color=BLUE, stroke_width=2,
        ).move_to(L_all.get_center())
        A_lbl = MathTex("A", font_size=28, color=BLUE).next_to(A_boundary, UP, buff=0.15)

        # ── Lado derecho: cociente A/R ──
        right_center = RIGHT * 3.3
        coc_red = Dot(right_center + UP * 0.9, color=RED_A, radius=0.22)
        coc_green = Dot(right_center, color=GREEN_A, radius=0.22)
        coc_purple = Dot(right_center + DOWN * 0.9, color=PURPLE, radius=0.22)

        coc_red_lbl = MathTex(r"\{1,2\}", font_size=22, color=WHITE_S).next_to(coc_red, RIGHT, buff=0.2)
        coc_green_lbl = MathTex(r"\{3\}", font_size=22, color=WHITE_S).next_to(coc_green, RIGHT, buff=0.2)
        coc_purple_lbl = MathTex(r"\{4,5\}", font_size=22, color=WHITE_S).next_to(coc_purple, RIGHT, buff=0.2)

        coc_dots = VGroup(coc_red, coc_green, coc_purple)
        coc_labels = VGroup(coc_red_lbl, coc_green_lbl, coc_purple_lbl)
        coc_all = VGroup(coc_dots, coc_labels)
        AR_boundary = Ellipse(
            width=coc_all.width + 0.7, height=coc_all.height + 0.6,
            color=CYAN, stroke_width=2,
        ).move_to(coc_all.get_center())
        AR_lbl = MathTex("A/R", font_size=28, color=CYAN).next_to(AR_boundary, UP, buff=0.15)

        # Flecha de proyección
        proj_arrow = Arrow(
            A_boundary.get_right() + RIGHT * 0.1,
            AR_boundary.get_left() + LEFT * 0.1,
            color=YELLOW_A, buff=0.05, stroke_width=3, tip_length=0.18,
        )
        proj_label = Text("proyección", font_size=18, color=YELLOW_A)
        proj_label.next_to(proj_arrow, UP, buff=0.1)

        # Mostrar A con burbujas
        self.play(Create(A_boundary), FadeIn(A_lbl))
        self.play(
            LaggedStart(*[FadeIn(d) for d in L_dots.values()], lag_ratio=0.05),
            LaggedStart(*[FadeIn(l) for l in L_labels.values()], lag_ratio=0.05),
            run_time=1.2,
        )
        self.play(
            Create(bub_red_L), Create(bub_green_L), Create(bub_purple_L),
            run_time=1,
        )
        self.next_slide()

        # Flecha y boundary del cociente
        self.play(
            Create(proj_arrow),
            FadeIn(proj_label),
            Create(AR_boundary),
            FadeIn(AR_lbl),
        )
        self.next_slide()

        # Colapso: cada burbuja se transforma en su punto en el cociente
        # (creamos copias trackeables para poder limpiarlas después)
        proj_red = bub_red_L.copy()
        proj_green = bub_green_L.copy()
        proj_purple = bub_purple_L.copy()
        self.add(proj_red, proj_green, proj_purple)
        self.play(
            Transform(proj_red, coc_red),
            Transform(proj_green, coc_green),
            Transform(proj_purple, coc_purple),
            run_time=1.5,
        )
        self.play(
            FadeIn(coc_red_lbl, shift=LEFT * 0.2),
            FadeIn(coc_green_lbl, shift=LEFT * 0.2),
            FadeIn(coc_purple_lbl, shift=LEFT * 0.2),
        )
        self.next_slide()

        # Caption explicativo
        caption = MathTex(
            r"A/R = \big\{\{1,2\},\;\{3\},\;\{4,5\}\big\}",
            font_size=30, color=CYAN,
        ).to_edge(DOWN, buff=0.7)

        caption_sub = Text(
            "Cada clase se convierte en UN punto del cociente.",
            font_size=18, color=GRAY,
        ).next_to(caption, DOWN, buff=0.2)

        self.play(FadeIn(caption, shift=UP * 0.2))
        self.play(FadeIn(caption_sub))
        self.next_slide()

        # Limpieza (proj_* son las copias transformadas que están en escena)
        self.play(FadeOut(VGroup(
            header, A_boundary, A_lbl, bub_red_L, bub_green_L, bub_purple_L,
            *L_dots.values(), *L_labels.values(),
            proj_arrow, proj_label, AR_boundary, AR_lbl,
            proj_red, proj_green, proj_purple, coc_labels,
            caption, caption_sub,
        )))

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

        # ══ Visualización: conjunto A dividido en regiones ══
        # Rectángulo grande (A) partido en 4 piezas de distinto color

        A_rect = RoundedRectangle(
            width=6.5, height=3.5,
            corner_radius=0.3,
            color=BLUE, stroke_width=2,
        )
        A_rect.move_to(ORIGIN).shift(UP * 0.3)
        A_lbl = MathTex("A", font_size=30, color=BLUE).next_to(A_rect, UL, buff=-0.25)

        # 4 regiones internas (fills con polígonos)
        # Zona 1 (arriba-izq), 2 (arriba-der), 3 (abajo-izq), 4 (abajo-der)
        c = A_rect.get_center()
        def region(corner_from, corner_to, fill_color, name, name_offset):
            r = RoundedRectangle(
                width=2.8, height=1.4,
                corner_radius=0.15,
                color=fill_color, stroke_width=2,
                fill_opacity=0.3, fill_color=fill_color,
            )
            r.move_to(c + corner_from)
            lbl = MathTex(name, font_size=28, color=fill_color).move_to(r.get_center())
            return r, lbl

        r1, l1 = region(LEFT * 1.5 + UP * 0.75, None, RED_A, "A_1", None)
        r2, l2 = region(RIGHT * 1.5 + UP * 0.75, None, GREEN_A, "A_2", None)
        r3, l3 = region(LEFT * 1.5 + DOWN * 0.75, None, YELLOW_A, "A_3", None)
        r4, l4 = region(RIGHT * 1.5 + DOWN * 0.75, None, PURPLE, "A_4", None)

        regions = VGroup(r1, r2, r3, r4)
        region_labels = VGroup(l1, l2, l3, l4)

        self.play(Write(header))
        self.play(Create(A_rect), FadeIn(A_lbl))
        self.next_slide()

        self.play(
            LaggedStart(
                *[FadeIn(r) for r in regions],
                lag_ratio=0.2,
            ),
            LaggedStart(
                *[FadeIn(l) for l in region_labels],
                lag_ratio=0.2,
            ),
            run_time=1.8,
        )
        self.next_slide()

        # Las 3 condiciones compactas, con checkmarks
        conds = VGroup(
            VGroup(
                Text("1.", font_size=24, color=YELLOW_A, weight=BOLD),
                MathTex(r"A_i \neq \emptyset", font_size=28, color=WHITE_S),
                MathTex(r"\checkmark", font_size=28, color=GREEN_A),
            ).arrange(RIGHT, buff=0.25),
            VGroup(
                Text("2.", font_size=24, color=ORANGE, weight=BOLD),
                MathTex(r"A_i \cap A_j = \emptyset \;\;(i \neq j)",
                        font_size=28, color=WHITE_S),
                MathTex(r"\checkmark", font_size=28, color=GREEN_A),
            ).arrange(RIGHT, buff=0.25),
            VGroup(
                Text("3.", font_size=24, color=PURPLE, weight=BOLD),
                MathTex(r"\bigcup_i A_i = A", font_size=28, color=WHITE_S),
                MathTex(r"\checkmark", font_size=28, color=GREEN_A),
            ).arrange(RIGHT, buff=0.25),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        conds.to_edge(DOWN, buff=0.6)

        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.2) for c in conds], lag_ratio=0.3),
                  run_time=1.8)
        self.next_slide()

        self.play(FadeOut(VGroup(A_rect, A_lbl, regions, region_labels, conds)))

        # ══ Teorema fundamental ══
        teo_label = Text("Teorema Fundamental", font_size=26, color=CYAN, weight=BOLD)
        teo_label.next_to(header, DOWN, buff=0.5)

        # Diagrama visual: Equivalencia ⟺ Partición
        # Izq: icono clases coloreadas (3 círculos juntos)
        left_bubbles = VGroup(
            Circle(radius=0.35, color=RED_A, fill_opacity=0.4, fill_color=RED_A, stroke_width=2),
            Circle(radius=0.30, color=GREEN_A, fill_opacity=0.4, fill_color=GREEN_A, stroke_width=2),
            Circle(radius=0.32, color=PURPLE, fill_opacity=0.4, fill_color=PURPLE, stroke_width=2),
        ).arrange(RIGHT, buff=0.1)
        left_outer = Ellipse(
            width=left_bubbles.width + 0.4, height=left_bubbles.height + 0.4,
            color=CYAN, stroke_width=2,
        ).move_to(left_bubbles.get_center())
        left_icon = VGroup(left_outer, left_bubbles)
        left_label = MathTex(r"R \text{ equivalencia}", font_size=24, color=CYAN)
        left_label.next_to(left_icon, DOWN, buff=0.3)
        left_side = VGroup(left_icon, left_label)

        # Der: icono partición (rectángulo con divisiones)
        right_rect = RoundedRectangle(width=1.8, height=1.1, corner_radius=0.12,
                                      color=BLUE, stroke_width=2)
        r_a = RoundedRectangle(width=0.75, height=0.45, corner_radius=0.06,
                               color=RED_A, fill_opacity=0.4, fill_color=RED_A, stroke_width=1.5)
        r_b = RoundedRectangle(width=0.75, height=0.45, corner_radius=0.06,
                               color=GREEN_A, fill_opacity=0.4, fill_color=GREEN_A, stroke_width=1.5)
        r_c = RoundedRectangle(width=0.75, height=0.45, corner_radius=0.06,
                               color=PURPLE, fill_opacity=0.4, fill_color=PURPLE, stroke_width=1.5)
        r_a.move_to(right_rect.get_center() + LEFT * 0.4 + UP * 0.25)
        r_b.move_to(right_rect.get_center() + RIGHT * 0.4 + UP * 0.25)
        r_c.move_to(right_rect.get_center() + DOWN * 0.25)
        right_icon = VGroup(right_rect, r_a, r_b, r_c)
        right_label = MathTex(r"A/R \text{ partición}", font_size=24, color=CYAN)
        right_label.next_to(right_icon, DOWN, buff=0.3)
        right_side = VGroup(right_icon, right_label)

        # Flecha bidireccional entre ambos
        equiv_arrow = MathTex(r"\Longleftrightarrow", font_size=54, color=YELLOW_A)

        teorema_row = VGroup(left_side, equiv_arrow, right_side).arrange(RIGHT, buff=0.9)
        teorema_row.next_to(teo_label, DOWN, buff=0.6)

        nota = Text(
            "Equivalencias y particiones son dos caras de la misma moneda.",
            font_size=20, color=GRAY,
        )
        nota.next_to(teorema_row, DOWN, buff=0.7)

        self.play(FadeIn(teo_label))
        self.play(
            FadeIn(left_side, shift=RIGHT * 0.3),
            FadeIn(right_side, shift=LEFT * 0.3),
        )
        self.play(Write(equiv_arrow))
        self.next_slide()

        self.play(FadeIn(nota, shift=UP * 0.2))
        self.next_slide()

        self.play(FadeOut(VGroup(header, teo_label, teorema_row, nota)))

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
