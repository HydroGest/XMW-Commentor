import requests
import json
import sys

# 你的AccessToken
Token = "..."

# 要评论的用户名ID
targetID = 114514

content = ""
time = 1
if __name__ == '__main__':
    for value in sys.argv:
        if time > 1:
            content = content + " " + str(value)
        time = time + 1
url = 'https://community-api.xiaomawang.com/api/v1/user/comment'
#content = input("内容？")
body = {
  "targetId": targetID,
  "targetType": 7,
  "type": 1,
  "content": content,
  "adType": 0
}
headers = {'content-type': "application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.105 Safari/537.36","Access-token":token}
response = requests.post(url, data = json.dumps(body), headers = headers)

print(response.text)

print(response.status_code)
