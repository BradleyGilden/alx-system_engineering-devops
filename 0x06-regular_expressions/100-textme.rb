#!/usr/bin/env ruby
# # output [SENDER], [RECEIVER], [FLAGS] from the log file [text_messages.log]

puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
