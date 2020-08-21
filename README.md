# Projects Archive

A web archive of everything I've built.

## Development

The site is basic static HTML and CSS. It's built from markdown files with `compiler.py`. If you want to play around with the compiler, make sure you have the python packages `markdown` and `python-frontmatter` installed (see requirements.txt.)

Build the files and images then serve:

```shell
python compiler.py compile-pages compile-images serve
```

Or, just serve the files:

```shell
python compiler.py serve
```
