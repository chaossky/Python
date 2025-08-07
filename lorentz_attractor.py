from manim import *
import numpy as np
from scipy.integrate import solve_ivp

# Parameters for Lorenz system
sigma = 10
rho = 28
beta = 8 / 3

# Lorenz system differential equations
def lorenz(t, state):
    x, y, z = state
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return [dx, dy, dz]

# Generate Lorenz data using scipy's solve_ivp
def generate_lorenz_data(start_point, t_max=40, dt=0.01):
    t_span = (0, t_max)
    t_eval = np.arange(0, t_max, dt)
    sol = solve_ivp(lorenz, t_span, start_point, t_eval=t_eval, method="RK45")
    return sol.y.T  # Transpose to get array of [x, y, z]

class LorenzAttractor3D(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)

        # Axes
        axes = ThreeDAxes(
            x_range=[-30, 30, 10],
            y_range=[-30, 30, 10],
            z_range=[0, 60, 10],
            x_length=10,
            y_length=10,
            z_length=6,
        )
        self.add(axes)

        # Generate Lorenz data
        initial_point = [1, 1, 1]
        lorenz_points = generate_lorenz_data(initial_point, t_max=30)
        manim_points = [axes.c2p(x, y, z) for x, y, z in lorenz_points]

        # Create the path
        attractor_path = VMobject(color=YELLOW).set_points_smoothly(manim_points[:2])

        # Dot at the head
        dot = Dot3D(point=manim_points[0], color=RED)

        # Animation
        self.add(attractor_path, dot)

        def update_path(mob, dt):
            current_len = len(mob.get_points())
            if current_len < len(manim_points):
                new_points = manim_points[:current_len + 1]
                mob.set_points_smoothly(new_points)
                dot.move_to(new_points[-1])

        attractor_path.add_updater(update_path)

        self.wait(10)
        attractor_path.remove_updater(update_path)

