"""从Raycast获取扩展数据并更新飞书表格。"""

from raycast_api import get_extension_data
from feishu_api import update_feishu_table

def job():
    """获取扩展数据并更新飞书表格。"""
    extension_data = get_extension_data()
    update_feishu_table(extension_data)
    print("数据已更新")

def main():
    """运行主程序。"""
    job()

if __name__ == "__main__":
    main()
