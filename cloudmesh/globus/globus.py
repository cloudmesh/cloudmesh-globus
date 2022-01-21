import os
from cloudmesh.common.util import readfile
import yaml
from pprint import pprint
from cloudmesh.common.Shell import Shell
from cloudmesh.common.console import Console
class Globus:

    def __init__(self,
                 source_endpoint=None,
                 destination_endpoint=None,
                 source_dir=None,
                 destination_dir=None):
        self.source_dir = source_dir
        self.destination_dir = destination_dir
        try:
            content = readfile("~/.cloudmesh/globus.yaml")
            self.bookmarks = yaml.safe_load(content)
        except:
            pass
        self.source_endpoint = self.bookmark(source_endpoint)
        self.destination_endpoint = self.bookmark(destination_endpoint)

    def bookmark(self, name):
        if name in self.bookmarks["bookmark"]:
            return self.bookmarks["bookmark"][name]
        else:
            return name


    def info(self):
        print(79*"=")
        print (f"Source     : {self.source_endpoint}:{self.source_dir}")
        print (f"Destination: {self.destination_endpoint}:{self.destination_dir}")
        print(79*"=")

    def login(self, source_endpoint=None, destination_endpoint=None):
        os.system(f"globus login")
        self.info()

    def mkdir(self, ep, destination):
        mkdir = f"globus mkdir {ep}:{destination}"
        print (mkdir)
        r = Shell.run(mkdir)
        if "Path already exists, Error (mkdir)" in r:
            Console.ok("Path exists. ok")
        elif "The directory was created successfully" in rsa:
            Console.ok("Path created. ok")
        else:
            Console.error("mkdir error")
            Console.error(str(r))

    def transfer(self, source, destination, label="cloudmesh transfer"):
        command = f"globus transfer {source} {destination}" \
                  f' --recursive --label "{label}"'
        print(command)



        os.system(command)
