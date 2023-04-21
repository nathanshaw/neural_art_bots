# Import the nessisary libraries
from tensorflow import keras
import tensorflow as tf
import openai
import json
import requests
import os
from random import shuffle, randint, uniform, choice
import pyttsx3


def getRandomName(gender):
    male_names = ['Adam', 'Alan', 'Albert', 'Alex', 'Alfred', 'Amir', 'Andre', 'Anthony', 'Antonio',
                  'Archer', 'Arthur', 'Ashton', 'Austin', 'Barrett', 'Benjamin', 'Bennett', 'Billy',
                  'Blake', 'Bradley', 'Brandon', 'Brayden', 'Brendan', 'Brett', 'Brian', 'Bruce',
                  'Caleb', 'Calvin', 'Cameron', 'Carl', 'Carlos', 'Carson', 'Carter', 'Casey', 'Chad',
                  'Charles', 'Chase', 'Chris', 'Christian', 'Christopher', 'Clayton', 'Cody', 'Cole',
                  'Colin', 'Collin', 'Connor', 'Conor', 'Corey', 'Craig', 'Curtis', 'Dakota', 'Dale',
                  'Dallas', 'Dalton', 'Damian', 'Daniel', 'Dante', 'Darian', 'Darius', 'Darnell',
                  'Darren', 'David', 'Davis', 'Dean', 'Devin', 'Diego', 'Dillon', 'Dominic', 'Donovan',
                  'Douglas', 'Drake', 'Drew', 'Dustin', 'Dwayne', 'Dylan', 'Easton', 'Eddie', 'Edgar',
                  'Edmund', 'Edward', 'Edwin', 'Eli', 'Elias', 'Elijah', 'Elliot', 'Ellis', 'Elmer',
                  'Elton', 'Elvin', 'Emil', 'Emmett', 'Enrique', 'Eric', 'Erick', 'Ernest', 'Ethan',
                  'Eugene', 'Evan', 'Everett', 'Fabian', 'Felix', 'Fernando', 'Finley', 'Floyd',
                  'Forrest', 'Francis', 'Frank', 'Franklin', 'Frederick', 'Gabriel', 'Gage', 'Gary',
                  'Gavin', 'Gene', 'Geoffrey', 'George', 'Gerald', 'Giovanni', 'Glen', 'Glenn', 'Gordon',
                  'Graham', 'Grant', 'Greg', 'Gregory', 'Gunnar', 'Gustavo', 'Guy', 'Hank', 'Harold',
                  'Harry', 'Harvey', 'Hayden', 'Heath', 'Hector', 'Henry', 'Herbert', 'Houston', 'Howard',
                  'Hudson', 'Hugh', 'Hunter', 'Ian', 'Ivan', 'Izaiah', 'Jack', 'Jackson', 'Jacob',
                  'Jaden', 'Jagger', 'Jaime', 'Jake', 'Jamal', 'James', 'Jared', 'Jarrett', 'Jason',
                  'Jasper', 'Javier', 'Jay', 'Jayce', 'Jayden', 'Jeff', 'Jeffrey', 'Jeremiah',
                  'Jeremy', 'Jermaine', 'Jerome', 'Jerry', 'Jesse', 'Jesus', 'Jim', 'Jimmy', 'Joel',
                  'John', 'Johnny', 'Jon', 'Jonathan', 'Jordan', 'Jorge', 'Jose', 'Joseph', 'Josh',
                  'Joshua', 'Josiah', 'Juan', 'Kai', 'Kale', 'Kameron', 'Kane', 'Karl', 'Karter', 'Kase', 'Kash', 'Kason',
                  'Kato', 'Kayden', 'Kayson', 'Keanu', 'Keaton', 'Kellan', 'Kelvin', 'Kendrick',
                  'Kenny', 'Kent', 'Kenzo', 'Kieran', 'Killian', 'King', 'Knox', 'Kobe', 'Koda',
                  'Kody', 'Kolby', 'Kole', 'Kolton', 'Konnor', 'Korbin', 'Kris', 'Krish', 'Kristian',
                  'Kurt', 'Kyler', 'Lamar', 'Landon', 'Lane', 'Lars', 'Lawson', 'Layne', 'Leandro',
                  'Ledger', 'Lee', 'Leif', 'Leighton', 'Leland', 'Lenny', 'Leo', 'Leon', 'Leonard',
                  'Leonardo', 'Levi', 'Lewis', 'Liam', 'Lincoln', 'Lionel', 'Logan', 'London', 'Loren',
                  'Lorenzo', 'Louie', 'Louis', 'Lucas', 'Lucca', 'Lucian', 'Luciano', 'Luigi', 'Luka',
                  'Luke', 'Luther', 'Lyle', 'Lyndon', 'Mac', 'Mack', 'Maddox', 'Magnus', 'Malachi',
                  'Malcolm', 'Malik', 'Manny', 'Manuel', 'Marcel', 'Marco', 'Marcus', 'Mario', 'Mark',
                  'Marley', 'Marshall', 'Martin', 'Marty', 'Marvin', 'Mason', 'Mateo', 'Mathew',
                  'Matias', 'Matt', 'Matthew', 'Maurice', 'Maverick', 'Max', 'Maxim', 'Maximilian',
                  'Maximus', 'Mekhi', 'Melvin', 'Memphis', 'Merrick', 'Merritt', 'Mervin', 'Micah',
                  'Michael', 'Michelangelo', 'Mickey', 'Miguel', 'Mike', 'Milan', 'Miles', 'Miller',
                  'Milo', 'Milton', 'Mirza', 'Mitchell', 'Mohammed', 'Moises', 'Monte', 'Montgomery',
                  'Morris', 'Moses', 'Muhammad', 'Murray', 'Mustafa', 'Nash', 'Nasir', 'Nate', 'Nathan',
                  'Nathanael', 'Nehemiah', 'Neil', 'Nelson', 'Nestor', 'Nevin', 'Nicholas', 'Nick',
                  'Nickolas', 'Nico', 'Nicolas', 'Nigel', 'Nikolas', 'Noah', 'Nolan', 'Norman', 'Nyle',
                  'Oakley', 'Obi', 'Omar', 'Orion', 'Orlando', 'Oscar', 'Osvaldo', 'Otis', 'Otto',
                  'Owen', 'Pablo', 'Parker', 'Pat', 'Patrick', 'Paul', 'Paxton', 'Payton', 'Pedro',
                  'Perry', 'Peter', 'Quentin', 'Quincy', 'Quinn', 'Rafael', 'Ralph', 'Ramiro', 'Ramon',
                  'Randy', 'Raphael', 'Raul', 'Ray', 'Rayan', 'Raymond', 'Reece', 'Reed', 'Reese',
                  'Reginald', 'Reid', 'Remington', 'Remy', 'Renato', 'Rene', 'Reuben', 'Rex', 'Rey',
                  'Rhett', 'Ricardo', 'Richard', 'Richie', 'Rick', 'Ricky', 'Rider', 'Riley', 'River',
                  'Robbie', 'Robert', 'Roberto', 'Robin', 'Rocco', 'Rocky', 'Rodney', 'Rodolfo', 'Rodrigo',
                  'Rohan', 'Roland', 'Roman', 'Romeo', 'Ronald', 'Ronan', 'Ronnie', 'Rory', 'Roscoe', 'Rowan',
                  'Royce', 'Ruben', 'Rudy', 'Rufus', 'Russell', 'Ryan', 'Ryder', 'Ryland', 'Rylie', 'Zachariah',
                  'Zachary', 'Zaid', 'Zaire', 'Zander', 'Zane', 'Zayden', 'Zechariah', 'Zion', 'Zoltan']
    
    female_names = ['Abigail', 'Addison', 'Adeline', 'Adriana', 'Aileen', 'Aisha', 'Alaina', 'Alana',
                    'Alessandra', 'Alexa', 'Alexandra', 'Alice', 'Alicia', 'Alina', 'Alison', 'Alivia',
                    'Allison', 'Allyson', 'Alyssa', 'Amara', 'Amaya', 'Amelia', 'Amelie', 'Amira',
                    'Amy', 'Ana', 'Annabelle', 'Annalise', 'Ariana', 'Arianna', 'Ariel', 'Arielle',
                    'Arya', 'Asha', 'Ashley', 'Ashton', 'Aubrey', 'Aurora', 'Ava', 'Avery', 'Bella',
                    'Brianna', 'Bridgette', 'Brooklyn', 'Caitlyn', 'Camila', 'Carla', 'Carly', 'Carmen',
                    'Caroline', 'Cassandra', 'Catherine', 'Chelsea', 'Chloe', 'Claire', 'Clara', 'Corinne',
                    'Crystal', 'Daisy', 'Daniela', 'Daphne', 'Darlene', 'Destiny', 'Diana', 'Donna',
                    'Eden', 'Elena', 'Eliana', 'Elise', 'Eliza', 'Elizabeth', 'Ella', 'Ellie', 'Elvira',
                    'Emily', 'Emma', 'Erica', 'Erin', 'Evelyn', 'Faith', 'Felicity', 'Francesca', 'Gabriela',
                    'Gabriella', 'Genevieve', 'Gianna', 'Giselle', 'Grace', 'Gracie', 'Greta', 'Gwendolyn',
                    'Hadley', 'Haley', 'Hannah', 'Harley', 'Harper', 'Hazel', 'Heather', 'Hope',
                    'Imani', 'India', 'Irene', 'Isabel', 'Isabella', 'Isabelle', 'Isla', 'Ivy', 'Jada',
                    'Jade', 'Jasmine', 'Jayla', 'Jayleen', 'Jazmin', 'Jenna', 'Jennifer', 'Jessica',
                    'Jocelyn', 'Jordan', 'Jordyn', 'Joselyn', 'Julianna', 'Julie', 'Juliette', 'Jillian',
                    'Kaitlyn', 'Katherine', 'Kayla', 'Kaylee', 'Keira', 'Kelly', 'Kendall', 'Kennedy',
                    'Kensley', 'Khloe', 'Kimberly', 'Kinley', 'Kinsley', 'Kira', 'Kylee', 'Kylie', 'Laila',
                    'Lana', 'Lara', 'Larissa', 'Laura', 'Lauren', 'Layla', 'Leah', 'Leilani', 'Lena',
                    'Leona', 'Leslie', 'Lia', 'Lila', 'Liliana', 'Lillian', 'Lillie', 'Lily', 'Lina',
                    'Linda', 'Lisa', 'Lola', 'London', 'Londyn', 'Lorelei', 'Lucia', 'Luciana', 'Lucille',
                    'Lucy', 'Luna', 'Lydia', 'Lyla', 'Mackenzie', 'Madeline', 'Madelyn', 'Madison', 'Maggie',
                    'Maisie', 'Makayla', 'Makenzie', 'Malaysia', 'Malia', 'Mallory', 'Margaret', 'Maria',
                    'Marie', 'Marilyn', 'Marina', 'Marissa', 'Marlee', 'Mary', 'Mckenzie', 'Megan', 'Melanie',
                    'Quinn', 'Raegan', 'Raelynn', 'Raina', 'Ramona', 'Raven', 'Reagan', 'Rebecca', 'Reese',
                    'Regina', 'Renata', 'Rhiannon', 'Riley', 'River', 'Rosalie', 'Rose', 'Rosie', 'Rowan',
                    'Ruby', 'Ruth', 'Sabrina', 'Sadie', 'Sage', 'Saige', 'Samantha', 'Samara', 'Samira',
                    'Sandra', 'Saniyah', 'Sara', 'Sarah', 'Sarai', 'Savannah', 'Scarlett', 'Serena', 'Shayla',
                    'Shelby', 'Sienna', 'Sierra', 'Skye', 'Skylar', 'Sloane', 'Sofia', 'Sophia', 'Sophie',
                    'Stella', 'Stephanie', 'Summer', 'Sunny', 'Sylvia', 'Sydney', 'Talia', 'Tamara', 'Tara',
                    'Taryn', 'Tatiana', 'Tatum', 'Taylor', 'Tegan', 'Tenley', 'Teresa', 'Tessa', 'Thalia',
                    'Thea', 'Theresa', 'Tiana', 'Tianna', 'Tiffany', 'Tori', 'Trinity', 'Valentina', 'Valerie',
                    'Vanessa', 'Vera', 'Veronica', 'Victoria', 'Vienna', 'Violet', 'Virginia', 'Vivian',
                    'Waverly', 'Willow', 'Winter', 'Wren', 'Wynter', 'Ximena', 'Yara', 'Yaretzi', 'Yasmine',
                    'Ysabel', 'Zaniyah', 'Zara', 'Zaria', 'Zariah', 'Zoe', 'Zoey', 'Zuri']

    neutral_names = ['Addison', 'Adrian', 'Ainsley', 'Alex', 'Alexis', 'Ali', 'Allie', 'Ariel', 'Arin',
                     'Ash', 'Ashton', 'Aubrey', 'August', 'Avery', 'Bailey', 'Blair', 'Blake', 'Bobby',
                     'Brett', 'Brook', 'Cameron', 'Campbell', 'Casey', 'Charlie', 'Chris', 'Dakota',
                     'Dana', 'Darcy', 'Drew', 'Eli', 'Ellis', 'Emerson', 'Emery', 'Finley', 'Frankie',
                     'Harley', 'Harper', 'Hayden', 'Hollis', 'Hunter', 'Jaden', 'Jamie', 'Jayden', 'Jordan',
                     'Justice', 'Kai', 'Kendall', 'Kennedy', 'Kyle', 'Lee', 'Logan', 'London', 'Lou',
                     'Mackenzie', 'Madison', 'Marley', 'Mason', 'Max', 'Morgan', 'Nico', 'Noah', 'Ollie',
                     'Parker', 'Pat', 'Peyton', 'Phoenix', 'Quinn', 'Rain', 'Reese', 'Rey', 'Riley',
                     'River', 'Robin', 'Rowan', 'Ryan', 'Sage', 'Sam', 'Sawyer', 'Scout', 'Shane', 'Shawn',
                     'Shay', 'Sidney', 'Sky', 'Skyler', 'Sloan', 'Spencer', 'Stevie', 'Tanner', 'Tatum',
                     'Tayler', 'Terry', 'Theo', 'Toby', 'Tommy', 'Tony', 'Tyler', 'Val', 'Wren', 'Wyatt', 'Zion']
    names = []
    if gender == 'Male':
        names = male_names + neutral_names
    else:
        names = female_names + neutral_names
    name = choice(names)
    return name

