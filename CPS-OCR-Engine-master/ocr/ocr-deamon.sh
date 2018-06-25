#!/bin/sh
while true
do
  count=$(ps -ef | grep -c Chinese_OCR) #查找当前的进程中，计算server程序的数量
  if [ $count -lt 2 ]
   then        #判断服务器进程的数量是否小于3（根据实际填上你的服务器进程数量）
    python Chinese_OCR.py --mode=train --max_steps=16002 --eval_steps=100 --save_steps=500              #这里填入需要重启的服务器进程
  fi
  sleep 2                          #睡眠2s，周期性地检测服务器程序是不是崩溃了
done