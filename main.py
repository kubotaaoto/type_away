from generate_words import generate_words 
from count_chars import count_num_chars
from record import load_total_chars, set_total_chars

def main():
    try:
        print("---Enter to generate next line, ctrl + c to quit---")
        total_chars = load_total_chars()
        while True:
            words_typed = input(generate_words())
            num_chars = count_num_chars(words_typed)
            total_chars += num_chars
            set_total_chars(total_chars)
    except KeyboardInterrupt:
        print("\n-----------------------------------------")
        print(f"total chars: {total_chars} (appx. {total_chars / 4} words)")
main()