def generateRandomPersonalityTraits(complexity):
    traits = []
    pos_traits = ['Warm', 'Friendly', 'Clean', 'Honest', 'Loyal', 'Trustworthy', 'Dependable', 'Open-Minded', 'Thoughtful', 'Wise', 'Mature', 'Ethical', 'Courageous', 'Constructive', 'Productive', 'Progressive', 'Individualistic', 'Observant', 'Neat', 'Punctual', 'Logical', 'Prompt', 'Accurate', 'Self-Reliant', 'Independent', 'Inventive', 'Wholesome', 'Attentive', 'Frank', 'Purposeful', 'Realistic', 'Adventurous', 'Relaxed', 'Curious', 'Modern', 'Charming', 'Modest', 'Enthusiastic',
                  'Polite', 'Patient', 'Talented', 'Perceptive', 'Forgiving', 'Ambitious', 'Respectful', 'Grateful', 'Resourceful', 'Courteous', 'Helpful', 'Appreciative', 'Imaginative', 'Self-Disciplined', 'Decisive', 'Humble', 'Self-Confident', 'Easygoing', 'Consistent', 'Positive', 'Artistic', 'Fashionable', 'Convincing', 'Thrifty', 'Bold', 'Suave', 'Methodical', 'Interesting', 'Unselfish', 'Responsible', 'Reasonable', 'Likable', 'Clever', 'Cooperative', 'Romantic', 'Proficient']
    neg_traits = ['Aggressive', 'Arrogant', 'Belligerent', 'Bigoted', 'Blunt', 'Boastful', 'Callous', 'Careless', 'Censorious', 'Chaotic', 'Childish', 'Clumsy', 'Compulsive', 'Conceited', 'Cowardly', 'Crafty', 'Cruel', 'Cynical', 'Deceitful', 'Defensive', 'Delusional', 'Demanding', 'Dependent', 'Desperate', 'Destructive', 'Disloyal', 'Disobedient', 'Disrespectful', 'Distracted', 'Domineering', 'Dull', 'Egocentric', 'Envious', 'Erratic', 'Explosive', 'Extravagant', 'Fanatical', 'Fatalistic', 'Fawning', 'Fearful', 'Fickle', 'Finicky', 'Flirtatious', 'Foolish', 'Forgetful', 'Fraudulent', 'Fussy', 'Greedy', 'Gullible', 'Hateful', 'Haughty', 'Hedonistic', 'Hesitant', 'Hidebound', 'High-handed', 'Hostile', 'Ignorant', 'Imitative', 'Impatient', 'Impersonal', 'Impulsive', 'Inconsiderate', 'Inconsistent', 'Indecisive', 'Indulgent', 'Insecure', 'Insensitive', 'Insincere', 'Intolerant', 'Irresponsible', 'Jealous', 'Lazy', 'Malicious', 'Mannered', 'Miserly', 'Mistrustful', 'Moody', 'Morbid', 'Narrow-minded', 'Nasty', 'Naughty', 'Nervous', 'Obnoxious', 'Obsessive',
                  'Obvious', 'Opinionated', 'Oppressed', 'Outrageous', 'Overcritical', 'Overemotional', 'Paranoid', 'Passive', 'Patronizing', 'Perfectionist', 'Pessimistic', 'Pompous', 'Possessive', 'Power-hungry', 'Prejudiced', 'Presumptuous', 'Pretentious', 'Prim', 'Procrastinating', 'Provocative', 'Pugnacious', 'Quarrelsome', 'Quick-tempered', 'Reactionary', 'Reckless', 'Resentful', 'Ridiculous', 'Rigid', 'Sadistic', 'Sanctimonious', 'Sarcastic', 'Scheming', 'Scornful', 'Secretive', 'Sedentary', 'Self-centered', 'Self-indulgent', 'Selfish', 'Shallow', 'Shortsighted', 'Shy', 'Silly', 'Sneaky', 'Spiteful', 'Stingy', 'Stubborn', 'Stupid', 'Superficial', 'Superstitious', 'Suspicious', 'Tactless', 'Tasteless', 'Tense', 'Thievish', 'Thoughtless', 'Timid', 'Transparent', 'Treacherous', 'Trendy', 'Troublemaking', 'Unappreciative', 'Uncaring', 'Uncharitable', 'Unconvincing', 'Uncooperative', 'Uncreative', 'Undependable', 'Unforgiving', 'Unfriendly', 'Ungrateful', 'Unhealthy', 'Unimaginative', 'Unimpressive', 'Unkind', 'Unpredictable', 'Unrealistic', 'Unreflective']
    neutral_traits = ['Adaptable', 'Adventurous', 'Affectionate', 'Ambitious', 'Analytical', 'Appreciative', 'Assertive', 'Attentive', 'Candid', 'Capable', 'Careful', 'Cautious', 'Charming', 'Cheerful', 'Clear-headed', 'Competent', 'Composed', 'Confident', 'Conscientious', 'Considerate', 'Constant', 'Cooperative', 'Courageous', 'Creative', 'Curious', 'Daring', 'Decisive', 'Dedicated', 'Dependable', 'Dignified', 'Discerning', 'Discreet', 'Determined', 'Devoted', 'Diplomatic', 'Direct', 'Disciplined', 'Earnest', 'Economical', 'Efficient', 'Empathetic', 'Enduring', 'Energetic', 'Enthusiastic', 'Exact', 'Expressive', 'Fair-minded', 'Faithful', 'Farsighted', 'Flexible', 'Focused', 'Forgiving', 'Frank', 'Friendly', 'Frugal', 'Generous', 'Gentle', 'Genuine', 'Good-humored', 'Gracious', 'Hardworking', 'Healthy', 'Helpful', 'Honest', 'Honorable', 'Humorous', 'Idealistic', 'Imaginative', 'Impartial', 'Independent', 'Industrious', 'Ingenious', 'Initiative', 'Innovative', 'Inquisitive', 'Insightful', 'Intelligent', 'Intuitive', 'Just', 'Kind', 'Knowledgeable', 'Leaderly', 'Logical', 'Lovable', 'Loyal',
                      'Mature', 'Methodical', 'Meticulous', 'Moderate', 'Modest', 'Objective', 'Observant', 'Open-minded', 'Optimistic', 'Orderly', 'Organized', 'Original', 'Outgoing', 'Passionate', 'Patient', 'Peaceful', 'Perceptive', 'Persistent', 'Persuasive', 'Pioneering', 'Pleasant', 'Polished', 'Practical', 'Precise', 'Productive', 'Professional', 'Progressive', 'Punctual', 'Quick-witted', 'Quiet', 'Rational', 'Realistic', 'Reflective', 'Relaxed', 'Reliable', 'Resourceful', 'Respectful', 'Responsible', 'Responsive', 'Restrained', 'Reverent', 'Risk-taking', 'Self-critical', 'Self-controlled', 'Self-effacing', 'Self-reliant', 'Sensitive', 'Serious', 'Sincere', 'Skillful', 'Smart', 'Sober', 'Sociable', 'Solid', 'Sophisticated', 'Stable', 'Steadfast', 'Stimulating', 'Straightforward', 'Studious', 'Subtle', 'Successful', 'Supportive', 'Sympathetic', 'Systematic', 'Tasteful', 'Tenacious', 'Thorough', 'Thoughtful', 'Tidy', 'Tolerant', 'Tractable', 'Trustful', 'Trustworthy', 'Truthful', 'Unassuming', 'Understanding', 'Unselfish', 'Versatile', 'Vigilant', 'Warm', 'Well-behaved', 'Well-informed', 'Willing', 'Witty']

    for i in range(complexity):
        chance = uniform(0, 1.0)
        if chance < 0.15:
            traits.append(neg_traits[randint(0, len(neg_traits) - 1)])
        if chance < 0.5:
            traits.append(neutral_traits[randint(0, len(neutral_traits) - 1)])
        else:
            traits.append(pos_traits[randint(0, len(pos_traits) - 1)])
    return traits

