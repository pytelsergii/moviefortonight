import logging.config
import os

import yaml

from definitions import ROOT_DIR


def create_tmp_dir():
    tmp_dir_path = f'{ROOT_DIR}/tmp'
    os.makedirs(tmp_dir_path, exist_ok=True)


def setup_config(path=f'{ROOT_DIR}/configs/config.yaml', default_level=logging.INFO):
    config = None
    if os.path.exists(path):
        with open(file=path, mode='r') as f:
            try:
                config = yaml.safe_load(f.read())
                logging_section = config['logging']
                log_name = f"{ROOT_DIR}/{logging_section['handlers']['file_handler']['filename']}"
                logging_section['handlers']['file_handler']['filename'] = log_name
                create_tmp_dir()
                logging.config.dictConfig(logging_section)
            except Exception as e:
                print(e)
                print('Error in Logging Configuration. Using default configs')
                logging.basicConfig(level=default_level)

    else:
        print(f'Specified path to config file: {path} does not exist')
    return config
