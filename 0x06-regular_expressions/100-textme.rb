#!/usr/bin/env ruby
# # output [SENDER], [RECEIVER], [FLAGS] from the log file [text_messages.log]

sender = ARGV[0].scan(/(?<=\[from:)([a-zA-Z]+|\+?[0-9]+)(?=\])/).join
receiver = ARGV[0].scan(/(?<=\[to:)([a-zA-Z]+|\+?[0-9]+)(?=\])/).join
flags = ARGV[0].scan(
    /(?<=\[flags:)-?[0-1]:-?[0-1]:-?[0-1]:-?[0-1]:-?[0-1](?=\])/).join

puts "#{sender}, #{receiver}, #{flags}"
