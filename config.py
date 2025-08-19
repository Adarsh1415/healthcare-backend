import os

class Config:
    """Base configuration class."""
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT Config
    JWT_SECRET_KEY = os.environ.get(
        'JWT_SECRET_KEY',
        'a_very_secure_secret_key_that_should_be_in_a_.env_file'
    )
    JWT_TOKEN_LOCATION = ["headers"]
    JWT_HEADER_NAME = "Authorization"
    JWT_HEADER_TYPE = "Bearer"

    if not os.environ.get('JWT_SECRET_KEY'):
        print("⚠️ Warning: JWT_SECRET_KEY is not set. Using a dummy key.")
