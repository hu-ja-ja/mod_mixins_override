import os
import requests
import urllib.parse


def download(suffix:str, url:str) -> str:
  parsed_url = urllib.parse.urlparse(url)
  name, ext = os.path.splitext(os.path.basename(parsed_url.path))
  
  filename = f".builds/{name}{suffix}{ext}"

  urlData = requests.get(url).content

  with open(filename ,mode='wb') as f:
    f.write(urlData)
  
  return filename