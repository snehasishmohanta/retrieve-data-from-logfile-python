import re         #importing regularexpression
import sys        
file1 = sys.argv[1]  #here creating the environment to pass the argument the logfile
auto_prefix = u'\u200B'

with open(file1) as text:
        for line in text:
                date = re.match("^\[.*?]",line)     # matching the pattern to get the date
                Iq = re.match(".*?Input query[^:]*:(.*?,)", line)    #matching the pattern to get the Initial query
                Ns = re.match(".*?NumSuggestions[^:]*:(.*?,)", line)  #matching the pattern to get the NumSuggestions
                if date and Iq and Ns:
                        q = Iq.group(1)
                        q = q.decode('utf-8').replace(auto_prefix, "") #decoding the unicode
                        print date.group(0), q.encode('utf-8'), Ns.group(1) # prnting all the value
