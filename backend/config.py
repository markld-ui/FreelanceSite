# Other modules
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    SECRET_KEY: str = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI: str = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    MAIL_SERVER: str | None = os.environ.get('MAIL_SERVER')
    MAIL_PORT: int = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS: str | None = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME: str = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD: str = os.environ.get('MAIL_PASSWORD')
    ADMINS: list[str] = ['thankr3@example.com']
    LANGUAGES: list[str] = ['en', 'ru']
    MS_TRANSLATOR_KEY: str | None = os.environ.get('MS_TRANSLATOR_KEY')
    POSTS_PER_PAGE: int = 25

    ELASTICSEARCH_URL: str | None = os.environ.get('ELASTICSEARCH_URL')
