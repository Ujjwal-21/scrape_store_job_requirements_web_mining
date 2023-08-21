import yaml
chromeDriverPath=""
mongoDbURL=""

def readConfig():
   with open('.\\config\\config.yml', 'r') as file:
      file = yaml.safe_load(file)
      global chromeDriverPath, mongoDbURL
      chromeDriverPath = file['chromeDriverPath']
      mongoDbURL = file['mongoDbURL']

