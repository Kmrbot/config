import os
import json
import random
from nonebot.log import logger
from configs import get_config_path


def random_get_bili_cookies():
    # 随机获取一个登录凭证
    with open(os.path.join(get_config_path(), "cookies/bili_cookies.json"), encoding="utf-8") as f:
        try:
            cookies = json.load(f)
            if cookies.get("cookies") is None or len(cookies["cookies"]) == 0:
                logger.error("random_get_bili_cookies bili_cookies invalid !")
                return None
        except json.JSONDecodeError:
            logger.error("random_get_bili_cookies json decode fail !")
            return None
    return cookies["cookies"][random.randint(0, len(cookies) - 1)]


def get_dynamic_session_cookies():
    # 获取动态缓存登录凭证
    with open(os.path.join(get_config_path(), "cookies/bili_cookies.json"), encoding="utf-8") as f:
        try:
            cookies = json.load(f)
            if cookies.get("dynamic_session") is None or len(cookies["dynamic_session"]) == 0:
                logger.error("get_dynamic_session_cookies bili_cookies invalid !")
                return None
        except json.JSONDecodeError:
            logger.error("random_get_bili_cookies json decode fail !")
            return None
    return cookies["dynamic_session"]
