from bs4 import BeautifulSoup
from selenium import webdriver
import json
import telegram
import time
import schedule

"""
Algoritmo de Captura de dados
"""

colorPath = []
LastCommand = ""
api_key = '5140294430:AAH0UKPWi8RKmo9I1CJyzCO_24IvJ36m8iE'
user_id = '1824713549'
bot = telegram.Bot(token=api_key)
ultima_cor = ['']


def sequenceColor(color, vezes):
    cont = 0;

    for c in colorPath:
        if c == color:
            cont = cont + 1
            if cont == int(vezes):
                return True
        else:
            return False     
    
def verifyIfNeedAlarm():
    print(colorPath)
    with open("commands\configuracao.json", encoding='utf-8') as meu_json:
        dados = json.load(meu_json)

        for i in dados:
            cor = i['cor']
            vezes = i['vezes']
            jogar = i['jogar']
            emote = i['emote']
            mensagem = i['mensagem']
            
            if sequenceColor(cor, vezes):
                # if ultima_cor[0] != colorPath[1]:
                #     bot.send_message(chat_id=user_id, text=f'Recuar, resposta incorreta.')
                #     ultima_cor.clear()
                    
                #     return
                    
                if jogar == "vermelho":
                    print(jogar)
                    bot.send_message(chat_id=user_id, text=f'Sequencia: [{colorPath[0], colorPath[1], colorPath[2], colorPath[3]}]\n{mensagem} {emote}')     
                    return
                else:
                    print(jogar)
                    bot.send_message(chat_id=user_id, text=f'Sequencia: [{colorPath[0], colorPath[1], colorPath[2], colorPath[3]}]\n{mensagem} {emote}')
                    return
     
def startVerification():
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    options.add_argument('--log-level=3')
    profile = webdriver.FirefoxProfile()
    profile.set_preference("network.http.pipelining", True)
    profile.set_preference("network.http.proxy.pipelining", True)
    profile.set_preference("network.http.pipelining.maxrequests", 8)
    profile.set_preference("content.notify.interval", 500000)
    profile.set_preference("content.notify.ontimer", True)
    profile.set_preference("content.switch.threshold", 250000)
    profile.set_preference("browser.cache.memory.capacity", 65536) # Increase the cache capacity.
    profile.set_preference("browser.startup.homepage", "about:blank")
    profile.set_preference("reader.parse-on-load.enabled", False) # Disable reader, we won't need that.
    profile.set_preference("browser.pocket.enabled", False) # Duck pocket too!
    profile.set_preference("loop.enabled", False)
    profile.set_preference("browser.chrome.toolbar_style", 1) # Text on Toolbar instead of icons
    profile.set_preference("browser.display.show_image_placeholders", False) # Don't show thumbnails on not loaded images.
    profile.set_preference("browser.display.use_document_colors", False) # Don't show document colors.
    profile.set_preference("browser.display.use_document_fonts", 0) # Don't load document fonts.
    profile.set_preference("browser.display.use_system_colors", True) # Use system colors.
    profile.set_preference("browser.formfill.enable", False) # Autofill on forms disabled.
    profile.set_preference("browser.helperApps.deleteTempFileOnExit", True) # Delete temprorary files.
    profile.set_preference("browser.shell.checkDefaultBrowser", False)
    profile.set_preference("browser.startup.homepage", "about:blank")
    profile.set_preference("browser.startup.page", 0) # blank
    profile.set_preference("browser.tabs.forceHide", True) # Disable tabs, We won't need that.
    profile.set_preference("browser.urlbar.autoFill", False) # Disable autofill on URL bar.
    profile.set_preference("browser.urlbar.autocomplete.enabled", False) # Disable autocomplete on URL bar.
    profile.set_preference("browser.urlbar.showPopup", False) # Disable list of URLs when typing on URL bar.
    profile.set_preference("browser.urlbar.showSearch", False) # Disable search bar.
    profile.set_preference("extensions.checkCompatibility", False) # Addon update disabled
    profile.set_preference("extensions.checkUpdateSecurity", False)
    profile.set_preference("extensions.update.autoUpdateEnabled", False)
    profile.set_preference("extensions.update.enabled", False)
    profile.set_preference("general.startup.browser", False)
    profile.set_preference("plugin.default_plugin_disabled", False)
    profile.set_preference("permissions.default.image", 2) # Image load disabled again
    
    browser = webdriver.Firefox(firefox_profile=profile,options=options, executable_path='./geckodriver')
    browser.get("https://blaze.com/pt/games/double")
    html = browser.page_source
    browser.quit()
    
    
    soup = BeautifulSoup(html, features="html.parser").div
    colors = soup.findAll("div", class_="sm-box")
    
    for color in colors:
        colorPath.append(color['class'][1])
        
    verifyIfNeedAlarm()
        
schedule.every(4).seconds.do(startVerification)

while 1:
    schedule.run_pending()
    colorPath.clear()
    