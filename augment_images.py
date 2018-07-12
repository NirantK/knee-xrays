import Augmentor as aug
from pathlib import Path
datapath = Path('./data/raw/')
assert datapath.exists()

p = aug.Pipeline(datapath)
print(p.status())
p.rotate(probability=0.81, max_left_rotation=10, max_right_rotation=10)
p.zoom(probability=0.5, min_factor=0.9, max_factor=1.4)
p.greyscale(probability=0.01)
p.random_distortion(probability=0.5, magnitude=5, grid_width=5, grid_height=5)
p.random_contrast(probability=0.81, min_factor=0.81, max_factor=1.0)
p.random_color(probability=0.81, min_factor=0.7, max_factor=1.0)
p.histogram_equalisation(probability=0.5)
p.shear(probability=0.3, max_shear_left=5, max_shear_right=5)
p.skew(probability=0.4, magnitude=0.5)
print(p.status())
p.sample(1000)