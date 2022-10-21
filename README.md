# cloudflare-ddns
A script that automatically updates your IP address to Cloudflare


## Setup

1. install python3: https://www.python.org/
2. install modules `requests` and `cloudflare`: https://pypi.org/project/requests/ , https://github.com/cloudflare/python-cloudflare
3. generate an API token with cloudflare and give it permissions to Edit Zone DNS: https://developers.cloudflare.com/fundamentals/api/get-started/create-token/
4. open the cfupdate.py file with the text editor of your choice
5. Paste your token into line 4 so that it shows `cftoken = '<your toke here>'`, keep the parenthesis
6. login to your cloudflare dashboard, go into the website you want to use this and copy the `Zone ID` on the right side below the `API` section
7. Paste the string into line 5 so that it shows `cfzone = '<zone id here>'`, keep the parenthesis
8. 
