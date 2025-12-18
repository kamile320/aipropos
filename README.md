# aipropos

<a href="https://github.com/kamile320/aipropos/releases">![GitHub Release](https://img.shields.io/github/v/release/kamile320/aipropos)</a>
<a href="https://github.com/kamile320/aipropos/blob/main/LICENSE">![GitHub License](https://img.shields.io/github/license/kamile320/aipropos)</a>
<a href="">![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/kamile320/aipropos/total)</a>
<a href="https://github.com/kamile320/aipropos/commits/main/">![GitHub commits since latest release](https://img.shields.io/github/commits-since/kamile320/aipropos/latest)</a>

Linux simple 'apropos'-like command that uses AI

Search for command after describing it.  
Uses Google's Gemini API - you need to create API Token in [Google AI Studio](https://aistudio.google.com/) and type it in .env file.  
I recommend installing it via .deb file (it will work as normal linux command) - source code works only in one directory. You can also build .deb file using [build-deb.sh](https://github.com/kamile320/aipropos/blob/main/build-deb.sh).  

This command uses python virtual environment (venv) but it can also work without it*  
*When you add the --install argument, it will install all necessary packages, python libraries and venv. If you don't want to use venv, install python modules using the --install-lib argument.  
To see all arguments, see **aipropos --help** 

Usage: aipropos [command description]
