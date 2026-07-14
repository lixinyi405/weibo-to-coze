# main.py

from modules.weibo import fetch_latest_posts
from modules.dedup import (
    is_uploaded,
    mark_uploaded
)
from modules.formatter import (
    format_weibo
)
from modules.coze import (
    CozeClient
)

from logger import logger



def sync_weibo():

    logger.info(
        "====== 开始同步单依纯微博 ======"
    )


    # 获取微博

    posts = fetch_latest_posts(
        pages=2
    )


    if not posts:

        logger.warning(
            "没有获取到微博"
        )

        return



    coze = CozeClient()



    upload_count = 0



    for post in posts:


        weibo_id = post["id"]



        # 已同步跳过

        if is_uploaded(
            weibo_id
        ):

            logger.info(
                f"跳过已存在微博:{weibo_id}"
            )

            continue



        try:


            # 转Markdown

            document = format_weibo(
                post
            )



            # 上传Coze

            coze.upload_text(

                title=document["title"],

                content=document["content"]

            )



            # 记录

            mark_uploaded(
                post
            )


            upload_count += 1



        except Exception as e:


            logger.exception(

                f"同步失败:{weibo_id}:{e}"

            )



    logger.info(

        f"本次同步完成，新上传 {upload_count} 条"

    )




if __name__ == "__main__":

    sync_weibo()
