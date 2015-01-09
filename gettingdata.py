# below is the log file look alike
# and this file saved in "nginx.log.2014-12-17-00"

"""
[Dec 17 00:00:00] [27075] [shopclues-suggest] [info] -  Initial query: stives
[Dec 17 00:00:00] [27075] [shopclues-suggest] [info] -  Input query: stives, Spell-corrected query: stives, NumSuggestions: 0, Time taken: 110 microseconds
[Dec 17 00:00:04] [27075] [shopclues-suggest] [info] -  Initial query: west<U+200B><U+200B><U+200B>jackets
[Dec 17 00:00:04] [27075] [shopclues-suggest] [info] -  Input query: west<U+200B><U+200B><U+200B>jackets, Spell-corrected query: west <U+200B>
<U+200B><U+200B> jackets, NumSuggestions: 0, Time taken: 88 microseconds
[Dec 17 00:00:05] [27075] [shopclues-suggest] [info] -  Initial query: <U+200B><U+200B><U+200B>combo offers 
[Dec 17 00:00:05] [27075] [shopclues-suggest] [info] -  Input query: <U+200B><U+200B><U+200B>combo, Spell-corrected query: <U+200B><U+200B>
<U+200B> combo offers, NumSuggestions: 10, Time taken: 164 microseconds
[Dec 17 00:00:05] [27075] [shopclues-suggest] [info] -  Initial query: <U+200B><U+200B><U+200B>combo offer
[Dec 17 00:00:05] [27075] [shopclues-suggest] [info] -  Input query: <U+200B><U+200B><U+200B>combo, Spell-corrected query: <U+200B><U+200B>
<U+200B> combo offer, NumSuggestions: 10, Time taken: 126 microseconds
[Dec 17 00:00:05] [27075] [shopclues-suggest] [info] -  Initial query: <U+200B><U+200B><U+200B>comb
[Dec 17 00:00:05] [27075] [shopclues-suggest] [info] -  Input query: <U+200B><U+200B><U+200B>comb, Spell-corrected query: <U+200B><U+200B>
<U+200B> comb, NumSuggestions: 10, Time taken: 58 microseconds
"""
# below is code to find out the  requrie data

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
