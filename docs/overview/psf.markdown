---
layout: default
title: Phase space files
nav_order: 8
parent: Overview
---
# How to read Phase Space Files (PSF) in molecularDNA

This guide explains how to use **Phase Space Files (PSF)** as a particle source for simulations with molecularDNA.

## Supported PSF formats

molecularDNA supports PSF files in the following formats: ROOT, text and CSV.

## Example of PSF and molecularDNA macro

**Three** PSF are provided and placed in the `phase_space` sub-directory : `example.root` and `example.txt`, containing 100 particles each, and `example.csv`, containing 20 electrons of 45 keV and created by the [GRAS Two-Stage Analysis](https://spitfire.estec.esa.int/trac/GRAS/wiki/GRAS/GRAS-05-02/UserGuideTwoStage) (including specific header).

The `ecoli_PSF.mac` macro (derived from the `ecoli.mac` macro) can be used to read them. 

This approach works in MT-mode.

## Reading PSF files in simulations

We provide several User Interface commands for the handling of PSF.

### Replace the source with PSF particles

```
/psf/pattern PSFName
```

- Can be use to replace the simulation source with particles from the specified PSF file (`PSFName`).
- If **no `/run/beamOn nOfEvents`** is specified, the entire PSF is read automatically.
- If `/run/beamOn nOfEvents` is issued:
  - The simulation shoots `nOfEvents` particles from the PSF.
  - If `nOfEvents` exceeds the number of particles in the PSF, the simulation **reuses the PSF from the beginning**.

### Set the sampling mode

```
/psf/samplingMode Mode
```

- **Default**: Sequential reading of the PSF.
- **`Sampling`**: Randomly samples particles **without replacement** (no particle is reused unless `nOfEvents` &gt; total particles).
- **`Sampling_wRplc`**: Randomly samples particles **with replacement** (particles can be reused).

### Specify the ROOT NTuple name

```
/psf/NTupleName NTupleName
```

- Defines the title of the **Root NTuple** in the PSF file.
- Default: `"PSF"`.
- The particles in this NTuple will serve as the simulation source.

### Store the number of primaries

```
/psf/nOriginal numberOfPrimaries
```

If the entry PSF has been generated using a previous simulation, this command can be used to store the number of primaries of the previous simulation in a variable (not used yet).
