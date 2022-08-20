# Random OS things
Things I often forget how to do.

## Linux Stuff


## Windows Stuff

### Postgres
1. To start/stop/restart Posgres on Windows, easiest to use Windows Services as it will tell you anything that may have gone wrong: 
	- *Type "services.msc" in run popup(windows + R). This will show all services running. Select Postgres service from list and click on start/stop/restart.*
	- Tested on Windows 10 Pro 

### Ruby
Steps used to resolve *ArgumentError wrong numner of arguments...* issue when installing using WSL
- gem uninstall psych
- sudo apt remove ruby2.5*
- sudo apt-get install ruby2.7 ruby2.7-dev build-essential dh-autoreconf
- gem update

HT: https://github.com/jekyll/jekyll/issues/8842

## OS X Stuff
