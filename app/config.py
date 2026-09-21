class Config:
    API_TITLE = "API Playground"
    API_VERSION = "1.0.0"


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


config_by_name = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
}
