##################################################################
import requests
urlstr='https://www.wanandroid.com/user/login'
payload={"username":"lily","password":'123456'}
re=requests.post(url=urlstr,data=payload)
r2=requests.get('https://wanandroid.com/lg/todo/list/0',cookies=re.cookies)
print(r2.text)

# print(re.cookies)
# header2={
#     "cookie":re.cookies
# }