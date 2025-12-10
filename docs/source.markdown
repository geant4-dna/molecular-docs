---
layout: default
title: Running the example
nav_order: 4
---

# Running the example
{: .no_toc }

Geant4.11.1 or higher is required (see [Geant4]({{ "https://geant4.web.cern.ch" | relative_url }}){:target="_blank"}).

To build the example:

```
mkdir build
cd build
cmake ../pathToExamples/moleculardna
make
```
This example needs internet to download the pre-existing geometry data file. Please, check your connection.

To run the example:
```
./molecular -m cylinders.mac -t 2 -p 2
```

-m : macro file (see [available geometries]({{ "/docs/examples/parameter-study" | relative_url }}))

-t : number of threads to run

-p : physics constructor option (see [physics model]({{ "/docs/overview/physics-model" | relative_url }}))

-v : set to 1 only to activate visualization (0 is the default value)

