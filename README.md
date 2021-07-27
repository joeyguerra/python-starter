# Python Starter App

## First time setup

### Install Python with pyenv

Install `pyenv` to manage Python versions, install Python and set the global version to use.

```sh
brew install pyenv

# install python 3.9.4
pyenv install 3.9.4

# set global version of python
pyenv global 3.9.4
```


If you're using MacOS and `zsh`, then run this too:

```sh
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.zshrc
echo 'PATH=$(pyenv root)/shims:$PATH' >> ~/.zshrc
```

For Bash:

```sh
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
echo 'PATH=$(pyenv root)/shims:$PATH' >> ~/.bash_profile
echo 'PATH=$(python -m site --user-base)/bin:$PATH' >> ~/.bash_profile
```

You might need to also alias `pip` to `pip3`:

```sh
echo 'alias pip=/opt/homebrew/bin/pip3' >> ~/.zshrc
```

For Bash:

```sh
echo 'alias pip=/opt/homebrew/bin/pip3' >> ~/.bashrc
```

### Manage dependencies with pipenv

```sh
pip install pipenv
```


## Day to day development

Set `PIPENV_VENV_IN_PROJECT='enabled'` to create `.ven` at the root level instead of at the user level.

```sh
export PIPENV_VENV_IN_PROJECT='enabled'
```

### Run tests

```sh
pipenv runt test
```

