question=int(input("How are you feeling today 1-10? "))
quote1= "The first step is you to say that you can"
quote2 = "It is going to turn out better than you ever imagined"
quote3 = "You're not lost in life, you're just early in the process"
quote4 = "Tell yourself this: The only person who can pull me down is myself and I am not going to let myself pull me down anymore."
quote5 = "You can't be done, There's still so much to do, so much to see, so much to feel, so much to say in this life"
quote6 = "Don't count the days, make the days count"
quote7 = "If you don't give up on something you truly believe in, you will find a way"
quote8 = "The strongest people are the ones who get beaten down by life, but always find a way back up."
quote9 = "If you focus on what you left behind, you will never see what lies ahead"
if question in range(1,4):
    import random
    print (random.choice([quote1, quote2, quote3, quote5]))
if question in range(4,8):
    import random
    print(random.choice([quote4, quote5, quote7, quote8, quote9]))
if question in range(8,11):
    print("Help someone who needs it today")
