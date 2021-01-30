print("Hello, please answer any question from below:")
print("Hello" or "Hi")
print("How are you")
print("Whats your name?")
print("How old are you?")
print("What do you do for a living?")
print("Quit")

while True:

    user_input = input("Enter a question from the list above:")
    user_input = user_input.lower()

    if 'Hi' in user_input or 'Hello' in user_input:
        print("Hello")
    elif user_input in 'How are you':
        print("I'm fine thanks")
    elif user_input in 'Whats your name?':
        print("Lambda.bot")
    elif user_input in 'How old are you?':
        print("I do not know when i was created")
    elif user_input in 'What do you do for a living?':
        print("I am here only to serve my master, Lambda x")
    elif user_input in 'Quit':
        break
    else:
        print("I don't understand what you're saying")
