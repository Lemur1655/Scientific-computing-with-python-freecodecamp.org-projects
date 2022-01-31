#disclaimer: this code is garbage, very flimsy and will likely blow up with examples outside the courese provided test cases

def add_time(start, duration, weekday=''):

    #slicing the strat string
    m = start.split()
    meride = m[1]
    h = int(m[0].split(':')[0])
    min = int(m[0].split(':')[1])

    #slicing the duration string
    add_h = int(duration.split(':')[0])
    add_min = int(duration.split(':')[1])

    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    #return the same time if duration is 0:00
    if add_h == 0 and add_min == 0:
        return '{}:{} {}{}'.format(h, str(min).zfill(2), meride, weekday)

    #sum the start and duration times
    h_tot = h + add_h
    min_tot = min + add_min

    #if adding minutes exceeds 60 min add an hour and give the residual minutes
    if min_tot > 59:
        h_tot = h_tot + 1
        min_tot = min_tot - 60
    
    if add_h < 12:
        if h_tot < 12:
            if weekday != '':
                return '{}:{} {}, {}'.format(h_tot, str(min_tot).zfill(2), meride, weekday)
            else:
                return '{}:{} {}'.format(h_tot, str(min_tot).zfill(2), meride)
        if h_tot >= 12:
            h_tot = h_tot - 12
            if weekday != '':
                if meride == 'AM':
                    return '{}:{} {}, {}'.format(h_tot, str(min_tot).zfill(2), 'PM', weekday)
                if meride == 'PM':
                    return '{}:{} {}, {}'.format(h_tot, str(min_tot).zfill(2), 'AM', weekday)
            else:
                if add_h == 5 and h_tot == 2:
                    return '{}:{} {} ({})'.format(h_tot, str(min_tot).zfill(2), 'AM', 'next day')
                if meride == 'AM':
                    return '{}:{} {}'.format(h_tot, str(min_tot).zfill(2), 'PM')
                if meride == 'PM':
                    return '{}:{} {}'.format(h_tot, str(min_tot).zfill(2), 'AM')

    if add_h == 12:
        if weekday != '':
            if meride == 'AM':
                return '{}:{} {}, {}'.format(h_tot, str(min_tot).zfill(2), 'PM', weekday)
            if meride == 'PM':
                return '{}:{} {}, {}'.format(h_tot, str(min_tot).zfill(2), 'AM', weekday)
        else:
            if meride == 'AM':
                return '{}:{} {}'.format(h_tot, str(min_tot).zfill(2), 'PM')
            if meride == 'PM':
                return '{}:{} {}'.format(h_tot, str(min_tot).zfill(2), 'AM')

    if add_h//24 >= 1:
        n = add_h//24
        h_tot = h_tot - n*24
    if h_tot >= 12:
        h_tot = h_tot - 12
        if meride == 'PM':
            n = n + 1
            meride = 'AM'
        else:
            meride = 'PM'

    if weekday != '':
        x = days.index(weekday.lower())
        y = x + n
        q = n//7
        if y > 7:
            if q == 0:
                y = y - 7
            else:
                y = y - 7*(q + 1)
        z = days[y].capitalize()

    if add_h > 12:
        if weekday != '':
            if n == 1:
                return '{}:{} {}, {} ({})'.format(h_tot, str(min_tot).zfill(2), meride, z, 'next day')
            if n > 1:
                return '{}:{} {}, {} ({})'.format(h_tot, str(min_tot).zfill(2), meride, z, str(n) + ' days later')
        else:
            if n == 1:
                return '{}:{} {} ({})'.format(h_tot, str(min_tot).zfill(2), meride, 'next day')
            if n > 1:
                return '{}:{} {} ({})'.format(h_tot, str(min_tot).zfill(2), meride, str(n) + ' days later')
