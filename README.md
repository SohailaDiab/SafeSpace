# Spacey 🤖💗
***By SafeSpace***

![image](https://user-images.githubusercontent.com/70928356/224434109-3485e827-12c0-4aa5-90aa-528899af97b8.png)

## Our Concern
With the advent of social media platforms, cyberbullying has become much more prevalent in our everyday lives. Therefore, a question arises: How can we ensure students' safety and emotional well-being on e-learning platforms? Some platforms are trying to deal with cyberbullying, but no one is trying to raise awareness, foster empathy, and change behavior.

A study by the University of British Columbia found that one in three teens has experienced cyberbullying, while one in five teens have cyberbullied others. The study also found that the effects of cyberbullying can be just as harmful as traditional forms of bullying, including depression, anxiety, and even suicide.<br>

## Meet Spacy!
In response to this growing problem, we have developed a solution in the form of a Discord bot called `Spacey` that can help reduce bullying behavior on the platform by encouraging empathy and spreading awareness messages. <br>

### Who is Spacy? 🤔

**Spacey** is a Discordbot that monitors the messages and images sent to Discord Server and detects toxic images and messages. If any such incident is detected, Spacey deletes the message immediately, sends a direct message to that user on your behalf to raise awareness on bullying behavior.

It also sends a message to the moderators to inform them of the behavior that was issued by the person, making it easier to identify and take appropriate action towards the user. This system is designed to create a safer, more positive environment on Discord, promoting respectful communication and discouraging bullying behavior. :) <br>

### Why Spacey?

![image](https://user-images.githubusercontent.com/70928356/224436791-795c6aa5-f4b9-48a8-8e53-d45d6310745c.png)


## Our Goal
Our goal is to help reduce the negative effects of cyberbullying on Discord and create a more inclusive, welcoming community for all users. By implementing this bot, we hope to encourage positive communication and support a culture of kindness and respect on the platform.<br>


## Set Up 
1. Use requirements.txt to install all dependent packages.<br>
2. Create a new application in the [Discord Developer Portal](https://discord.com/developers/applications) and add a bot user to it.<br>
3. Copy your bot token from the Bot tab of your application page.<br>
4. Change TOKEN variable in [config.py](https://github.com/SohailaDiab/SafeSpace/blob/main/config.py) with your bot token.<br>
5. Change moderator_id variable in [config.py](https://github.com/SohailaDiab/SafeSpace/blob/main/config.py) to your server moderator id.<br>
6. Write in cmd `python Bot.py` and make sure you in the right path.


## About Model
First, we got a ready transformer from [hugging face](https://huggingface.co/) called [toxic-bert](https://huggingface.co/unitary/toxic-bert) and this falls under the category, which is `Text Classification`. It detects toxic words, are they toxic, obscene, insult, identity_hate, threat, serve_toxic, or neutral?

After that, we used another transformer named [CLIPProcessor from openai](https://huggingface.co/openai/clip-vit-large-patch14), and this falls under the category, which is `Zero-Shot Image Classification`. We enter the input image and the Labels that we would like to classify on in order to detect the content of the images, is it bullying or not?

And by using these two models in Discord, we can identify bullying, whether in pictures or text messages, but otherwise it is ignored.


## Our Demo!
![Spacey Demo](https://user-images.githubusercontent.com/100795596/224210288-61b4bea7-e8f0-440a-991a-8c95a1a94aea.gif)

