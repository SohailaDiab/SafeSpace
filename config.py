import numpy as np

TOKEN = "MTA4MjM2NTIxOTUyMDY1OTU0Ng.GIDlaz.rasVn4mY7ecON9YgUpVadRZkPwRFmsnPlDDV7M"
PREFIX= "$"
moderator_id = 907992236522864710

hello_msg = "Hi , I hope you’re doing awesome! 😄\n "

reply_members = [
    """Which could be hurtful to your colleague 😢 Did you mean to send that?\nI’d be very happy if you rephrase it. Let’s keep our server a safe place for all 🙌""",
    
    """It could hurt the other person’s feelings ☹️\nYou might wanna reconsider the words you chose.\nLet’s aim to keep this server a safe place for all! 🙌
    """,
    
    """I know you might not realize it, but your words can have a big impact on others ☹️\nI’d be very happy if you think through what you said. Let’s try to keep this server a positive, safe place for all ❤️\n 
    """

]

def choose_msg():
    return np.random.choice(reply_members, 1)[0]

