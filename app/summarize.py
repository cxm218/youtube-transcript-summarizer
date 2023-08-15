
#import json
#from pprint import pprint
#from statistics import mean

#import requests
#from plotly.express import line



# from getpass import getpass

# OPENAI_API_KEY = getpass("Please provide your OpenAI API Key:")


# import openai

# openai.api_key = OPENAI_API_KEY



#import openai
#import os
#from dotenv import load_dotenv
#from app.alpha import API_KEY
#
#from openai import ChatCompletion
#
#openai.api_key = API_KEY
#
##chat_text should be transcript from the pull audio file
#chat_text = "Before we start learning about Python or software development, it will be helpful for us to achieve a basic level of familiarity with the command-line. Throughout the semester, we will be using the command-line to navigate and manage our computer's filesystem, execute Python scripts, and perform other important tasks using various command-line utilities (CLIs). Commands can differ based on which operating system and command-line application you're using, but all students are encouraged to learn the prevalent unix-style commands: On Mac OS, the default Terminal application will allow students to use unix-style commands. On Windows OS, the default Command Prompt application uses different commands, but installing the Git Bash application will allow students to use unix-style commands."
#
##audience = input('Who is the summary for?')
#
#audience = input('Select who the summary is for: \n A) A programmer \n B) A college student \n C) A 2nd grader \n')
#
#if audience.upper() == 'A':
#    audience = "a programmer"
#elif audience.upper() == 'B':
#    audience = "a college student"
#elif audience.upper() == 'C':
#    audience = "a 2nd grader"
#else:
#    print('INVALID RESPONSE. PLEASE TRY AGAIN.')
#
##summary_length = input('How long do you want the summary?')
#summary_length = input('Select the type of summary you want: \n A) 1 sentence \n B) 5 bullet points \n C) An outline \n')
#
#if summary_length.upper() == 'A':
#    summary_length = "1 sentence"
#elif summary_length.upper() == 'B':
#    summary_length = "5 bullet points"
#elif summary_length.upper() == 'C':
#    summary_length = "an outline"
#else:
#    print('INVALID RESPONSE. PLEASE TRY AGAIN.')
#
#
#chat_completion = ChatCompletion.create(model="gpt-3.5-turbo", messages=[
#    {"role": "user", "content": f"Summarize this for {audience} text in {summary_length}: {chat_text}"}
#])
#
## print the chat completion
#print('SUMMARY:')
#print(chat_completion.choices[0].message.content)
#print('END SUMMARY.')
