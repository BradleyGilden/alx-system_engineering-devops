#!/usr/bin/env ruby
# match 'h{character}tn' where character must be 1 or no instances of 'b'

puts ARGV[0].scan(/hb?tn/).join
