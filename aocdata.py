import requests, json
from pathlib import Path
#from os import environ

def getdata(url, token):
  header = {'Cookie': f'session={token}'}
  r = requests.get(url, headers=header)
  if len(r.text) > 0:
    return r.text

def datafile(yearno, dayno):
  filename = f'aoc_day{dayno}.txt'
  path = Path(filename)
  if path.is_file():
    print(f'{filename} present')
  else:
    with open('.config/token') as conf:
      token = json.load(conf)['session']
    dat = getdata(f'https://adventofcode.com/{yearno}/day/{dayno}/input', token)
    with open(filename, 'w') as inp:
      inp.write(dat)
  return filename

if __name__ == '__main__':
  main(2015, 6)