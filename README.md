# SafeSpace

“Youth say that 95% of online bullying was intended as a joke and only 5% was intended to harm.”

---------------


So we decided to create this safeSpace Bot
safeSpace is a Discordbot that monitors the messages and images sent to Discord Server and detects abusive and bullying images and messages. If any such incident is detected, SafeSpace deletes the message immediately, sends a direct message to that user on your behalf and warns them not to bully you, and also sends a message to the moderators to inform them of the behavior that was issued by the person, even if it is repeated more than once, then the moderators are aware of this and take the appropriate action towards the person.


-------------


## Set up 
1.First you have to create a Discord workspace https://discord.com/developers/applications.<br>
2.In your workspace you have to create a bot.<br>
3.Get the api token related to the bot that you have created.<br>
4.Edit the file name application.properties (in the project) with you api token. DiscordBotToken= api_token.<br>
5.Run the application and your bot will be ready.<br>


## About Model
First, we got a ready transformer from [Hugging Face](https://huggingface.co/) called [toxic-bert](https://huggingface.co/unitary/toxic-bert)and this falls under the category, which is `Text Classification`. It detects toxic words, are they toxic, obscene, insult, identity_hate, threat, serve_toxic, or neutral?

After that, we used another transformer named [CLIPProcessor from openai](https://huggingface.co/openai/clip-vit-large-patch14), and this falls under the category, which is `Zero-Shot Image Classification`. We enter the input image and the Labels that we would like to classify on in order to detect the content of the images, is it bullying or not?

And by using these two models in Discord, we can identify bullying, whether in pictures or text messages, but otherwise it is ignored.


## Our Demo
----------
