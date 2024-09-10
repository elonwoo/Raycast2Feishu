"""飞书多维表格记录创建模块。"""

import lark_oapi as lark
from lark_oapi.api.bitable.v1 import CreateAppTableRecordRequest, AppTableRecord
from config import APP_ID, APP_SECRET, FEISHU_APP_TOKEN, FEISHU_TABLE_ID

def create_bitable_record(client, app_token, table_id, fields):
    """创建一条多维表格记录。"""
    request = CreateAppTableRecordRequest.builder() \
        .app_token(app_token) \
        .table_id(table_id) \
        .request_body(AppTableRecord.builder().fields(fields).build()) \
        .build()

    response = client.bitable.v1.app_table_record.create(request)

    if not response.success():
        lark.logger.error(
            "创建记录失败: code=%s, msg=%s, log_id=%s",
            response.code, response.msg, response.get_log_id())
        return None

    return response.data

def update_feishu_table(extension_data):
    """初始化飞书客户端并创建多条多维表格记录。"""
    client = lark.Client.builder() \
        .app_id(APP_ID) \
        .app_secret(APP_SECRET) \
        .build()

    for data in extension_data:
        fields = {
            "插件名称": data['name'],
            "安装数量": data['download_count'],
        }

        result = create_bitable_record(client, FEISHU_APP_TOKEN, FEISHU_TABLE_ID, fields)

        if result:
            lark.logger.info("创建记录成功:")
            lark.logger.info(lark.JSON.marshal(result, indent=4))
        else:
            lark.logger.error("创建记录失败")
