import cryptogram_Functions as md
import time

print("This program will create an encryption for your Message in Multiple Encrypting Algorithms")

encryptions = {
    '1': md.Blake2s,
    '2': md.SHA3_256,
    '3': md.SHA3_224,
    '4': md.SHA3_384,
    '5': md.SHA224,
    '6': md.SHA3_512,
    '7': md.Blake2b,
    '8': md.SHA512,
    '9': md.SHAKE_256,
    '10': md.SHAKE_128,
    '11': md.MD5,
    '12': md.SHA256,
    '13': md.SHA1,
    '14': md.SHA384,
}

user_input = input("Enter a String You Want to Encrypt: ")

print("Now choose which encryptions you want to use:")
print("\n".join(f"[{key}] {value.__name__}" for key, value in encryptions.items()))

user_opt = input("Enter any Option: ")

selected_encryption = encryptions.get(user_opt)

if user_opt == "00":
    for key, value in encryptions.items():
        value(user_input)
        time.sleep(1)
elif selected_encryption:
    selected_encryption(user_input)
else:
    print("Wrong output")
