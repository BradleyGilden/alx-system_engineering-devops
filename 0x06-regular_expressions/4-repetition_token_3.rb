#!/usr/bin/env ruby
# matches 'hbtn' where 't' can be have 0 or more occurences

puts ARGV[0].scan(/hbt*n/).join
