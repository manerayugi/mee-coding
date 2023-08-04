def convert48_49_32(number):
    if int(number) == 48:
        return '0'
    elif int(number) == 49:
        return '1'
    else:
        return ''

def binaryASCIItoText(str_binary):
    # Initialize a binary string
    input_string=int(str_binary, 2);
    
    #Obtain the total number of bytes
    Total_bytes= (input_string.bit_length() +7) // 8
    
    #Convert these bits to bytes
    input_array = input_string.to_bytes(Total_bytes, "big")
    
    #Convert the bytes to an ASCII value and display it on the output screen
    ASCII_value=input_array.decode()
    # print(ASCII_value)
    return ASCII_value