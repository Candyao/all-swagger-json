#!/bin/bash
if [ $1 == "start" ];then
  hug -f get_json.py -p 8890 > log-$(date +%y%m%d)_$(date +%H%M) 2>&1 &
  exit 0
fi
if [ $1 == "restart" ];then
  ps -ef | grep get_json | grep -v grep | cut -c 9-15 | xargs kill
  hug -f get_json.py -p 8890 > log-$(date +%y%m%d)_$(date +%H%M) 2>&1 &
  exit 0
fi
if [ $1 == "stop" ];then
  ps -ef | grep get_json | grep -v grep | cut -c 9-15 | xargs kill
  exit 0
fi
echo "need param.return 1"
exit 1

