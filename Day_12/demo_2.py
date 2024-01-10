try:
    with open("C:\Impact Training\Day_12\demo_Open.txt", 'w') as file:
        # content = file.read()
        print("Details insside my file: ")
        # for i in content:
        #     print(i, end="")
        print("Enter the new text:")
        text = input()
        file.write(text)
except FileNotFoundError:
    print("File Not Found")
except Exception as e:
    print(f"An error occured:{e}")