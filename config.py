from r2 import R2Storage

BOT_TOKEN = "main_bot_token"
LOG_BOT_TOKEN = "log_channel_bot_token"

BOT_API_SERVER = ""
BOT_API_FILE_SERVER = ""

REDIS_URL = "redis://localhost:0000"
DATABASE_URL = "mangoDB_URL"

PASSWORD = "1"

LOG_CHAT_ID = 0

MULTI_UDID_LIMIT = 100
MAX_KEYGEN_PER_REQUEST = 60

MAX_P8_FILE_SIZE = 1024 * 1024

API_URL = ""
INSTALL_APP_URL = ""
GET_UDID_WEBAPP = ""
WEBAPP_URL = ""
SHORTNER_API_URL = ""

CHECK_DURATION = 2

R2 = R2Storage(
    endpoint_url="",
    key_id="",
    access_key="",
    bucket="",
    bucket_url="",
)

KEYS_R2 = R2Storage(
    endpoint_url="",
    key_id="",
    access_key="",
    bucket="",
    bucket_url="",
)

STATUS_R2 = R2
