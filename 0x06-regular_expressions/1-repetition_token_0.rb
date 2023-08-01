#!/usr/bin/env ruby
# Must match 'hb{letter}n' where letter must be 2-5 't' characters

puts ARGV[0].scan(/hbt{2,5}n/).join
