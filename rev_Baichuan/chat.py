import json
import sys
import requests


class Baichuan:
    def __init__(self, cookie: str):
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
            "Cookie": cookie,
            "Connection": "keep-alive"
        }
        self.history = []

    def ask(self, prompt: str, repetition_penalty: int = -1, temperature: int = 16, top_k: int = -1, top_p: int = -1,
            do_sample: int = -1, history: bool = True):
        payload = {"type": "input",
                   "stream": True,
                   "prompt": {
                       "data": prompt
                   },
                   "session_info": {},
                   "parameters": {
                       "repetition_penalty": repetition_penalty,
                       "temperature": temperature,
                       "top_k": top_k,
                       "top_p": top_p,
                       "max_new_tokens": -1,
                       "do_sample": do_sample,
                       "regenerate": 0
                   },
                   "history": self.history if history else [],
                   "retry": 3
                   }

        response = requests.post("https://www.baichuan-ai.com/api/chat/v1/chat", json=payload, headers=self.headers)
        response_ = response.text.split("\n")
        answer = ""
        for i in response_:
            try:
                content = json.loads(i)
                answer += content["answer"]["data"]
            except json.decoder.JSONDecodeError:
                break
            except KeyError:
                continue

        if history:
            self.history.append({"from": 0, "data": prompt})
            self.history.append({"from": 1, "data": answer})

        return answer

    def stream(self):
        try:
            while 1:
                prompt = input("You: ")
                print(self.ask(prompt))
        except KeyboardInterrupt:
            sys.exit()

