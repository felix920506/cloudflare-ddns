# cloudflare-ddns
A script that automatically updates your IP address to Cloudflare


## Setup

1. install python 3 if you don't have it already. MacOS and Most Linux Distros come with it by default. : https://www.python.org/
2. install modules `requests` and `cloudflare`: https://pypi.org/project/requests/ , https://github.com/cloudflare/python-cloudflare
3. generate an API token with cloudflare and give it permissions to Edit Zone DNS: https://developers.cloudflare.com/fundamentals/api/get-started/create-token/
4. open the cfupdate.py file with the text editor of your choice
5. Paste your token into line 4 so that it shows `cftoken = '<your toke here>'`, keep the parenthesis
6. login to your cloudflare dashboard, go into the website you want to use this and copy the `Zone ID` on the right side below the `API` section
7. Paste the string into line 5 so that it shows `cfzone = '<zone id here>'`, keep the parenthesis
8. Save the file.


## Running

 First, open a command prompt or shell at where the file is located

Windows CMD: run `python cfupdate.py` command in CMD
Windows Powershell: run `python .\cfupdate.py` command in Powershell
Other OSes: run `python3 cfupdate.py` command in your shell


## Other notes

1. It uses an Amazon service to get your public IP address by default, you can change it to anything you like as long as it returns a IPv4 IP in plain text. Popular ones include `https://ipv4.icanhazip.com` and `https://api.ipify.org`. I am in no way affiliated with any of these parties.
2. Please report issues in the issues section
3. This script comes with NO WARRANTY and NO GARUANTEES. Please be sure what you are doing. Checking for problems isn't that hard, its only 17 lines.
