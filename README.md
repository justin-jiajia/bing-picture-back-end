# 必应每日一图
必应每日一图-爬取后端

## 通知

之前的数据可能出现“查看更多”字样，已修复。可以运行以下命令来修复之前的数据：

```shell
python fix.py
```

我们加入了页数系统所以JSON文件名有所改变，请在`SAVE_JSON_PATH`中加入`*`这个字符。设置为`data*.json`的效果：保存为`data.json`、`data1.json`...

由于加入页数系统JSON结构也有改变，同样运行`fix.py`!

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
  "SAVE_JSON_PATH": "data*.json",
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
