# Pearl
Pearl is a lightweight framework for making Google Hangouts bots. It is structured as a set of plugins, which either run passively or respond to commands. For example, `plugins/hello.py` replies with a custom greeting whenever a user sends `/pearl hello`. Pearl's sample plugins are meant to be for a group chat manager, but it's incredibly easy to make custom plugins.

# Setup
Setting up Pearl is incredibly easy. First, install dependencies with `pip install -r requirements.txt`.

Pearl also requires a Gmail account. This is specified by `auth.json`, which you need to create. The file needs to contain credentials for your bot account, structured like so:
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