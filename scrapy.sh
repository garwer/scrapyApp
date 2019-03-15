#0 5 * * * /root/bin/backup.sh 每天8点执行
#! /bin/sh
export PATH=$PATH:/home/conda/anaconda3/envs/py36/bin
# 跳转至Scrapy项目目录
cd /home/conda/.qqbot-tmp/plugins/scrapyApp
# 后台运行抓取，并将日志输出到scrapyApp.log文件
nohup scrapy crawl scrapyApp >> logs/scrapyApp.log 2>&1 &