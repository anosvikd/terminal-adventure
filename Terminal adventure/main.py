import time

def animate_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)  # adjust this value for the speed of the animation

animate_text("WELCOME TO THE DAY IN THE LIFE OF SARAH...")
print('\n')



#The main character, Sarah, wakes up in her cozy apartment in the bustling city. She's a graphic designer working at a small design firm, passionate about her work but sometimes feeling overwhelmed by deadlines.
#arah's goal for the day is to balance her work responsibilities with self-care and social interaction.

player_name = input('Enter your name: ')


animate_text(f'\nWelcome to the game, {player_name}!')
print('\n')


game_start = input('Would you like to start the game? (yes/no)')

while game_start not in ['yes', 'no']:
   print('Invalid input. Please enter yes or no.')
   game_start = input('Would you like to start the game? (yes/no)')

if game_start == 'no':
   print('Thank you for considering the game. Goodbye!')
   exit()


if game_start == 'yes':
  
  print ('\n=================================================================================================================================================================================')

  animate_text('\nWelcome to the day in the life of Sarah...')
  print('\n')
  


  animate_text('\nSarah wakes up in her cozy apartment in the bustling city. She is a graphic designer working at a small design firm, passionate about her work but sometimes feeling overwhelmed by deadlines.')
  print('\n')

  animate_text('\nSarah\'s goal for the day is to balance her work responsibilities with self-care and social interaction.')
  print('\n')
  print('\n=================================================================================================================================================================================')
  #Morning Routine:Option 1: Stay in bed for a few more minutes, feeling the warmth of the blankets and enjoying a moment of relaxation before starting the day.
  #Option 2: Get up immediately, eager to tackle the day's challenges head-on. Sarah feels motivated and ready to seize the day.
  #Sarah decides to have a healthy breakfast of oatmeal with fruit, wanting to start the day with nourishing fuel for her body and mind.
  animate_text('\nIn the morning...')
  print('')

  animate_text('\nChoose the following options:')
  print('')
  print(' 1. Stay in bed for a few more minutes, feeling the warmth of the blankets and enjoying a moment of relaxation before starting the day.')
  print(' 2. Get up immediately, eager to tackle the day\'s challenges head-on. ')

morning_routine = int(input('Enter your choice(1/2): '))

while morning_routine not in [1, 2]:
   print('Invalid input. Please enter 1 or 2.')
   morning_routine = int(input('Enter your choice(1/2): '))
  

if morning_routine == 1:
   animate_text('\n She cherishes the warmth of the blankets and enjoys a moment of relaxation.')
   print('')
   animate_text('\nAfter a few minutes of rest, she eventually gets up feeling refreshed.')
   print('')
   animate_text('\nSarah then proceeds to have a healthy breakfast of oatmeal with fruit, wanting to start the day with nourishing fuel for her body and mind.')
   print('')
else: 
   animate_text('\nShe feels motivated and ready to tackle the day\'s challenges head-on.')
   print('')
   animate_text('\nWithout hesitation, she gets out of the bed and starts the day.')
   print('')
   animate_text('\nSarah then proceeds to have a healthy breakfast of oatmeal with fruit, wanting to start the day with nourishing fuel for her body and mind.')
   print('')

print('\n=================================================================================================================================================================================')


#Sarah arrives at the design studio and is greeted by her colleagues. She faces a choice:
#Option 1: Tackle a challenging project first, diving straight into brainstorming ideas and working out design concepts.
#Option 2: Start with smaller tasks like responding to emails and organizing files, easing into the day's work gradually.
animate_text('\nGoing to work...')
print('')


animate_text('\nSarah arrives at the design studio and is greeted by her colleagues. She faces a choice:')
print('')

animate_text('\nChoose the following options:')
print('')

print(' 1. Tackle a challenging project first, diving straight into brainstorming ideas and working out design concepts.')
print(' 2. Start with smaller tasks like responding to emails and organizing files, easing into the day\'s work gradually.')

work_choice = int(input('Enter your choice(1/2): '))

while work_choice not in [1, 2]:
   print('Invalid input. Please enter 1 or 2.')
   work_choice = int(input('Enter your choice(1/2): '))
  
if work_choice == 1:
   animate_text('\nShe dives straight into brainstorming ideas and working out design concepts for a challenging project. ')
   print('')
   animate_text('\nSarah may spend a few hours focused on the project, immersing herself in the creative process.')
   print('')
else:
   animate_text('\nShe begins her day by responding to emails and organizing files, easing into the day\'s work gradually.')
   print('')
   animate_text('\nSarah may prioritize completing smaller, more manageable tasks before tackling larger projects, potentially helping her feel more organized and prepared for the rest of the day\'s work.')
   print('')
   
print('\n=================================================================================================================================================================================')

#During her lunch break, Sarah has some free time to herself. She decides:
#Option 1: Eat lunch alone at her desk, using the time to catch up on personal tasks like checking social media and reading the news.
#Option 2: Join her colleagues for lunch in the break room, enjoying their company and engaging in casual conversation.
animate_text('\nLunch break session...')
print('')
animate_text('\nDuring her lunch break, Sarah has some free time to herself. She decides:')
print('')
animate_text('\nChoose the following options:')
print('')

print(' 1. Eat lunch alone at her desk, using the time to catch up on personal tasks like checking social media and reading the news.')
print(' 2. Join her colleagues for lunch in the break room, enjoying their company and engaging in casual conversation.')

lunch_choice = int(input('Enter your choice(1/2): '))

