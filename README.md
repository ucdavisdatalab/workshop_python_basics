# Workshop: Python Basics

_[UC Davis DataLab](https://datalab.ucdavis.edu/)_  
_Fall 2021_  
_Instructors: Arthur Koehl <<avkoehl@ucdavis.edu>>,
  Nick Ulle <<naulle@ucdavis.edu>>_  

This 4-part workshop series provides an introduction to using the Python
programming language for reproducible data analysis and scientific computing.
Topics include programming basics, how to work with tabular data, how to break
down programming problems, and how to organize code for clarity and
reproducibility.

After this workshop, learners will be able to load tabular data sets into
Python, compute simple summaries and visualizations, do common data-tidying
tasks, write reusable functions, and identify where to go to learn more.

TODO: Requirements
<!--
No prior programming experience is necessary. All learners will need access to
an internet-connected computer and the latest version of Zoom, R, and RStudio.
-->

## Common Links

* [Reader](https://ucdavisdatalab.github.io/workshop_python_basics/)
* Event Page


## Contributing

The course reader is a live webpage, hosted through GitHub, where you can enter
curriculum content and post it to a public-facing site for learners.

To make alterations to the reader:

1.  Run `git pull`, or if it's your first time contributing, see the
    [Setup](#setup) section of this document.

2.  Edit an existing chapter file or create a new one. Chapter files are
    Markdown files (`.md`) in the `chapters/` directory. Enter your text, code,
    and other information directly into the file. Make sure your file:

    - Follows the naming scheme `##_topic-of-chapter.md` (the only exception is
      `index.md`, which contains the reader's front page).
    - Begins with a first-level header (like `# This`). This will be the title
      of your chapter. Subsequent section headers should be second-level
      headers (like `## This`) or below.

    Put any supporting resources in `data/` or `img/`. For large files, see the
    [Large Files](#large-files) section of this document. You do not need to
    add resources generated by your code (such as plots). The next step saves
    these in `docs/` automatically.

3.  Run the command `jupyter-book build .` in a shell at the top level of the
    repo to regenerate the HTML files in the `_build/`.

4.  When you're finished, `git add`:
    - Any files you edited directly
    - Any supporting media you added to `img/`
    - The `.gitattributes` file (if you added a large file)

    Then `git commit` and `git push`. This updates the `main` branch of the
    repo, which contains source materials for the web page (but not the web
    page itself).

5.  Run the command `ghp-import -n -p -f _build/html` in a shell at the top
    level of the repo to update the `gh-pages` branch of the repo. This uses
    the [`ghp-import` Python package][ghp-import], which you will need to
    install first (`pip install ghp-import`). The live web page will update
    automatically after 1-10 minutes.

[ghp-import]: https://github.com/c-w/ghp-import

### Large Files

If you want to include a large file (say over 1 MB), you should use git LFS.
You can register a large file with git LFS with the shell command:

```sh
git lfs track YOUR_FILE
```

This command updates the `.gitattributes` file at the top level of the repo. To
make sure the change is saved, you also need to run:

```sh
git add .gitattributes
```

Now that your large is registered with git LFS, you can add, commit, and push
the file with git the same way you would any other file, and git LFS will
automatically intercede as needed.

GitHub provides 1 GB of storage and 1 GB of monthly bandwidth free per repo for
large files. If your large file is more than 50 MB, check with the other
contributors before adding it.


## Setup


### Git LFS

This repo uses [Git Large File Storage][git-lfs] (git LFS) for large files. If
you don't have git LFS installed, [download it][git-lfs] and run the installer.
Then in the shell (in any directory), run:

```sh
git lfs install
```

Then your one-time setup of git LFS is done. Next, clone this repo with `git
clone`. The large files will be downloaded automatically with the rest of the
repo.

[git-lfs]: https://git-lfs.github.com/
