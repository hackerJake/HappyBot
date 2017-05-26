import praw

bot = praw.Reddit(user_agent='HappyBot v0.1',
                  client_id='Kum-y-9S3wVk6A',
                  client_secret='bYOWkBM3D84dnCWvFvM5RaGX_I8',
                  username='Happy_Bot-',
                  password='beveryhappy')

sub = bot.subreddit('sadness')


match_words_sadness = ["i am so sad", "he is sad", "she is sad", "i am unhappy", "sadness",
                       "i want to be happy", "i can't escape sadness", "i can not escape sadness",
                       "i can't escape this sadness", "i can not escape this sadness", "i want to feel better",
                       "i wish I felt better", "help me feel better", "i am an emotional wreck", "sad",
                       "i need help to feel better", "sadness controls my life", "sadness is all i feel",
                       "help me with this sadness", "sadness won't leave me alone", "i want to end this sadness",
                       "why won't sadness stop", "i feel bad for myself", "sadness"]


match_words_depression = ["depression", "depressed", "why is everything so depressing"]

replies_sadness = ["I hope you have a nice day", "I hope you feel better"]

replies_depression = ["Find someone close who you can talk about your feelings with. I hope you feel better."]

replied_to = []

comments = sub.stream.comments()

for comment in comments:
    comment_body = comment.body.lower()
    author = comment.author

    for match in match_words_sadness:
        print("searching matches")
        if match in comment_body:
            if comment.id in replied_to:
                print("already replied to this message")
                break
            else:
                comment.reply(match_words_sadness[random.randint(0, len(match_words_sadness) - 1)])
                print("replied to message")

                replied_to.append(comment.id)

    for match in match_words_depression:
        print("searching matches")
        if match in comment_body:
            if comment.id in replied_to:
                print("already replied to this message")
                break
            else:
                comment.reply(match_words_depression[random.randint(0, len(match_words_depression) - 1)])
                print("replied to message")

                replied_to.append(comment.id)
