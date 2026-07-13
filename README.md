# 🌸 Weibo to Coze

一个用于自动同步微博内容到 Coze 知识库的项目。

## 功能

- 自动获取指定微博用户最新动态
- 自动去重
- 自动生成知识库文档
- 自动上传到 Coze Knowledge
- GitHub Actions 自动运行
- 自动记录同步日志

## 项目结构

```
weibo-to-coze/
│
├── README.md
├── requirements.txt
├── config.py
├── crawler.py
├── uploader.py
├── main.py
├── cache/
│   └── history.json
└── .github/
    └── workflows/
        └── update.yml
```

## 当前开发进度

- [x] 创建仓库
- [ ] 获取微博
- [ ] 上传 Coze
- [ ] 自动更新
- [ ] GitHub Actions# weibo-to-coze
