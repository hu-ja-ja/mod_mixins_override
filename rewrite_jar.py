import json
from rich import print
import zipfile

def rewrite(jar_path:str, version_suffix:str, mixin_json_path:str, mixin_mixins: list[str], mixin_client: list[str], mixin_server: list[str]):

  with zipfile.ZipFile(jar_path, "r") as zip_ref:

    with zip_ref.open("fabric.mod.json", "r") as file:
      raw = file.read().decode("utf-8")
      new_fabric_mod_json = json.loads(raw)
      new_fabric_mod_json["version"] += version_suffix

    with zip_ref.open(mixin_json_path, "r") as file:
      raw = file.read().decode("utf-8")
      new_mixin_json: dict = json.loads(raw)

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

  with zipfile.ZipFile(jar_path, "w") as zip_ref:

    with zip_ref.open("fabric.mod.json", "w") as file:
      file.write(json.dumps(new_fabric_mod_json).encode())

    with zip_ref.open(mixin_json_path, "w") as file:
      file.write(json.dumps(new_mixin_json).encode())


  # with zipfile.ZipFile(zip_file_path, "r") as zip_ref:

  #   with zip_ref.open("fabric.mod.json", "r") as file:
  #     data = json.loads(file.read().decode("utf-8"))["version"]
  #     print(data)

  #   with zip_ref.open("carpet-tis-addition.mixins.json", "r") as file:
  #     data = json.loads(file.read().decode("utf-8"))
  #     print(data.get("mixins"))
  #     print(data.get("client"))
  #     print(data.get("server"))

