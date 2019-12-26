'''Arquivo responsável por gerenciar o projeto.
É uma classe de configuração que seta os parâmetros do Flask.
manter todas as opções alteráveis aqui para que seja mais fácil editar mudanças.
'''

from decouple import config
from pathlib import Path

root_location = Path(__file__).resolve().parent
class Config(object):
    #App Conf
    DEBUG = False
    TESTING = False
    AIO_PORT = config('AIO_PORT', 5000)
    AIO_HOST = config('AIO_HOST', '0.0.0.0')
    TEMPLATE_FOLDER = config("TEMPLATE_FOLDER", f'{root_location}/template')
    STATIC_FOLDER = config("STATIC_FOLDER", f'{root_location}/static')

    MONGODB_URI = config('MONGODB_URI',
                         default=('mongodb://heroku_5lklhmz5:bs29c5m1jjahg21jhmtmk2o474@ds143451.mlab.com:43451/heroku_5lklhmz5'))

    SECRET_KEY = config('SECRET_KEY',
                        default='`)$GGx*&:0sZgxBv5kE{-8URC:ANzd2DRCW}`-<1DYk=7e<U^}nccg!`zj@0wo4')
    

class ProdConfig(Config):
    DEBUG = False
    ENV='production'


class DevConfig(Config):
    ENV='development'
    DEBUG = True

    MONGODB_URI = config('MONGODB_URI',
                  default='mongodb://labmainternet:labMA1nt4rnet!!@127.0.0.1:27017/labma')

def config_to_class(environ_class):
    class_dict = {
        'development': DevConfig(),
        'production': ProdConfig()
    }
    return class_dict[environ_class]
