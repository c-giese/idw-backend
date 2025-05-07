## What and why
A Python virtual environment is a self-contained directory tree that contains a Python installation for a specific version of Python, plus a number of additional packages. It's essentially an isolated environment where you can install Python packages without interfering with the global Python installation on your system or other projects.

Think of it like having separate toolboxes for different projects. Each toolbox has its own set of tools (Python packages) in specific versions, ensuring that using a tool in one toolbox doesn't affect the tools or projects in another.

## How to use one
Create a new virtual environment with the name .venv
`python -m venv .venv`

Activate the environment 
`.\.venv\Scripts\activate`

### Useful command
`pip list` Shows all installed dependencies

`pip install` <PACKAGE_NAME> Installs the package

`pip install -r .\requirements.txt` installs all dependencies defined in requirements.txt

`deactivate` Deactivates the currently active virtual environment
