# Pearl
<p align="center"><img src="pearl.png" width="100"/></p>

Pearl is a lightweight framework for making Google Hangouts bots. It is structured as a set of plugins, which either run passively or respond to commands. For example, the `hello.py` plugin replies with a custom greeting whenever a user sends `/pearl hello`. Pearl's sample plugins are meant to be for a group chat manager, but it's incredibly easy to make custom plugins. Pearl is built on [hangups](https://github.com/tdryer/hangups).

# Getting Started
For those looking to try out Pearl, a guide is available at [quickstart](quickstart). More extensive documentation will be provided soon. Pearl's code will be changing quite frequently, and we aren't focused on legacy support. However, if you've only messed with plugins, migrating to the newest version should not be difficult.

The easiest way to test Pearl is by running `pearl.py`. If you want Pearl to run permanently, build and run a docker instance with the provided Dockerfile.
