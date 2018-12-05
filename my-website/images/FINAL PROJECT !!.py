import time
#This is a comment
def trench():
    print("We've been here the whole time. You were asleep. Time to wake up. ")
    time.sleep(3)
    print ('  ______                            _______                  _     ')
    print (' |  ____|                          |__   __|                | |    ')
    print (' | |__   ___  ___ __ _ _ __   ___     | |_ __ ___ _ __   ___| |__  ')
    print (' |  __| / __|/ __/ _  |  _ \ / _ \    | |  __/ _ \  _ \ / __|  _ \ ')
    print (' | |____\__ \ (_| (_| | |_) |  __/    | | | |  __/ | | | (__| | | |')
    print (' |______|___/\___\__,_| .__/ \___|    |_|_|  \___|_| |_|\___|_| |_|')
    print ('                      | |                                          ')
    print ('                      |_|                                          ')

 
    time.sleep(2)
    print('Huh ? Where am I ? WHY AM I WET ?')
    time.sleep(2)
    choice=raw_input('Tyler wakes up confused. Should he get up ? (Y/IDK)')
    if choice == 'Y':
        print('He wanders in the large trench')
    if choice == 'IDK': 
        choice=raw_input('OH YEAH ? IM GETTING UP ANYWAYS. I DON\'T WANT TO DIE. Shall we continue ? (Y/N)')
        time.sleep(1)
    print('Welp...time to investigate!')
    time.sleep(3)
    choice=raw_input('Tyler looks up. BaNDItoS ? Do you continue walking ? (Y/N)')
    while choice != 'Y' and choice !='N':
        choice=raw_input('Invalid Answer. Try again(Y/N)')
    if choice == 'N':
        choice=raw_input('You suddenly trip on rocks and crack your head open.')
        time.sleep(1)
        print('Oh no ! Looks like you have died from excessive blood loss !')
        time.sleep(1) ('You have failed to escape trench.')
        return
    else: #you chose Y
        print ('You continue to walk. In the distance you see a bishop.' )
        time.sleep(1)
        print ('He charges at you. Your first impulse is to shut your eyes.')
        time.sleep(2)
        print ('A few seconds pass. Nothing happens. Do you open your eyes ? (Y)')
        if choice == 'y':
               print('The bishop is a few feet away from you. He orders to follow him. You have no choice.')
        time.sleep(2)
        print ('You begin to follow him and stop when out of the corner of your eye you see yellow flower petals falling from the sky.')
        time.sleep(3)
        choice=raw_input('BANDITOS !! They startle the horse and bishop. nOW IS YOUR CHANCE TO ESCAPE. DO YOU TAKE IT AND RUN ? (Y/N)')
        if choice == 'Y':
            print('You sprint away from the Bishop but he goes right after you')
            time.sleep(2)
            print('You keep running as fast as you can but soon, you run out of breath and trip in the rocky creek.')
            time.sleep(1)
            print('You don\'t have the strength to get up and you pass out')
            time.sleep(2)
            print('What will happen next ??? Will Tyler escape or will Bishop Nico lock him up? Was he able to escape trench? Stay tuned because we\'ll win but not everyone will get out...')
            return
        elif choice == 'N':
            choice=raw_input ('The bishop takes you and locks you away with no way for the banditos to find you.')
            print('WaRnINg. Failed Perimeter Escape. You are now trapped in Trench')
            return