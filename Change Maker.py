while True:
    tot = str(input('How much change do you need?\n'))
    if tot[0] == '£':
        tot = tot[1:]
    tot = float(tot) * 100
    change = ''

    while tot >= 5000:
        tot = tot - 5000
        change = change + '£50, '
    while tot >= 2000:
        tot = tot - 2000
        change = change + '£20, '
    while tot >= 1000:
        tot = tot - 1000
        change = change + '£10, '
    while tot >= 500:
        tot = tot - 500
        change = change + '£5, '
    while tot >= 200:
        tot = tot - 200
        change = change + '£2, '
    while tot >= 100:
        tot = tot - 100
        change = change + '£1, '
    while tot >= 50:
        tot = tot - 50
        change = change + '50p, '
    while tot >= 20:
        tot = tot - 20
        change = change + '20p, '
    while tot >= 10:
        tot = tot - 10
        change = change + '10p, '
    while tot >= 5:
        tot = tot - 5
        change = change + '5p, '
    while tot >= 2:
        tot = tot - 2
        change = change + '2p, '
    while tot >= 1:
        tot = tot - 1
        change = change + '1p, '
    
    print(change)
