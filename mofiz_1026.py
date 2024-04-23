def mofiz() -> None:
    while True:
        try:
            int_A, int_B = map(int, input().split())
            bin_A, bin_B = format(int_A, 'b'), format(int_B, 'b')
            len_A, len_B = len(bin_A), len(bin_B)
            if len_A > len_B:
                bin_B = '0'*(len_A-len_B) + bin_B
            else:
                bin_A = '0'*(len_B-len_A) + bin_A
            ans = ''
            for i in range(len(bin_A)):
                ans += str(int(bin_A[i])^int(bin_B[i])) # XOR operation
            print(int(ans, 2))
        except EOFError:
            break
        
if __name__ == "__main__":
    mofiz()