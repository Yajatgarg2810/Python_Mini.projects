def email_slicer():
    email=input("Enter your email: ")

    # index= email.index("@")
    # username=email[:index]
    # domain=email[index+1:]

    username=email[:email.index("@")]
    domain=email[email.index("@")+1:]

    print(f"Your email is {username} and domain is {domain}")

email_slicer()