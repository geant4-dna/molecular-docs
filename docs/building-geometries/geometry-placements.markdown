---
layout: default
title: Geometry placements
nav_order: 2
permalink: docs/geometry-library/geometry-placements
parent: Building geometries
---

# Geometry placements

The geometry placements here were built using the [FractalDNA package]({{"/docs/geometry-library/fractal-dna" | relative_url}})
package in Python. Accompanying each geometry is the Python code to
generate it.

These geometries are based on iterating a fractal [L-string](https://en.wikipedia.org/wiki/L-system){:target="_blank"}.

## Square geometry

A square geometry can be easily generated using the `X` fractal seed.

![]({{"assets/images/fractal-X-3-centred.svg" | relative_url}}){: width="45%"}
{: .text-center}

- Download with 1 iteration ([link]({{"assets/csv/fractal-X-1-centred.csv" | relative_url}}))
- Download with 2 iteration ([link]({{"assets/csv/fractal-X-2-centred.csv" | relative_url}}))
- Download with 3 iteration ([link]({{"assets/csv/fractal-X-3-centred.csv" | relative_url}}))
- Download with 4 iterations ([link]({{"assets/csv/fractal-X-4-centred.csv" | relative_url}}))
- Download with 5 iterations ([link]({{"assets/csv/fractal-X-5-centred.csv" | relative_url}}))
- Download with 6 iterations ([link]({{"assets/csv/fractal-X-6-centred.csv" | relative_url}}))
- Download with 7 iterations ([link](https://zenodo.org/record/6658889/files/fractal-X-7-centred.csv.zip?download=1){:target="_blank"})
- Download with 8 iterations ([link](https://zenodo.org/record/6658889/files/fractal-X-8-centred.csv.zip?download=1){:target="_blank"})

```
# Start with the initial L-String X for a Hilbert Curve
initial_string = 'X'
# Iterate it as required (here, nn=3)
# for nn = 8, this takes about two hours on my MacBook Pro 16GB RAM
nn = 3
iterated_lstring = h.iterate_lstring(initial_string)
for _ in range(nn-1):
    iterated_lstring = h.iterate_lstring(iterated_lstring)

vf = v.VoxelisedFractal.fromLString(iterated_lstring, pbar=True)
vf.center_fractal()
# fig = vf.to_plot()
# fig.savefig('results/fractal-X-3-centred.svg')

# If you are saving a BIG fractal, try using the to_text() method instead
# as large dataframes are very slow to generate beyond 6 iterations.
# with open(f'results/fractal-X-{nn}-centred.csv', 'w') as ff:
#     ff.write(vf.to_text())
vf.to_frame().to_csv(f'results/fractal-X-{nn}-centred.csv', index=False, sep=' ')
```

## Rectangular geometry

A square geometry can be easily generated using the `XFXFX` fractal seed.

![]({{"assets/images/fractal-XFXFX-2-centred.svg" | relative_url}}){: width="45%"}
{: .text-center}

The aspect ratio will be:
- 1x1x2 for `XFX`
- 1x1x3 for `XFXFX`
- 1x1x4 for `XFXFXFX`
- and so on as the seed changes.

- Download `XFXFX` iterated 2 times ([link]({{"assets/csv/fractal-XFXFX-2-centred.csv" | relative_url}}))
- Download `XFXFX` iterated 3 times ([link]({{"assets/csv/fractal-XFXFX-3-centred.csv" | relative_url}}))
- Download `XFXFX` iterated 4 times ([link]({{"assets/csv/fractal-XFXFX-4-centred.csv" | relative_url}}))

```
# Start with the initial L-String XFXFX for a Hilbert Curve
initial_string = 'XFXFX'
# Iterate it as required (here, nn=4)
nn = 4
iterated_lstring = h.iterate_lstring(initial_string)
for _ in range(nn-1):
    iterated_lstring = h.iterate_lstring(iterated_lstring)

vf = v.VoxelisedFractal.fromLString(iterated_lstring, pbar=True)
vf.center_fractal()
# fig = vf.to_plot()
# fig.savefig(f'results/fractal-XFXFX-{nn}-centred.svg')

vf.to_frame().to_csv(f'results/fractal-XFXFX-{nn}-centred.csv', index=False, sep=' ')
```


## Generating geometries from a path

The `voxelisation` model can convert the path of this curve to a voxelised
representation, of straight and curved boxes.

In this example we perform this on a text file with X/Y/Z columns
([link]({{"assets/csv/example-path.csv" | relative_url}})) to produce
[this output file]({{"assets/csv/example-path-voxels.csv" | relative_url}})

```
df = pd.read_csv('example-path.csv', sep='\t')
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot(df.X, df.Y, df.Z)
fig.savefig('example-path.svg')

vf = v.VoxelisedFractal.from_path(df.values)
fig_fractal = vf.to_plot()
fig_fractal.savefig('example-path-voxels.svg')

vf.to_frame().to_csv('results/example-path-voxels.csv', sep=' ')
```

The below images show that the paths made by the voxelised geometry (right)
are identical to those in the source geometry (left)

![]({{"assets/images/example-path.svg" | relative_url}}){: width="45%"}
![]({{"assets/images/example-path-voxels.svg" | relative_url}}){: width="45%"}
{: .text-center}


## Generating random placements


It can be useful to generate randomised volumes for testing a simulation (see [parameter study]({{ "/docs/examples/parameter-study" | relative_url }})).
This was the subject of [this article](https://doi.org/10.1016/j.ejmp.2018.02.011){:target="_blank"}.

To generate a randomised volume, the `fractaldna.structure_models.random_placements`
is available.

In that paper, 200,000 non overlapping prisms were simulated in a r=3000nm
ball.
The prisms had dimensions 30x30x100nm and a sample file can be
downloaded [here]({{"assets/csv/prisms_200k_r3000.csv" | relative_url}}).

Note that the saved file doesn't contain the dimensions of the prisms as this
is instead fed to the macro file directly.

```
from fractaldna.structure_models import random_placements as rp

# Generating 200,000 prisms can take around 4-5 hours and will slow down
# as more are added
prisms = rp.generate_non_overlapping_prisms(
    n_prisms=200_000,
    size=[30, 30, 100],  # nanometres
    rad=3000,  # nanometres
    early_exit=-1,
    verbose=True)

df = prisms.to_frame()
df.to_csv('results/prisms_200k_r3000.csv', sep=' ', index=False)

```
