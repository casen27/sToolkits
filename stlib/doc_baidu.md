# 百度AI接口、说明文档


## 百度翻译接口说明文档


### 一、说明

[百度翻译官方技术说明](http://api.fanyi.baidu.com/api/trans/product/apidoc)
后台  ./st_baidu.py
界面  ./st_ui_baidu.py


### 二、支持的语言

源语言语种不确定时可设置为 auto，目标语言语种不可设置为 auto

| 语言简写 |     名称     |
| :------: | :----------: |
|   auto   |   自动检测   |
|    zh    |   简体中文   |
|   cht    |   繁体中文   |
|    en    |     英语     |
|   yue    |     粤语     |
|   wyw    |    文言文    |
|    jp    |     日语     |
|   kor    |    朝鲜语    |
|   fra    |     法语     |
|   spa    |   西班牙语   |
|    th    |     泰语     |
|   ara    |   阿拉伯语   |
|    ru    |     俄语     |
|    pt    |   葡萄牙语   |
|    de    |     德语     |
|    it    |   意大利语   |
|    el    |    希腊语    |
|    nl    |    荷兰语    |
|    pl    |    波兰语    |
|   bul    |  保加利亚语  |
|   est    |  爱沙尼亚语  |
|   dan    |    丹麦语    |
|   fin    |    芬兰语    |
|    cs    |    捷克语    |
|   rom    |  罗马尼亚语  |
|   slo    | 斯洛文尼亚语 |
|   swe    |    瑞典语    |
|    hu    |   匈牙利语   |
|   vie    |    越南语    |
|          |              |


### 三、错误码及解决方案

| 错误码 |        含义        |               解决方法               |
| :----: | :----------------: | :----------------------------------: |
| 52000  |        成功        |                  /                   |
| 52001  |      请求超时      |                 重试                 |
| 52002  |      系统错误      |                 重试                 |
| 52003  |     未授权用户     | 检查appid是否正确，或者服务是否开通  |
| 54000  |    必填参数为空    |           检查是否少传参数           |
| 54001  |      签名错误      |        请检查您的签名生成方法        |
| 54003  |    访问频率受限    |          请降低您的调用频率          |
| 54004  |    账户余额不足    |      请前往管理控制台为账户充值      |
| 54005  |  长query请求频繁   |  请降低长query的发送频率，3s后再试   |
| 58000  |    客户端IP非法    | 检查个人资料里填写的 IP地址 是否正确 |
| 58001  | 译文语言方向不支持 |     检查译文语言是否在语言列表里     |
| 58002  |   服务当前已关闭   |       请前往管理控制台开启服务       |
| 90107  | 认证未通过或未生效 |      请前往我的认证查看认证进度      |
|        |                    |                                      |
