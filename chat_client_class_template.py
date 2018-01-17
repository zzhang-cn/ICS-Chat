import time
import socket
import select
import sys
import string
from chat_utils import *
import threading

class Client:
    def __init__(self):
        ##DO NOT CHANGE THIS METHOD
        #this method initialises the Client class
        #name of the local user
        self.name=''
        #name of the user chatting with local user
        self.peer = ''
        #all messages inserted by local user
        self.console_input=[]
        #state of the client 
        self.state = S_OFFLINE
        #messages to be displayed on the screen
        #messages from the chat system
        self.system_msg = ''
        #messages inserted by local user
        self.local_msg = ''
        #messages received from remote user
        self.peer_msg = ''
        
    def quit(self):
        ##DO NOT CHANGE THIS METHOD
        #this method cleans up when the chat exits
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()
        
    def get_name(self):
        ##DO NOT CHANGE THIS METHOD
        #getter for local user name
        return self.name
        
    def init_chat(self):
        ##DO NOT CHANGE THIS METHOD
        #this method initialises the chat application
        #open socket to communicate with server
        self.socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM )
        self.socket.connect(SERVER)
        #create a new thread that reads messages from the local user and saves them to self.local_msg
        reading_thread = threading.Thread(target=self.read_input)
        reading_thread.daemon = True
        reading_thread.start()
        
    def send(self, msg):
        ##DO NOT CHANGE THIS METHOD
        #this method sends a message to the server through the socket
        mysend(self.socket, msg)
        
    def recv(self):
        ##DO NOT CHANGE THIS METHOD
        #this method receives a message from the server through the socket
        return myrecv(self.socket)
        
    def get_msgs(self):
        ##DO NOT CHANGE THIS METHOD
        #this method checks for loacl and remote messages and puts them in the corresponding lists
        #check for local messages
        my_msg = ''
        if len(self.console_input) > 0:
            my_msg = self.console_input.pop(0)
        #check for messages from server
        read, write, error=select.select([self.socket], [], [], 0)
        peer_msg = []
        peer_code = M_UNDEF       
        if self.socket in read:
            peer_msg = self.recv()
            peer_code = peer_msg[0]
            peer_msg = peer_msg[1:]
        return my_msg, peer_code, peer_msg
        
    def output(self):
        ##DO NOT CHANGE THIS METHOD
        #print all system messages and all peer messages 
        if len(self.peer_msg) > 0:
            print(self.peer_msg)
            self.peer_msg = ''
        if len(self.system_msg) > 0:
            print(self.system_msg)
            self.system_msg = ''
                
    def login(self):
        my_msg, peer_code, peer_msg = self.get_msgs()
#############IMPLEMENT THIS METHOD
##        it performs the login if the local user has input any text (check value of my_msg)
##        it returns True if the login was successful and False otherwise       
##        the login is performed by sending a login message to server, using self.send (see protocol)
##        the client waits for a response M_LOGIN+'ok'
##        if OK, the client has to change state to S_LOGGEDIN
#############################
        return False


    def connect_to(self, peer):
        ##DO NOT CHANGE THIS METHOD
        ##this method allows the local user to connect to a remote user
        ##this is done by sending to the server a M_CONNECT message plus the user name of the friend
        ##the server will reply 'ok' if connection was successful
        ##'busy' if friend was already chatting to someone else
        ##'hey you' if the friend name is the name of the local user and no_user if the friend is not online
        msg = M_CONNECT + peer
        self.send(msg)
        response = self.recv()
        if response == (M_CONNECT+'ok'):
            self.peer = peer
            self.system_msg += 'You are connected with '+self.peer + '\n'
            return (True)
        elif response == (M_CONNECT+'busy'):
            self.system_msg += 'User is busy. Please try again later\n'
        elif response == (M_CONNECT+'hey you'):
            self.system_msg += 'Cannot talk to yourself (sick)\n'
        else:
            self.system_msg += 'User is not online, try again later\n'
        return(False)

    def disconnect(self):
        ##DO NOT CHANGE THIS METHOD
        #this method disconnects the user from the friend, by sending a diconnect request
        msg = M_DISCONNECT
        self.send(msg)
        self.system_msg += 'You are disconnected from ' + self.peer + '\n'
        self.peer = ''
        
    def read_input(self):
        ##DO NOT CHANGE THIS METHOD
        #this method runs in teh bakground and collects all user input in self.console_input
        while True:     
            text=sys.stdin.readline()[:-1]
            self.console_input.append(text) # no need for lock, append is thread safe

    def print_instructions(self):
        ##DO NOT CHANGE THIS METHOD
        #this method prints instructions to the user
        self.system_msg += "\n++++ Choose one of the following commands\n"
        self.system_msg += "who: to find out who else are there\n"
        self.system_msg += "c _peer_: to connect to the _peer_ and chat\n"
        self.system_msg += "? _term_: to search your chat logs where _term_ appears\n"
        self.system_msg += "p _#_: to get number <#> sonnet\n"
        self.system_msg += "q: to leave the chat system\n"

    def run_chat(self):
        ##DO NOT CHANGE THIS METHOD
        #this method is the main method of the chat, it runs the chat
        #first initialise
        self.init_chat()
        self.system_msg+='Welcome to ICS chat\n'
        self.system_msg+='Please enter your name: '
        self.output()
        #then allow user to login
        while self.login() != True:
            self.output()
        self.system_msg+='Welcome, ' + self.get_name() + '!'
        self.output()
        #then allow user to use the chat - either connect to a peer, or search, or listen to poems
        while self.state != S_OFFLINE:
            self.proc()      
            self.output()
            time.sleep(CHAT_WAIT)
        self.quit()

