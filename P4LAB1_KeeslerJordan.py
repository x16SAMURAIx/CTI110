user_text = input()

def main():
    count = 0
    for text in user_text:
        if not(text in " .,!"):
            count +=1
    print(count)

main()
