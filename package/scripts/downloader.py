import sys, os, pwd, signal, time, glob, json
from resource_management import *

class Master(Script):

    def download_files(self, data_string):
        import params
        for data in json.loads(data_string):
            install_dir = data["install-dir"]
            for file in data["files"]:
                Execute('echo "Downloading ' + file["name"] + ' from ' + file["url"] + '" >> ' + params.log_file)
                Execute('wget -d -N -O ' + install_dir + '/' + file["name"] + ' ' + file["url"] + ' >> ' + params.log_file)

    def remove_files(self, data_string):
        import params
        for data in json.loads(data_string):
            install_dir = data["install-dir"]
            for file in data["files"]:
                Execute('echo "Removing ' + file["name"] + ' from ' + file["url"] + '" >> ' + params.log_file)
                Execute('rm -f ' + install_dir + '/' + file["name"] + ' >> ' + params.log_file)

    def check_files(self, data_string):
        #import os.path
        i = 0
        for data in json.loads(data_string):
            install_dir = data["install-dir"]
            for file in data["files"]:
                if not os.path.isfile(install_dir + '/' + file["name"]):
                    i = 1
        return i

    def install(self, env):
        import params
        # Install packages listed in metainfo.xml
        self.install_packages(env)
        content = InlineTemplate(params.content_json)
        Execute('echo "Saving content_json at ' + params.content_filename + '" >> ' + params.log_file)
        File(format(params.content_filename), content=content, owner='root',group='root', mode=0644)

    def configure(self, env):
        import params
        env.set_params(params)

    def stop(self, env):
        import params
        self.remove_files(params.content_json)

    def start(self, env):
        import params
        self.download_files(params.content_json)

    def status(self, env):
        import params
        file = open(params.content_filename, "r")
        if self.check_files(file.read()) == 0:
            pass
        else:
            raise ComponentIsNotRunning()

if __name__ == "__main__":
    Master().execute()
