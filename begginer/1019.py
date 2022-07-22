t_event = int(input())

th = int(t_event / 3600)
t_event %= 3600

tm = int(t_event / 60)
t_event %= 60

ts = int(t_event)

print('{}:{}:{}'.format(th ,tm ,ts))