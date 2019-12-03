from manimlib.imports import *

class MapAnimation(Scene):
    def construct(self):
        mapHeadingText = TexMobject("``map\"")
        mapHeadingText.shift(LEFT*6 + UP*3)
        
        mapDefText = TextMobject("\small Takes a function  and applies it to every element in the RDD.")
        mapDefText.align_to(mapHeadingText, DOWN)
        mapDefText.shift(DOWN)
        mapEqnText = TextMobject("\small $x \Rightarrow f(x) \Rightarrow y$")
        mapEqnText.next_to(mapDefText, DOWN)

        rddText = TextMobject("RDD")
        rddText.shift(LEFT*4.25 + DOWN)
        rddVector = matrix_to_mobject(["x_1","x_2","x_3", "...", "...", "x_n"])
        rddVector.shift(LEFT*2.85 + DOWN)

        arrowText = TexMobject("\Rightarrow")
        arrowText.shift(DOWN)
        arrowText.stretch_in_place(2, [0])

        mappedRddText = TextMobject("RDD")
        mappedRddText.shift(RIGHT*1.5 + DOWN)
        mappedRddVector = matrix_to_mobject(["y_1=f(x_1)","y_2=f(x_2)","y_3=f(x_3)", "(...)", "(...)", "y_n=f(x_n)"])
        mappedRddVector.shift(RIGHT*3.85 + DOWN)

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

        self.wait(4.0)

