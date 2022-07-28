import json

with open('resources/password.json') as file:
    data = json.load(file)

class locator(object):
    url = "https://aszendit.woffu.com/v2/login"
    user = data['encryptedUser']
    password = data['encryptedPassword']
    user_box = "/html/body/div/div/section/div[1]/div/div/form/div/div/div/div/div[2]/div/input"
    pass_box = "/html/body/div/div/section/div[1]/form/div/div/div[1]/div/div[2]/div/input"
    siguiente_button = "/html/body/div/div/section/div[1]/div/div/form/div/div/button"
    iniciar_sesion_button = "/html/body/div/div/section/div[1]/form/div/div/button"
    day_color_element = ".fa-sign-in"
    iframe = "/html/body/div[1]/div[2]/main/div/div/div/iframe"
    workday_color = "rgba(88, 213, 110, 1)"
    button_clocking = "/html/body/div[2]/div/div/div[2]/div[2]/div/div[1]/div/span/div/span/div/button"