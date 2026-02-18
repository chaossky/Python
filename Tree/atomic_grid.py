from ase import Atoms
from ase.visualize import view
atoms=Atoms("Cu4", positions=[(0,0,0),(1,0,0),(0,1,0),(1,1,0)])

print(atoms)
view(atoms)