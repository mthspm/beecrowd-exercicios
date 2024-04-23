def corvo_westeros() -> None:
    blinks = 0
    int_value = 0
    while True:
        entry = input()
        
        match entry:
            case "caw caw":
                print(int_value)
                blinks += 1
                int_value = 0
                if blinks == 3: break
            case _:
                bin_int = entry.replace("-", "0").replace("*", "1")
                int_value += int(bin_int, base=2)
                
        
if __name__ == "__main__":
    corvo_westeros()