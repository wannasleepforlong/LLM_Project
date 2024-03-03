import uvicorn
from fastapi import FastAPI

app = FastAPI()

import google.generativeai as palm


with open("palm_api.txt") as f:
    api_key = f.read()
     
palm.configure(api_key=api_key)

prompt = 'I need help with my studies. Can TutKids assist me with tutoring services?'
examples = [
    ('Hello TutKids!', 'Hi there! How can we help you today?'),
    ('What subjects do you offer?', 'We offer tutoring services in various subjects, including math, science, and language arts.'),
    ('How does TutKids work?', 'TutKids provides personalized tutoring sessions. You can schedule a session, and our qualified tutors will assist you with your studies.'),
    ('I encountered an error', 'I apologize for the inconvenience. Please contact our support at 111-909090 for assistance with any errors.'),
    ('How can I get help?', 'If you need help, you can reach our support team at 111-909090 or by sending an email to support@tutkids.com.'),
    ('Tell me more about your tutors', 'Our tutors are highly qualified professionals with expertise in various subjects. They are dedicated to helping students succeed in their studies.'),
]

response = palm.chat(messages=prompt, temperature=0.2, context='Chatting with TutKids', examples=examples)

@app.get("/")
def read_root():
    return {"message": "Welcome to TutKids! How can we assist you today?"}

@app.get("/chat/{user_input}")
def get_chat_response(user_input: str):
    global response
    try:
        response = response.reply(user_input)
        return {"response": response.last}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
