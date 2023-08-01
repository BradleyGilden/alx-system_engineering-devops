# Regexp?

This directory contains practice on Regex/Regexp concepts and advanced concepts

## Directory Files

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
