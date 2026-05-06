"""
Presentación Manim Slides — Núcleo e Imagen de un Morfismo
Matemática 4 — Estructuras Algebraicas / Teoría de Grupos

Temas:
  1. Repaso: homomorfismo de grupos
  2. Definición de núcleo
  3. Definición de imagen
  4. Ejercicio 19 (TP5) — Nu(f) y Im(f) son subgrupos
  5. Ejercicio 22 (TP5) — f monomorfismo ⟺ Nu(f) = {e_1}

Renderizar:  manim render -qh presentacion.py NucleoImagenSlides
Presentar:   manim-slides NucleoImagenSlides
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


class NucleoImagenSlides(Slide):

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
        t = Text(text, font_size=40, color=CYAN, weight=BOLD)
        group = VGroup(t)
        if sub:
            s = Text(sub, font_size=24, color=GRAY)
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
        title = Text("Núcleo e Imagen", font_size=60, color=CYAN, weight=BOLD)
        subtitle = Text(
            "Morfismos de Grupos",
            font_size=32, color=GRAY,
        )
        subtitle.next_to(title, DOWN, buff=0.4)

        line = Line(LEFT * 3.5, RIGHT * 3.5, color=BLUE, stroke_width=2)
        line.next_to(subtitle, DOWN, buff=0.3)

        mat = Text("Matemática 4 — Estructuras Algebraicas", font_size=24, color=GRAY)
        mat.next_to(line, DOWN, buff=0.3)

        self.play(FadeIn(title, shift=DOWN * 0.3))
        self.play(FadeIn(subtitle, shift=UP * 0.2), GrowFromCenter(line))
        self.play(FadeIn(mat))
        self.next_slide()

        self.play(FadeOut(VGroup(title, subtitle, line, mat)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 2 — Repaso: homomorfismo
    # ══════════════════════════════════════════════════════════════

    def slide_repaso_morfismo(self):
        section = self.section_title(
            "Repaso",
            "Homomorfismo de grupos",
        )
        self.play(FadeIn(section, shift=DOWN * 0.3))
        self.next_slide()
        self.play(FadeOut(section))

        header = self.header_text("¿Qué es un morfismo de grupos?")

        intro = Text(
            "Sean (G, ∗) y (H, ◦) dos grupos.\n"
            "Una función f : G → H es un homomorfismo si\n"
            "respeta la operación de los grupos:",
            font_size=28, color=WHITE_S, line_spacing=1.4,
        )
        intro.next_to(header, DOWN, buff=0.4)

        formula = MathTex(
            r"f(a \ast b) \;=\; f(a) \circ f(b)",
            r"\quad\forall\, a, b \in G",
            font_size=42, color=WHITE_S,
        )
        formula[0].set_color(CYAN)
        formula.next_to(intro, DOWN, buff=0.5)

        nota = VGroup(
            Text("Consecuencias inmediatas:", font_size=24, color=YELLOW_A, weight=BOLD),
            MathTex(r"f(e_G) = e_H",
                    font_size=32, color=WHITE_S),
            MathTex(r"f(a^{-1}) = f(a)^{-1}",
                    font_size=32, color=WHITE_S),
        ).arrange(DOWN, buff=0.25)
        nota.next_to(formula, DOWN, buff=0.5)

        self.play(Write(header))
        self.play(FadeIn(intro, shift=UP * 0.2))
        self.next_slide()

        self.play(Write(formula), run_time=2)
        self.next_slide()

        self.play(FadeIn(nota, shift=UP * 0.2))
        self.next_slide()

        self.play(FadeOut(VGroup(header, intro, formula, nota)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 3 — Definición de Núcleo
    # ══════════════════════════════════════════════════════════════

    def slide_definicion_nucleo(self):
        section = self.section_title(
            "Núcleo de un morfismo",
            "Notación: Nu(f)",
        )
        self.play(FadeIn(section, shift=DOWN * 0.3))
        self.next_slide()
        self.play(FadeOut(section))

        header = self.header_text("Definición — Núcleo")

        defn = MathTex(
            r"\mathrm{Nu}(f)", r"\;=\;",
            r"\{\, x \in G \;:\; f(x) = e_H \,\}",
            font_size=42, color=WHITE_S,
        )
        defn[0].set_color(CYAN)
        defn[2].set_color(GREEN_A)
        defn.next_to(header, DOWN, buff=0.5)

        defn_sub = Text(
            "= elementos de G que f envía al neutro de H",
            font_size=22, color=GRAY,
        )
        defn_sub.next_to(defn, DOWN, buff=0.25)

        # ── Diagrama: G ────► H con los puntos del núcleo destacados
        # G a la izquierda, H a la derecha
        G_center = LEFT * 3.5 + DOWN * 0.5
        H_center = RIGHT * 3.5 + DOWN * 0.5

        G_oval = Ellipse(width=3.2, height=3.4, color=BLUE, stroke_width=2).move_to(G_center)
        H_oval = Ellipse(width=3.2, height=3.4, color=BLUE, stroke_width=2).move_to(H_center)
        G_lbl = MathTex("G", font_size=30, color=BLUE).next_to(G_oval, UP, buff=0.15)
        H_lbl = MathTex("H", font_size=30, color=BLUE).next_to(H_oval, UP, buff=0.15)

        # Puntos del núcleo en G (van todos al neutro)
        k1 = Dot(G_center + UP * 0.6 + LEFT * 0.4, color=RED_A, radius=0.10)
        k2 = Dot(G_center + UP * 0.1 + RIGHT * 0.5, color=RED_A, radius=0.10)
        k3 = Dot(G_center + DOWN * 0.5 + LEFT * 0.2, color=RED_A, radius=0.10)
        # Otros puntos en G (no son del núcleo)
        o1 = Dot(G_center + UP * 1.0 + RIGHT * 0.6, color=WHITE_S, radius=0.08)
        o2 = Dot(G_center + DOWN * 1.0 + RIGHT * 0.4, color=WHITE_S, radius=0.08)

        # Neutro de H
        eH = Dot(H_center, color=GREEN_A, radius=0.14)
        eH_lbl = MathTex("e_H", font_size=26, color=GREEN_A).next_to(eH, RIGHT, buff=0.15)
        # Otros puntos en H (imágenes de o1 y o2)
        h1 = Dot(H_center + UP * 0.9 + RIGHT * 0.3, color=WHITE_S, radius=0.08)
        h2 = Dot(H_center + DOWN * 0.9 + LEFT * 0.4, color=WHITE_S, radius=0.08)

        # Burbuja del núcleo
        nu_bubble = Ellipse(
            width=1.8, height=2.0, color=RED_A, stroke_width=2,
            fill_opacity=0.15, fill_color=RED_A,
        ).move_to(VGroup(k1, k2, k3).get_center())
        nu_lbl = MathTex(r"\mathrm{Nu}(f)", font_size=22, color=RED_A).next_to(nu_bubble, DOWN, buff=0.1)

        # Flechas
        a1 = Arrow(k1.get_center(), eH.get_center(), color=RED_A,
                   buff=0.15, stroke_width=2, tip_length=0.15, max_tip_length_to_length_ratio=0.06)
        a2 = Arrow(k2.get_center(), eH.get_center(), color=RED_A,
                   buff=0.15, stroke_width=2, tip_length=0.15, max_tip_length_to_length_ratio=0.06)
        a3 = Arrow(k3.get_center(), eH.get_center(), color=RED_A,
                   buff=0.15, stroke_width=2, tip_length=0.15, max_tip_length_to_length_ratio=0.06)
        a4 = Arrow(o1.get_center(), h1.get_center(), color=GRAY,
                   buff=0.15, stroke_width=1.5, tip_length=0.13, max_tip_length_to_length_ratio=0.06)
        a5 = Arrow(o2.get_center(), h2.get_center(), color=GRAY,
                   buff=0.15, stroke_width=1.5, tip_length=0.13, max_tip_length_to_length_ratio=0.06)

        diagram = VGroup(G_oval, H_oval, G_lbl, H_lbl,
                         nu_bubble, nu_lbl,
                         k1, k2, k3, o1, o2,
                         eH, eH_lbl, h1, h2,
                         a1, a2, a3, a4, a5)
        diagram.shift(DOWN * 0.5)

        self.play(Write(header))
        self.play(Write(defn), run_time=1.5)
        self.play(FadeIn(defn_sub))
        self.next_slide()

        # Mover defn arriba para hacer espacio al diagrama
        self.play(
            defn.animate.scale(0.75).next_to(header, DOWN, buff=0.25),
            FadeOut(defn_sub),
        )

        self.play(
            Create(G_oval), Create(H_oval),
            FadeIn(G_lbl), FadeIn(H_lbl),
        )
        self.play(
            FadeIn(VGroup(k1, k2, k3, o1, o2)),
            FadeIn(eH), FadeIn(eH_lbl),
            FadeIn(h1), FadeIn(h2),
        )
        self.play(
            Create(nu_bubble), FadeIn(nu_lbl),
        )
        self.play(
            LaggedStart(GrowArrow(a1), GrowArrow(a2), GrowArrow(a3),
                        GrowArrow(a4), GrowArrow(a5),
                        lag_ratio=0.15),
            run_time=2,
        )
        self.next_slide()

        self.play(FadeOut(VGroup(header, defn, diagram)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 4 — Definición de Imagen
    # ══════════════════════════════════════════════════════════════

    def slide_definicion_imagen(self):
        section = self.section_title(
            "Imagen de un morfismo",
            "Im(f)",
        )
        self.play(FadeIn(section, shift=DOWN * 0.3))
        self.next_slide()
        self.play(FadeOut(section))

        header = self.header_text("Definición — Imagen")

        defn = MathTex(
            r"\mathrm{Im}(f)", r"\;=\;",
            r"\{\, y \in H \;:\; \exists\, x \in G,\; f(x) = y \,\}",
            font_size=38, color=WHITE_S,
        )
        defn[0].set_color(CYAN)
        defn[2].set_color(GREEN_A)
        defn.next_to(header, DOWN, buff=0.5)

        defn_alt = MathTex(
            r"\mathrm{Im}(f) \;=\; f(G) \;=\; \{\, f(x) : x \in G \,\}",
            font_size=34, color=WHITE_S,
        )
        defn_alt.next_to(defn, DOWN, buff=0.3)

        defn_sub = Text(
            "= todos los elementos de H que son alcanzados por f",
            font_size=22, color=GRAY,
        )
        defn_sub.next_to(defn_alt, DOWN, buff=0.3)

        # ── Diagrama Im(f) ⊆ H ──
        G_center = LEFT * 3.5 + DOWN * 0.8
        H_center = RIGHT * 3.5 + DOWN * 0.8

        G_oval = Ellipse(width=3.2, height=3.0, color=BLUE, stroke_width=2).move_to(G_center)
        H_oval = Ellipse(width=3.2, height=3.0, color=BLUE, stroke_width=2).move_to(H_center)
        G_lbl = MathTex("G", font_size=28, color=BLUE).next_to(G_oval, UP, buff=0.1)
        H_lbl = MathTex("H", font_size=28, color=BLUE).next_to(H_oval, UP, buff=0.1)

        # Puntos en G
        g1 = Dot(G_center + UP * 0.6, color=WHITE_S, radius=0.09)
        g2 = Dot(G_center + LEFT * 0.5 + DOWN * 0.2, color=WHITE_S, radius=0.09)
        g3 = Dot(G_center + RIGHT * 0.4 + DOWN * 0.4, color=WHITE_S, radius=0.09)

        # Puntos en H, imagen del subconjunto
        i1 = Dot(H_center + UP * 0.5 + LEFT * 0.3, color=GREEN_A, radius=0.10)
        i2 = Dot(H_center + DOWN * 0.2 + RIGHT * 0.3, color=GREEN_A, radius=0.10)
        i3 = Dot(H_center + DOWN * 0.6 + LEFT * 0.4, color=GREEN_A, radius=0.10)
        # Punto en H fuera de Im(f)
        out = Dot(H_center + UP * 1.0 + RIGHT * 0.6, color=GRAY, radius=0.09)

        im_bubble = Ellipse(
            width=2.0, height=2.2, color=GREEN_A, stroke_width=2,
            fill_opacity=0.18, fill_color=GREEN_A,
        ).move_to(VGroup(i1, i2, i3).get_center())
        im_lbl = MathTex(r"\mathrm{Im}(f)", font_size=22, color=GREEN_A).next_to(im_bubble, DOWN, buff=0.1)

        a1 = Arrow(g1.get_center(), i1.get_center(), color=GREEN_A,
                   buff=0.15, stroke_width=2, tip_length=0.14, max_tip_length_to_length_ratio=0.06)
        a2 = Arrow(g2.get_center(), i2.get_center(), color=GREEN_A,
                   buff=0.15, stroke_width=2, tip_length=0.14, max_tip_length_to_length_ratio=0.06)
        a3 = Arrow(g3.get_center(), i3.get_center(), color=GREEN_A,
                   buff=0.15, stroke_width=2, tip_length=0.14, max_tip_length_to_length_ratio=0.06)

        diagram = VGroup(G_oval, H_oval, G_lbl, H_lbl,
                         im_bubble, im_lbl,
                         g1, g2, g3, i1, i2, i3, out,
                         a1, a2, a3)

        self.play(Write(header))
        self.play(Write(defn), run_time=1.5)
        self.next_slide()
        self.play(FadeIn(defn_alt, shift=UP * 0.2))
        self.play(FadeIn(defn_sub))
        self.next_slide()

        self.play(
            defn.animate.scale(0.7).next_to(header, DOWN, buff=0.2),
            FadeOut(defn_alt), FadeOut(defn_sub),
        )

        self.play(
            Create(G_oval), Create(H_oval),
            FadeIn(G_lbl), FadeIn(H_lbl),
        )
        self.play(
            FadeIn(VGroup(g1, g2, g3, out)),
        )
        self.play(
            Create(im_bubble), FadeIn(im_lbl),
            FadeIn(VGroup(i1, i2, i3)),
        )
        self.play(
            LaggedStart(GrowArrow(a1), GrowArrow(a2), GrowArrow(a3),
                        lag_ratio=0.2),
            run_time=1.5,
        )
        self.next_slide()

        self.play(FadeOut(VGroup(header, defn, diagram)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 5 — Ejercicio 19 (TP5)
    # ══════════════════════════════════════════════════════════════

    def slide_ejercicio_19(self):
        section = self.section_title(
            "Ejercicio 19",
            "Trabajo Práctico 5",
        )
        self.play(FadeIn(section, shift=DOWN * 0.3))
        self.next_slide()
        self.play(FadeOut(section))

        # ── Enunciado ──
        header = self.header_text("Ej. 19 — Enunciado")

        enunc = VGroup(
            Text(
                "Sea f : G ⟶ H un homomorfismo de grupos.",
                font_size=30, color=WHITE_S,
            ),
            Text(
                "Demostrar que:",
                font_size=28, color=WHITE_S,
            ),
            VGroup(
                MathTex(r"\bullet \;\; \mathrm{Nu}(f) \text{ es subgrupo de } G",
                        font_size=34, color=CYAN),
                MathTex(r"\bullet \;\; \mathrm{Im}(f) \text{ es subgrupo de } H",
                        font_size=34, color=CYAN),
            ).arrange(DOWN, buff=0.3, aligned_edge=LEFT),
        ).arrange(DOWN, buff=0.45)
        enunc.next_to(header, DOWN, buff=0.5)

        self.play(Write(header))
        self.play(FadeIn(enunc, shift=UP * 0.2))
        self.next_slide()

        self.play(FadeOut(enunc))

        # ── Estrategia: criterio de subgrupo ──
        self.play(header.animate.become(
            self.header_text("Ej. 19 — Estrategia")
        ))

        criterio = VGroup(
            Text("Criterio de subgrupo:", font_size=28, color=YELLOW_A, weight=BOLD),
            Text("S ⊆ G es subgrupo de G ⟺", font_size=26, color=WHITE_S),
            VGroup(
                MathTex(r"\text{(i)} \;\; S \neq \emptyset",
                        font_size=30, color=WHITE_S),
                MathTex(r"\text{(ii)} \;\; \forall\,a, b \in S:\; a \ast b^{-1} \in S",
                        font_size=30, color=WHITE_S),
            ).arrange(DOWN, buff=0.3, aligned_edge=LEFT),
            Text("Aplicaremos este criterio a Nu(f) y a Im(f).",
                 font_size=24, color=GRAY),
        ).arrange(DOWN, buff=0.4)
        criterio.next_to(header, DOWN, buff=0.45)

        self.play(FadeIn(criterio, shift=UP * 0.2))
        self.next_slide()
        self.play(FadeOut(criterio))

        # ══════════════════════════════════════════════
        # PARTE A — Nu(f) ≤ G
        # ══════════════════════════════════════════════
        self.play(header.animate.become(
            self.header_text("Ej. 19 (a) — Nu(f) es subgrupo de G")
        ))

        # Paso 1: no vacío
        paso1 = VGroup(
            Text("Paso 1: Nu(f) ≠ ∅", font_size=28, color=YELLOW_A, weight=BOLD),
            MathTex(r"f(e_G) = e_H \;\;(\text{prop. de morfismo})",
                    font_size=32, color=WHITE_S),
            MathTex(r"\Rightarrow\; e_G \in \mathrm{Nu}(f)",
                    font_size=34, color=GREEN_A),
            Text("Por lo tanto Nu(f) ≠ ∅ ✓", font_size=26, color=GREEN_A, weight=BOLD),
        ).arrange(DOWN, buff=0.3)
        paso1.next_to(header, DOWN, buff=0.45)

        self.play(FadeIn(paso1, shift=UP * 0.2))
        self.next_slide()
        self.play(FadeOut(paso1))

        # Paso 2: cerrado bajo a*b^-1
        paso2 = VGroup(
            Text("Paso 2: cierre bajo a ∗ b⁻¹", font_size=28, color=YELLOW_A, weight=BOLD),
            MathTex(r"\text{Sean } a, b \in \mathrm{Nu}(f)"
                    r"\;\Rightarrow\; f(a) = e_H \,\land\, f(b) = e_H",
                    font_size=28, color=WHITE_S),
            MathTex(r"f(a \ast b^{-1}) = f(a) \circ f(b^{-1}) = f(a) \circ f(b)^{-1}",
                    font_size=28, color=WHITE_S),
            MathTex(r"= e_H \circ e_H^{-1} = e_H \circ e_H = e_H",
                    font_size=30, color=WHITE_S),
            MathTex(r"\Rightarrow\; a \ast b^{-1} \in \mathrm{Nu}(f) \;\checkmark",
                    font_size=32, color=GREEN_A),
        ).arrange(DOWN, buff=0.28)
        paso2.next_to(header, DOWN, buff=0.4)

        self.play(FadeIn(paso2, shift=UP * 0.2))
        self.next_slide()
        self.play(FadeOut(paso2))

        # Conclusión parte (a)
        concl_a = VGroup(
            MathTex(r"\mathrm{Nu}(f) \neq \emptyset \;\;\land\;\;"
                    r"a, b \in \mathrm{Nu}(f) \Rightarrow a \ast b^{-1} \in \mathrm{Nu}(f)",
                    font_size=30, color=WHITE_S),
            MathTex(r"\therefore\; \mathrm{Nu}(f) \leq G \;\;\blacksquare",
                    font_size=42, color=CYAN),
        ).arrange(DOWN, buff=0.5)
        concl_a.next_to(header, DOWN, buff=0.7)
        concl_a_box = SurroundingRectangle(concl_a[1], color=CYAN, buff=0.25, corner_radius=0.1)

        self.play(FadeIn(concl_a, shift=UP * 0.2))
        self.play(Create(concl_a_box))
        self.next_slide()
        self.play(FadeOut(VGroup(concl_a, concl_a_box)))

        # ══════════════════════════════════════════════
        # PARTE B — Im(f) ≤ H
        # ══════════════════════════════════════════════
        self.play(header.animate.become(
            self.header_text("Ej. 19 (b) — Im(f) es subgrupo de H")
        ))

        # Paso 1: no vacío
        paso1b = VGroup(
            Text("Paso 1: Im(f) ≠ ∅", font_size=28, color=YELLOW_A, weight=BOLD),
            MathTex(r"f(e_G) = e_H",
                    font_size=32, color=WHITE_S),
            MathTex(r"\Rightarrow\; e_H \in \mathrm{Im}(f)",
                    font_size=34, color=GREEN_A),
            Text("Por lo tanto Im(f) ≠ ∅ ✓", font_size=26, color=GREEN_A, weight=BOLD),
        ).arrange(DOWN, buff=0.3)
        paso1b.next_to(header, DOWN, buff=0.45)

        self.play(FadeIn(paso1b, shift=UP * 0.2))
        self.next_slide()
        self.play(FadeOut(paso1b))

        # Paso 2: cierre
        paso2b = VGroup(
            Text("Paso 2: cierre bajo y₁ ◦ y₂⁻¹", font_size=28, color=YELLOW_A, weight=BOLD),
            MathTex(r"\text{Sean } y_1, y_2 \in \mathrm{Im}(f)",
                    font_size=28, color=WHITE_S),
            MathTex(r"\Rightarrow\; \exists\, x_1, x_2 \in G:\;"
                    r"f(x_1) = y_1,\; f(x_2) = y_2",
                    font_size=28, color=WHITE_S),
            MathTex(r"y_1 \circ y_2^{-1} = f(x_1) \circ f(x_2)^{-1}"
                    r"= f(x_1) \circ f(x_2^{-1})",
                    font_size=28, color=WHITE_S),
            MathTex(r"= f(x_1 \ast x_2^{-1})",
                    font_size=30, color=WHITE_S),
            MathTex(r"\text{Como } x_1 \ast x_2^{-1} \in G"
                    r"\Rightarrow y_1 \circ y_2^{-1} \in \mathrm{Im}(f) \;\checkmark",
                    font_size=28, color=GREEN_A),
        ).arrange(DOWN, buff=0.22)
        paso2b.next_to(header, DOWN, buff=0.35)

        self.play(FadeIn(paso2b, shift=UP * 0.2))
        self.next_slide()
        self.play(FadeOut(paso2b))

        # Conclusión parte (b)
        concl_b = VGroup(
            MathTex(r"\mathrm{Im}(f) \neq \emptyset \;\;\land\;\;"
                    r"y_1, y_2 \in \mathrm{Im}(f) \Rightarrow y_1 \circ y_2^{-1} \in \mathrm{Im}(f)",
                    font_size=28, color=WHITE_S),
            MathTex(r"\therefore\; \mathrm{Im}(f) \leq H \;\;\blacksquare",
                    font_size=42, color=CYAN),
        ).arrange(DOWN, buff=0.5)
        concl_b.next_to(header, DOWN, buff=0.7)
        concl_b_box = SurroundingRectangle(concl_b[1], color=CYAN, buff=0.25, corner_radius=0.1)

        self.play(FadeIn(concl_b, shift=UP * 0.2))
        self.play(Create(concl_b_box))
        self.next_slide()

        self.play(FadeOut(VGroup(header, concl_b, concl_b_box)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 6 — Ejercicio 22 (TP5)
    # ══════════════════════════════════════════════════════════════

    def slide_ejercicio_22(self):
        section = self.section_title(
            "Ejercicio 22",
            "Trabajo Práctico 5",
        )
        self.play(FadeIn(section, shift=DOWN * 0.3))
        self.next_slide()
        self.play(FadeOut(section))

        # ── Enunciado ──
        header = self.header_text("Ej. 22 — Enunciado")

        enunc = VGroup(
            Text(
                "Sea f : G₁ ⟶ G₂ un morfismo de grupos.",
                font_size=30, color=WHITE_S,
            ),
            Text("Probar que:", font_size=28, color=WHITE_S),
            MathTex(
                r"f \text{ es monomorfismo}",
                r"\;\Longleftrightarrow\;",
                r"\mathrm{Nu}(f) = \{e_1\}",
                font_size=38, color=WHITE_S,
            ),
            Text(
                "(monomorfismo = morfismo inyectivo)",
                font_size=22, color=GRAY,
            ),
        ).arrange(DOWN, buff=0.45)
        enunc[2][0].set_color(CYAN)
        enunc[2][2].set_color(CYAN)
        enunc.next_to(header, DOWN, buff=0.45)

        self.play(Write(header))
        self.play(FadeIn(enunc, shift=UP * 0.2))
        self.next_slide()
        self.play(FadeOut(enunc))

        # ══════════════════════════════════════════════
        # IDA: f inyectiva ⟹ Nu(f) = {e1}
        # ══════════════════════════════════════════════
        self.play(header.animate.become(
            self.header_text("Ej. 22 — (⟹)  f inyectiva ⟹ Nu(f) = {e₁}")
        ))

        ida = VGroup(
            Text("Hipótesis: f es inyectiva.", font_size=26, color=YELLOW_A, weight=BOLD),
            MathTex(r"\text{Sea } x \in \mathrm{Nu}(f) \Rightarrow f(x) = e_2",
                    font_size=30, color=WHITE_S),
            MathTex(r"\text{Por morfismo: } f(e_1) = e_2",
                    font_size=30, color=WHITE_S),
            MathTex(r"\Rightarrow\; f(x) = f(e_1)",
                    font_size=32, color=WHITE_S),
            MathTex(r"\text{Como } f \text{ es inyectiva: } x = e_1",
                    font_size=30, color=WHITE_S),
            MathTex(r"\therefore\; \mathrm{Nu}(f) = \{e_1\} \;\checkmark",
                    font_size=34, color=GREEN_A),
        ).arrange(DOWN, buff=0.28)
        ida.next_to(header, DOWN, buff=0.4)

        self.play(FadeIn(ida, shift=UP * 0.2))
        self.next_slide()
        self.play(FadeOut(ida))

        # ══════════════════════════════════════════════
        # VUELTA: Nu(f) = {e1} ⟹ f inyectiva
        # ══════════════════════════════════════════════
        self.play(header.animate.become(
            self.header_text("Ej. 22 — (⟸)  Nu(f) = {e₁} ⟹ f inyectiva")
        ))

        vuelta = VGroup(
            Text("Hipótesis: Nu(f) = {e₁}.", font_size=26, color=YELLOW_A, weight=BOLD),
            MathTex(r"\text{Sean } a, b \in G_1 \text{ con } f(a) = f(b)",
                    font_size=30, color=WHITE_S),
            MathTex(r"f(a) \circ f(b)^{-1} = e_2",
                    font_size=30, color=WHITE_S),
            MathTex(r"f(a) \circ f(b^{-1}) = e_2 \;\Rightarrow\; f(a \ast b^{-1}) = e_2",
                    font_size=28, color=WHITE_S),
            MathTex(r"\Rightarrow\; a \ast b^{-1} \in \mathrm{Nu}(f) = \{e_1\}",
                    font_size=30, color=WHITE_S),
            MathTex(r"\Rightarrow\; a \ast b^{-1} = e_1 \;\Rightarrow\; a = b",
                    font_size=30, color=WHITE_S),
            MathTex(r"\therefore\; f \text{ es inyectiva} \;\checkmark",
                    font_size=32, color=GREEN_A),
        ).arrange(DOWN, buff=0.22)
        vuelta.next_to(header, DOWN, buff=0.35)

        self.play(FadeIn(vuelta, shift=UP * 0.2))
        self.next_slide()
        self.play(FadeOut(vuelta))

        # ── Conclusión final del Ej. 22 ──
        self.play(header.animate.become(
            self.header_text("Ej. 22 — Conclusión")
        ))

        concl = VGroup(
            MathTex(r"(\Rightarrow) \;\;\checkmark \quad (\Leftarrow) \;\;\checkmark",
                    font_size=36, color=GREEN_A),
            MathTex(
                r"f \text{ monomorfismo}",
                r"\;\Longleftrightarrow\;",
                r"\mathrm{Nu}(f) = \{e_1\}",
                font_size=40, color=CYAN,
            ),
            Text(
                "Para chequear inyectividad de un morfismo,\n"
                "basta con calcular el núcleo.",
                font_size=24, color=GRAY, line_spacing=1.3,
            ),
        ).arrange(DOWN, buff=0.5)
        concl.next_to(header, DOWN, buff=0.6)
        concl_box = SurroundingRectangle(concl[1], color=CYAN, buff=0.25, corner_radius=0.1)

        self.play(FadeIn(concl, shift=UP * 0.2))
        self.play(Create(concl_box))
        self.next_slide()

        self.play(FadeOut(VGroup(header, concl, concl_box)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 7 — Resumen
    # ══════════════════════════════════════════════════════════════

    def slide_resumen(self):
        header = self.header_text("Resumen")

        items = VGroup(
            VGroup(
                Text("Núcleo", font_size=26, color=RED_A, weight=BOLD),
                MathTex(r"\mathrm{Nu}(f) = \{x \in G : f(x) = e_H\}",
                        font_size=30, color=WHITE_S),
            ).arrange(DOWN, buff=0.18),
            VGroup(
                Text("Imagen", font_size=26, color=GREEN_A, weight=BOLD),
                MathTex(r"\mathrm{Im}(f) = \{f(x) : x \in G\}",
                        font_size=30, color=WHITE_S),
            ).arrange(DOWN, buff=0.18),
            VGroup(
                Text("Subgrupos (Ej. 19)", font_size=26, color=CYAN, weight=BOLD),
                MathTex(r"\mathrm{Nu}(f) \leq G \quad \mathrm{Im}(f) \leq H",
                        font_size=30, color=WHITE_S),
            ).arrange(DOWN, buff=0.18),
            VGroup(
                Text("Test de inyectividad (Ej. 22)", font_size=26, color=YELLOW_A, weight=BOLD),
                MathTex(r"f \text{ monomorfismo} \Leftrightarrow \mathrm{Nu}(f) = \{e_G\}",
                        font_size=28, color=WHITE_S),
            ).arrange(DOWN, buff=0.18),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        items.next_to(header, DOWN, buff=0.5)

        self.play(Write(header))
        self.play(
            LaggedStart(*[FadeIn(it, shift=UP * 0.3) for it in items], lag_ratio=0.25),
            run_time=2.5,
        )
        self.next_slide()

        self.play(FadeOut(VGroup(header, items)))

    # ══════════════════════════════════════════════════════════════
    #  SLIDE 8 — Cierre
    # ══════════════════════════════════════════════════════════════

    def slide_cierre(self):
        title = Text("Núcleo e Imagen", font_size=54, color=CYAN, weight=BOLD)
        thanks = Text("¡Gracias!", font_size=48, color=WHITE_S)
        thanks.next_to(title, DOWN, buff=0.5)

        line = Line(LEFT * 3, RIGHT * 3, color=BLUE, stroke_width=2)
        line.next_to(thanks, DOWN, buff=0.3)

        self.play(FadeIn(title, shift=DOWN * 0.3))
        self.play(GrowFromCenter(line), FadeIn(thanks, shift=UP * 0.2))
        self.next_slide()

    # ══════════════════════════════════════════════════════════════
    #  CONSTRUCT
    # ══════════════════════════════════════════════════════════════

    def construct(self):
        self.slide_titulo()
        self.slide_repaso_morfismo()
        self.slide_definicion_nucleo()
        self.slide_definicion_imagen()
        self.slide_ejercicio_19()
        self.slide_ejercicio_22()
        self.slide_resumen()
        self.slide_cierre()
