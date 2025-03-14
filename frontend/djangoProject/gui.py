import os
import sys
from threading import Thread
import webview


def start_webview():
    window = webview.create_window('Minute Meet', 'http://127.0.0.1:8000/minuteMeet', confirm_close=True)
    
    def hide_scrollbars():
        window.evaluate_js("document.body.style.overflow = 'hidden';")
    
    webview.start(hide_scrollbars)
    window.closed = os._exit(0)


def start_startdjango():
    if sys.platform in ['win32', 'win64']:
        os.system("python frontend/djangoProject/manage.py runserver 127.0.0.1:8000")
    else:
        os.system("python3 frontend/djangoProject/manage.py runserver 127.0.0.1:8000")


if __name__ == '__main__':
    Thread(target=start_startdjango).start()
    start_webview()