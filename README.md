## kmrbot通用配置

配置需要将目录放在kmrbot的根目录下。

## 目录结构
* common 用于一些bot的基本功能配置

**common_config.json**
* bili.user.cache_expire : B站用户缓存的过期时间，一般60s足够。
 > 该缓存过期不代表缓存失效，仅代表添加缓存时该缓存需要刷新。
* dynamic.pusher.retry_max_count : B站动态推送器的重试次数，一般3次足够。用来当网络错误时尝试重新绘制，如果是因代码原因导致绘制失败则也会重试直到次数上限溢出。
* live.pusher.judgement_by_user_info : 是否根据用户信息来决策开播状态。建议开启。不开启可能会导致直播状态发生抖动。
* live.pusher.judgement_by_room_message : 是否根据直播间消息来决策开播状态。建议开启，不开启会导致直播状态推送速度有较高延迟（1分钟左右）。
> [!NOTE]  
> 开启该选项时强烈建议开启judgement_by_user_info，不然一定会导致开播后状态抖动！
* cookies 用于拉取B站信息的缓存

**bili_cookies.json**
* cookies : 一个数组，每一个元素都是一个独立的B站缓存。仅当监控了直播间消息，或judgement_by_room_message启用时才需要。
* dynamic_session : 拉取动态和直播状态的session。
* plugin.yaml 插件管理配置文件，可以独立管理每个插件的开启与暂停，以及插件在哪些群组内才会生效。**（支持动态修改，即当修改该文件后会立刻生效）**