def getSystemVoices():
    good_voices = ['Agnes', 'Albert', 'Alice', 'Allison', 
                   'Alva', 'Amira', 'Anna', 'Ava', 'Bahh', 
                   'Bells', "Boing", "Bubbles", "Carmit", 
                   "Cellos", 'Damayanti', 'Daniel', 'Daria', 
                   'Ellen', 'Evan', 'Fred', 'Ioana', 'Joana', 
                   "Junior", "Kanya", "Karen", "Kate", "Kathy", 
                   "Kyoko", "Lana", "Laura", "Lekha", "Lesya", 
                   "Linh", "Luciana", "Meijia", "Melina", "Milena", 
                   "Moira", 'Nathan', 'Nora', 'Oliver', 'Paulina',
                   'Ralph', 'Rishi', 'Samantha', 'Sangeeta', 'Sara',
                   'Satu', 'Sinji','Stephanie', 'Tessa', 'Thomas', 
                   'Tingting', 'Trinoids', 'Whisper', 'Xander', 'Yelda',
                   'Yuna', 'Zarvox', 'Zosia', 'Zuzana']
    bad_voices = ['Bahh', 'Sinja', 'Paulina', 'Jasper' ]
    # TODO - need to check that each voice exists and can be called somehow TODO TODO
    # Extract the voice names from each line
    voices = ['com.apple.speech.synthesis.voice.{}'.format(
        voice) for voice in good_voices if voice not in bad_voices]
    return voices

