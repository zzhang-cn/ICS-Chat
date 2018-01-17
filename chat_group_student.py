# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 09:58:31 2015

@author: zhengzhang
"""
S_ALONE = 0
S_TALKING = 1

#==============================================================================
# Member class: per user -- her name and status
#==============================================================================
class Member:
    
    def __init__(self, name):
        self.name = name
        self.state = S_ALONE
        
    def get_name(self):
        return
        
    def set_name(self, name):
        return
        
    def get_state(self):
        return
        
    def set_state(self ,state):
        return

#==============================================================================
# Group class:
# member fields: 
#   - An array of items, each a Member class
#   - A dictionary that keeps who is a chat group
# member functions:
#	- join: first time in
#	- leave: leave the system, and the group
#	- list_my_peers: who is in chatting with me?
#	- list_all: who is in the system, and the chat groups
#	- connect: connect to a peer in a chat group, and become part of the group
#	- disconnect: leave the chat group but stay in the system
#==============================================================================

class Group:
    
    def __init__(self):
        self.members = []
        self.chat_grps = {}
        
    def join(self, name):
        return
        
    def leave(self, name):
        return
        
    def connect(self, me, peer):
        return
        
    def disconnect(self, me):
        return
        
    def list_all(self, name):
        return
        
    def list_me(self, name):
        return
    
    
    
