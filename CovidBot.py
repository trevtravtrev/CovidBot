import webbrowser
import pyautogui

from time import sleep


def open_website():
    webbrowser.open('https://mychart.hfhs.org/MyChart/Scheduling')
    sleep(4)


def click_button(button_image, delay=1):
    location = pyautogui.locateCenterOnScreen(button_image, confidence=.5)
    pyautogui.moveTo(location)
    pyautogui.click()
    sleep(delay)


def check_appointment():
    return pyautogui.locateOnScreen('no_appointment.png', confidence=.5)


def main():
    try:
        open_website()
        while True:
            click_button('covid19.png')
            click_button('no.png')
            click_button('continue.png')
            click_button('no.png')
            click_button('continue.png')
            click_button('teacher.png')
            click_button('continue.png')
            click_button('yes.png')
            click_button('continue.png')
            click_button('no.png')
            click_button('continue.png')
            click_button('no.png')
            click_button('continue.png')
            click_button('no.png')
            click_button('continue.png')
            click_button('questions.png')
            click_button('yes2.png')
            click_button('yes2.png')
            click_button('yes2.png')
            click_button('continue.png', delay=3)
            click_button('location.png')
            click_button('continue.png')

            no_appointment = check_appointment()
            if no_appointment:
                click_button('start_over.png', delay=3)
                continue
            else:
                print("Appointments found!!!")
                break

    except Exception as e:
        print(f'main error: {e}')


if __name__ == '__main__':
    main()
