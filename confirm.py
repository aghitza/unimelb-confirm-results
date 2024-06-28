import argparse
import csv
import os


def find_file_or_quit(fname):
    if not os.path.exists(fname):
        print("Cannot find file %s" % fname)
        exit(-1)


def diff(loc, rem, verbose=False):
    with open(loc) as csvfile:
        readr = csv.reader(csvfile)
        local_data = dict()
        count = 0
        for row in readr:
            if count == 1:
                id_col = row.index('Student Id')
                name_col = row.index('Student Name')
                mark_col = row.index('Mark')
            elif count > 1:
                local_data[row[id_col]] = [row[mark_col], row[name_col], False]
            count += 1

    with open(rem) as txtfile:
        for row in txtfile:
            lst = row.split()
            id = lst[0][:-1]
            mark = lst[-4]
            name = ' '.join(lst[1:-4])
            if id not in local_data:
                print('conflict between')
                print('  local:  does not exist')
                print('  remote: %s %s mark %s' %(id, name, mark))
            else:
                local_data[id][2] = True
                if mark != local_data[id][0]:
                    print('conflict between')
                    print('  local:  %s %s mark %s' %(id, local_data[id][1], local_data[id][0]))
                    print('  remote: %s %s mark %s' %(id, name, mark))
                elif verbose:
                    print(row)

    for id in local_data:
        if local_data[id][2] == False:
            print('%s %s (mark %s) exists locally but not remotely' %(id, local_data[id][1], local_data[id][0]))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', dest='local', help='name of csv file with local data')
    parser.add_argument('-r', dest='remote', help='name of txt file with remote data')
    parser.add_argument('-v', dest='verbose', action='count', help='verbose mode (list records that agree as well as those that do not)')
    args = parser.parse_args()

    if args.local is None:
        print("You have to specify a csv file with local data")
    else:
        find_file_or_quit(args.local)
    if args.remote is None:
        print("You have to specify a txt file with remote data")
    else:
        find_file_or_quit(args.remote)

    if args.verbose is None:
        verbose = False
    else:
        verbose = True

    diff(args.local, args.remote, verbose)


if __name__ == "__main__":
    main()
