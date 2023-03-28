# iresearch-crawl
A crawler classification project for iresearch

### 目标网站：

https://www.iresearch.com.cn/report.shtml

### 流程：

1. 运行**load_data.py**来通过获取所有的request url中的json格式来读取艾瑞咨询所有公开的报告，并保存在all_json格式文件中。不过这步可以省略，
   因为已经上传了目前艾瑞咨询编号为1650-4045的json信息到all_json文件中。

2. 关于**main.py**读取所有报告的json并经型分类下载。1650-4045运行需要15-30分钟

3. 第二步运行结束后即可在工程文件夹下看到已经建好的文件夹和分类完成的艾瑞咨询报告。


### 仍需改进的地方：

**load_data.py**，由于1650-4045的request_url中有很多是空信息，无法用循环遍历进行爬取，
未来需要写一个函数从最新的url request中读取最后一条信息的freport.xxx并依次循环遍历所有的url并读取其中的request url