while lunch_choice not in [1, 2]:
    print('Invalid input. Please enter 1 or 2.')
    lunch_choice = int(input('Enter your choice(1/2): '))

if lunch_choice == 1:
    animate_text('\nShe decides to eat lunch alone at her desk, using the time to catch up on personal tasks like checking social media and reading the news.')
    print('')
    animate_text('\nSarah takes a moment to relax and recharge during her lunch break, enjoying some quiet time to herself.')
    print('')
else:
    animate_text('\nShe decides to join her colleagues for lunch in the break room, enjoying their company and engaging in casual conversation.')
    print('')
    animate_text('\nSarah values the opportunity to connect with her coworkers and build positive relationships in the workplace.')
    print('')

print('\n=================================================================================================================================================================================')

#After lunch, Sarah has some flexibility in how she spends her afternoon:
#Option 1: Go for a walk outside to clear her head and get some fresh air, taking a break from the screen and enjoying nature.
#Option 2: Stay indoors to focus on work, determined to make progress on her projects and meet deadlines.
animate_text('\nAfternoon session (post-lunch)...')
print('')

animate_text('\nAfter lunch, Sarah has some flexibility in how she spends her afternoon:')
print('')

animate_text('\nChoose the following options:')
print('')

print(' 1. Go for a walk outside to clear her head and get some fresh air, taking a break from the screen and enjoying nature.')
print(' 2. Stay indoors to focus on work, determined to make progress on her projects and meet deadlines.')

afternoon_choice = int(input('Enter your choice(1/2): '))

while afternoon_choice not in [1, 2]:
    print('Invalid input. Please enter 1 or 2.')
    afternoon_choice = int(input('Enter your choice(1/2): '))

if afternoon_choice == 1:
    animate_text('\nShe decides to go for a walk outside to clear her head and get some fresh air, taking a break from the screen and enjoying nature.')
    print('')
    animate_text('\nSarah finds the walk refreshing and invigorating, helping her feel recharged and ready to tackle the rest of the day.')
    print('')
else:
   animate_text('\nShe remains determined to make progress on her projects and meet deadlines.')
   print('')
   animate_text('\nSarah focuses on her work, immersing herself in the creative process and making strides towards completing her tasks.')
   print('')

print('\n=================================================================================================================================================================================')

#As the day winds down, Sarah faces decisions about how to spend her evening:
#Option 1: Attend a networking event for creative professionals, hoping to make new connections and gain inspiration for her work.
#Option 2: Opt for a quiet night at home, indulging in a relaxing bath and cozying up with a book or watching her favorite TV show.
animate_text('\nEvening session...')
print('')

animate_text('\nAs the day winds down, Sarah faces decisions about how to spend her evening:')
print('')

animate_text('\nChoose the following options:')
print('')

print(' 1. Attend a networking event for creative professionals, hoping to make new connections and gain inspiration for her work.')
print(' 2. Opt for a quiet night at home, indulging in a relaxing bath and cozying up with a book or watching her favorite TV show.')

evening_choice = int(input('Enter your choice(1/2): '))

while evening_choice not in [1, 2]:
    print('Invalid input. Please enter 1 or 2.')
    evening_choice = int(input('Enter your choice(1/2): '))

if evening_choice == 1:
    animate_text('\nShe decides to invest her evening in networking and professional development.')
    print('')
    animate_text('\nSarah may hope to make new connections, exchange ideas with other creatives, and gain inspiration for her work through engaging with fellow professionals in her field.')
    print('')
else:
    animate_text('\nShe decides to prioritize relaxation and self-care after a busy day.')
    print('')
    animate_text('\nSarah indulges in a relaxing bath, cozying up with a book, or watching her favorite TV show, allowing herself to unwind and recharge for the day ahead.')
    print('')

print('\n=================================================================================================================================================================================')

#After returning home from the event, Sarah prepares for bed:
#Option 1: Watch TV for a little while before going to sleep, unwinding with a favorite show and allowing her mind to relax.
#Option 2: Read a book in bed, choosing a novel that transports her to another world and helps her escape the stresses of the day.

animate_text('At the end of the day...')
print('')

animate_text('\nAfter returning home from the event, Sarah prepares for bed:')
print('')

animate_text('\nChoose the following options:')
print('')

print(' 1. Watch TV for a little while before going to sleep, unwinding with a favorite show and allowing her mind to relax.')
print(' 2. Read a book in bed, choosing a novel that transports her to another world and helps her escape the stresses of the day.')

bedtime_choices = int(input('Enter your choice(1/2):'))

while bedtime_choices not in [1,2]:
   print('Invalid input. Please enter 1 or 2.')
   bedtime_choices = int(input('Enter your choice(1/2):'))

if bedtime_choices == 1:
    animate_text('\nShe unwinds with a favorite show, allowing her mind to relax and decompress.')
    print('')
    animate_text('\nSarah finds comfort and entertainment in the familiar routines of watching TV before bed, helping her to ease into sleep and let go of any lingering stresses from the day.')
    print('')
else:
    animate_text('\nShe chooses a novel that transports her to another world, providing an escape from the stresses of the day.')
    print('')
    animate_text('\nSarah may find solace and relaxation in the immersive experience of reading, allowing her to disconnect from the outside world and drift off to sleep peacefully.')
    print('')

print('\n=================================================================================================================================================================================')

animate_text(f'\nThank you for playing the game, {player_name}! We hope you enjoyed it! See you next time')
print('\n')

animate_text('\nGoodbye!')



