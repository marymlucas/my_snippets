# Random OS things
Things I sometimes forget how to do.

## Linux Stuff
1. Install Miniconda from shell
	- *curl -sL "https://repo.anaconda.com/miniconda/Miniconda3-py311_23.5.2-0-Linux-x86_64.sh" >   "Miniconda3.sh"*
	- *bash Miniconda3.sh*
	- Replace the URL with whichever version of miniconda you want to install (see https://docs.conda.io/en/latest/miniconda.html)

2. tmux
	- start new session with name: *tmux new -s <sesh_name>*
	- detach from session: *Ctrl-B D*
	- list existing sessions: *tmux ls*
	- reattach session: *tmux a -t <sesh_name>*
		- if only one session exists: *tmux a* will suffice
	- force terminate a specific session: *tmux kill-session -t <sesh_name>*
		- *kill-session* will kill all active sessions

## Windows Stuff

### Postgres
1. To start/stop/restart Posgres on Windows, easiest to use Windows Services as it will tell you anything that may have gone wrong: 
	- *Type "services.msc" in run popup(windows + R). This will show all services running. Select Postgres service from list and click on start/stop/restart.*
	- Tested on Windows 10 Pro 

### Ruby
Steps used to resolve *ArgumentError wrong number of arguments...* issue when installing using WSL
- gem uninstall psych
- sudo apt remove ruby2.5*
- sudo apt-get install ruby2.7 ruby2.7-dev build-essential dh-autoreconf
- gem update

HT: https://github.com/jekyll/jekyll/issues/8842

## OS X Stuff
