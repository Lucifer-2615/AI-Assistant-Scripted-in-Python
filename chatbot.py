import random


hello = ('hello','hey','hi','hii','buddy')

reply_hello = ('Hello sir, I am Shelly',
               "Hey , What's up ?",
               "Hello , How may I help you ?",
               'Hi sir, nice to meet you again',
               'hello sir, what can I do for you ?',
               'Hello sir, I am here for you',
               'Alert, alert, the most wonderful human on earth is about to wake up!',
               "Have a fantastic day, weirdo!",
               "Satan, it’s time to work!",
               'Tick tock, tick tock, tick tock...boom!'
               
               )

bye = ('Bye','Bye Bye','See you soon','good bye','exit','You need a break')

reply_bye = ('Bye.',
       'Bye Bye sir',
       "It's okay sir",
       'See you soon sir',
       'Okay...bye, fry guy!'
       "If I don’t see you around, I'll see you square."
       'Catch you on the rebound',
       'Gotta go, Bug',
       "Well, I'm off!",
       'Bye-bye, butterfly.',
       "You're still here? It's over. Go home. Go!",
       "Catch you later!",
       "Chop chop, lollipop!",
       )

sorry = ('sorry sir',
         'sorry it\'s beyond my abilitiy sir'
         )

def ChatterBot(Text):
    Text = str(Text) 
    
    for word in Text.split():
           if word in hello:
                  reply = random.choice(reply_hello)
                  
                  return reply
           elif word in bye:
                  reply = random.choice(reply_bye)
                  
                  return reply
           else:
                  return random.choice(sorry)
           
value = ChatterBot('hello')

print(value)
                  
    