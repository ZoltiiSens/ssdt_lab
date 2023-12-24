import os

PROPAGATE_EXCEPTIONS = True
FLASK_DEBUG = True

db_user = os.environ['DB_USER']
db_password = os.environ['DB_PASSWORD']
db_name = os.environ['DB_NAME']
db_host = os.environ['DB_HOST']
SQLALCHEMY_DATABASE_URI = f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
JWT_SECRET_KEY = os.environ["JWT_SECRET_KEY"]
# API_TITLE = "ssdt lab"
# API_VERSION = "v1.0.0"
# OPENAPI_VERSION = "3.0.3"
# OPENAPI_URL_PREFIX = "/"
# OPENAPI_SWAGGER_UI_PATH = "/swagger-ui"
# OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"





