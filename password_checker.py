"""
Created By - Prathamesh Sanjay Karne
Date - 8 July 2026
Time - 1430Hrs
Name - Basic Password Strength Verifier 
"""

password = input("Enter your password [Max Special Characters to Use = 8]: ")

length = len(password)

check1 = password.count("!")
check2 = password.count("@")
check3 = password.count("#")
check4 = password.count("$")
check5 = password.count("%")
check6 = password.count("&")
check7 = password.count("_") 
check8 = password.count(" ")
final_check = check1 + check2 + check3 + check4 + check5 + check6 + check7
    
class main:

    def length_check():
        if length < 8:
            return False
        else:
            return True

    def finalize(final_check):
        if final_check < 1:
            return "Weak"
        elif final_check <= 8:
            return False
        else:
            return "Strong"


    if not length_check():
        print("Password Is Too Short")
    else:
        print("Password Length Is Accepted..........")

        if check8 > 0:
            print("But, Spaces are not allowed")
        else:
            strength = finalize(final_check)
            
            if strength == "Strong":
                print(f"And Password Works. So, Go On with '{password}' !")
            elif not strength:
                print("But, Why you have added a password with <= 8 special characters. Change It")
            else:
                print("But, Try Again by adding more special character as Password is Weak.")