def testSystemVoices(voices):
    bad_voices = []
    for voice in voices:
        fake_persona = {
            'voice_name': voice,
            'voice_rate': 150
        }
        try:
            speakYourMind(fake_persona, "Test")
        except OSError as e:
            print(f"Error: {e}")
            print("Failed to load the specified voice. Please check the voice identifier.")
            bad_voices.append(voice)
    return voices - bad_voices

def randomlyGeneratePersona(complexity, model):
    # function that returns a dict containing all the personality parameters to run the program
    genders = ['Male', 'Female']
    gender = genders[randint(0, len(genders) - 1)]
    voices = getSystemVoices()
    persona = {
        'name': getRandomName(gender),
        'gender': gender,
        'traits': generateRandomPersonalityTraits(complexity),
        'model': model,
        'temperature': uniform(0.5, 1.5),
        'voice_name': voices[randint(0, len(voices) - 1)],
        'voice_rate': randint(150, 220)
    }
    print("Created a new persona: {}".format(persona))
    return persona


def speakYourMind(speaker_parms, message):
    # voices = tts.getProperty('voices')
    # for idx, voice in enumerate(voices):
    #    print(idx, voice.id)
    print(speaker_parms['voice_name'] + ": ", message)
    tts.setProperty('voice', speaker_parms['voice_name'])
    tts.setProperty('rate', speaker_parms['voice_rate'])
    tts.say(message)
    tts.runAndWait()


