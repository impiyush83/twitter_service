from taas_restful.app import create_app
from taas_restful.settings import Config

if __name__ == '__main__':
    app = create_app(Config)
    app.run()
