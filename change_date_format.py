#pass 56 minutes

import dateutil.parser
from datetime import datetime

def change_date_format(dates):
    x = []
    for i in dates:
        r = dateutil.parser.parse(i)
        x.append(r.strftime('%Y%m%d'))
    return [x]

dates = change_date_format(["2010/03/30", "15/12/2016", "11-15-2012", "20130720"])
print(*dates, sep='\n')