def sendDebateRequest(debater_params, topic, initial_call=False):
    max_tokens = 200
    # Create a dictionary to store our headers
    if initial_call is False:
        topic = 'Lets assume that you have the personality traits of {} and that this argument is incorrect,\n{}\n Please provide a counter argument in the first person that is fewer than {} words'.format(
            " ".join(debater_params['traits']), topic, max_tokens // 2)
    else:
        topic = "Assuming you are taking the role of someone with these personality traits: {}. Lets have a debate about the following topic: {}, can you please respond in under {} words in the first person?".format(
            " ".join(debater_params['traits']), topic, max_tokens // 2)

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + os.environ.get('OPENAI_API_KEY')
    }
    # create the data dictionary for our API call
    data = {
        'model': debater_params['model'],
        'temperature': debater_params['temperature'],
        'n': 1,
        'max_tokens': max_tokens,
        'prompt':  topic  # TODO, what does the 'role' potion of this dict do?
        # 'stop' : ';'
    }
    # print("Our data dict is as follows: ", data)
    # print("Our header dict is as follows: {}".format(headers))
    # Pose the debate topic question to our first debater
    # print("{} is generating a response to the prompt of: {}".format(
    #    debater_params['name'], topic))
    response = requests.post(
        'https://api.openai.com/v1/completions', headers=headers, json=data).json()
    return response['choices'][0]['text']


def generateVariation(message):
    p = "Please rewrite this sentence while keeping the overall message and Names the same: {}".format(
        message)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + os.environ.get('OPENAI_API_KEY')
    }
    # create the data dictionary for our API call
    data = {
        'model': 'text-babbage-001',
        'temperature': 1.1,
        'n': 1,
        'max_tokens': 100,
        'prompt':  p  # TODO, what does the 'role' potion of this dict do?
        # 'stop' : ';'
    }
    revised_message = requests.post(
        'https://api.openai.com/v1/completions', headers=headers, json=data).json()['choices'][0]['text']
    # print("initial message: {}\nrevised message: {}".format(
    #    message, revised_message))
    return revised_message


