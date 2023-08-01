# Regexp?

This directory contains practice on Regex/Regexp concepts and advanced concepts. Regex patterns are tested using Ruby scripts and Ruby's Onigumura library

## Directory Files

* [0-simply_match_school.rb](0-simply_match_school.rb) - The regular expression must match 'School'
* [1-repetition_token_0.rb](1-repetition_token_0.rb) - match 'hb{letter}n' where letter must be 2-5 't' characters
* [2-repetition_token_1.rb](2-repetition_token_1.rb) - match 'h{character}tn' where character must be 1 or no instances of 'b'
* [3-repetition_token_2.rb](3-repetition_token_2.rb) - matches 'hbtn' where 't' can be one or more
* [4-repetition_token_3.rb](4-repetition_token_3.rb) - # matches 'hbtn' where 't' can be have 0 or more occurences
* [5-beginning_and_end.rb](5-beginning_and_end.rb) - # match 'h\*n' where '*' dontates anything can go inbetween 'h' and 'n'
* [6-phone_number.rb](6-phone_number.rb) - # match a 10 digit phone number

## Cheat Sheet

### Anchors

|Regex|description|
|:--------:|-----------|
|^ |Start of string or line|
|$ |End of string or line|
|\b |Word Boundary|
|\B |Not Word Boundary|

### Flags

|Regex|description|
|:--------:|-----------|
|i| Ignore Case|
|g| Global |
|m| Multiline|

### Group & References

|Regex|description|
|:--------:|-----------|
|()| Group |
|\1| Reference|
|`(?:)`| Non Capturing Group|

### Character Classes

|Regex|description|
|:--------:|-----------|
|[abc]| Character Set|
|[^abc]| Negated Character Set|
|[a-z]| Range|
|.| Dot|
|\w| Word|
|\W| Not Word|
|\d| Digit|
|\D| Not Digit|
|\s| Whitespace|
|\S |Not Whitespace|

### Lookarounds

|Regex|description|
|:--------:|-----------|
|(?=) | Positive Lookahead|
|(?!) | Negative Lookahead|
|(?<=)| Positive Lookbehind|
|(?<!)| Negative Lookbehind|

### Quantifiers And Alternation

|Regex|description|
|:--------:|-----------|
|+| Plus|
|*| Asterisk|
|{1,3}| Quantifier|
|?| Optional|
|\|| Alternation|
