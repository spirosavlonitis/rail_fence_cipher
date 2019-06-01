class RailFenceCipher():
    def encode_rail_fence_cipher(self, string, n):
        if string == "": return ""
        result = ""
        hop = n + n-2
        correction = 0
        i = j = 0
        c = False
        while True :
            if j < len(string):
                result += string[j]
            else:
                i += 1
                j = i
                n -= 1
                if n == 0:
                    break
                hop -=  2
                correction += 2
                result += string[j]
                c = False
            if c == False:
                j += hop if hop > 0 else correction
                c = True
            else:
                j += correction if correction > 0 else hop
                c = False
        return result

    def decode_rail_fence_cipher(self, string, n):
        result = ['0']*len(string)
        k = j = 0
        hop = 2*n - 2
        correction = 0
        while n > 0:
            c = False
            i = k
            while i < len(string):
                result[i] = string[j]
                j += 1
                if c == False:
                    i += hop if hop > 0 else correction
                    c = True
                else:
                    i += correction if correction > 0 else hop
                    c = False 
            k += 1
            n -= 1
            hop -= 2
            correction += 2
        return ''.join(result)