#==============================================================================
# main processing loop
#==============================================================================
    def proc(self):
        my_msg, peer_code, peer_msg = self.get_msgs()#get local and peer messages
#==============================================================================
# Once logged in, do a few things: get peer listing, connect, search
# And, of course, if you are so bored, just go
#==============================================================================
#############IMPLEMENT THIS METHOD
##        check in which state the client is (can be either S_LOGGEDIN or S_CHATTING)
##        in each state, check if my_msg and peer_msg have messages
##        depending on the user input and peer input decide what to do
##        use the state diagram and the protocol to decide what to do at each step
##        use the methods above if you need to receive a message, connect to a peer,
##        disconnect from apeer or print instructions.
##        you have the first case for the state S_LOGGEDIN as example below
##        follow that to fill in the rest of the code
#############################
        
        if self.state == S_LOGGEDIN:
            #the user is logged in but not connected to a friend
            #check first if there is any input from the user
            if len(my_msg) > 0:
                #there is input, the user can enter 5 types of messages, so we need to check which one they chose
                if my_msg == 'q':
                    #user wants to quit (already implemented)
                    self.system_msg += 'See you next time!\n'
                    self.state = S_OFFLINE
                elif my_msg == 'who':
                    #user wants to see who is online (already implemented)
                    self.send(M_LIST)
                    logged_in = self.recv()
                    self.system_msg += 'Here are all the users in the system:\n'
                    guys = logged_in.split('.')
                    for g in guys:
                        if g == self.name:
                            self.system_msg += g + '(you)\n'
                        else:
                            self.system_msg += g + '\n'
                elif my_msg[0] == 'c':
                    #user wants to connect to a friend
#############IMPLEMENT THIS ELIF STATEMENT
##                    extract the name of the friend
##                    call the method connect_to to connect to friend
##                    depending on the output of the connect_to method, change the state
##                    to S_CONNECTED and add a confirmation message to self.system_msg
##                    or add an error message to  self.system_msg
##########################################                    
                    pass
                elif my_msg[0] == '?':
                    #user is performing a search
#############IMPLEMENT THIS ELIF STATEMENT
##                    extract the term to search
##                    send a M_SEARCH message to server (check the protocol for format)
##                    receive from server the search results
##                    add results (if any) or an error message (if no results) to self.system_msg
##########################################
                    pass
                elif my_msg[0] == 'p':
                    #user wants a sonnet
#############IMPLEMENT THIS ELIF STATEMENT
##                    extract the sonnet to ask for
##                    send a M_POEM message to server (check the protocol for format)
##                    receive from server the poem text
##                    add poem text (if any) or an error message (if no text) to self.system_msg
########################################## 
                    pass
                else:
                    #the user inserted some text that does not match the 5 supported commands
                    self.system_msg += 'supported command: who, c \'peer\', ? \'term\', p _#_, q\n\n'
            #finished with localuser input, check if any message from a peer
            if len(peer_msg) > 0:
                #there is a message, the only possibility is an M_CONNECT from a friend
                if peer_code == M_CONNECT:
#############IMPLEMENT THIS IF STATEMENT
##                    extract the name of the friend and put it into self.peer
##                    prepare a message for the local user saying they are connected to their friend
##                    add the message to self.system_msg and change state to S_CHATTING
########################################## 
                    pass
#==============================================================================
# Start chatting, 'bye' for quit
#==============================================================================
        elif self.state == S_CHATTING: ##the second possible state
            if len(my_msg) > 0:     # local message waiting to be sent
#############IMPLEMENT THIS IF STATEMENT
##                    send an M_EXCHNAGE message with my_msg as content
##                    check if my_msg is 'bye' and in that case disconnect the user (call self.disconnect)
##########################################                 
                pass
            if len(peer_msg) > 0:    # peer message to be processed
#############IMPLEMENT THIS IF STATEMENT
##                    add the new message to self.peer_msg
##                    check if peer_msg is 'bye' and in that case change the state to S_LOGGEDIN
##########################################                 
                pass
            if self.state == S_LOGGEDIN:
                #print instructions if the user was disconnected
                self.print_instructions()
#==============================================================================
# invalid state                       
#==============================================================================
        else:
            self.system_msg += 'How did you wind up here??\n'
            
        return
