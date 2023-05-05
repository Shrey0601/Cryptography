#!/usr/bin/expect -f
spawn ssh student@172.27.26.188  
expect ": "
send "cs641\n"
expect ": "
send "sha4269\n"
expect ": "
send "feb431a65\n"
expect ": "
send "4\n"
expect "> "
send "read\n"
set inputfile "inpair.txt"
set filepointer [open "$inputfile" r]
set inputpairs [read $filepointer]
foreach input $inputpairs {
    expect "> "
    send "$input\n"
    expect "> "
    send "c\n"
}