from conf import app_config
from src.app import generateMaze
from src.my_utils.common import loadInputFile

    
def main():
    # app_conf = app_config["development"]()
    app_conf = app_config["production"]()
    input_data_Path = app_conf.INPUT_FILE_PATH
    data = loadInputFile(input_data_Path)
    for i in data:
        generateMaze(i)


if __name__ == "__main__":
    # execute only if run as a script
    main()