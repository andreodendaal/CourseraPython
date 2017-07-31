# performances = {'Ventriloquism':       '9:00am',
#                 'Snake Charmer':       '12:00pm',
#                 'Amazing Acrobatics':  '2:00pm',
#                 'Enchanted Elephants': '5:00pm'}
#
# schedule_file = open('schedule.txt', 'w')
#
# for key, val in performances.items():
#     schedule_file.write(key + '- ' + val + '\n')

schedule_file = open('schedule.txt', 'r')
performances = { }
for line in schedule_file:
    line.strip()
    #print(line)
    (show, time) = line.split('- ')
    print(show, time)
    performances[show] = time.strip()

schedule_file.close()
print(performances)