#!/usr/bin/env ruby
# matches 'hbtn' where 't' can be one or more

puts ARGV[0].scan(/hbt+n/).join
