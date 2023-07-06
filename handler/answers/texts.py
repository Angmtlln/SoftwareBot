emoji = {'correct': '\U00002705', 'wrong': '\U0000274C', 'back': '\U00002B05', 'hi': '\U0001F44B',
         't-shirt': '\U0001F455', 'bag': '\U0001F6CD', 'cap': '\U0001F9E2', 'photo': '\U0001F9B0', 'dice': '\U0001F3B2',
         'time': '\U000023F3', 'cup': '\U00002615', 'long sleeve': '\U0001F97C', 'food': '\U0001F372',
         'blocknote': '\U0001F4D2', }

greetings = '''
Welcome to InnoSportChallengesBot.
'''
login = '''
To register you on Innopolis Sport website, please write your Innopolis email.
'''
About_Button = f'{emoji["hi"]}Hello! \nIt is a bot with sport challenges for Innopolis University’s students.\n ' \
               f'Here you can perform sports challenges, earn SportPoints for it and exchange them for merch.'

Help_Button = '''
If you have any questions or suggestions you can write it here: @sleeepy_zzzzz 
'''
Notification_Button = '''
Turn the Notifications ON or OFF ?
'''

On = f'{emoji["correct"]} ON'

Off = f'{emoji["wrong"]} OFF'

Notifications_On = 'Notifications are ON'

Notifications_Off = 'Notifications are OFF'

Back = 'Back'

Mistake = '''
Sorry, I don't understand you.
'''

password = '''
Please write your password.
'''
registered = '''
Your account has been successfully registered.
'''
already_registered = "Your account is already registered"

stores = {
    '''Pass cover''': "70 P",
    '''Sincerest meeting with the 319 team''': "1500 P",
    f'''{emoji['time']}\tTime Management class with E. Serochudinov''': '1500 P',
    f'''{emoji['dice']}\tInno Roulette''': '800 P',
    f'''{emoji['photo']}\tYour photo in 319 for 5 working days''': '250 P',
    f'''{emoji['t-shirt']}\t IU T-Shirt Pattern''': '1800 P',
    f'''{emoji['t-shirt']}\t IU T-Shirt Squared Logo Black (oversized)''': '1500 P',
    f'''{emoji['t-shirt']}\t IU T-Shirt Squared Logo White (oversized)''': '1500 P',
    f'''{emoji['t-shirt']}\t IU T-Shirt Black Emblem (oversized)''': '1500 P',
    f'''{emoji['t-shirt']}\t IU T-Shirt White Emblem (oversized)''': '1500 P',
    f'''{emoji['t-shirt']}\t IU T-Shirt Black Classic (oversized)''': '1500 P',
    f'''{emoji['t-shirt']}\t IU T-Shirt White Classic (oversized)''': '1500 P',
    f'''{emoji['bag']}\tIU shopper''': '300 P',
    f'''{emoji['cap']}\tIU cap''': '500 P',
    '''IU chevron badge''': '150 P',
    '''IU Popsocket''': '200 P',
    f'''{emoji['cup']}IU Mug Classic''': '350 P',
    '''Campus Accommodation (works from the 1 day of the month)''': '3000 P',
    '''IU Winter Knitted Gloves''': '300 P',
    f'''{emoji['long sleeve']}IU sleeves gray''': '1200 P',
    f'''{emoji['t-shirt']}IU gray''': '900 P',
    f'''{emoji['long sleeve']}Code your life''': '1200 P',
    f'''{emoji['t-shirt']}Student affairs bot''': '900 P',
    f'''{emoji['t-shirt']}To C++ or not to C++''': '900 P',
    f'''{emoji['long sleeve']}IT is awesome''': '1200 P',
    f'''{emoji['long sleeve']}Think twice code once''': '1200 P',
    f'''{emoji['t-shirt']}Things aren't always''': '900 P',
    f'''{emoji['long sleeve']}IU sleeves blue''': '1200 P',
    f'''{emoji['long sleeve']}Code hard or go home''': '1200 P',
    f'''{emoji['long sleeve']}Born to code 2020''': '1200 P',
    f'''{emoji['food']}Dinner one month (works from the 1 day of the month)''': '3000 P',
    f'''{emoji['food']}Lunch one month (works from the 1 day of the month)''': '3500 P',
    f'''{emoji['food']}Breakfast one month (works from the 1 day of the month)''': '2500 P',
    '''Sports bag ibc 2019''': '75 P',
    f'''{emoji['blocknote']}Notepad ibc''': '50 P',
    f'''{emoji['long sleeve']}Coding god''': '450 P',
    f'''{emoji['long sleeve']}Code or die''': '450 P'
}


def merch():
    array_of_items = []
    for i in stores:
        array_of_items.append(f'{i}: {stores[i]}')
    return array_of_items
