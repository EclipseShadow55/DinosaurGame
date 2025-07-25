import numpy as np
import trimesh
import geometry as geo

mesh = trimesh.load_mesh('pyramid.obj')
geo.ExtendedTrimesh.smooth(mesh, alpha=0.5, iterations=1)
mesh.export("smoothed_pyramid.obj")