def judgeArgument(debater1, debater2, judge, responses, topic):
    debater_names = [debater1['name'], debater2['name']]
    max_tokens = 200
    # Create a dictionary to store our headers
    topic = 'I need you to judge which of two arguments are better according to the criteria of {} for the topic of {}.\n Here is the first agument {}.\n Here is the second argument {}. Please respond with a single character consisting of either a "0" for the first argument or "1" for the second argument.'.format(
        " ".join(judge['traits']), topic, responses[-2], responses[-1])
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + os.environ.get('OPENAI_API_KEY')
    }
    # create the data dictionary for our API call
    data = {
        'model': judge['model'],
        'temperature': judge['temperature'],
        'n': 1,
        'max_tokens': max_tokens,
        'prompt':  topic  # TODO, what does the 'role' potion of this dict do?
        # 'stop' : ';'
    }
    # print("Our data dict is as follows: ", data)
    # print("Our header dict is as follows: {}".format(headers))
    # Pose the debate topic question to our first debater
    print("Our Judge {} is generating a response to the prompt of: {}".format(
        judge['name'], topic))
    response = requests.post(
        'https://api.openai.com/v1/completions', headers=headers, json=data).json()
    print("The judges response is: {}".format(response['choices'][0]['text']))
    widx_string = response['choices'][0]['text'].strip("/n")
    if widx_string == '':
        widx_string = "1"
    print("widx_string: ", widx_string)
    widx = int(widx_string)
    return ("You both make good arguments, but {} has provided the strongest argument and therefore is awarded the point for this round.".format(debater_names[widx]), widx)


