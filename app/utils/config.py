import os


class AppConfig:
    def __init__(self):
        self.__load_env_file__()

        self.APP_BASE_DIR = os.getenv('APP_BASE_DIR')
        if self.APP_BASE_DIR is None:
            self.APP_BASE_DIR = os.getenv('APP_BASE_DIR_DEV')

        self.APP_NAME = os.getenv('APP_NAME')
        self.APP_LOGS_DIR = os.path.join(self.APP_BASE_DIR, 'logs')


    def __getitem__(self, key):
        return getattr(self,key)

    def __load_env_file__(self):
        import dotenv
        p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
        env_path = os.path.join(p, '.env')

        if os.path.exists(env_path):
            dotenv.load_dotenv(dotenv_path=env_path)


cfg = AppConfig()
