#!/usr/bin/expect -f
spawn ssh student@172.27.26.188 
expect ": "
send "cs641\n"
expect ": "
send "sha4269\r"
expect ": "
send "feb431a65\r"
expect ": "
send "6\r"

expect "> "
send "exit2\r"



expect "> "
send "exit4\r"



expect "> "
send "exit3\r"



expect "> "
send "exit1\r"



expect "> "
send "exit4\r"



expect "> "
send "exit4\r"



expect "> "
send "exit2\r"



expect "> "
send "exit2\r"



expect "> "
send "exit1\r"



expect "> "
send "read\r"

expect "> "
