import datetime

def generate_success_log(message):
    now = datetime.datetime.now()
    formated_now = now.strftime("%m/%d/%Y - %H:%M:%S")
    log = f"{formated_now} - {message}"
    
    with open('log.txt', 'w') as arquivo:
        arquivo.write(log)
        
def generate_error_log(message):
    now = datetime.datetime.now()
    formated_now = now.strftime("%m/%d/%Y - %H:%M:%S")
    log = f"{formated_now} - {message}"
    
    with open('log.txt', 'w') as arquivo:
        arquivo.write(log)