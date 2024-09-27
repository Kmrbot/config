import os
import json
from nonebot.log import logger
from configs import get_config_path
from nonebot import get_driver


class CommonConfig:
    __config = None

    @classmethod
    def load_common_config(cls):
        with open(os.path.join(get_config_path(), "common/common_config.json"), encoding="utf-8") as f:
            try:
                cls.__config = json.load(f)
            except json.JSONDecodeError:
                logger.error("load_common_config json decode fail !")
                __config = None
        logger.info("load_common_config success.")

    @classmethod
    def get_user_cache_expire(cls) -> int:
        """
        获取用户缓存过期时间
        """
        expire = None
        if cls.__config is not None:
            expire = cls.__config.get("bili", {}).get("user", {}).get("cache_expire")
        if expire is None or type(expire) != int:
            logger.error("get_user_cache_expire fail ! expire invalid !")
            return 0
        else:
            return expire

    @classmethod
    def get_dynamic_retry_max_count(cls) -> int:
        """
        获取动态重试最大次数
        """
        max_count = None
        if cls.__config is not None:
            max_count = cls.__config.get("bili", {}).get("dynamic", {}).get("pusher", {}).get("retry_max_count")
        if max_count is None or type(max_count) != int:
            logger.error("get_dynamic_retry_max_count fail ! max_count invalid !")
            return 0
        else:
            return max_count

    @classmethod
    def is_live_status_judgement_by_user_info(cls) -> bool:
        """
        是否直播状态通过玩家信息来进行辅助抉择
        """
        if cls.__config is not None:
            return cls.__config.get("bili", {}).get("live", {}).get("pusher", {}).get("judgement_by_user_info")
        return False

    @classmethod
    def is_live_status_judgement_by_room_message(cls) -> bool:
        """
        是否直播状态通过直播间消息来进行辅助抉择
        """
        if cls.__config is not None:
            return cls.__config.get("bili", {}).get("live", {}).get("pusher", {}).get("judgement_by_room_message")
        return False
