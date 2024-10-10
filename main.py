import os
import yaml
import rewrite_jar
import downloader

with open('config.yml', 'r') as yml:
  config = yaml.safe_load(yml)

suffix:str = config["suffix"]

tasks:list[dict[str, str|list[str]]] = config["tasks"]

build_dir = "./build"
download_dir = "./cache"

os.makedirs(build_dir, exist_ok=True)
os.makedirs(download_dir, exist_ok=True)

count = 0
for task in tasks:
  url = task["download_url"]
  print(f"[{count}] start download... {url}")
  filename = downloader.download(
    suffix = suffix,
    url = url,
    dir = download_dir,
  )
  print(f"[{count}] finish download {filename}")

  print(f"[{count}] start rewrite_jar...")
  rewrite_jar.rewrite(
    jar_path = filename,
    build_dir = build_dir,
    download_dir = download_dir,
    version_suffix = suffix,
    mixin_json_path = task["json"],
    
    mixin_mixins = task.get("mixins"),
    mixin_client = task.get("client"),
    mixin_server = task.get("server"),
  )
  print(f"[{count}] finish rewrite_jar")
  print(f"[{count}] complate task")

  count += 1
