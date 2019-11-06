# importing libraries
from socket import *
import os
import time
from custom_logger import custom_logger
from result_display import displaying_results

# init_dir
text_file = 'output.txt'
log_dir = 'server.log'
version_control_dir = ''
real_time_yolo_prediction_dir = ''

# logger_init
logger = custom_logger(log_dir=log_dir)
logger.info('------------------------------------------------------------------------------------')
logger.info('logger created')

# socket_init
sock = socket()
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
logger.info('socket created')

# shell command to execute
version_control_cmd = 'git pull'
real_time_yolo_prediction_cmd = ''
start_video_recording_cmd = ''
logger.info('commands inititalised')

# defining server properties
port = 9002
logger.info('port set : {}'.format(port))

# starting server and binding it with the IP address of the client
sock.bind(('',port))
sock.listen(5)
logger.info('sockey is open for connections')

try:
    logger.debug('Excahnging data between server and client')
    # flag = True
    while True:
        connection, address = sock.accept()
        logger.info('Connection established: {}'.format(address))

        task_to_perform = bytes.decode(connection.recv(1024)).strip()
        print(task_to_perform)
        # flag = False
        if task_to_perform.split(' ')[0] == 'record_video':
            logger.info('Activity logged: video_recording')
            height = task_to_perform.split(' ')[1]
            width = task_to_perform.split(' ')[2]
            fps = task_to_perform.split(' ')[3]
            # os.system(start_video_recording_cmd)

        elif task_to_perform == 'real_time_result':
            logger.info('Activity logged: real_time_analysis')
            os.system(real_time_yolo_prediction_cmd)

        elif task_to_perform == 'show_result':
            logger.info('Activity logged: displaying result')
            values = displaying_results(text_file)
            print(values)
            connection.send(bytes('realTime_{}_{}_{}_{}'.format(values[0],values[1],values[2],values[3]),'utf-8'))
            # connection.send(bytes('realTimeResult_','utf-8'))
            # connection.send(bytes(values[0]+'_','utf-8'))
            # connection.send(bytes(values[1]+'_','utf-8'))
            # connection.send(bytes(values[2]+'_','utf-8'))
            # connection.send(bytes(values[3],'utf-8'))



        elif task_to_perform == 'version_control':
            logger.info('Activity logged: version_control')
            # os.chdir(version_control_dir)
            # os.system(version_control_cmd)

        else:
            logger.info('command terminated')


except Exception as error:
    logger.error(error)
    print(error)