def runDebate(debater1, debater2, judge, topic, points_to_win):
    points = [0, 0]
    print("-"*60)
    prompt = topic
    print("Out first debater is {} : who has the traits of {}".format(
        debater1['name'], debater1['traits']))
    print("Out second debater is {} : who has the traits of {}".format(
        debater2['name'], debater2['traits']))
    print("Out Judge is {} : who has the traits of {}".format(
        judge['name'], judge['traits']))
    print("The topic of our debate is: {}".format(prompt))
    intro_p = "Hello, my name i Judge {} and I am going to be the judge of today's debate. The topic of our debate is: {}. {}, what are your opening arguments?".format(
        judge['name'], topic, debater1['name'])
    intro_p = generateVariation(intro_p)
    speakYourMind(judge, intro_p)
    print("-"*60)
    while (max(points) < points_to_win - 1):
        responses = []
        responses.append(sendDebateRequest(
            debater1, prompt, initial_call=True))
        speakYourMind(debater1, responses[-1])
        judge_response = "{}, you have made some valid points. {} what is your rebuttal?".format(
            debater1['name'], debater2['name'])
        judge_response = generateVariation(judge_response)
        speakYourMind(judge, judge_response)
        print("The generated response is: ", responses[-1])
        prompt = responses[-1]
        responses.append(sendDebateRequest(debater2, prompt))
        speakYourMind(debater2, responses[-1])
        prompt = responses[-1]
        print("The generated reply is: ", prompt)
        judgement, idx = judgeArgument(
            debater1, debater2, judge, responses, topic)
        if idx == 0:
            points[0] += points[0] + 1
        else:
            points[1] += points[1] + 1
        speakYourMind(judge, judgement)
    if points[0] > points[1]:
        winner = debater1
    else:
        winner = debater2
    verdict = "I have heard enough, the winner of todays debate is {}, you made the best arguments.".format(
        winner['name'])
    verdict = generateVariation(verdict)
    speakYourMind(judge, verdict)

