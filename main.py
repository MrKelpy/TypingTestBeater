from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import time


def lock():

    # Locks the program flow in place

    while True:
        time.sleep(1000)


with Chrome() as browser:
    browser.get("https://typing-speed-test.aoeu.eu/")
    browser.maximize_window()

    # Prepares the browser to answer the typing test

    # Agrees with the cookies
    try:
        agree = browser.find_element_by_class_name("css-flk0bs")
        agree.click()
    except:
        pass

    # Scrolls down to the challenge box
    border = browser.find_element_by_id("border")
    _ = border.location_once_scrolled_into_view

    # Gets all the words and text_input place
    text_input = browser.find_element_by_id("input")

    # Parses out all the next words with BeautifulSoup4 html.parser
    soup = BeautifulSoup(browser.page_source, "html.parser")
    all_words = [word.text for word in soup.find_all(class_="nextword")]
    all_words.insert(0, browser.find_element_by_id("currentword").text)

    # Types in the words until the test finishes
    for index, current_word in enumerate(all_words):

        print(f"Word {index+1}: {current_word}")
        current_word += ' '  # Adds a space to the current word for the site to recognise the end of typing
        text_input.send_keys(current_word)  # Types in the current word

    lock()  # This lock may be removed, but the browser will close upon finishing.
