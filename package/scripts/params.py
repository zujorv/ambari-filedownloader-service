#!/usr/bin/env python
from resource_management import *

# server configurations
config = Script.get_config()

content_filename = "./GFD_downloaded_files.info.json"
content_json = config['configurations']['downloader-config']['content.json']
log_file = config['configurations']['downloader-config']['log.file']
