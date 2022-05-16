import requests,json
import urllib3
urllib3.disable_warnings()  #禁用安全请求警告

# Cheese接口
class Api():
    # common接口
    def content_config(self, Language, clinet_version, os_version, phone_model):
        self.s = requests.Session()
        self.url = "https://api.earncheese.net/dec/v1"
        # self.heads={}
        data = json.dumps({"language": Language,"client_version": clinet_version,"os_version": os_version,"phone_model": phone_model})
        r = self.s.post(self.url+"/common/content_config", data=data, verify=False)
        re = r.json()
        print(re)

    def banner(self):
        self.s = requests.Session()
        self.url = "https://api.earncheese.net/dec/v1"
        # self.heads={}
        r = self.s.get(self.url+"common/banner")
        re = r.json()
        print(re)

if __name__ == '__main__':
    a = Api()
    # a1 = a.content_config()
    a2 = a.banner()
    print(a2)