import os

class Config:
    SECRET_KEY = '4970ca2d4778a43fbde60f643b417502'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'chavi11204@gmail.com'#os.environ.get('MAIL_USER')
    MAIL_PASSWORD = 'jvvxmhdgbiyhbxfb'#os.environ.get('MAIL_PASSWORD')
