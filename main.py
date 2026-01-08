from generate_words import generate_words 

def main():
    try:
        print("---Enter to generate next line, ctrl + c to quit---")
        while True:
            words_typed = input(generate_words())
    except KeyboardInterrupt:
        print("\n--------------------------------------------")
main()