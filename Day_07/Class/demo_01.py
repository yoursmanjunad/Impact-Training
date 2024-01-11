test = int(input())

while test != 0:
    staff = int(input())
    ranks = list(map(int, input().split()))

    if staff != len(ranks):
        print("Not allowed")
    else:
        total_gifts = staff  # Each staff must receive at least one gift

        # Distribute additional gifts based on rank
        total_gifts += sum(ranks) // staff

        print(total_gifts)

    test -= 1
