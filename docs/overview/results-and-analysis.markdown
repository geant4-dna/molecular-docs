---
layout: default
title: Results and analysis
permalink: /docs/overview/results-and-analysis
nav_order: 6
parent: Overview
---
<!-- Need to import MathJax for this post -->
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!-- END MathJax Import -->


# Results and analysis
{: .no_toc }



## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Implementation overview

As the simulation runs, it keeps track of three main elements in relation to DNA damage.
- Energy depositions in each chromosome
- Energy depositions and track length in the cell
- DNA damage in the DNA geometry

At the end of each event, the DNA damage events are collected and analysed, reconstructing the
damage pattern in the DNA and assigning it a complexity.

In the damage model, a probability is assigned that certain events cause strand breaks
(i.e. $$ Pr(\ce{e^{-}_{aq}} + \mathrm{Sugar} \rightarrow \mathrm{SSB}) $$). These conditions
are tested at the end of each event when the analysis runs to determine the damage that occurs.

At the completion of the run, the following outputs in a ROOT file are saved:

### Histograms

- SSB counter (ssb_counts)
- Deposit energy in SSBs (ssb_energies_ev)
- DNA fragment size
- Strand interaction positions

### Tuples

- Primary Source
  1. Primary
  2. Energy
  3. PosX in um
  4. PosY in um
  5. PosZ in um
  6. Momentum X
  7. Momentum Y
  8. Momentum Ζ


- Source (Break Source Frequency)
  1. Primary
  2. Energy
  3. None
  4. SSBd
  5. SSBi
  6. SSBm
  7. DSBd
  8. DSBi
  9. DSBm
  10. DSBh


- Damage (DNA damage locations)
  1. Event
  2. Primary
  3. Energy
  4. TypeClassification
  5. SourceClassification
  6. Position_x_um
  7. Position_y_um
  8. Position_z_um
  9. Size_nm
  10. FragmentLength
  11. BaseDamage
  12. StrandDamage
  13. DirectBreaks
  14. IndirectBreaks
  15. EaqBaseHits
  16. EaqStrandHits
  17. OHBaseHits
  18. OHStrandHits
  19. HBaseHits
  20. HStrandHits
  21. EnergyDeposited_eV
  22. InducedBreaks
  23. Chain
  24. Strand
  25. BasePair
  26. Name


## ROOT Analysis files

An output ROOT data file (molecular-dna.root) is created by the simulation. [ROOT6.x]( {{ "https://root.cern/install/" | relative_url }} ){:target="_blank"} should be installed.

Several ROOT macro files are provided to analyse the corresponding results:
- cylinders.C : to plot damage from cylinders geometry
- phage.C : to plot damage from phage geometry
- plasmid.C : to plot damage from plasmid geometry
- ecoli.C : to plot damage from E.coli geometry
- human_cell.C, human_cell_alphas.C and human_cell_chromosomes.C: to plot damage and fragments distribution from human cell geometries (as in [3] for human_cell_alphas.C, as in [4] for human_cell_chromosomes.C)

Simply do:
```
root cylinders.C
```

These macros calculate mean quantities and the associated standard error of the mean (SEM) [5].

A python macro file is provided to modify ROOT output in SDD [2] file format:
- createSDD.py : to use it, insert the command "python3 createSDD.py".
                 If error with ROOT, simply
                 source /path/to/root/bin/thisroot.(c)sh,
                 do "pip install pyroot" and try again.

## Note about python import in ROOT

If python cannot import ROOT, please configure your ROOT version to include PyROOT. 

For further instruction refer to the documentation of ROOT, paragraph 19.1.4.2, see [link]({{"https://root.cern.ch/root/htmldoc/guides/users-guide/ROOTUsersGuide.html#python-interface" | relative_url }}){:target="_blank"}.


## Text analysis files

Individual damage files can ge generated to display graphically hits on strands, using the command:
```
analysisDNA/saveStrands
```

They use the following naming scheme:
- "D" for a direct damage
- "I" for an indirect damage
- "~" if hit without damage
- "-" if not hit
- "X" for both damage types

The numbers 6 and 7 represent damage source and damage complexity, respectively.

## References

[1] Computational modelling of lowenergy electron-induced DNA damage by early physical and chemical events, H. Nikjoo et al., Int. J. Radiat. Biol. 71 (1997) 467–483 - [link]({{"https://doi.org/10.1080/095530097143798" | relative_url }}){:target="_blank"}

[2] A new standard DNA damage (SDD) data format, J. Schuemann et al., Rad. Res. 191 (2019) 76-92 - [link]({{"https://doi.org/10.1667/rr15209.1" | relative_url }}){:target="_blank"}  

[3] Geant4-DNA simulation of human cancer cells irradiation with helium ion beams, K. Chatzipapas et al., Phys. Med. 112 (2023) 102613 - [link]({{ "https://doi.org/10.1016/j.ejmp.2023.102613" | relative_url }}){:target="_blank"}

[4] Development of a novel computational technique to create DNA and cell geometrical models for Geant4-DNA, K. Chatzipapas et al., Phys. Med. 127 (2024) 104389 - [link]({{ "https://doi.org/10.1016/j.ejmp.2024.104839" | relative_url }}){:target="_blank"}

[5] What to use to express the variability of data: Standard deviation or standard error of mean?, Mohini P. Barde, Prajakt J. Barde, Perspectives in Clinical Research 3(3) (2012) 113-116 - [link]({{ "https://doi.org/10.4103/2229-3485.100662" | relative_url }}){:target="_blank"}
