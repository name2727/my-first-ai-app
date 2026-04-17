import requests

# 请替换成你自己的真实 API Key
api_key = "sk-14f508359c934348b33f0d7be2fb52e1"

url = "https://api.deepseek.com/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

print("聊天机器人已启动，输入问题后按回车，输入 '退出' 结束程序")

while True:
    question = input("\n你：")
    if question == "退出":
        print("再见！")
        break
    if question.strip() == "":
        print("请输入有效问题。")
        continue

    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": question}],
        "stream": False
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        answer = result["choices"][0]["message"]["content"]
        print(f"AI：{answer}")
    else:
        print(f"出错了，状态码：{response.status_code}")
        print("详细信息：", response.text)