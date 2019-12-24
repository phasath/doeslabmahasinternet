from decouple import config

'''Arquivo responsável por gerenciar o projeto.
É uma classe de configuração que seta os parâmetros do Flask.
manter todas as opções alteráveis aqui para que seja mais fácil editar mudanças.
'''

class Config(object):
    #App Conf
    DEBUG = False
    TESTING = False
    AIO_PORT = 5000
    AIO_HOST = '0.0.0.0'
    

class ProdConfig(Config):
    DEBUG = False
    ENV='production'


class DevConfig(Config):
    ENV='development'
    DEBUG = True

def config_to_class(environ_class):
    class_dict = {
        'development': DevConfig(),
        'production': ProdConfig()
    }
    return class_dict[environ_class]
