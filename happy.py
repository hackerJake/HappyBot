import praw
import random
import time

# signs bot into reddit jake
bot = praw.Reddit(user_agent='HappyBot v0.1',
                  client_id='Kum-y-9S3wVk6A',
                  client_secret='bYOWkBM3D84dnCWvFvM5RaGX_I8',
                  username='Happy_Bot-',
                  password='beveryhappytoday')

# targets subreddit hayden
sub = bot.subreddit('sad')

# array for comment ids that have been replied to jake
replied_to = []

# target words for sadness hayden
match_words_sadness = ["i am so sad", "he is sad", "she is sad", "sadness",
                       "i want to be happy",  "i want to feel better", "i wish I felt better",
                       "help me feel better", "i need help to feel better",
                       "help me with this sadness",  "i feel bad for myself",
                       "i am feeling down", "i am having a bad day", "i am not feeling well"]

# target words for depression jake
match_words_depression = ["i am depressed", "why is everything so depressing", "i can't escape sadness",
                          "i can not escape sadness", "i can't escape this sadness",  "i can not escape this sadness",
                          "sadness controls my life", "sadness is all i feel", "sadness won't leave me alone",
                          "i want to end this sadness",  "why won't sadness stop", "i hate my life"]

# target words for unhappiness hayden
match_words_unhappiness = ["unhappiness", "i am unhappy", "my friend is unhappy", "unhappiness is all I feel",
                           "i am supremely unhappy"]

# target words for happy jake
match_words_happy = ["i feel very happy today", "i am having a good day", "thank you happy bot",
                     "i am having a great day today", "i feel great today"]

# target words bobby hayden
match_words_bobby = ["Anyone who told you to be yourself couldn't have given you worse advice.",
                    "Calling you stupid would be an insult to stupid people.",
                    "Did your parents ever ask you to run away from home?",
                    "Every robot has the right to be ugly, but you abused the privilege!",
                    "I'd like to see things from your point of view but I can't seem to get my head that far up my ass.",
                    "There is no vaccine against stupidity.",
                    "[Thank you so much for your lovely words](https://static.superdeluxe.com/dankland/generated-memes/d4a66daeefd7de8df38eda1beef5e529.jpeg)"]

# array of replies for sadness hayden
replies_sadness = ["I hope you have a nice day", "I hope you feel better", "You are beautiful",
                   "Some days you'll have setbacks, but just know that tomorrow is a new day with new possibilities."]

# array of replies for depression jake
replies_depression = ["Find someone close who you can talk about your feelings with. I hope you feel better.",
                      "You’re not alone in this.",
                      "Even if it feels like this right now, this feeling won't last forever."]

# array of replies for unhappiness jake
replies_unhappiness = ["Relax and take deep breaths. Everything will be ok", "You can get through this.",
                       "We are not on this earth to see through one another, but to see one another through."]

replies_happy = ["Spread your joy!", "hold on to this feeling"]

replies_bobby = ["Please stop bobby, i am just a little bot trying to spread joy"]

# gets comments from the subreddit hayden
comments = sub.stream.comments()

# gets the comments and makes them lowercase hayden
for comment in comments:
    comment_body = comment.body.lower()
    author = comment.author

# SADNESS

# looks for match in sadness array jake
    for match in match_words_sadness:
        print("searching matches")
        if match in comment_body:

            # breaks if the comment has been replied to jake
            if comment.id in replied_to:
                print("already replied to this message")
                break

# random reply from sadness response array jake
            else:
                comment.reply(replies_sadness[random.randint(0, len(replies_sadness) - 1)])
                print("replied to sadness message")

# appends the comment id to the replied array jake
                replied_to.append(comment.id)

# sleeps for 10 seconds after it responds jake
                print("sleeping")
                time.sleep(10)
                print("awake")

# DEPRESSION

# looks for match in depression array hayden
    for match in match_words_depression:
        print("searching matches")
        if match in comment_body:

            # breaks if comment has been replied to jake
            if comment.id in replied_to:
                print("already replied to this message")
                break

# replies from array of depression responses jake
            else:
                comment.reply(replies_depression[random.randint(0, len(replies_depression) - 1)])
                print("replied to depression message")

# appends the comment id to the array jake
                replied_to.append(comment.id)

# sleeps after response jake
                print("sleeping")
                time.sleep(10)
                print("awake")

# UNHAPPINESS

# looks for match in the unhappy array hayden
    for match in match_words_unhappiness:
        print("searching matches")
        if match in comment_body:

            # breaks if comment id is in replied to hayden
            if comment.id in replied_to:
                print("already replied to this message")
                break

# replies from array of unhappiness responses jake
            else:
                comment.reply(replies_unhappiness[random.randint(0, len(replies_unhappiness) - 1)])
                print("replied to unhappy message")

# appends the comment id to the replied to array jake
                replied_to.append(comment.id)

# sleeps after response jake
                print("sleeping")
                time.sleep(10)
                print("awake")

# HAPPY

# looks for match in the happy array hayden
    for match in match_words_happy:
        print("searching matches")
        if match in comment_body:

            # breaks if comment id is in replied to hayden
            if comment.id in replied_to:
                print("already replied to this message")
                break

# replies from array of happy responses jake
            else:
                comment.reply(replies_happy[random.randint(0, len(replies_happy) - 1)])
                print("replied to happy message")

# appends the comment id to the replied to array jake
                replied_to.append(comment.id)

# sleeps after response jake
                print("sleeping")
                time.sleep(10)
                print("awake")

# BOBBY

# looks for match in the bobby array hayden
    for match in match_words_bobby:
        print("searching matches")
        if match in comment_body:

            # breaks if comment id is in replied to hayden
            if comment.id in replied_to:
                print("already replied to this message")
                break

# replies from array of bobby responses jake
            else:
                comment.reply(replies_bobby[random.randint(0, len(replies_bobby) - 1)])
                print("replied to bobby message")

# appends the comment id to the replied to array jake
                replied_to.append(comment.id)

# sleeps after response jake
                print("sleeping")
                time.sleep(10)
                print("awake")
