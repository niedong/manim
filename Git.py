from manimlib.imports import *


class GitScene(Scene):
    def construct(self):
        self.play(ShowCreation(SVGMobject("assets/git/GitHub-Mark.svg").scale(8).shift(DOWN * 5)), run_time=2)
        self.wait(2)
