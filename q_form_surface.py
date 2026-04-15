import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def quadratic_form_surface(A, x_range=(-2, 2), y_range=(-2, 2), resolution=100):
    """
    Visualize the quadratic form surface for a 2x2 matrix A.
    
    Parameters:
        A (np.ndarray): 2x2 matrix
        x_range (tuple): range for x-axis
        y_range (tuple): range for y-axis
        resolution (int): grid resolution
    """
    # Create grid
    x = np.linspace(x_range[0], x_range[1], resolution)
    y = np.linspace(y_range[0], y_range[1], resolution)
    X, Y = np.meshgrid(x, y)
    
    # Compute quadratic form Q(x,y) = [x y] A [x y]^T
    Z = A[0,0]*X**2 + (A[0,1] + A[1,0])*X*Y + A[1,1]*Y**2
    
    # Plot surface
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
    
    # Labels
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('Q(x,y)')
    ax.set_title(f'Quadratic Form Surface for Matrix:\n{A}')
    
    plt.show()

# Example matrices
A1 = np.array([[2, 0],
               [0, 1]])

A2 = np.array([[1, 2],
               [2, 3]])

A3 = np.array([[0, 1],
               [1, 0]])

# Visualize
quadratic_form_surface(A1)
quadratic_form_surface(A2)
quadratic_form_surface(A3)
