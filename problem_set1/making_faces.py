def emoji_convert(input):
    return input.replace(':)', '🙂').replace(':(', '🙁')

def main():
    user_input = input("Enter a sad face: ")
    result = emoji_convert(user_input)
    print(result)
    
if __name__ == "__main__":
    main()
