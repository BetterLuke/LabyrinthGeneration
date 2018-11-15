class Config(object):
    """
    Common configurations
    """  

class DevelopmentConfig(Config):
    """
    Development configurations
    """
    INPUT_FILE_PATH = "./test/test_input_data"


class ProductionConfig(Config):
    """
    Production configurations
    """ 
    INPUT_FILE_PATH = "./data.txt"

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}