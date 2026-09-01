# PyTranslate

A beautiful, modern and delightful translator TUI written in Python.

### Description

PyTranslate was built to solve a problem I had. Every time I needed to translate an unknown word, especially while it was in my production environment, there was all the complexity of opening a browser, opening the desired translation website and finally translating. PyTranslate solves this by already being easily located in my production environment. I can easily translate anything and quickly use it. In fact, this text was translated from Portuguese using PyTranslate!

## Install

1. Clone this repo locally.

```
git clone https://github.com/PedroBizachi/pytranslate.git
```

2. Install UV package manager for python.

MacOS/Linux:
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows:
Follow the instructions on the official website [here](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_2).

3. Build a virtual environment.

```
uv venv .venv
```

4. Let UV download the necessary dependencies.

```
uv sync
```

5. Run the application.

```
uv run pyt
```

## See also

[Roadmap](./roadmap.md)
[How to contribute](./CONTRIBUTING.md)
[deep-translator](https://github.com/nidhaloff/deep-translator)
[Textual](https://github.com/textualize/textual/)
[Posting](https://github.com/darrenburns/posting)
