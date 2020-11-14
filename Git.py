from manimlib.imports import *


class GitScene(Scene):
    def construct(self):
        self.play(ShowCreation(SVGMobject("assets/git/git.svg")), run_time=2)
        self.wait(2)
