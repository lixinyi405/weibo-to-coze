# modules/coze.py

import time
import requests

from config import (
    COZE_TOKEN,
    COZE_DATASET_ID,
    REQUEST_TIMEOUT
)

from logger import logger


class CozeClient:
    """
    Coze 知识库客户端

    功能：
    1. 身份认证
    2. 上传文本
    3. 错误重试
    """

    BASE_URL = "https://api.coze.cn"

    def __init__(self):

        self.token = COZE_TOKEN
        self.dataset_id = COZE_DATASET_ID

        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
            "Agw-Js-Conv": "str"
        }


    def upload_text(
        self,
        title: str,
        content: str,
        retry: int = 3
    ):
        """
        上传文本到 Coze 知识库

        title:
            文档标题

        content:
            Markdown正文
        """


        if not self.token:
            raise ValueError(
                "缺少 COZE_TOKEN"
            )

        if not self.dataset_id:
            raise ValueError(
                "缺少 COZE_DATASET_ID"
            )


        payload = {

            "dataset_id":
                self.dataset_id,

            "title":
                title,

            "content":
                content
        }


        api = (
            self.BASE_URL
            +
            "/open_api/knowledge/document/create"
        )


        for i in range(retry):

            try:

                logger.info(
                    f"上传Coze知识库: {title}"
                )


                response = requests.post(
                    api,
                    headers=self.headers,
                    json=payload,
                    timeout=REQUEST_TIMEOUT
                )


                data = response.json()


                if response.status_code == 200:

                    logger.info(
                        "Coze上传成功"
                    )

                    return data


                logger.warning(
                    f"Coze返回异常: {data}"
                )


            except Exception as e:

                logger.error(
                    f"上传失败 {e}"
                )


            time.sleep(
                2 ** i
            )


        raise RuntimeError(
            "Coze上传失败，超过最大重试次数"
        )
