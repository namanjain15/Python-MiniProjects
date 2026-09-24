# str = input("Enter the Message: ")
# words = str.split("*")

# coding = input("Do you want to code or decode the message? (Enter 'code' or 'decode'): ")

# coding = True if (coding == "code") else False

# if(coding):
#     new_words =[]
    
#     for word in words:
#         if (len(word) >=3):
#             r1 = "@#&"
#             r2 = "j$Q"
#             str_new = r1 + word[1:] + word[0] + r2
#             new_words.append(str_new)
#         else:
#             new_words.append(word[::-1])
            
#     print(" ".join(new_words))
    
# else: 
#     new_words = []
#     for word in words:
#         if(len(word) >= 3):
#             str_new = word[3:-3]
#             str_new = str_new[-1] + str_new[:-1]
#             new_words.append(str_new)
#         else:
#             new_words.append(word[::-1])
            
#     print(" ".join(new_words))


# Different approach



message = input("Enter the Message: ")

coding = input(
    "Do you want to code or decode the message? "
    "(Enter 'code' or 'decode'): "
)

# ---------------- CODING ----------------

if coding == "code":

    words = message.split(" ")
    new_words = []

    for word in words:

        if len(word) >= 3:
            r1 = "@#&"
            r2 = "j$Q"

            new_word = r1 + word[1:] + word[0] + r2
            new_words.append(new_word)

        else:
            new_words.append(word[::-1])

    # Replace spaces between words with *
    coded_message = "*".join(new_words)

    print("\nCoded Message:")
    print(coded_message)


# ---------------- DECODING ----------------

elif coding == "decode":

    # Split using * because * represents spaces
    words = message.split("*")
    new_words = []

    for word in words:

        if len(word) >= 3:
            str_new = word[3:-3]

            # Move last character back to beginning
            str_new = str_new[-1] + str_new[:-1]

            new_words.append(str_new)

        else:
            new_words.append(word[::-1])

    # Convert * back to spaces
    decoded_message = " ".join(new_words)

    print("\nDecoded Message:")
    print(decoded_message)


else:
    print("Invalid choice! Please enter 'code' or 'decode'.")

