from bakery import assert_equal

# Copy over existing code from earlier parts of the project

def encrypt_text(message:str,amount:int)->str:
    '''
    Purpose: 
        This function will intake a message that is a string and 
        using the other arguement that is an integer will give a new string based on the ASCII
        This new string is meant to represent an encrypted message. The function does this 
        by taking the message, using the ord function to convert the characters to integer values
        then using the amount changes the integer value. The new value is then ran through the 
        chr function to proudce a different character
    
    Arguments: 
        message: a string value that represents the message
        amount: the value that will be used to determine the new message
    
    Return:
        returns "encrypted" which is a new string that has been ran through 
        changes based on the amount
    '''
    ord_list=[]
    message_list=[]
    encrypted=""
    for character in message:
        value=ord(character)
        ord_list.append(value)
    for character in ord_list:
        rotated=((character+amount-32)%94+32)
        if rotated < 48:
            message_list.append(rotated)
            message_list.append(126)
        else: 
            message_list.append(rotated)
    for letter in message_list:
        new=chr(letter)
        encrypted=encrypted+new
    return encrypted
    
assert_equal(encrypt_text("Alex",1),"Bmfy")
assert_equal(encrypt_text("Emely",10),"Owov%~")
assert_equal(encrypt_text("Ciani",27),"^&~|+~&~")
                       
# 2) Define decrypt_text

def decrypt_text(message:str,amount:int)->str:
    '''
    Purpose: 
        This function will intake a message that is a string and 
        using the other arguement that is an integer will give a new string based on the ASCII
        This new string is meant to represent the decoding of an
        encrypted message by using the ord function to change the characters to integers
        using the integers manipulating by the amount then using the chr function on
        the new value
    
    Arguments: 
        message: a string value that represents the secret message
        amount: the value that will be used to determine the decrypted message
    
    Return:
        returns "decrypted" which is a new string that has been ran through 
        changes based on the amount to reverse the effects of the 
        encrypt_text function
    '''
    
    ord_list=[]
    message_list=[]
    decrypted=""
    for character in message:
        if not character=="~":
            value=ord(character)
            ord_list.append(value)
    for character in ord_list:
        if character > 126:
            unrotated=((character-amount-32))
            message_list.append(unrotated)
        if character <= 126 :
            unrotated=((character-amount))
            message_list.append(unrotated)
    for letter in message_list:
        if letter <= 32:
            letter=letter+94
        new=chr(letter)
        if new=="~":
            new=new.replace("~"," ")
        decrypted=decrypted+new
    return decrypted

assert_equal(decrypt_text(';<=>?', 10),"12345")
assert_equal(decrypt_text("Bmfy",1),"Alex")
assert_equal(decrypt_text("Owov%~",10),"Emely")
assert_equal(decrypt_text("^&~|+~&~",27),"Ciani")
assert_equal(decrypt_text("9",0),"9")

# 3) Define hash_text
def hash_text(message:str,base:int,hash_size:int)->int:
    '''
    Purpose: 
        This function intakes a message as a string, a base which is an integer
        and a hash size which is another integer in order to produce a "hash" which is 
        a unique integer that represents the message. It can do this by using the ord funtion
        for each character and manipulating the ord value with the given base. Then summing the 
        values and finally dividing by the desired hash size
    
    Arguements:
        message: a string that represents some message 
        base: an integer that represents a specfic value to be used
              for the hashing
        hash_size: an integer that helps condense the number down to 
              a chunck that is more usable
              
    Returns:
       This function returns an integer that is unique for every combination
       of characters in a string
       
    '''
    ord_list=[]
    hash_list=[]
    count=-1
    for character in message:
        ord_list.append(ord(character))
    for character in ord_list:
        count=count+1
        new_value=(count+base)**(character)
        hash_list.append(new_value)
    total = sum(hash_list)
    return (total%hash_size)

assert_equal(hash_text("Hello",31,1000000000),590934605)
assert_equal(hash_text("A",1,10*2),1)
assert_equal(hash_text("Alex",11,100),36)
        
# 4) Define main
def main():
    '''
    Purpose: 
        This function allows a user to input whether they want to encrypt a message or
    decrpty a message. Depending on the input the function can either encrypt a message
    and hash the message, returning both the coded message and hash OR if the user inputs
    decrypt the function can decrypt the message, returning the message if the user has the correct hash
    if they input the incorrect hash then return an error
    
    Arguements: 
        The function intakes an input from the user. It will require an initial input telling the 
        function which path to take
        if the user chooses to encrypt: the funtion will require one addition input of a message
        if the user chooses to decrypt: the function will require two additional inputs, 
        one being the message and the other being the hash.
    
    Returns:
        if the user chooses encrypt: the return will be a string representing the encrypted version of 
        a message and will also return the messages hash value
        if the user chooses decrpyt: the return will be a string representing the decrypted version
        of the message if the inputted hash values match. otherwise an error message with return
        if the user does not give valid inputs the function returns an error message
    
    '''
    
    print("Hello how can I help you?")
    user_input=input()
    user_input=user_input.lower()
    
    if user_input=="encrypt":
        print("Please input your message!")
        user_message=input()
        encrypted_message=encrypt_text(user_message,10)
        hashed_message=hash_text(user_message,31,10**9)
        return print(encrypted_message, hashed_message)
    
    if user_input=="decrypt":
        print("Please input your message!")
        secret_message=input()
        decrypted_message=decrypt_text(secret_message,10)
        print("Please input your hash")
        expected_hash=input()
        expected_hash=int(expected_hash)
        actual_hash=hash_text(decrypted_message,31,10**9)
        if expected_hash==actual_hash:
            return print(decrypted_message)
        else: 
            return print("error")
    else:
        return print("Error")
    
main()
