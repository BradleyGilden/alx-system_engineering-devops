# Processes & Signals

This directory deals with handling processes and signals in linux

## Directory Files

* [0-what-is-my-pid](0-what-is-my-pid) - bash script that displays it's own PID
* [1-list_your_processes](1-list_your_processes) - Bash script that displays a list of currently running processes
* [2-show_your_bash_pid](2-show_your_bash_pid) - Bash script that displays bash PID without the use of pgrep
* [3-show_your_bash_pid_made_easy](3-show_your_bash_pid_made_easy) - Bash script that displays the PID, along with the process name, of processes whose name contain the word bash
* [4-to_infinity_and_beyond](4-to_infinity_and_beyond) - Bash script that displays To infinity and beyond indefinitely.
* [5-dont_stop_me_now](5-dont_stop_me_now) - Bash script that stops 4-to_infinity_and_beyond process
* [6-stop_me_if_you_can](6-stop_me_if_you_can) - Bash script that stops 4-to_infinity_and_beyond process without kill and killall
* [67-stop_me_if_you_can](67-stop_me_if_you_can) - Bash script attempts to stop 7-highlander similar to 6-stop_me_if_you_can
* [7-highlander](7-highlander) - infinite loop that prevents exiting when SIGTERM in received
* [8-beheaded_process](8-beheaded_process) - Bash script that kills 7-highlander

## Important Commands Used:

* ps
* pgrep
* pkill
* kill
* exit
* trap
