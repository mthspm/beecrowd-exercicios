def search():
    
    while True:
        
        t = int(input())
        
        if t >= 1 and t <= 1000:
            break
        else:
            continue

    click2 = t * 2
    
    click1 = click2 * 2
    
    return(click1)

test = search()

print(test)