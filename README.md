# SafeSpace

“Youth say that 95% of online bullying was intended as a joke and only 5% was intended to harm.”

---------------


So we decided to create this SafeSpace Bot.<br>
SafeSpace is a Discordbot that monitors the messages and images sent to Discord Server and detects abusive and bullying images and messages. If any such incident is detected, SafeSpace deletes the message immediately, sends a direct message to that user on your behalf and warns them not to bully you, and also sends a message to the moderators to inform them of the behavior that was issued by the person, even if it is repeated more than once, then the moderators are aware of this and take the appropriate action towards the person.


-------------


## Set up 
1.Install Python and the Discord.py library.<br>
2.Create a new application in the [Discord Developer Portal](https://discord.com/developers/applications) and add a bot user to it.<br>
2.Copy your bot token from the Bot tab of your application page.<br>
3.Get the api token related to the bot that you have created.<br>
4.Write your bot code using Python and the Discord.py library.<br>
5.Run your bot code and test it in your Discord server.<br>
6.Deploy your bot code to a hosting service such as Heroku or Digital Ocean to keep it running 24/7<br>


## About Model
First, we got a ready transformer from [Hugging Face](https://huggingface.co/) called [toxic-bert](https://huggingface.co/unitary/toxic-bert)and this falls under the category, which is `Text Classification`. It detects toxic words, are they toxic, obscene, insult, identity_hate, threat, serve_toxic, or neutral?

After that, we used another transformer named [CLIPProcessor from openai](https://huggingface.co/openai/clip-vit-large-patch14), and this falls under the category, which is `Zero-Shot Image Classification`. We enter the input image and the Labels that we would like to classify on in order to detect the content of the images, is it bullying or not?

And by using these two models in Discord, we can identify bullying, whether in pictures or text messages, but otherwise it is ignored.


## Our Demo
----------
