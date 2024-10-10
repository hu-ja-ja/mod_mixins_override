import json
import zipfile

def rewrite(jar_path:str, build_dir:str, download_dir:str, version_suffix:str, mixin_json_path:str, mixin_mixins: list[str], mixin_client: list[str], mixin_server: list[str]):

  with zipfile.ZipFile(f"{download_dir}/{jar_path}", "r") as inzip, zipfile.ZipFile(f"{build_dir}/{jar_path}", "w") as outzip:
    for file in inzip.infolist():
      with inzip.open(file, "r") as f:
        data = f.read()

        # fabric.mod.json
        if file.filename == "fabric.mod.json":
          new_fabric_mod_json = json.loads(data.decode("utf-8"))
          new_fabric_mod_json["version"] += version_suffix
          data = json.dumps(new_fabric_mod_json).encode()

        # mixin.json
        elif file.filename == mixin_json_path:
          new_mixin_json: dict = json.loads(data.decode("utf-8"))
          if mixin_mixins != None and len(mixin_mixins) > 0:
            mixins: list[str] = new_mixin_json.get("mixins")
            for mixin in mixin_mixins:
              mixins.remove(mixin)
            new_mixin_json["mixins"] = mixins

          if mixin_client != None and len(mixin_client) > 0:
            client: list[str] = new_mixin_json.get("client")
            for mixin in mixin_client:
              client.remove(mixin)
            new_mixin_json["mixins"] = mixins

          if mixin_server != None and len(mixin_server) > 0:
            server: list[str] = new_mixin_json.get("server")
            for mixin in mixin_server:
              server.remove(mixin)
            new_mixin_json["mixins"] = mixins
          data = json.dumps(new_mixin_json).encode()

        outzip.writestr(file, data)
