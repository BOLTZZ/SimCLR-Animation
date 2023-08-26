from manim import *

class SimCLR2D(Scene):
    def construct(self):
        # Load the images
        anchor = ImageMobject("/content/whitecat.jpg").scale(0.15).move_to(UP*2 + LEFT*2)
        positive = ImageMobject("/content/blackcat.jpeg").scale(0.8).move_to(LEFT*2)
        negative = ImageMobject("/content/puppy.jpg").scale(0.2).move_to(DOWN*2 + LEFT*2)

        # Create the vectors
        anchor_vector = Arrow(anchor.get_center() + RIGHT*2, anchor.get_center() + RIGHT*4, buff=0, color=RED)
        positive_vector = Arrow(positive.get_center() + RIGHT*2, positive.get_center() + RIGHT*4, buff=0, color=GREEN)
        negative_vector = Arrow(negative.get_center() + RIGHT*2, negative.get_center() + RIGHT*4, buff=0, color=BLUE)

        # Add the anchor vector and image to the scene
        self.play(FadeIn(anchor), run_time=2)
        self.play(FadeIn(anchor_vector), run_time=2)

        # Add the positive vector and image to the scene
        self.play(FadeIn(positive), run_time=2)
        self.play(FadeIn(positive_vector), run_time=2)

        # Add the negative vector and image to the scene
        self.play(FadeIn(negative), run_time=2)
        self.play(FadeIn(negative_vector), run_time=2)

        self.wait(2)
