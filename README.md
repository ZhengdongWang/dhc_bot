# DHC Bot
If you know, you know. Save time! No misclicks!

## Install

Put unzipped [geckodriver](https://github.com/mozilla/geckodriver) in python bin (default `~/.local/bin` on MacOS). A version is provided in this repository.

You also need to open geckodriver once. There is an issue [here](https://github.com/mozilla/geckodriver/releases/tag/v0.27.0) on Catalina. Get by the notarization by running the command on [this page](https://firefox-source-docs.mozilla.org/testing/geckodriver/Notarization.html).

[Install Selenium](https://selenium-python.readthedocs.io/installation.html) for python. Requires pip.

Clone and edit login file.

## Run

Three options.

`$ chmod +x dhc.command` once, then double click on the executable in the future.

`$ python dhc.py` in directory.

Add `alias dhc='python /path/to/dhc_bot/dhc.py'` to zshrc to run `dhc` in terminal.
