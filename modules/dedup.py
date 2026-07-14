# modules/dedup.py

import json
from pathlib import Path
from datetime import datetime

from logger import logger


HISTORY_FILE = Path(
    "data/history.json"
)


def ensure_file():

    HISTORY_FILE.parent.mkdir(
        exist_ok=True
    )

    if not HISTORY_FILE.exists():

        HISTORY_FILE.write_text(
            "[]",
            encoding="utf-8"
        )



def load_history() -> list:
    """
    读取同步历史
    """

    ensure_file()

    try:

        with open(
            HISTORY_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    except Exception:

        return []



def save_history(history:list):
    """
    保存同步历史
    """

    ensure_file()

    with open(
        HISTORY_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            history,
            f,
            ensure_ascii=False,
            indent=2
        )



def is_uploaded(
    weibo_id:str
)->bool:
    """
    判断微博是否已经上传
    """

    history = load_history()


    for item in history:

        if item.get(
            "id"
        ) == str(weibo_id):

            return True


    return False



def mark_uploaded(
    post:dict
):
    """
    标记微博已同步
    """

    history = load_history()


    history.append({

        "id":
            str(post["id"]),


        "created_at":
            post.get(
                "created_at",
                ""
            ),


        "sync_time":
            datetime.now()
            .strftime(
                "%Y-%m-%d %H:%M:%S"
            )

    })


    # 保留最近1000条
    history = history[-1000:]


    save_history(
        history
    )


    logger.info(
        f"记录微博 {post['id']}"
    )
