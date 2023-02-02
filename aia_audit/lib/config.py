import os

class Config:

    website_address = "0.0.0.0"
    website_port = "5000"
    website_password = ""
    configured = "no"

    def __init__(self):
        self.config_start()

    def config_start(self):
        #Check if config file exists and if not create it
        if not os.path.isfile("aia_audit/data/config.json"):
            with open("aia_audit/data/config.json", "w") as config_file:
                config_file.write("{ \"website_address\": \"" + self.website_address + "\", \"website_port\": \"" + self.website_port + "\", \"website_password\": \"" + self.website_password + "\", \"configured\": \"" + self.configured + "\" }")
        else:
            with open("aia_audit/data/config.json", "r") as config_file:
                config = config_file.read()
                #Extract values from json file
                self.website_address = config.split("\"website_address\": \"")[1].split("\",")[0]
                self.website_port = config.split("\"website_port\": \"")[1].split("\",")[0]
                self.website_password = config.split("\"website_password\": \"")[1].split("\",")[0]
                self.configured = config.split("\"configured\": \"")[1].split("\",")[0]
        