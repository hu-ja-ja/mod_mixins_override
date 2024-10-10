import os
import yaml
import rewrite_jar
import downloader

with open('config.yml', 'r') as yml:
  config = yaml.safe_load(yml)

suffix:str = config["suffix"]

tasks:list[dict[str, str|list[str]]] = config["tasks"]

os.makedirs("./build", exist_ok=True)

count = 0
for task in tasks:
  url = task["download_url"]
  print(f"[{count}] start download... {url}")
  filename = downloader.download(
    suffix = suffix,
    url = task["download_url"],
  )
  print(f"[{count}] finish download {filename}")
  
  if filename != "build/fabric-carpet-1.18.1-1.4.57+v220119+vulpeus.jar":
    continue


  print(f"[{count}] start rewrite_jar...")
  rewrite_jar.rewrite(
    jar_path = filename,
    version_suffix = suffix,
    mixin_json_path = task["json"],
    
    mixin_mixins = task.get("mixins"),
    mixin_client = task.get("client"),
    mixin_server = task.get("server"),
  )
  print(f"[{count}] finish rewrite_jar")
  print(f"[{count}] complate task")

  count += 1
