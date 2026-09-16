---
layout: default
title: Phase space files
nav_order: 8
parent: Overview
---
# How to Read Phase Space Files (PSF) in MolecularDNA

This guide explains how to use **Phase Space Files (PSF)** as a particle source for simulations with molecularDNA.

## Supported PSF formats

molecularDNA supports PSF files in the following formats: ROOT, text, CSV

## Example files and macros

They are located in the `phase_space` sub-directory.

- **ROOT and text**: examples of PSF (example.root and example.txt, containing 100 particles each) and ROOT conversion macros (txtToRoot.C and rootToTxt.C) are available. The ecoli_PSF.mac macro can be used (derived from the ecoli.mac macro).
- **CSV**: can be used by GRAS Two-Stage Analysis. Example file (phase_space.csv, containing 20 electrons of 45 keV) and macro (phase_space_test.mac, derived from the cylders.mac macro) are provided. This approach does not work in MT-mode.

## Reading PSF Files in Simulations

### Replace the Source with PSF Particles

```
/psf/pattern PSFName
```

- Can be use to replace the simulation source with particles from the specified PSF file (`PSFName`).
- If **no `/run/beamOn nOfEvents`** is specified, the entire PSF is read automatically.
- If `/run/beamOn nOfEvents` is issued:
  - The simulation shoots `nOfEvents` particles from the PSF.
  - If `nOfEvents` exceeds the number of particles in the PSF, the simulation **reuses the PSF from the beginning**.

### Set the Sampling Mode

```
/psf/samplingMode Mode
```

- **Default**: Sequential reading of the PSF.
- **`Sampling`**: Randomly samples particles **without replacement** (no particle is reused unless `nOfEvents` &gt; total particles).
- **`Sampling_wRplc`**: Randomly samples particles **with replacement** (particles can be reused).

### Specify the Root NTuple Name

```
/psf/NTupleName NTupleName
```

- Defines the title of the **Root NTuple** in the PSF file.
- Default: `"PSF"`.
- The particles in this NTuple will serve as the simulation source.

### Set the Sampling Mode

```
/psf/nOriginal numberOfPrimaries
```

If the entry PSF has been generated using a previous simulation, this command can be used to store the number of primaries of the previous simulation in a variable (not used yet).
