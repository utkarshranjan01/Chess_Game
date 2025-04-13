import socket
import threading
import time
from errno import ECONNRESET, EPIPE

server_connected=0
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sleep_counter1=0 
sleep_counter2=0
sleep_counter3=0
opponent_color=0

turn_played=0
opponent_turn_played=0

total_moves_when_opponent_played=0
def server_join():
    global server_connected, client, sleep_counter1
    while(True):
        if (sleep_counter1==10):
            time.sleep(0)
            sleep_counter1=0
        sleep_counter1+=1

        if(server_connected==0):
            try:
                # Connecting to server
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.connect(('127.0.0.1', 9999))
                server_connected=1
            except:
                server_connected=0

server_connection_thread = threading.Thread(target=server_join, daemon=True)
server_connection_thread.start()

message=''
message_content=''

opponent_joined=0
your_color=0
start_selection=0
selected_color=0
selection_done=0

mouse_x1_coordinate=-1
mouse_y1_coordinate=-1
mouse_x2_coordinate=-1
mouse_y2_coordinate=-1

final_selected_color=0
final_opponent_color=0

opponent_in_menu=0

# Function to continuously send a message to the server
def send_active_connections_request():
    global server_connected, your_color, start_selection, sleep_counter2
    while True:  # Check if it needs to stop
        if (sleep_counter2==10):
            time.sleep(0)
            sleep_counter2=0
        sleep_counter2+=1
        if (server_connected==1):
                time.sleep(5)
                message = "3^%&^5768>[]&|"
                try:
                    client.send(message.encode('ascii'))
                except ConnectionRefusedError:
                    server_connected=0
                    your_color=0
                    start_selection=0
                    # Handle connection refusal
                except ConnectionResetError:
                    server_connected=0
                    your_color=0
                    start_selection=0
                    # Handle connection reset
                except BrokenPipeError:
                    server_connected=0
                    your_color=0
                    start_selection=0
                    # Handle broken connection
                except OSError as e:
                    # if e.errno == ETIMEDOUT:
                    #     print("Timeout occurred while waiting for data.")
                    #     # Handle timeout but commented it as it might automatically reconnect so pointless is adding overlay of reconnecting
                    if e.errno in (ECONNRESET, EPIPE):
                        server_connected=0
                        your_color=0
                        start_selection=0
                        # Handle graceful closure
                    # if e.errno == ETIMEDOUT:
                    #     server_connected=0
                    #     # Handle timeout


# Starting a new thread for sending active connections requests to the server
active_connections_thread = threading.Thread(target=send_active_connections_request, daemon=True)
active_connections_thread.start()

numbers_str=[]
click_event1=-1
click_event2=-1
click_event3=-1
click_event4=-1

prev_total_moves=0
move_made_by_opponent=-1

# Listening to Server
def receive():
    global your_color, opponent_joined, server_connected, start_selection, sleep_counter3, opponent_color, selection_done, selected_color, start_time, countdown_time, total_moves, numbers_str, move_made_by_opponent, prev_total_moves, total_moves_when_opponent_played, click_event1, click_event2, click_event3, click_event4, reset_pressed_opponent, game_end, sound_end, reset_allowed, opponent_gamemode, opponent_game_end
    while True:
        if (sleep_counter3==10):
            time.sleep(0)
            sleep_counter3=0
        sleep_counter3+=1
        if (server_connected==1):
            try:
                # Receive Message From Server
                data = client.recv(1024).decode('ascii')
                if (len(data)!=0):
                    messages = data.split("|")
                    # Basically if your the first to join you are white and if you are second to join you are black
                    for message in messages:
                        if message == '1':
                            opponent_joined=0
                            # your_color=2
                            start_selection=0
                            selection_done=0
                            selected_color=0
                            opponent_color=0
                            start_time=-1
                            countdown_time=5

                        elif message == '2':
                            opponent_joined=1
                            # your_color=1
                            if (selection_done==0):
                                start_selection=1
                        
                        elif message== 'Player : 1':
                            opponent_color=1
                        
                        elif message== 'Player : 2':
                            opponent_color=2
                        
                        elif message== 'Player : 0':
                            opponent_color=0
                        
                        elif message=='reset':
                            reset_pressed_opponent=1
                            game_end=1
                            sound_end.play()
                            reset_allowed=1

                        elif message=='earlyexit':
                            opponent_color=0
                            selected_color=0

                        elif message=='endscreen':
                            opponent_game_end=1

                        elif message=='endscreen0':
                            opponent_game_end=0

                        elif message=='game1':
                            opponent_gamemode=1

                        elif message=='game2':
                            opponent_gamemode=2

                        elif message=='game0':
                            opponent_gamemode=0

                        elif message.startswith("mouse"):
                            numbers_str = message.split(",")
                            numbers_str[0] = numbers_str[0][6:]
                            numbers_str[0]=int(numbers_str[0])
                            numbers_str[1]=int(numbers_str[1])
                            numbers_str[2]=int(numbers_str[2])
                            numbers_str[3]=int(numbers_str[3])

                            if selection_done==1:
                                click_event1=(numbers_str[0], numbers_str[1])
                                click_event2=(numbers_str[2], numbers_str[3])

                
            except ConnectionRefusedError:
                    server_connected=0
                    your_color=0
                    start_selection=0
                    # Handle connection refusal
            except ConnectionResetError:
                server_connected=0
                your_color=0
                start_selection=0
                # Handle connection reset
            except BrokenPipeError:
                server_connected=0
                your_color=0
                start_selection=0
                # Handle broken connection
            except OSError as e:
                if e.errno in (ECONNRESET, EPIPE):
                    server_connected=0
                    your_color=0
                    start_selection=0
                    # Handle graceful closure
                # if e.errno == ETIMEDOUT:
                #         server_connected=0
                #         # Handle timeout

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive, daemon=True)
receive_thread.start()

# Sending Messages To Server
def write(event=None):
    global message_content, server_connected, your_color, start_selection
    if (server_connected==1):
        # message_content = message_entry.get()
        try:
            if message_content != '':  # ensures non-empty messages
                message=message_content
                client.send(message.encode('ascii'))

        except ConnectionRefusedError:
            server_connected=0
            your_color=0
            start_selection=0
            # Handle connection refusal
        except ConnectionResetError:
            server_connected=0
            your_color=0
            start_selection=0
            # Handle connection reset
        except BrokenPipeError:
            server_connected=0
            your_color=0
            start_selection=0
            # Handle broken connection
        except OSError as e:
            if e.errno in (ECONNRESET, EPIPE):
                server_connected=0
                your_color=0
                start_selection=0
                # Handle graceful closure
            # if e.errno == ETIMEDOUT:
            #             server_connected=0
            #             # Handle timeout
