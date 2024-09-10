"""raycast-to-feishu 项目的配置文件，包含各种API和凭证信息。"""

import os

APP_ID = os.environ.get('FEISHU_APP_ID')
APP_SECRET = os.environ.get('FEISHU_APP_SECRET')
FEISHU_APP_TOKEN = os.environ.get('FEISHU_APP_TOKEN')
FEISHU_TABLE_ID = os.environ.get('FEISHU_TABLE_ID')
RAYCAST_API_URL = os.environ.get('RAYCAST_API_URL')
