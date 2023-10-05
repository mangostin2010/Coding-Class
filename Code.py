# OPENAI 라이브러리를 가져옴.
import openai

# 자신의 API키를 사용
openai.api_key = "자신의 api key"

# 메시지를 보관하는 리스트를 생성
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
]

# while True 문은 파이썬에서 '항상 반복하기'이다. 
while True:
    # 전에 배운 input 함수를 사용하여 사용자의 질문을 받는다
    user_content = input("user : ")

    # 'messages'라는 리스트에 사용자의 질문과 아래와 같은 형식의 데이터를 넣는다 
    messages.append({"role": "user", "content": user_content})

    # 굳이 몰라도 되는 부분. OpenAI의 GPT-3.5-turbo 모델에게 사용자의 질문을 보내는 코드  
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    # GPT-3.5-turbo 코드에서 답변이 오는데 이 답변은 JSON(존슨) 형식이다. 그래서 존슨 형식에서 'content'라는 부분만 가져온다. 이는 존슨형식의 답변에서 오직 챗봇의 답변만 가져온다는 말이다.
    assistant_content = completion.choices[0].message["content"].strip()

    # GPT-3.5-turbo의 답변을 messages 리스트에 저장
    messages.append({"role": "assistant", "content": assistant_content})

    #GPT의 답변을 'GPT : ' 라는 문구를 앞에 넣구 출력
    print("GPT : ", assistant_content)

