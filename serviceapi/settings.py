import os

environ = os.environ

SECRET_KEY = environ.get('SECRET_KEY', 'dlbNwHcHX85fMb4pbyqTXmFYjJPM5iHkbsJUi3rRRy4nEESsQF')
DATABASE_URI = environ.get('DATABASE_URI', 'postgresql+psycopg2://lefty@db/api')
SQLALCHEMY_DATABASE_URI = DATABASE_URI
REDIS_URL = environ.get('REDIS_URL', 'redis://redis@redis:6379')

CORS_ORIGINS = ''.join([
    'localhost:*',
    'api.docker',
    '*.local',
    '*.leftronic.local',
    '*.leftronic.com',
    'leftronic.com'
])
