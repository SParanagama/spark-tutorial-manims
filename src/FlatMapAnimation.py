from manimlib.imports import *

class FlatMapAnimation(Scene):
    def construct(self):
        mapHeadingText = TexMobject("``flatMap\"")
        mapHeadingText.shift(LEFT*5.5 + UP*3)
        
        mapDefText = TextMobject("\small Takes a function which returns a traversable and applies it to every element in the RDD and then flattens it.")
        mapDefText.scale(0.8)
        mapDefText.align_to(mapHeadingText, DOWN)
        mapDefText.shift(DOWN)
        mapEqnText = TextMobject("\small $x \Rightarrow f(x) \Rightarrow [y_1, y_2, ...]$")
        mapEqnText.next_to(mapDefText, DOWN)

        rddText = TextMobject("RDD")
        rddText.shift(LEFT*6.25 + DOWN)
        rddVector = matrix_to_mobject(["x_1","x_2","x_3", "...", "...", "x_n"])
        rddVector.shift(LEFT*4.75 + DOWN)

        arrowText = TexMobject("\Rightarrow")
        arrowText.shift(LEFT*3.65 + DOWN)
        
        mappedRddText = TextMobject("RDD")
        mappedRddText.set_color(YELLOW_C)
        mappedRddText.shift(LEFT*2.65 + DOWN)
        mappedRddVector = matrix_to_mobject(["y_{11}, y_{12}","y_{21}, y_{22}, y_{23}","y_{31}, y_{32}, y_{33}", "(...)", "(...)", "y_{n1}, y_{n2}"])
        mappedRddVector.set_color(YELLOW_C)
        mappedRddVector.shift(LEFT*0.35 + DOWN)

        arrowText2 = TexMobject("\Rightarrow")
        arrowText2.shift(RIGHT*1.95 + DOWN)

        flattenedRddText = TextMobject("RDD")
        flattenedRddText.shift(RIGHT*2.95 + DOWN)
        flattenedRddVector = matrix_to_mobject(["y_{11}", "y_{12}", "y_{21}" , "y_{22}", "y_{23}", "y_{31}", "y_{32}", "y_{33}", "(...)", "(...)", "y_{n1}", "y_{n2}"])
        flattenedRddVector.shift(RIGHT*4.25 + DOWN)
        flattenedRddVector.scale(0.67)

        self.play(Write(mapHeadingText, run_time=2.0))
        self.play(FadeIn(mapDefText, run_time=2.0))
        self.wait(0.10)
        self.play(FadeIn(mapEqnText, run_time=1.0))
        self.wait(0.5)

        self.play(FadeIn(rddText, run_time=2.0))
        self.play(Write(rddVector, run_time=2.0))

        self.play(Write(arrowText, run_time=1.0))
        
        self.play(FadeIn(mappedRddText, run_time=2.0))
        self.play(Write(mappedRddVector, run_time=2.0))

        self.play(Write(arrowText2, run_time=1.0))

        self.play(FadeIn(flattenedRddText, run_time=2.0))
        self.play(Write(flattenedRddVector, run_time=2.0))
        
        self.wait(2.0)

