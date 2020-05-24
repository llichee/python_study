#！/usr/bin/env python
#_*_coding:utf-8 _*_
__author__ = "Xzw"
import os
import time
import urllib2
import json
#企业号ID
wxid = ""
#应用ID
depid = ""
#认证密码
secret = ""
#获取主机的名称
hostname =
os.popen("hostname").read()
#日志存储文件
log_file =
'/var/log/ljf_status.log'
#监听端口列表
check_port = (
	"8500"
	"3306"
)
#发送的消息
msg = ""
#获取当前的时间
date_time = time.strftime("%Y-%m-%d %X")
#检查端口是否在监听
for i in check_port:
	shell = "netstat -nutlp | grep "" + i + """
	recv = os.popen(shell).read()
	if recv == "":
		msg = msg + hostname + ": The Port " + i + "is down"
#预警判断
if msg != "":
	url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=" + wxid + "&corpsecret=" + secret
	request = urllib2.Request(url)
	response = urllib2.urlopen(request)
	recv_info = response.read()
	recv_info = eval(recv_info)
	wx_token = recv_info['access_token']
	msg_url = "https://qyapi.weixin.qq.com/cgi-bin/message/send? access_token=" + wx_token
	send_msg = {
		"tuoser": "@all",
		"msgtype": "text",
		"agentid": depid,
		"text": {"content": msg},
		"safe": 0
	}
	send_msg_json = json.dumps(send_msg)
	request_post = urllib2.urlopen(msg_url, send_msg_json)
	recv_msg = request_post.read()
	with open(log_file, mode='a') as f:
		f.write(date_time)
		f.write("")
		f.write(msg)
		f.write(recv_msg)
		f.write("")