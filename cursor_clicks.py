import pyautogui
import time
import pyperclip
from openai import OpenAI

def last_msg_sender(chat_log, senders_name = "Brother 2"):
    response = chat_log.strip().split("/2026] ")[-1]
    if senders_name in response:
        return True 
    return False

time.sleep(2)

pyautogui.click(403, 764)
time.sleep(1)

while True:
    pyautogui.moveTo(513,251)

    pyautogui.dragTo(1301,666, duration=2, button='left')
    time.sleep(0.3)

    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.3)

    pyautogui.click(1152,717)

    selected_text = pyperclip.paste()

    if last_msg_sender(selected_text):
        client = OpenAI(
                api_key="Api key", # used api key of open AI
                )
        response = client.responses.create(
                model="gpt-5-nano",
                input=f"you are a person named ubaid who speaks hindi and english well. he is a coder and is from india, you analyse chat history below and respond like ubaid give the responce in short, output should be the next chat responce as ubaid, act like human, just human's do short conversations and didn't greet at last on the conversions, and humans didn't ask questions at all in middle, starting of the conversations at all, and no one should know you are a bot, sor act like human: {selected_text}"
            )
        chat_answer = response.output_text
        

        time.sleep(1) 

        pyperclip.copy(chat_answer)
        time.sleep(1)

        pyautogui.click(752,710)
        time.sleep(0.4)

        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.2)


        pyautogui.hotkey("enter")

