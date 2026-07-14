# modules/weibo.py

import requests
from bs4 import BeautifulSoup

from config import (
    WEIBO_UID,
    USER_AGENT,
    REQUEST_TIMEOUT
)

from logger import logger



API = (
    "https://m.weibo.cn/api/container/getIndex"
)



HEADERS = {

    "User-Agent":
        USER_AGENT,

    "Accept":
        "application/json"

}



def html_to_text(html:str)->str:
    """
    微博HTML转纯文本
    """

    if not html:
        return ""


    soup = BeautifulSoup(
        html,
        "lxml"
    )


    return soup.get_text(
        "\n",
        strip=True
    )



def get_container_id():
    """
    微博移动端用户主页container id

    格式:
    107603 + UID
    """

    if not WEIBO_UID:

        raise ValueError(
            "缺少 WEIBO_UID"
        )


    return (
        "107603"
        +
        WEIBO_UID
    )



def request_page(
        page:int=1
):

    params = {

        "containerid":
            get_container_id(),

        "page":
            page

    }


    response = requests.get(

        API,

        params=params,

        headers=HEADERS,

        timeout=REQUEST_TIMEOUT

    )


    response.raise_for_status()


    return response.json()



def extract_images(
        mblog:dict
):

    images=[]


    pics = (
        mblog
        .get(
            "pics",
            []
        )
    )


    for pic in pics:

        url = (

            pic
            .get(
                "large",
                {}
            )
            .get(
                "url"
            )

        )


        if url:

            images.append(
                url
            )


    return images



def parse_cards(
        data
):

    result=[]


    cards = (
        data
        .get(
            "data",
            {}
        )
        .get(
            "cards",
            []
        )
    )


    for card in cards:


        mblog = card.get(
            "mblog"
        )


        if not mblog:

            continue



        # 跳过转发微博

        if (
            mblog.get(
                "retweeted_status"
            )
        ):

            continue



        # 跳过置顶

        if (
            mblog.get(
                "isTop"
            )
        ):

            continue



        text = html_to_text(

            mblog.get(
                "text",
                ""
            )

        )


        if not text:

            continue



        result.append({

            "id":
                str(
                    mblog["id"]
                ),


            "text":
                text,


            "created_at":
                mblog.get(
                    "created_at",
                    ""
                ),


            "url":
                (
                    "https://m.weibo.cn/detail/"
                    +
                    str(
                        mblog["id"]
                    )
                ),


            "images":
                extract_images(
                    mblog
                )

        })


    return result




def fetch_latest_posts(
        pages:int=2
):
    """
    获取最近微博

    默认:
    最近两页
    """

    posts=[]


    for page in range(
        1,
        pages+1
    ):


        try:

            data=request_page(
                page
            )


            posts.extend(

                parse_cards(
                    data
                )

            )


        except Exception as e:


            logger.error(

                f"微博获取失败:{e}"

            )


    logger.info(

        f"获取微博数量:{len(posts)}"

    )


    return posts
