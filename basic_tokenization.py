import nltk

text = "That U.S.A. poster-print costs $12.40..."

pattern = r'''(?x)
    (?:[A-Z]\.)+
    | \w+(?:-\w+)*
    | \$?\d+(?:\.\d+)?%?
    | \.\.\.
    | [][.,;"'?():-_`]
'''

result = nltk.regexp_tokenize(text, pattern)
print(result)

