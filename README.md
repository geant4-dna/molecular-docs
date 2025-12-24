# Documentation for molecularDNA example

The documentation here is built using Jekyll, which allows to build https://geant4-dna.github.io/molecular-docs/
using markdown.



*Pushing this repository to the master branch will trigger a build of the
website and documentation.*

The site can be viewed locally by calling:
```
bundle install  # if you haven't already
bundle exec jekyll serve
```

*This packages requires Ruby to be installed.*

## How to update the documentation

*Detailed instructions on how to update the docs are available from [Just The Docs](https://pmarsceill.github.io/just-the-docs/).*

To update the documentation here, you will need to edit markdown files.
These files are located in the `docs` folder, and the main page is located at `index.markdown`

The project is set up so that the directories inside `docs` align with the site structure. The actual
structure of the site is defined in the five or so lines of markdown at the top of every page
that look like this:
```
---
layout: default                # Page Layout
title: Overview                # Page Title
nav_order: 2                   # How deep is the page in the navigation tree
has_children: true             # Does the page have sub-pages
permalink: docs/overview       # Page address
---
```

Hyperlinks can be built internally using the page permalinks and the `{{site.url}}` macro command, which
brings in the site url defined in `_config.yml` (from url and baseurl variables).

An example hyperlink in markdown would look like this:
```
[Anatomy of a Macro File]({{site.url}}/docs/overview/macro-anatomy)
```

Beyond standard markdown syntax, classes can be applied to make objects look different
using this braces and a colon as follows: `{: .classname}`. For example, an image can 
be centred by assigning the `text-center` class. The below example points to the image
located at `assets/images/placements.png`, transforms that path to a relative URL, and
then centres the image.

```
![Placements for DNA Geometries]({{"assets/images/placements.png" | relative_url}})
{: .text-center}
```

## File breakdown

```
.
├── _site                          # Folder where the site is built
├── .github                        # Folder to store github actions
├── assets                         # Store images, files and objects here
│   ├── images
│   └── js
├── docs                           # Documentation Markdown by Category
│   ├── examples                   # Edit the markdown in the docs folder
│   ├── geometry-library           #     to publish changes
│   ├── overview
│   ├── publications.markdown
│   └── source.markdown
├── lib                            # Folder containing task definitions
├── 404.html                       # Page to show for 404 errors
├── Gemfile                        # Ruby package list
├── Gemfile.lock
├── README.md                      # The project Readme (this file)
├── _config.yml                    # Project configuration
├── favicon.ico                    # Icon image
├── g4command_processor.py         # Python file to load G4 commands to a table
├── index.markdown                 # Index.html source
└── rakefile                       # Points to the Rake search definitions
```

## Updating the configuration macro documentation.

1. Make a Geant4 macro `get_commands.mac` which extracts all possible commands as follows:
```
/control/manual /world
/control/manual /analysisDNA
/control/manual /dnageom
/control/manual /cell
```
2. Run `molecular -t 1 -m get_commands.mac` > commands.txt
3. Run `python g4command_processor.py commands.txt --markdown`
4. Copy the stdout output to the Configuration markdown file.
