import os
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = "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"
           
client = OpenAI()

# stream = client.chat.completions.create(
#     model="gpt-3.5-turbo",
# messages=[
#                 {"role": "user", "content": "Say this is a test"},
#                 {"role": "system", "content": "Answer the question based on the context below, and if the question can't be answered based on the context, say \"I don't know\"\n\n"},
#                 {"role": "user", f"content": "Context: {context}\n\n---\n\nQuestion: {question}\nAnswer:"}
#             ],
#     stream=True,
# )

# for chunk in stream:
#     if chunk.choices[0].delta.content is not None:
#         print(chunk.choices[0].delta.content, end="")

response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Say this is a test"},
            ],
            temperature=0,
            max_tokens=1800,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None,
        )

print(response.choices[0].message.strip())