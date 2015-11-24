# coding: utf-8
# ref: http://stackoverflow.com/questions/5757290/http-header-line-break-style

import socket, re

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 3000))

head = ""
head += 'POST /upload/ HTTP/1.1\r\n'
head += 'Host: 127.0.0.1:3000\r\n'
head += 'Content-Length: 128\r\n'
head += 'Content-Type: multipart/form-data; boundary=abcd\r\n'
head += '\r\n'

print "Head: ", len(head)
print "Data: \n", head

body = ""
body += '--abcd\r\n'
body += 'Content-Disposition: form-data; name=\"input_file\"; filename=\"TestFile.log\"\r\n'
body += 'Content-Type: text/x-log\r\n'
body += '\r\n'
body += 'testXX\r\n'
body += '--abcd--\r\n'
print "Body: ", len(body)
print "Data: \n", body

sock.send(head + body)
print sock.recv(512)

# 最後一個 \r\n 可以忽略所以可以把 ContentLength 設定成 128
