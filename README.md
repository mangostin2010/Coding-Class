# 개요
코딩의 재미와 매력을 알아보는 시간을 가지자

## 주제
openai의 API를 사용하고 나만의 ChatGPT를 만들자

## 요구 사항
시작하기 전에 아래와 같은 코드를 터미널에서 실행해야 한다
```python
pip install openai
```
## 코드
아래는 OpenAI의 API를 사용하여 ChatGPT를 만드는 코드이다
또한 [위에서 보고 다운받을 수 있으니 참고](youtube.com)
```python
import openai

openai.api_key = "자신의 api key"

messages = []
while True:
    user_content = input("user : ")
    messages.append({"role": "user", "content": f"{user_content}"})

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    assistant_content = completion.choices[0].message["content"].strip()

    messages.append({"role": "assistant", "content": f"{assistant_content}"})

    print(f"GPT : {assistant_content}")
```
