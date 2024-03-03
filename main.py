import google.generativeai as palm

api_key = 'AIzaSyA0dtcycpyZIFYKEK-N3UUphgZstk1394A'
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

print("Welcome to TutKids! How can we assist you today?")

while True:
    user_input = input("You: ")
    response = response.reply(user_input)
    print("TutKids:", response.last)
    
import uvicorn
from fastapi import FastAPI
app = FastAPI(title='MADS API')
uvicorn.run(app, host='0.0.0.0', port=8127, workers=2)
