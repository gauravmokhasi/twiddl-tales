"""
@author = gauravmokhasi
File reads character names, dialogues and time delays from one file, and posts them to slack using bot names and webhooks from another file.
"""
import json
import requests
import re
import time

def read_file(file_name):
    return open(file_name, 'r')

def slack_post(dialogue, url):
    """
    posts dialogues to slack using correct account
    """
    slack_data = {'text': "" + dialogue}
    response = requests.post(
        url, data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}
    )

def create_dict(raw_webhooks):
    webhooks_dict = {}

    for line in raw_webhooks:
        array_text = line.split(",")
        webhooks_dict[array_text[0].lower()] = array_text[1]

    return webhooks_dict

webhook_binding_file = read_file(input("Enter webhook binding file name: "))
dialogue_file = read_file(input("Enter dialogue file name: "))

raw_webhooks = webhook_binding_file.readlines()
webhooks_dict = create_dict(raw_webhooks)
webhook_binding_file.close()

raw_text = dialogue_file.readlines()

for line in raw_text:
    array_text = line.split("~")
    url = webhooks_dict[array_text[0].lower()]

    slack_post("" + array_text[1], url)
    time.sleep(int(array_text[2]))

dialogue_file.close()
