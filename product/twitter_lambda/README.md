This sub project is about adding a lambda to your aws for a basic twitterbot.   

First we need to get our twitter api credentials, this is done by navigating to https://apps.twitter.com/ and 
making an app, then once that has been done you can go to "keys and Access Tokens" to request keys. Ensure your 
app has the rights to read, write, and direct messages. Generate keys and put them in our creds.json as our 
application will use them to connect to twitter as that app.

We can test our lambda function locally first before uploading it to aws, to do this source the environment then type python3.6.
'import twitter bot'
'twitter_bot.handler('','')'
We can do this because the event and context is not actually used, specific tweets are sent by sending in an os environment 
variable. Anyhow if you check twitter now there should be a tweet on your page.

Once we have ensured it works locally we want to get started with deploying our lambda to the aws cloud.

Run the deployment.sh script, this will do all the work for you, basically installs the package requirements along with source 
code and credentials and zips it all up for aws.

Navigate to lambda page, add lambda and role for it if needed, then upload the zip set handler to be twitter_bot.handler. 

Next we want to add some environment details, (optional it works fine without) I have included two possible ones tweet and debug.
If they are not empty the bot will tweet the text in "tweet" instead of a random one. If debug value is not null you will get
some extra logging showing what api keys you are using to attempt to connect.

Future work could include:
* reading a text out of the parameters fed into the handler.
* validation around if the tweet worked or not.



