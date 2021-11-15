
# Hi,

# Here is my cover letter written in a Python Class format.
# If you are familiar with Python, you can actually run this code in Python (https://github.com/maxvalencik/bedrock-cover-letter) and call all methods on <maxime> to learn more about me...,
# or simply keep reading below!

# I am looking forward to hearing from you!
#
# Thanks!

# Maxime Valencik

class Cover_Letter:

    company = 'Bedrock'
    position = 'Opportunistic Talent'
    date = 'November 2021'

    def __init__(self):
        """Constructor: my personal information"""

        self.first_name = 'Maxime'
        self.last_name = 'Valencik'
        self.email = 'valencikmaxime@gmail.com'
        self.phone = '+1(321) 900-3035'
    ########################################

    def who_I_am(self):
        """This method will tell you a bit more about me!"""

        print('I am originally from France and I have spent most of my career in the aviation industry for 10+ years. I started as an air traffic controller in France and went back to college to study engineering. At that time, I had the opportunity to join an exchange program with the Florida Institute of Technology and graduated with a MS in Aerospace Engineering and an MS in Aviation. I permanently moved to the US after graduation and have been working as an airport engineer since then. It has been so far a great adventure!\n')

        print('I am adventurous in my personal life as well. I am an avid scuba diver with a love for the oceans! I have had the chance to explore multiple parts of the underwater world with my scuba gear. I am also excited about exploring mountains as a mountainer and rock climber! Always on the lookout for my next adventure, whether is personal or professional...')
     ########################################

    def why_I_apply(self):
        """This method will explain why I want to apply for a position at Bedrock"""

        print('My time spent in the aviation world has been challenging but rewarding, with a lot of learning in between. However, I have now reached a point in my life where I am ready to take the leap! I am looking for a career transition into the world of software engineering. Similarly to aviation, I believe that being a software engineer is very exciting with the opportunity to keep learning continuously while...sometimes...feel like a pioneer.\n')

        print('Fully embracing this new challenge, I enrolled in a software engineering bootcamp with Springboard where I have been brushing up my coding skills and learning new ones such as Javascript, Python, React, Flask, Node.js, SQL, and more. I also have advanced knowledge of Java and C++ languages, and a little bit of a passion to learn more about IOS application development with Swift.\n')

        print('In addition to my personal desire to explore new horizons in my career, I would like to share a purpose I believe in; and I am thrilled about the mission at Bedrock! At the age of space exploration, it is sometimes easy to forget about our own home and our oceans, source of all life. As a scuba diver and a passionate about all underwater things, I am truly excited about the opportunity of joining Bedrock and explore more the bottom of our oceans.\n')

        print('Coming from an unusual background, I decided to apply to the Opportunistic Talent posting, hoping that you could find the best fit for me in your company and allow me to plunge in and start a new incredible adventure...\n')
    ########################################

    def what_I_bring(self):
        """This method will explain what I can bring to your team"""

        whatIBring = {
            'Passionate about what I do',
            'Avid learner who loves challenges',
            'Multidisciplinary engineer with project management experience',
            'Problem solver',
            'Knowledge of multiple coding languages and full stack technologies',
            'Thrive in fast-pace environment',
            'Both, team player and autonomous',
            'Lover of what life has to offer'
        }

        for skill in whatIBring:
            print(skill)
    ########################################

    def contact_me(self):
        print(f'My email is {self.email} and my phone number is {self.phone}')


maxime = Cover_Letter()
