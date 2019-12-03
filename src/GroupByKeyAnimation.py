from manimlib.imports import *

class GroupByKeyAnimation(Scene):
    def construct(self):
        
        topGroup = VGroup()
        headingText = TexMobject("``groupByKey\"")
        headingText.to_corner(LEFT+TOP).shift(LEFT*0.25+UP*1.75)

        defText = TextMobject("Groups a `Pair RDD' according to its key. Often followed by a call to mapValues()")
        defText.scale(0.7)
        defText.align_to(headingText, UP).shift(DOWN) #.align_to(headingText, LEFT)
    
        eqnText = TextMobject("$RDD[(K, V)] \Rightarrow RDD[(K, Iterable[V])]$")
        eqnText.scale(0.7)
        eqnText.next_to(defText, DOWN*1.5)

        #topGroup.add(headingText, defText, eqnText)
        #topGroup.scale(0.6)

        bottomGroup = VGroup()
        rddGroup = VGroup()
        bottomGroup.add(rddGroup)
        rddText = TextMobject("RDD")
        rddGroup.add(rddText)
        emptyRddVector = matrix_to_mobject(["\ \ \ \ \ \ \ \ \ " for i in range(0,10)])
        rddGroup.add(emptyRddVector)
        emptyRddVector.next_to(rddText, RIGHT*0.5)

        k1Group = [TextMobject("$k_1$","$,$", "$v_{1%d}$" % i, arg_separator="" ) for i in range(1,4)]
        k2Group = [TextMobject("$k_2$","$,$", "$v_{2%d}$" % i, arg_separator="" ) for i in range(1,4)]
        k3Group = [TextMobject("$k_3$","$,$", "$v_{3%d}$" % i, arg_separator="" ) for i in range(1,4)]
        
        keyValueStartingPoint = emptyRddVector.get_edge_center(TOP) + DOWN*0.55
        keyValueOrderedPositions = [keyValueStartingPoint + DOWN*i*0.60 for i in range (0,len(k1Group)*3)]
        keyValueRandomPositions =  keyValueOrderedPositions.copy()
        random.shuffle(keyValueRandomPositions)
        
        arrowText = TexMobject("\Rightarrow")
        bottomGroup.add(arrowText)
        arrowText.next_to(emptyRddVector, RIGHT*2)
        arrowText.stretch_in_place(1.5, [0])

        i=0
        for group in [k1Group, k2Group, k3Group]:
            for kv in group:
                rddGroup.add(kv)
                kv.move_to(keyValueRandomPositions[i])
                i=i+1
        
        
        groupedRddText = rddText.copy()
        bottomGroup.add(groupedRddText)
        groupedRddText.next_to(arrowText, RIGHT*2)
        emptyRddVector2 = matrix_to_mobject(["\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ " for i in range(0,7)])
        bottomGroup.add(emptyRddVector2)
        emptyRddVector2.next_to(groupedRddText, RIGHT*0.5)

        bottomGroup.to_edge(edge=LEFT)
        bottomGroup.shift(DOWN*1.5)
        bottomGroup.scale(0.75)

        groupedKeyValueStartingPoint = emptyRddVector2.get_left() + RIGHT*0.75 + UP
        groupedKeyPositions = [groupedKeyValueStartingPoint + DOWN*i for i in range(0,4) ]
        groupedValuePositions = [ [pos+ RIGHT*1.1, pos + RIGHT*2.1, pos + RIGHT*3.1] for pos in groupedKeyPositions]        
        
        self.play(Write(headingText, run_time=2.0))
        self.play(Write(defText),
                  Write(eqnText))

        self.play(Write(rddGroup))
        self.play(FadeIn(arrowText))
        self.wait(2.0)

        self.play(
            Write(groupedRddText),
            Write(emptyRddVector2)
        )

        #self.wait(2.0)

        for group, key_pos, value_pos in zip([k1Group, k2Group, k3Group], groupedKeyPositions, groupedValuePositions):
            self.play( *[Indicate(kv) for kv in group] )
            #for kv in group:
            #    kv.set_color(YELLOW_C)

            self.play( *[ApplyMethod(kv.split()[0].copy().move_to, key_pos) for kv in group],
                        *[Transform(kv.split()[0], kv.split()[0].copy().set_color(YELLOW_C)) for kv in group] )
            self.play(Write(TextMobject(", (\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ )").next_to(key_pos+RIGHT*0.15)))
            self.play( *[ApplyMethod(kv.split()[2].copy().move_to, val_pos) for kv, val_pos in zip(group, value_pos)],
                        *[Transform(kv.split()[2], kv.split()[2].copy().set_color(YELLOW_C)) for kv in group] )

        self.wait(5.0)



