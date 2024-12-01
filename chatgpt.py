import openai

# 设置 API 密钥
openai.api_key = 'your-api-key-here'  # 替换为你自己的 API 密钥

def chat_with_gpt3_5(prompt):
    try:
        # 使用 openai.chat.Completion.create 调用 GPT-3.5 或 GPT-4
        response = openai.chat.Completion.create(
            model="gpt-3.5-turbo",  # 可以替换为 "gpt-4" 使用 GPT-4
            messages=[{"role": "user", "content": prompt}],  # 用户输入消息
            max_tokens=150,  # 最大生成的 token 数量
            temperature=0.7,  # 控制输出的随机性
        )

        # 提取并返回模型的回复
        message = response['choices'][0]['message']['content'].strip()
        return message

    except Exception as e:
        return f"Error: {str(e)}"

# 示例对话
user_input = "你好，今天的天气怎么样？"
response = chat_with_gpt3_5(user_input)
print(f"GPT 回复: {response}")
