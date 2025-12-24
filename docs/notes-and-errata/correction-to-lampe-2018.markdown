

<!-- Need to import MathJax for this post -->
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!-- END MathJax Import -->

## Correction to 2018 Publication

**NOTE: These corrections are produced using the same chemistry as in the
[the original work](https://doi.org/10.1016/j.ejmp.2017.12.008){:target="_blank"} from 2018.
Since this time, the Geant4 chemistry and physics models have been updated, more recent simulations will not produce these results.**

As part of the process of preparing for the open source release of this geometry,
an error was noted in Lampe et al.'s [2018 work](https://doi.org/10.1016/j.ejmp.2017.12.008){:target="_blank"}.

Due to a bug in the code, the geometry that was actually simulated was a rectangular
DNA region with an ellipsoidal source, as below:

![True Geometry in Original Paper]({{"/assets/images/original-geometry.png" | relative_url}}){: width="60%"}\
{: .text-center}

The mathematics in the paper however assumed the ellipsoidal cell shape as described in
the work, resulting in an increase of the density of DNA modelled from the true value
of $$3.81\ \text{Mbp}\ \mu \text{m}^{-3}$$ to
$$7.277\ \text{Mbp}\ \mu \text{m}^{-3}$$. The consequence of this is that in general, the damage
yields in the 2018 work are around 52% of their true value.

### Correction Geometries

To explore this, we have created three geometries to investigate the consequences of this error.

_Correct Geometry_

This is what should have been simulated in our 2018 paper. The density of DNA in this
simulation is $$7.67\ \text{Mbp}\ \mu\text{m}^{-3}$$, and the ellipsoid
is a little smaller. The version available in the public release of Geant4-DNA uses this geometry.

![Corrected Geometry]({{"/assets/images/corrected-geometry.png" | relative_url}}){: width="60%"}
{: .text-center}

_Original Geometry_

This is the geometry that was actually modelled in the [original 2018 paper](https://doi.org/10.1016/j.ejmp.2017.12.008){:target="_blank"}, as presented above.

![True Geometry in Original Paper]({{"/assets/images/original-geometry.png" | relative_url}}){: width="60%"}
{: .text-center}

_Low Density Geometry_

This is a geometry that parallels exactly the geometry simulated in the 2018 work without
exceeding the ellipsoidal boundary. It is useful to see whether the DNA at the edge
of the ellipse caused an impact to the simulation results.

![Low Density Geometry]({{"/assets/images/low-density-geometry.png" | relative_url}}){: width="60%"}
{: .text-center}

### Correction Results

Across these 3 geometries when considering electrons
(Figure 7 in the [original work](https://doi.org/10.1016/j.ejmp.2017.12.008){:target="_blank"}), we see that the three geometries
actually produce reasonably similar damage yields:

![Electron Damage Yields]({{"/assets/images/yields-electron.svg" | relative_url}}){: width="100%"}
{: .text-center}

Compared to the original paper, the results which only consider radical activity within the hydration
shell of DNA (radical kill distance of 1nm) provide a better match to experimental results,
while the 4nm kill distance overstates damage.

The original study results are shown here
(see Figure 7 [herein](https://doi.org/10.1016/j.ejmp.2017.12.008){:target="_blank"}),
and indicate damage yields about half of what we see in the
corrected results.

![Original Electron Damage Yields]({{"/assets/images/figure-7-old.svg" | relative_url}}){: width="70%"}
{: .text-center}

When comparing ratios of strand breaks in the new geometry, we do see a slight increase
in the DSB/SSB ratio (see Figure 8 [herein](https://doi.org/10.1016/j.ejmp.2017.12.008){:target="_blank"}):

|  Original Work  |  Corrected Geometry  |
|:---------------:|:--------------------:|
| ![Original SSB/DSB Ratio]({{"/assets/images/ecoli-ssb-dsb-old.svg" | relative_url}}) | ![Updated SSB/DSB Ratio]({{"/assets/images/ecoli-ssb-dsb-new.svg" | relative_url}}) |
