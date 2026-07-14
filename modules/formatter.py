# modules/formatter.py

from datetime import datetime


def clean_text(text: str) -> str:
    """
    清理微博文本
    """

    if not text:
        return ""

    text = text.strip()

    # 去除多余空行
    lines = [
        line.strip()
        for line in text.split("\n")
        if line.strip()
    ]

    return "\n".join(lines)



def format_weibo(post: dict) -> dict:
    """
    将微博数据转换成知识库文档

    输入:

    {
        id:
        text:
        created_at:
        url:
        images:
    }


    输出:

    {
        title:
        content:
    }

    """

    text = clean_text(
        post.get("text", "")
    )


    created_at = (
        post.get(
            "created_at",
            ""
        )
    )


    url = (
        post.get(
            "url",
            ""
        )
    )


    images = (
        post.get(
            "images",
            []
        )
    )


    image_text = ""


    if images:

        image_text = (
            "\n\n图片链接:\n"
        )

        for img in images:

            image_text += (
                f"- {img}\n"
            )


    title = (
        "单依纯微博动态 "
        +
        created_at
    )


    content = f"""
# 单依纯微博动态


## 发布时间

{created_at}


## 微博正文

{text}


## 图片信息

{image_text}


## 来源

微博


## 原始链接

{url}

"""


    return {

        "title":
            title.strip(),

        "content":
            content.strip()

    }
