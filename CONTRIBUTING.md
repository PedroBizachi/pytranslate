# Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### Report Bugs

Report bugs at https://github.com/PedroBizachi/pytranslate/issues.

If you are reporting a bug, please include:

- Your operating system name and version.
- Any details about your local setup that might be helpful in troubleshooting.
- Detailed steps to reproduce the bug.
- If the bug includes a tracelog, include that in your bug report. Remember, on github you can enclose code or console output in ` insert code here `.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with "enhancement" and "help wanted" is open to whoever wants to implement it.

Note

You can contact @PedroBizachi or comment on the issue if you wish to be listed under 'Assigned'.

### Write Documentation

PyTranslate needs a documentation! We're looking forward to it, but your help will be really appreciated.

### Submit Feedback

The best way to send feedback is to file an issue at https://github.com/PedroBizachi/pytranslate/issues.

If you are proposing a feature:

- Explain in detail how it would work.
- Keep the scope as narrow as possible, to make it easier to implement.
- Remember that this is a volunteer-driven project, and that contributions are welcome :)

## Get Started!

Ready to contribute? Here's how to set up PyTranslate for local development.

1. Fork the PyTranslate repo on GitHub.

2. Clone your fork locally:

```sh
git clone git@github.com:your_name_here/pytranslate.git
```

3. Install your local copy into a virtualenv. Assuming you have UV installed, this is how you set up your fork for local development:

```sh
cd path/to/project
uv venv .venv
source .venv/bin/activate
uv sync
```

>Note
>
>`uv sync` will automatically install all package dependencies AND development dependencies.

4. Create a branch for local development:

```sh
git checkout -b name-of-your-bugfix-or-feature
```

Now you can make your changes locally.

5. Ensure your changes are covered by test modules and that the tests pass with pytest before committing.

6. Commit your changes and push your branch to GitHub:

```sh
git add .
git commit -m "Your detailed description of your changes."
git push origin name-of-your-bugfix-or-feature
```

7. Submit a pull request through the GitHub website.

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include any relevant tests;
2. If the pull request adds functionality, the docs should be updated. Put your new functionality into a function with a docstring;
3. Pull requests are automatically tested on GitHub for compatibility with Python version >=3.9. Please review your test results and ensure your request passes all tests.
