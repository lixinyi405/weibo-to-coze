# 🌸 Weibo to Coze

基于 GitHub Actions + Coze 知识库 + RAG 的微博自动同步系统。

本项目用于自动获取指定微博账号（以单依纯为例）的最新动态，经过清洗、去重、结构化处理后，自动上传至 Coze 国内版知识库，为后续 AI Bot 提供实时知识来源。
## 功能

- 自动获取指定微博用户最新动态
- 自动去重
- 自动生成知识库文档
- 自动上传到 Coze Knowledge
- GitHub Actions 自动运行
- 自动记录同步日志
## 项目功能

- 自动获取微博最新动态
- 自动过滤转发微博
- 自动过滤置顶微博
- 自动去重
- 自动转换 Markdown 文档
- 自动上传 Coze 知识库
- GitHub Actions 定时运行
- 无需服务器长期运行
## 项目结构

```
weibo-to-coze/

├── main.py

├── config.py

├── logger.py

├── modules/

│ ├── weibo.py

│ ├── formatter.py

│ ├── dedup.py

│ └── coze.py

├── data/

│ └── history.json

├── logs/

├── requirements.txt

├── .env.example

└── .github/

└── workflows/

    └── sync.yml

## 当前开发进度

## 项目架构
微博

↓

微博JSON接口

↓

数据清洗

↓

去重模块

↓

Markdown格式化

↓

Coze知识库

↓

## 一、本地运行


## 1. 安装环境


Python >= 3.11


安装依赖：

```bash
pip install -r requirements.txt
2. 配置环境变量

复制：

.env.example

改名：

.env

填写：

WEIBO_UID=微博用户ID

COZE_TOKEN=Coze Token

COZE_DATASET_ID=知识库ID
3. 运行
python main.py
##二、GitHub Actions部署
1. 创建仓库

创建：

weibo-to-coze

上传全部代码。

2. 设置Secrets

进入：

Settings

↓

Secrets and variables

↓

Actions

↓

New repository secret

添加：

WEIBO_UID

COZE_TOKEN

COZE_DATASET_ID
3. 开启Actions

上传代码后：

Actions

↓

Weibo To Coze Sync

↓

Run workflow

即可测试。

##三、自动运行时间

GitHub Actions默认：

UTC时间

当前配置：

00:00 UTC

06:00 UTC

12:00 UTC

18:00 UTC

北京时间：

08:00

14:00

20:00

02:00
##四、Coze知识库配置

需要准备：

创建文本知识库
获取：
dataset_id
创建API Token

填写：

COZE_TOKEN

COZE_DATASET_ID

##五、数据格式

微博会转换成：

# 单依纯微博动态


## 发布时间

2026-07-14


## 微博正文

今天发布新歌啦！


## 图片信息

图片链接


## 来源

微博


这种格式更适合 RAG 检索。

##六、后续扩展方向

可以继续增加：

微博评论分析
热搜监控
B站视频同步
抖音动态同步
AI每日追星日报
多明星知识库
自动生成粉丝周报
##七、项目定位

该项目本质为：

AI Agent

+

RAG Pipeline

+

自动化数据工程


可用于：

AI应用开发
知识库构建
信息聚合机器人
数字内容管理
