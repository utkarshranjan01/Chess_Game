import socket
import time
from errno import ECONNRESET, EPIPE
from src.variables import *

gs, ntw = None, None

def init_globals(game_state, network_manager):
    global gs, ntw
    gs = game_state
    ntw = network_manager

def receive():
    receive2(gs, ntw)
    
# def write():
#     write2(gs, ntw)

def server_join():
    server_join2(gs, ntw)

def send_active_connections_request():
    send_active_connections_request2(gs, ntw)

def receive2(gs, ntw):
    # Listening to Server
    sleep_counter3=0
    while True:
        if (sleep_counter3==10):
            time.sleep(0)
            sleep_counter3=0
        sleep_counter3+=1
        if (ntw.server_connected==1):
            try:
                # Receive Message From Server
                data = ntw.client.recv(1024).decode('ascii')
                if (len(data)!=0):
                    messages = data.split("|")

                    for message in messages:
                        if message == '1':
                            if(not gs.reset_allowed): # This condition is so first reset the current game before joining a new game as if the other player closes the entire game and rejoins and first play still did not reset
                                gs.opponent_joined=0
                                gs.start_selection=0
                                gs.selection_done=0
                                gs.selected_color=0
                                gs.opponent_color=0
                                gs.start_time=-1
                                gs.countdown_time=3

                        elif message == '2':
                            if(not gs.reset_allowed): # This condition is so first reset the current game before joining a new game as if the other player closes the entire game and rejoins and first play still did not reset
                                gs.opponent_joined=1
                                if (gs.selection_done==0):
                                    gs.start_selection=1
                        
                        elif message== 'Player : 1':
                            gs.opponent_color=1
                        
                        elif message== 'Player : 2':
                            gs.opponent_color=2
                        
                        elif message== 'Player : 0':
                            gs.opponent_color=0
                        
                        elif message=='reset':
                            gs.reset_pressed_opponent=1
                            gs.game_end=1
                            sound_end.play()
                            gs.reset_allowed=1

                        elif message=='earlyexit':
                            gs.opponent_color=0
                            gs.selected_color=0

                        elif message=='endscreen':
                            gs.opponent_game_end=1

                        elif message=='endscreen0':
                            gs.opponent_game_end=0

                        elif message=='game1':
                            gs.opponent_gamemode=1

                        elif message=='game2':
                            gs.opponent_gamemode=2

                        elif message=='game0':
                            gs.opponent_gamemode=0

                        elif message.startswith("mouse"):
                            gs.numbers_str = message.split(",")
                            gs.numbers_str[0] = gs.numbers_str[0][6:]
                            gs.numbers_str[0]=int(gs.numbers_str[0])
                            gs.numbers_str[1]=int(gs.numbers_str[1])
                            gs.numbers_str[2]=int(gs.numbers_str[2])
                            gs.numbers_str[3]=int(gs.numbers_str[3])

                            if gs.selection_done==1:
                                gs.click_event1=(gs.numbers_str[0], gs.numbers_str[1])
                                gs.click_event2=(gs.numbers_str[2], gs.numbers_str[3])

                
            except ConnectionRefusedError:
                ntw.server_connected=0
                gs.your_color=0
                gs.start_selection=0
                # Handle connection refusal
            except ConnectionResetError:
                ntw.server_connected=0
                gs.your_color=0
                gs.start_selection=0
                # Handle connection reset
            except BrokenPipeError:
                ntw.server_connected=0
                gs.your_color=0
                gs.start_selection=0
                # Handle broken connection
            except OSError as e:
                if e.errno in (ECONNRESET, EPIPE):
                    ntw.server_connected=0
                    gs.your_color=0
                    gs.start_selection=0
                    # Handle graceful closure
                # if e.errno == ETIMEDOUT:
                #         ntw.server_connected=0
                #         # Handle timeout

# def write2(gs, event=None):
def write(gs, ntw, event=None):
    # Sending Messages To Server

    if (ntw.server_connected==1):
        # message_content = message_entry.get()
        try:
            if gs.message_content != '':  # ensures non-empty messages
                message=gs.message_content
                ntw.client.send(message.encode('ascii'))

        except ConnectionRefusedError:
            ntw.server_connected=0
            gs.your_color=0
            gs.start_selection=0
            # Handle connection refusal
        except ConnectionResetError:
            ntw.server_connected=0
            gs.your_color=0
            gs.start_selection=0
            # Handle connection reset
        except BrokenPipeError:
            ntw.server_connected=0
            gs.your_color=0
            gs.start_selection=0
            # Handle broken connection
        except OSError as e:
            if e.errno in (ECONNRESET, EPIPE):
                ntw.server_connected=0
                gs.your_color=0
                gs.start_selection=0
                # Handle graceful closure
            # if e.errno == ETIMEDOUT:
            #             ntw.server_connected=0
            #             # Handle timeout


def server_join2(gs, ntw):

    sleep_counter1=0
    while(True):
        if (sleep_counter1==10):
            time.sleep(0)
            sleep_counter1=0
        sleep_counter1+=1
        # print(sleep_counter1)

        if(ntw.server_connected==0):
            try:
                # Connecting to server
                ntw.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                ntw.client.connect((ip_address, 9999))
                ntw.server_connected=1
            except:
                ntw.server_connected=0

def send_active_connections_request2(gs, ntw):
    # Function to continuously send a message to the server

    sleep_counter2=0
    while True:  # Check if it needs to stop
        if (sleep_counter2==10):
            time.sleep(0)
            sleep_counter2=0
        sleep_counter2+=1
        if (ntw.server_connected==1):
                time.sleep(5)
                message = "3^%&^5768>[]&|"
                try:
                    ntw.client.send(message.encode('ascii'))
                except ConnectionRefusedError:
                    ntw.server_connected=0
                    gs.your_color=0
                    gs.start_selection=0
                    # Handle connection refusal
                except ConnectionResetError:
                    ntw.server_connected=0
                    gs.your_color=0
                    gs.start_selection=0
                    # Handle connection reset
                except BrokenPipeError:
                    ntw.server_connected=0
                    gs.your_color=0
                    gs.start_selection=0
                    # Handle broken connection
                except OSError as e:
                    # if e.errno == ETIMEDOUT:
                    #     print("Timeout occurred while waiting for data.")
                    #     # Handle timeout but commented it as it might automatically reconnect so pointless is adding overlay of reconnecting
                    if e.errno in (ECONNRESET, EPIPE):
                        ntw.server_connected=0
                        gs.your_color=0
                        gs.start_selection=0
                        # Handle graceful closure
                    # if e.errno == ETIMEDOUT:
                    #     ntw.server_connected=0
                    #     # Handle timeout

def color_selection_message(gs, ntw, write):
    if gs.selection_done==0 and gs.gamemode==2 and gs.opponent_gamemode==2:
        if gs.selected_color==1:
            gs.message_content="Player : 1|"
            write(gs, ntw)
        if gs.selected_color==2:
            gs.message_content="Player : 2|"
            write(gs, ntw)

