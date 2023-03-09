import numpy as np

TOKEN = "MTA4MjM2NTIxOTUyMDY1OTU0Ng.GIDlaz.rasVn4mY7ecON9YgUpVadRZkPwRFmsnPlDDV7M"
PREFIX= "$"
moderator_id = 907992236522864710

# These are the messages sent to the user that said toxic words

hello_msg = "Hi there {name}, I hope you’re doing awesome! 😄\n "

reply_members = [
    """Which could be hurtful to your colleague 😢 Did you mean to send that?\n
       I’d be very happy if you rephrase it. Let’s keep our server a safe place for all 🙌"""
    
    """It could hurt the other person’s feelings ☹️\n
       You might wanna reconsider the words you chose.\n 
       Let’s aim to keep this server a safe place for all! 🙌
    """
    
    """I know you might not realize it, but your words can have a big impact on others ☹️\n 
       I’d be very happy if you think through what you said. Let’s try to keep this server a positive, safe place for all ❤️\n 
    """
]
    
#     """Sometimes we all say things we don't mean when we're upset, but it's important to be mindful of how our words can affect others. Let's strive to treat everyone with kindness and respect, even when we're feeling angry or frustrated. If you need support or guidance, please don't hesitate to reach out""",
    
#     """I noticed that some of your recent comments or actions may have been hurtful to others. It's important to remember that everyone deserves to be treated with kindness and respect, no matter our differences. Let's work together to create a community where everyone feels valued and supported.""",
    
#     """"Bullying can hurt everyone involved, including the person doing the bullying. If you're struggling with something, please know that there are resources and people who can help you. Let's work together to find a solution that works for everyone and create a positive, inclusive community""",
    
#     """It's never okay to make someone feel small or to put them down. Please consider how your words and actions affect those around you.""",
    
#     """It's important to remember that everyone is fighting their own battles. Let's choose compassion and understanding over judgment and criticism.""",
    
#     """Sometimes it can be hard to see the impact our words and actions have on others. Take a step back and think about the kind of energy you want to put out into the world.""",
    
#     """I know you might not realize it, but your words can have a big impact on others. So let's spread some kindness instead of negativity, and make the world a better place one message at a time!""",
    
#     """ I wanted to reach out and remind you that everyone deserves to be treated with respect and kindness, regardless of their background or beliefs. So let's focus on building each other up and spreading positivity instead of tearing each other down.""",
    
#     """ I wanted to send you a friendly reminder that we're all in this together. No matter our differences, we all deserve to be treated with respect and kindness. So let's spread some love and positivity today, and make the world a better place!""",
# ]

def choose_msg():
    return np.random.choice(reply_members, 1)[0]

