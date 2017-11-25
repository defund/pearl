# Quickstart
<p align="center"><img src="pearl.png" width="100"/></p>

This is a guide aimed to get you running Pearl in a matter of minutes. The quickstart consists of the main Pearl code as well as a limited set of plugins that don't need much setup. Once you've gotten it set up, check out a more comprehensive set of plugins at the [main project](https://github.com/defund/pearl/tree/master/pearl).

# Prerequisites
Pearl requires a Gmail account, which you must independently create. Pearl does not support accounts with two factor authentication. In Hangouts, add the account to some sort of conversation, such as a group chat.

Next, from the main project, copy `interactive.py`, `pearl.py`, and `utils.py` into your quickstart folder. For plugins, make a `plugins` folder and add the following plugins from the main project:
* about
* eightball
* hello
* help

# Configuration
In the quickstart folder, create a file called `auth.json`. Store your Gmail credentials as such:
```json
{
	"email": "pearl@gmail.com",
	"password": "pearl"
}
```

# Running
You can run Pearl by executing `python3 pearl.py`. In your group chat, try sending `/pearl help`. Pearl will respond with a usage format and command list.