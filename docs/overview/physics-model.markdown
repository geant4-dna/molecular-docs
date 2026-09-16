---
layout: default
title: Physics model
nav_order: 1
parent: Overview
---

# Physics model

Geant4-DNA Monte-Carlo track-structure code describes spatial distribution of energy depositions, interaction types in material of biological interest (water, DNA,...) based on interaction probabilities (cross sections). Geant4-DNA physics processes and models have been built in physics constructors which are designed to activate required physical models in a single command line.

![physics]({{"/assets/images/DNAPhysics.mp4" | relative_url}})
{: .text-center}
*Example of movie by V. Stepan : 20 keV electron and 20 MeV alpha tracks in 10 micrometer cube of liquid water, generated using Geant4 10.0p2 microdosimetry example.*

G4EmDNAPhysics_option2, G4EmDNAPhysics_option4 or G4EmDNAPhysics_option6 constructors are recommended to use in the molecularDNA example.

Please refer to [Geant4-DNA]({{ "http://geant4-dna.in2p3.fr/styled-3/styled-8/index.html" | relative_url }}){:target="_blank"} for details.

**Important note**: The DNA geometry is defined as being composed of DNA materials, for which the current public version of “molecularDNA” does not include cross sections.
Physical interactions are simulated within the DNA volumes assuming they contain liquid water only.

## References

[1] Geant4-DNA example applications for track structure simulations in liquid water: a report from the Geant4-DNA Project, S. Incerti et al., Med. Phys. 45 (2018) e722-e739 - [link]({{ "https://doi.org/10.1002/mp.13048" | relative_url }}){:target="_blank"}
