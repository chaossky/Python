import pyvista as pv
sphere=pv.Sphere()

plotter=pv.Plotter()
plotter.add_mesh(sphere,color='blue',show_edges=True)
plotter.show()