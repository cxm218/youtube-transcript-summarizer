
#import json
#from pprint import pprint
#from statistics import mean

#import requests
#from plotly.express import line



# from getpass import getpass

# OPENAI_API_KEY = getpass("Please provide your OpenAI API Key:")


# import openai

# openai.api_key = OPENAI_API_KEY



import openai
from openai import ChatCompletion

def get_user_input(prompt):
    response = input(prompt)
    return response

def get_audience():
    audience = get_user_input('Select who the summary is for:\nA) A programmer\nB) A college student\nC) A 2nd grader\n')
    if audience.upper() == 'A':
        return "a programmer"
    elif audience.upper() == 'B':
        return "a college student"
    elif audience.upper() == 'C':
        return "a 2nd grader"
    else:
        print('INVALID RESPONSE. PLEASE TRY AGAIN.')
        return get_audience()

def get_summary_length():
    summary_length = get_user_input('Select the type of summary you want:\nA) 1 sentence\nB) 5 bullet points\nC) An outline\n')
    if summary_length.upper() == 'A':
        return "1 sentence"
    elif summary_length.upper() == 'B':
        return "5 bullet points"
    elif summary_length.upper() == 'C':
        return "an outline"
    else:
        print('INVALID RESPONSE. PLEASE TRY AGAIN.')
        return get_summary_length()

def generate_summary(chat_text, audience, summary_length):
    completion = ChatCompletion.create(model="gpt-3.5-turbo", messages=[
        {"role": "user", "content": f"Summarize this for {audience} text in {summary_length}: {chat_text}"}
    ])
    return completion.choices[0].message.content

if __name__ == "__main__":
    chat_text = "Before we start learning about Python or software development, it will be helpful for us to achieve a basic level of familiarity with the command-line. Throughout the semester, we will be using the command-line to navigate and manage our computer's filesystem, execute Python scripts, and perform other important tasks using various command-line utilities (CLIs). Commands can differ based on which operating system and command-line application you're using, but all students are encouraged to learn the prevalent unix-style commands: On Mac OS, the default Terminal application will allow students to use unix-style commands. On Windows OS, the default Command Prompt application uses different commands, but installing the Git Bash application will allow students to use unix-style commands."
    
    audience = get_audience()
    summary_length = get_summary_length()

    summary = generate_summary(chat_text, audience, summary_length)
    
    print('SUMMARY:')
    print(summary)
    print('END SUMMARY.')

