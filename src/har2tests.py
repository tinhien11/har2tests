import json
import os
import sys
import autopep8
from haralyzer import HarParser

def main():
    pass

har_file = sys.argv[1]

with open(har_file, 'r') as f:
    har_parser = HarParser(json.loads(f.read()))

SEP = os.linesep
count = 1

result_lines = [
'''
import requests
import unittest
class TestRequest(unittest.TestCase):

'''
]
har_page = har_parser.pages[0]
entries = har_page.filter_entries(content_type='application/json')
for entry in entries:
    if 'websocket' in entry['response']['content']['text']:
        continue

    request_el = entry['request']
    method = request_el['method'].lower()
    url = request_el['url']
    data = {}
    if 'postData' in request_el:
        if 'text' in request_el['postData']:
            data = request_el['postData']['text']
        elif 'params' in request_el['postData']:
            raise NotImplementedError(
                "Haven't seen 'params' in the wild yet.")
    headers = dict((d['name'], d['value']) for d in request_el['headers'])
    call_code = '''
    def test_request{count}(self):
        response = requests.{method}('{url}', data={data}, headers={headers})        
        self.assertEqual(response.status_code, {status_code})
        self.assertEqual(len(response.content), {response})
    '''.format(method=method, url=url, data=data,
               headers=headers,
               status_code=entry['response']['status'],
               response=entry['response']['content']['size'],
               count=count
               )
    result_lines.append(call_code)
    count += 1

result = SEP.join(result_lines)
result = autopep8.fix_code(
result, options={'aggressive': 1})
print(result)
