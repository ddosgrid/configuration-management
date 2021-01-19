import requests
import sys

if len(sys.argv) < 8:
    print(str(8 - len(sys.argv)) + ' argument(s) missing!')
    sys.exit(1)
client_id = sys.argv[1]
client_secret = sys.argv[2]
client_cb = sys.argv[3]
client_name = sys.argv[4]
username = sys.argv[5]
password = sys.argv[6]
baseurl = sys.argv[7]

login_endpoint = '/login'
create_oauth_app_endpoint = '/admin/oauth2_provider/application/add/'

headers = {'User-Agent': 'Mozilla/5.0'}

session = requests.Session()
print('GETTING csrf token')
r = session.get(baseurl + login_endpoint)
#print(session.cookies)
#print(r.cookies)
payload = {
  'username': username,
  'password': password,
  'csrfmiddlewaretoken': session.cookies['csrftoken']
}
print('POSTING credentials to get session ID')
r = session.post(baseurl + login_endpoint, headers=headers, data=payload)
# print(r.text)
r = session.get(baseurl + '/admin/oauth2_provider/application/')
# print(r.text)
form = {
  'csrfmiddlewaretoken': session.cookies['csrftoken'],
  'client_id': client_id,
  'initial-client_id': 'iLmHRVtzJYydzN4vazEF5npsq9BQJmlb8d8OYovM',
  'user': 1,
  'redirect_uris': client_cb,
  'client_type': 'public',
  'authorization_grant_type': 'authorization-code',
  'client_secret': client_secret,
  'initial-client_secret': 'om4VgRXeO1yriY9ujWsugAJOn34pSnZDfnBUMfzi97oW5aSBM3Oz4x6R4GFtExYEwRbmkDrdfGESjBQ9zqSICZNsA2gqjPmCjvZVI8PBPN05DbzgvBHeJINYPLgNAApb',
  'name': client_name,
  '_save': 'Save'
}
r = session.post(baseurl + create_oauth_app_endpoint, headers=headers, data=form)

#print(r.text)
