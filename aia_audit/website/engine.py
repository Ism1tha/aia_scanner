from flask import Flask, render_template
import logging, threading

app = Flask(__name__, static_url_path='', static_folder='./frontend/dist', template_folder="./frontend/dist")

#Import flask routes file to handle all the requests
from aia_audit.website.routes import *

class Website:

    thread = None

    def website_start(self, config):
        log = logging.getLogger('werkzeug')
        log.disabled = True
        thread = threading.Thread(target=lambda: app.run(host=config.website_address, port=config.website_port, debug=False, use_reloader=False))
        thread.setDaemon(True)
        thread.start()
        self.thread = thread
        print("[*] Website started on " + config.website_address + ":" + config.website_port + " ... Done!")