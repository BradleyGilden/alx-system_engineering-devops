#!/usr/bin/env ruby
# match 'h*n' where '*' dontates anything can go inbetween 'h' and 'n'

puts ARGV[0].scan(/h.n/).join
