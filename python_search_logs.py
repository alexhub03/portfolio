#!/usr/bin/python

import os 
import re                                                             # works with regular expressions in R



def main():

    # Request input you'd like to search for in /var/log/messages
    print("Enter keywords you'd like to search (/var/log/messages with: )")
    s=input()
    file = open("/var/log/messages", "r")                              # Uses open method with "r" read                                  
    save = open("/root/var_output.txt", 'w')        

    while True:
        for line in file:
            if re.search(s, line):                                     # Uses search method to find pattern and print output
                    print(line, file = save )                          # Note this will save the output to /root/var_output.txt silently
                    print(line)                                        # Added this line to display output
        else:
            break




if __name__ == '__main__':
    main()


def main():

    # Request input you'd like to search for in /var/log/messages
    print("Enter keywords you'd like to search (/var/log/secure with: )")
    s=input()
    file = open("/var/log/secure", "r")                              # Uses open method with "r" read                                  
    save = open("/root/var_secure_output.txt", 'a')        

    while True:
        for line in file:
            if re.search(s, line):                                     # Uses search method to find pattern and print output
                    print(line, file = save )
                    print(line)
            
        else:
            break

if __name__ == '__main__':
    main()
