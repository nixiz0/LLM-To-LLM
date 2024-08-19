import requests
import json


def start_llm_chat(name_model, llm_model, prompt, conversation_history, visual_talk):
    url = "http://localhost:11434/api/chat"
    headers = {'Content-Type': "application/json",}
    
    def talk(text):
        visual_talk.speak(text)

    def beforeSay(response):
        return response

    def say(response):
        if len(response) == 0:
            return
        talk(beforeSay(response))

    def generate_response(prompt, chat_history):
        if len(prompt) == 0:
            return "", chat_history

        full_prompt = []
        for i in chat_history:
            full_prompt.append({
                "role": "user",
                "content": i[0]
            })
            full_prompt.append({
                "role": "assistant",
                "content": i[1]
            })
        full_prompt.append({
            "role": "user",
            "content": prompt
        })

        data = {
            "model": llm_model,
            "stream": True,
            "messages": full_prompt,
        }

        response = requests.post(url, headers=headers, data=json.dumps(data), stream=True)
        if response.status_code == 200:
            print(f'\n\n{name_model}:\n', end='')
            all_response = ''
            this_response = ''
            for line in response.iter_lines():
                if line:
                    jsonData = json.loads(line)
                    this_response += jsonData["message"]['content']
                    if '.' in this_response or '?' in this_response or '!' in this_response:
                        print(f'{this_response}', end='')
                        say(this_response)
                        all_response += this_response
                        this_response = ''
            if len(this_response) > 0:
                print(f'{this_response}', end='')
                say(this_response)
                all_response += this_response
                this_response = ''
            chat_history.append((prompt, all_response))
            return all_response, chat_history
        else:
            return "Error: Unable to fetch response", chat_history
    
    response, conversation_history = generate_response(prompt, conversation_history)
    return response, conversation_history