if __name__ == "__main__":
    # Create a list of possible debate topics
    topics = ["What is the cutest animal?", 
            "Who was the greatest president?",
            "What is the best way to cook a chicken dinner?",
            "What is the meaning of life?",
            "What is love?",
            "What is the most magical place on earth?"]

    persona_num = 10
    complexity = 4
    personality_params = []

    # Initialize the Text-to-Speech engine
    tts = pyttsx3.init()

    # make sure we have the OpenAi API key stored as a 
    # environment variable
    assert os.environ.get('OPENAI_API_KEY') is not None, 'ERROR, your environment variable OPENAI_API_KEY is not set properly'

    # load the API key into our instance of the openai library
    # to make method calls simpler later on in the program
    openai.api_key = os.getenv('OPENAI_API_KEY')

    # create an list to store the parameters
    # for our three personalities which take turns
    #  serving as the two debaters and the judge
    # TODO, consider generating the personality traits randomly using a master list of personality traits
    personality_model = 'text-babbage-001'
    while True:
        shuffle(topics)
        for topic in topics:
            for i in range(persona_num):
                personality_params.append(randomlyGeneratePersona(complexity, personality_model))
                shuffle(personality_params)
            # randomly shuffle the order of our personality_parms indices
            # select one of the personality profiles at random for debater1
            debater1_params = personality_params[0]
            debater2_params = personality_params[1]
            judge_params = personality_params[2]
            # select one of the other profiles for debater 2
            
            runDebate(debater1_params, debater2_params, judge_params, topic, 4)