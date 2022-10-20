import telebot
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

bot = telebot.TeleBot("5773818973:AAHZ2-Nf8anGiL7dNeqI2AZAjIWq-SF6JGc")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hi there, {0.first_name} ! Select a function from the menu to get started.".format(message.from_user))


@bot.message_handler(commands=['sv'])
def search_videos(message):
    msg = bot.send_message(message.chat.id, "Please, enter the title of the video you are looking for")
    bot.register_next_step_handler(msg, search)


@bot.message_handler(commands=['sc'])
def search_channel(message):
    msg = bot.send_message(message.chat.id, "Please, enter the title of the youtube channel you are looking for")
    bot.register_next_step_handler(msg, search_from_channel)


@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, "Did you want to search ? Select a function from the menu to get started.")


def search_from_channel(message):
    bot.send_message(message.chat.id, "Start searching...")
    driver.get(message.text + "/videos")
    videos = driver.find_elements_by_id("video-title")
    for i in range(len(videos)):
        bot.send_message(message.chat.id, videos[i].get_attribute('href'))
        if i == 2:
            break


def search(message):
    bot.send_message(message.chat.id, "Start searching...")
    video_href = "https://www.youtube.com/results?search_query=" + message.text
    driver.get(video_href)
    sleep(2)
    videos = driver.find_elements_by_id("video-title")
    for i in range(len(videos)):
        bot.send_message(message.chat.id, videos[i].get_attribute('href'))
        if i == 2:
            break


bot.polling()