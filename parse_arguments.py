import argparse
    
# Funkcja parsująca argumenty
# zwraca krotkę (months, days, times, operation, file_type)
# months - lista miesięcy
# days - lista zakresów dni
# times - lista rano/wieczorem
# operation - operacja tworzenia/usuwania w postaci chara 't' lub 'u'
# file_type - typ pliku csv/json w postaci stringa 'csv' lub 'json'
def parse_arguments():
    miesiace = ['styczen', 'luty', 'marzec', 'kwiecien', 
                'maj', 'czerwiec', 'lipiec', 'sierpien', 
                'wrzesien', 'pazdziernik', 'listopad', 'grudzien']

    parser = argparse.ArgumentParser(description="Generate paths based on given parameters.")
    parser.add_argument('-m', '--months', nargs='+', choices=miesiace, required=True, help="List of months")
    parser.add_argument('-d', '--days', nargs='+', required=True, help="List of day ranges")
    parser.add_argument('-t', '--times', nargs='*', choices=['r','w'], default=['r'], help="List of times (r for rano, w for wieczorem)")
    parser.add_argument('-o', '--operation', choices=['t', 'u'], required=True, help="Operation: t for tworzenie (create), u for usuwanie (delete)")
    parser.add_argument('-c', '--csv', action='store_true', help="File type: csv")   
    parser.add_argument('-j', '--json', action='store_true', help="File type: json")

    args = parser.parse_args()

    if len(args.days) != len(args.months):
        raise argparse.ArgumentTypeError("Number of days must be equal to number of months.")
    
    if len(args.times) > len(args.days) * len(args.months):
        raise argparse.ArgumentTypeError("Number of times of day must less or equal to product of number of months and number of days.")

    if (not args.csv and not args.json) or (args.csv and args.json):
        raise argparse.ArgumentTypeError("Exactly one file type must be specified.")
    
    file_type = 'csv' if args.csv else 'json'

    week_days = ['pn', 'wt', 'sr', 'czw', 'pt', 'sb', 'nd']

    for day in args.days:
        if '-' in day:
            days = day.split('-')
            if days[0] not in week_days or days[1] not in week_days or days[0] == days[1]:
                raise argparse.ArgumentTypeError("Invalid day range.")
        elif day not in week_days:
            raise argparse.ArgumentTypeError("Invalid day.")
            

    return args.months, args.days, args.times, args.operation, file_type

if __name__ == '__main__':
    print(parse_arguments())
    months, days, times, operation, file_type = parse_arguments()