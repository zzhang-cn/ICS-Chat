
from chat_client_class import *

def main():
    import argparse
    parser = argparse.ArgumentParser(description='chat client argument')
    parser.add_argument('-d', type=str, default=None)
    args = parser.parse_args()
    print(args)

    client = Client(args)
    client.run_chat()

main()
