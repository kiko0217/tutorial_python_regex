import re

test_string = '123abc456789abc123ABC'

print("\ttest")
print(r"\ttest")
pattern= re.compile(r'abc')
matches = pattern.finditer(test_string)

for match in matches:
    print(match)

matches_other = re.finditer(r'abc', test_string)
for match_other in matches_other:
    print(match_other)

matcher_findall = pattern.findall(test_string)
for match_findall in matcher_findall:
    print(match_findall)

match_abc = pattern.match(test_string)
print(match_abc) # output none because it not first string

pattern_match = re.compile(r'123')
match_match = pattern_match.match(test_string)
print(match_match)

match_abc_search = pattern.search(test_string)
print(match_abc_search)

matches = pattern.finditer(test_string)
for match in matches:
    print(match.span(), match.start(), match.end(), match.group())

""" all meta characters: . ^ $ * + ? { } [ ] \ | ( )

. any character (except newline character)
 """
pattern_with_dot = re.compile(r'.')
matches_with_dot = pattern_with_dot.finditer(test_string)
for match in matches_with_dot:
    print(match.span(), match.start(), match.end(), match.group())