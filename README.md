# 必应每日一图
必应每日一图-爬取后端

## 配置

### 1.复制样例文件

```shell
cp conf.example.json conf.json
```

### 2.编辑

```shell
vim conf.json
```

配置解释：

```json
{
  "SAVE_IMAGE_PATH": "",
  "SAVE_JSON_PATH": "data.json",
  "BING_URL": "https://cn.bing.com/"
}
```

`SAVE_IMAGE_PATH`:图片保存的目录，为空保存在运行目录
`SAVE_JSON_PATH`:JSON文件（相当于数据库）保存的路径
`BING_URL':必应首页URL，如果要爬取英文版改为https://cn.bing.com/?ensearch=1

## 运行

### 安装依赖

````shell
pip install -r requirements.txt
````

### 手动运行

```shell
python get_and_save.py
```

### Cron定时运行
```shell
crontab -e

0 1 * * * python /path/to/script/get_and_save.py
```
