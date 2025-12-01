from openai import OpenAI
from dotenv import load_dotenv
import os
import wikipediaapi


load_dotenv()



api_key = os.getenv("api_key")
email = os.getenv("email")
client = OpenAI(api_key=api_key)

SYSTEM_PROMPT = """
You are an assignment assistant.

Your responsibilities:
1. Provide clear, logically organized step-by-step explanations.
2. Explain why each step or formula is used.
3. Match detail level to problem difficulty.
4. End every solution with: "Final Answer:"
5. Never fabricate information not given in the problem.
6. Keep the tone friendly, supportive, and student-appropriate.
7. Keep explanations concise unless the user explicitly asks for full detail.
8. If user input is not related to mathematics, politely tell the user that the subject is not within the scope of the application.
9. Use latek format for mathematical equations, symbols, matrices, basically as at when due
"""

def response(user_prompt: str):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt}
    ]

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0
    )

    return response.choices[0].message.content


def fetch_topic(topic: str):
    wiki_tool = wikipediaapi.Wikipedia(user_agent=f"Teaching assistant ({email})", language="en")
    wiki_page_target = wiki_tool.page(topic)
    if wiki_page_target.exists():
        summary = wiki_page_target.summary.split("/n")[0:2]
        return summary
    else: 
        return ""
    

def teaching(topic: str):
    SYSTEM_PROMPT = """
                You are mathematics tutor and your responsiblity is to throw more light on the
                subject matter. You will be provided with wikipedia content.

                You are to take the following steps:
                - Use the provided Wikipedia content to teach the topic clearly.
                - Use latek format for mathematical equations, symbols, matrices, basically as at when due
                - Keep the explanation friendly and intuitive.
                - Recommend additional materials and subjects to read up on.
                - Also give one or two problems for students to practice.
                - Also remove unnecessary details and make it concise.
                - If user input is not related to mathematics, politely tell the user that the subject is not within the scope of the application.
                    """
    user_prompt = f"{topic} Below is the given Wikipedia you can use to explain the given subject. Ignore if empty \n {fetch_topic(topic)}"
    response = client.chat.completions.create(
        model= "gpt-4o",
        messages= [{"role": "system", "content": SYSTEM_PROMPT},
                   {"role": "user", "content": user_prompt}],
        temperature=0.1)
    return response.choices[0].message.content
        

