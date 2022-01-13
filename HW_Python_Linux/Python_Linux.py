import names
import time
from datetime import datetime

file_path = '/home/u_23_22/names.txt'

while True:

    with open(file_path, 'a+') as file_txt:
        now = datetime.now()

        user_name = names.get_full_name()
        dt_string = now.strftime('%d/%m/%Y %H:%M:%S')

        result_str = user_name + ' -- ' + dt_string + '\n'

        file_txt.write(result_str)

    time.sleep(0.5)