user_input = input("What is your base string?")

def fuzz_generator(target_input):
    
    fuzz_vectors = []
    payload_list = []

    bad_char = (input(f"What character would you like to use for your buffer overflow? ")) 
    count = int(input("Enter the number of bufffer text you would like included: "))

    for i in range(1, count + 1): 
        overflow = bad_char * (i * 2)
        fuzz_vectors.append(overflow) 

    for vector in fuzz_vectors:
        mutated_string = f"{target_input}{vector}"
        payload_list.append(mutated_string)  
    
    return (payload_list)

my_payloads = (fuzz_generator(user_input))
print (len(my_payloads))
print (my_payloads) 

save_choice = input("Would you like to save the payloads to a text file? yes or no?")
if save_choice.lower() == "yes":
    with open("payloads.txt", "w") as file:
        for payload in my_payloads:
            file.write(payload + "\n") 
    print("Payloads saved to payloads.txt")
else:    print("Payloads not saved.")