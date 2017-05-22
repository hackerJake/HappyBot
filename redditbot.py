import praw

bot = praw.Reddit(user_agent='HappyBot v0.1',
                  client_id='Kum-y-9S3wVk6A',
                  client_secret='bYOWkBM3D84dnCWvFvM5RaGX_I8',
                  username='Happy_Bot-',
                  password='beveryhappy')

match_words = ["i am so sad", "he is sad", "i am unhappy", "i hate the world", "sadness", "i want to be happy", "i can't escape sadness", "i can not escape sadness", "i can't escape this sadness", "i can not escape this sadness", "i want to feel better", "i wish I felt better", "help me feel better"]

subreddit = bot.subreddit('DeepThoughts')

comments = subreddit.stream.comments()

for comment in comments:
    text = comment.body # Fetch body
    author = comment.author # Fetch author
    #match_comment = any(string in text for string in match_words)

    for match in match_words:
        if match in text.lower(): # Generate a message
            message = "I hope you have a nice day".format(author)
            comment.reply(message) # Send message

