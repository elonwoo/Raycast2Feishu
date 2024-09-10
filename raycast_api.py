"""处理Raycast API相关操作的模块。"""

import requests
from config import RAYCAST_API_URL

def get_extension_data():
    """
    从Raycast API获取扩展数据。

    返回:
        list: 包含扩展名称和下载次数的字典列表。
    """
    response = requests.get(RAYCAST_API_URL, timeout=10)
    data = response.json()

    extension_data = []
    for extension in data['data']:
        extension_data.append({
            'name': extension['name'],
            'download_count': str(extension['download_count']),
        })

    return extension_data
