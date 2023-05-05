
#!/usr/bin/expect -f
spawn ssh student@172.27.26.188 
expect ": "
send "cs641\n"
expect ": "
send "sha4269\r"
expect ": "
send "feb431a65\r"
expect ": "
send "5\r"
expect "> "
send "go\r"

expect "> "
send "wave\r"

expect "> "
send "dive\r"

expect "> "
send "go\r"

expect "> "
send "read\r"

set fd "text.txt"
set fp [open "$fd" r]
set data [read $fp]
foreach line $data {
    expect "> "
    send "$line\r"
    expect "> "
    send "c\r"
}