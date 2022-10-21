import CloudFlare
import requests

cftoken = 'your_cloudflare_token'
cfzone = 'your_cloudflare_zone_id'
cfrecord = 'example.com'
ipservice = 'https://checkip.amazonaws.com/'

cf = CloudFlare.CloudFlare(token=cftoken)

record = cf.zones.dns_records.get(cfzone, params={'name': cfrecord, 'type': 'A'})[0]

ip = requests.get(ipservice).text.strip()

record['content'] = ip

cf.zones.dns_records.put(cfzone, record['id'], data=record)