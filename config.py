import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = 'nv93498NKAf32c12cap2ASOuy2vcjo8934cmht39xx20i949y2'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    WTF_CSRF_ENABLED = False
    WTF_CSRF_SECRET_KEY = 'fdskcmWocm238mc2387nN940Z213uyg1fv12C451'

    MAIL_SERVER = 'smtp.mail.ru'
    MAIL_PORT = 587
    MAIL_USE_TLS = 1
    MAIL_USERNAME = 'sidorevich.toxa@mail.ru'
    MAIL_PASSWORD = 'JFDJ2390cm23hmhMGc12'
    ADMINS = ['sidorevich.anton@gmail.com']


class Constants(object):
    IMAGE_UPLOAD_FOLDER = basedir + '/app/static/Data/UsersPhotos/'
    IMAGE_DB_FOLDER = '/static/Data/UsersPhotos'
    ROOM_IMAGE_UPLOAD_FOLDER = basedir + '/app/static/Data/RoomPhotos/'
    ROOM_IMAGE_DB_FOLDER = '/static/Data/RoomPhotos'
    DEFAULT_USER_PHOTO = '/static/images/no_photo.png'
    DEFAULT_ROOM_PHOTO = '/static/images/no_photo.png'

    USER_PER_PAGE = 8
    MESSAGE_PER_PAGE = 20

    TIME_OF_ACTUAL_REQUEST = 500
    TIME_OF_ONLINE = 2  # Minutes

    MAX_PHOTO_SIZE = 3  # MB

    NAME_LENGTH = 50
    SURNAME_LENGTH = 50
    USERNAME_LENGTH = 50
    EMAIL_LENGTH = 50
    MIN_AGE = 14
    MAX_AGE = 150
    ADDRESS_LENGTH = 50
    PHOTO_LENGTH = 256
    MIN_PASSWORD_LENGTH = 6
    MAX_PASSWORD_LENGTH = 30
    ARTICLE_LENGTH = 512
    ROOM_NAME_LENGTH = 50
    MAX_MESSAGE_LENGTH = 2048
