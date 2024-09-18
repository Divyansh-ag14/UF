# ICP_Week1A: Submission by Divyansh Agarwal


# utility funtion
def bio_bot():
    print("Welcome to the Biobot!\n")
    drink = input("What is your favorite drink?\n")
    passion = input("What are you passionate about?\n")
    motto = input("What is your motto?\n")
    steps = int(input("How many steps do you walk daily?\n"))
    steps = steps*2.1*0.000189394

    print("\nHere is your personalized social media bio:\n")
    
    print(f"|{drink} Lover\U0001F913", "Passionate about " + passion + "\U0001F913", motto + "|", sep="|")
    print(f'"Walking {steps:.1f} miles daily! #exercise"')
    
bio_bot()
