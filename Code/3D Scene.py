from manim import *

class SimCLR3D(ThreeDScene):
    def construct(self):
        # Set the orientation of the camera
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # Add a 3D axes
        axes = ThreeDAxes(x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1])
        self.add(axes)

        # Create the 3D vectors
        anchor_vector_3d = Arrow3D(start=np.array([0, 0, 0]), end=np.array([2, 2, 2]), thickness=0.02, height=0.3, base_radius=0.08, color=RED)
        positive_vector_3d = Arrow3D(start=np.array([0, 0, 0]), end=np.array([-2, -2, 2]), thickness=0.02, height=0.3, base_radius=0.08, color=GREEN)
        negative_vector_3d = Arrow3D(start=np.array([0, 0, 0]), end=np.array([2, -2, -2]), thickness=0.02, height=0.3, base_radius=0.08, color=BLUE)

        # Add the 3D vectors to the scene
        self.play(FadeIn(anchor_vector_3d), run_time=2)
        self.play(FadeIn(positive_vector_3d), run_time=2)
        self.play(FadeIn(negative_vector_3d), run_time=2)

        # Explain NT-Xent loss
        loss_explanation = Text("NT-Xent loss pushes positive examples\n(cat images) together and negative examples\n(puppy image) apart.").scale(0.5).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(loss_explanation)
        self.play(Write(loss_explanation), run_time=2)

        # Rotate the green vector until it lines up with the red vector
        self.play(Rotate(positive_vector_3d, angle=PI/1.2, about_point=ORIGIN), run_time=3)

        # Rotate the blue vector until it is completely opposite to the red vector
        self.play(Rotate(negative_vector_3d, angle= PI*1.5, about_point=ORIGIN), run_time=3)
