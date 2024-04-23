def main() -> None:
    while True:
        try:    
            string = input()
            new_string = ""
            upper = True
            
            for letter in string:
                if letter == " ":
                    new_string += " "
                    continue
                if upper:
                    new_string += letter.upper()
                    upper = False
                else:
                    new_string += letter.lower()
                    upper = True
            print(new_string)
        except EOFError:
            break
        
if __name__ == "__main__":
    main()