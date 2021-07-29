import sys
from stl import mesh

# find the max dimensions, so we can know the bounding box, getting the height, width, length

def find_mins_maxs(obj):
    minx = obj.x.min()
    maxx = obj.x.max()
    miny = obj.y.min()
    maxy = obj.y.max()
    minz = obj.z.min()
    maxz = obj.z.max()
    return minx, maxx, miny, maxy, minz, maxz

# Take path of the stl file.
stl_file_path = sys.argv[1]
stl_file = mesh.Mesh.from_file(stl_file_path)

# Calculate dimensions of bounding box
minx, maxx, miny, maxy, minz, maxz = find_mins_maxs(stl_file)
w = maxx - minx
l = maxy - miny
h = maxz - minz

# Calculate volume of models
volume, cog, inertia = stl_file.get_mass_properties()

print(f"Width = {w}")
print(f"Length = {l}")
print(f"Height = {h}")
print(f"Volume = {volume}")