# rev_Baichuan
使用Python, requests，用于快速将百川智能大语言模型接入项目


## 使用
### 安装
```commandline
pip install -U rev_Baichuan
```

### 基本使用
```python
from rev_Baichuan import *
bot = Baichuan(cookie="your_cookies_here")

result = bot.ask(prompt="你好", # 要发送的内容
                 repetition_penalty=-1, # 重复惩罚系数（非必须）
                 temperature=16, # 温度系数（非必须）
                 top_k=100, # 最高返回数量（非必须）
                 top_p=0.95, # 最低返回概率（非必须）
                 do_sample=-1, # 是否采样（非必须）
                 history=True # 是否考虑上下文内容（非必须）
                 )
print(result)

# 你好，有什么我可以帮助你的吗？

bot.stream()
# You: 你好
# 你好，有什么我可以帮助你的吗？
# You:
# ......
```
#### 获取cookie
1. 前往[百川智能](https://www.baichuan-ai.com/chat)，登录你的账号；
2. 打开”开发者工具“（F12），转到”网络“，随便发条消息；
3. 找到显示为`chat`的请求；
4. 在右侧”请求标头“一栏，找到”Cookie“，将其内容完整的复制下来即可。