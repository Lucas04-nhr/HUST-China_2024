# Team HUST-China 2024 Wiki

The main language used to write wikis in this repository is `Markdown`.

This repository **MUST** contain all coding assets to generate your team's wiki
(HTML, CSS, JavaScript, TypeScript, Python, etc).

Images, photos, icons and fonts **MUST** be stored on `static.igem.wiki` using
[tools.igem.org](https://tools.igem.org), and Videos **must** be embedded
from [iGEM Video Universe](https://video.igem.org).

For up-to-date requirements, resources, help and guidance, visit
[competition.igem.org/deliverables/team-wiki](https://competition.igem.org/deliverables/team-wiki).

## Getting started

You should probably only edit the files inside folders `static`, `wiki` and
`docs`.

1. Open the Web IDE
2. Make the changes on the files you wish.
3. Review the changes you made
4. Once you are done, save the changes by **committing** them to the _main branch_ of the repository
5. An automated script will build, test and deploy your wiki, which should take
   less than 30 seconds.

## About this Template

### Files

The static assets are in the `static` directory. The layout and templates are in
the `wiki` directory, and the pages live in the `docs` directory. Unless you are
an experienced and/or adventurous human, you probably shouldn't change other
files.

    |__ .github/            -> Workflow files used by GitHub actions
    |__ wiki/               -> Documentation files
        |__ *.md            -> Markdown files with the content of your wiki
    |__ _sass/              -> static assets (CSS files only)
    |__ _layout/            -> Page layout of our wiki
    |__ _includes/          -> static assets (inline HTML and JavaScript files only)
    |__ .gitignore          -> Tells GitLab which files/directories should not be uploaded to the repository
    |__ .gitlab-ci.yml      -> Automated flow for building, testing and deploying your website.
    |__ LICENSE             -> License CC-by-4.0, all wikis are required to have this license - DO NOT MODIFY
    |__ README.md           -> File containing the text you are reading right now
    |__ dependencies.txt    -> Software dependencies from the Python code
    |__ Gemfile.lock.       -> (Optional) Lockfile that captures the exact versions of packages and their dependencies
    |__ Gemfile.            -> (Optional) Ruby dependencies for formatting the code

### Building locally (advanced users)

To work locally with this project, follow the steps below:

**Make sure you've already installed `Ruby` on your machine first.**

#### Install and build

```bash
git clone https://gitlab.igem.org/2024/hust-china.git
cd hust-china
gem install bundler
gem install jekyll
bundle install
bundle update
bundle exec jekyll serve
```

#### Preview

If there's no `errors`, you can preview the page on [`localhost:4000`](http://127.0.1:4000/hust-china).
