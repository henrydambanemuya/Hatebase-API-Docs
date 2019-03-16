import requests

r = requests.get('https://api.hatebase.org/1-0/authenticate', 
                data = {'key':'YQQ7LfxUXEVfRXEVfRpUxdnrgyiNeZhkDiomGXYaAQvdjpUxdnrgyiNeZhkDiomGXYaAQvdjDRzgwNXeToekEmgovPCzAGfd'})

print r.status_code == requests.codes.ok

print r.json()