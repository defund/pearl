# Pearl
Pearl is a lightweight framework for making Google Hangouts bots. It is structured as a set of plugins, which either run passively or respond to commands. For example, the `hello.py` plugin replies with a custom greeting whenever a user sends `/pearl hello`. Pearl's sample plugins are meant to be for a group chat manager, but it's incredibly easy to make custom plugins. Pearl is built on [hangups](https://github.com/tdryer/hangups).

# Setup
Setting up Pearl is incredibly easy. First, install dependencies with `pip install -r requirements.txt`.

Pearl also requires a Gmail account, which is specified by `auth.json`. You need to create and keep this file secret, since it contains your credentials. `auth.json` is structured like so:
```json
{
	"email": "pearl@gmail.com",
	"password": "pearlbot"
}
```
If you choose to fork this repository, make sure to add your filename to `.gitignore`. `auth.json` is already included.

`config.json` has additional settings for Pearl:
* `auth` - Filepath to `auth.json`.
* `plugins` - List of plugins. The key value is command name and the value is the filepath to the plugin file.
* `format` - Prefix for identifying commands. For example, `/pearl` tells Pearl to look for messages with the format `/pearl <command>`.

Currently, plugins are only command-based. A plugin file must have a class with a handler function as well as an initialize function. See [hello.py](https://github.com/defund/pearl/blob/master/plugins/hello.py) for a basic example.

The easiest way to run Pearl is to run `python3 pearl.py`. If you want Pearl to run permanently, build and run a docker instance with the included `Dockerfile`.

A final technicality to note is that Hangups automatically uses your device's cached token. If you've previously logged into a different account, Hangups will not use the credentials from `auth.json`. If this is the case, run `clean.py` to clear your token cache.