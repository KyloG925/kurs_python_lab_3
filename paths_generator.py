import argparse
import os

def genPaths():
    Months = ['styczen', 'luty', 'marzec', 'kwiecien',
                    'maj', 'czerwiec', 'lipiec', 'sierpien', 
                    'wrzesien', 'pazdziernik', 'listopad', 'grudzien']
    Days = ['pn', 'wt', 'sr', 'czw', 'pt', 'sb', 'nd']
    Days_full = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']
    time_iterator = 0
    months, days, times, operation, file_type = parse_arguments()
    paths = []
    for i in range(len(months)):
        month = months[i]
        if '-' in days[i]:
            day = days[i].split('-')
            firstId = Days.index(day[0])
            secondId = Days.index(day[1])
            while firstId <= secondId:
                final_path = os.path.join(os.getcwd(), month, Days_full[firstId], nexttime(time_iterator))
                paths.append(final_path)
                firstId += 1
                time_iterator += 1
        else:
            final_path = os.path.join(os.getcwd(), month, Days_full[Days.index(days[i])], nexttime(time_iterator))
            paths.append(final_path)
            time_iterator += 1
    for path in paths:
        os.makedirs(path, exist_ok = True)
    return paths
                
def nexttime(time):
    if time >= len(times):
        return 'rano'
    elif times[time] == 'r':
        return 'rano'
    else:
        return 'wieczorem'