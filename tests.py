from functions.get_file_content import get_file_content

def test():
    result = get_file_content("calculator", "main.py")
    print("Result reading file:")
    print(result)
    print("")

    result = get_file_content("calculator", "pkg/calculator.py")
    print("Result reading file:")
    print(result)
    print("")

    result = get_file_content("calculator", "/bin/cat")
    print("Result reading file:")
    print(result)
    print("")

if __name__ == "__main__":
    test()
