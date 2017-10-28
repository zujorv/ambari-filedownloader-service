#!/usr/bin/env python
from resource_management import *

# server configurations
config = Script.get_config()
# constants
content_filename = "./GFD_downloaded_files.info.json"
# provided configuration
content_json = config['configurations']['downloader-config']['content.json']
log_file = config['configurations']['downloader-config']['log.file']
