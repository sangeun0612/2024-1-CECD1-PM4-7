# Assist content생성
import pandas as pd
import os
import sys
folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'public'))
temp = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'tuning'))
sys.path.append(temp)
from tuning.convert import complete_xlsx_to_jsonl


def makeAssistFile(PROMPT: str, conversation_history: list):
    system_content = []
    user_content = []
    assist_content = []

    for i in range(1, len(conversation_history), 2):
        system_content.append(PROMPT)
        user_content.append(conversation_history[i]['content'])
        if i + 1 < len(conversation_history):
            assist_content.append(conversation_history[i + 1]['content'])
        else:
            assist_content.append("")

    df = pd.DataFrame({
        "System content": system_content,
        "User content": user_content,
        "Assistant content": assist_content
    })

    filename = input("파일 이름: ")
    filePath = os.path.join(folder_path, filename + ".xlsx")
    df.to_excel(filePath, index=False)
    complete_xlsx_to_jsonl(filePath)
    print(f"대화모델용 학습데이터 {filename}.jsonl 저장 완료.")

