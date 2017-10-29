
s = 'hello world'

def lastwordlen(s):
    s = s[::-1]
    if ' ' in s:
            if s[0] == ' ':
                return 0
            else:
                lastWordLen = len(s[:s.index[' ']])
                return lastWordLen
    else:
        return 0
    
lastwordlen(s)
