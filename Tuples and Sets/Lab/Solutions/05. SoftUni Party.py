
def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())
    return lines


def input_to_lit_command(end_command):
    lines = []
    while True:
        command = input()
        if command == end_command:
            break
        lines.append(command)
    return lines


def is_vip_guest(guest):
    return guest[0].isdigit()


def separator(guests):
    vip_guests = []
    normal_guest = []
    for guest in guests:
        if is_vip_guest(guest):
            vip_guests.append(guest)
        else:
            normal_guest.append(guest)

    return (sorted(vip_guests), sorted(normal_guest))


def print_result(guests):
    print(len(guests))
    (vip_guests, normal_guest) = separator(guests)
    for guest in vip_guests:
        print(guest)
    for guest in normal_guest:
        print(guest)



n = int(input())
reservations = input_to_list(n)
arrived_guest = input_to_lit_command('END')

not_arrived = set(reservations).difference(arrived_guest)

print_result(not_arrived)