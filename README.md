# raycast-to-feishu

将 Raycast 扩展安装数据同步到飞书多维表格。

## 项目描述

raycast-to-feishu 是一个自动化工具，用于将您的 Raycast 扩展安装数据同步到飞书多维表格中。这个工具可以帮助您更好地管理和追踪您在 Raycast 中安装的扩展。

## 主要功能

- 从 Raycast 获取已安装扩展的数据
- 将扩展数据同步到指定的飞书多维表格
- 自动更新现有数据，添加新安装的扩展

## 项目结构

- `main.py`: 主程序入口
- `raycast_api.py`: Raycast API 交互
- `feishu_api.py`: 飞书 API 交互
- `config.py`: 配置文件
- `.github/workflows/scrape.yml`: GitHub Actions 自动化配置

## 使用方法

1. 克隆仓库
2. 复制 `config.py.example` 为 `config.py` 并填写必要的配置信息
3. 安装依赖: `pip install -r requirements.txt`
4. 运行主脚本: `python main.py`

## 自动化

本项目使用 GitHub Actions 进行自动化同步。查看 `.github/workflows/scrape.yml` 了解详情。

## 许可证

本项目采用 MIT 许可证 - 详情请见 [LICENSE](LICENSE) 文件。
