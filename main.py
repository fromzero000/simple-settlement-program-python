import os
import time

players: dict = {} #{개별 인원 : 원별 지불해야 할 금액}
tasks: dict = {} #{지불해야할 건 : 총 금액}
amounts: list = []
width = os.get_terminal_size().columns

def main():
    print('Settlement Init',end='\r')
    time.sleep (1)
    #인원 입력
    while True:
        name = input('\rEnter the player name(Press Enter key to quit): ')
        if name == '':
            break
        elif name in players.keys():
            print('input error: player already exists')
        else:
            players[name] = 0

    if players.keys() == []:
        return
    print('Initialized')
    print('players:',end=' ')
    for player in players:
        print(player, end=' ')
    
    #인원 입력 종료
    print('\nStart Settlement')
    while True:
        task = input('\rEnter Task(Press Enter key to quit): ')
        if task == '':
            break
        elif task in tasks.keys():
            print('input error: task already exists')
        else:
            tasks[task] = []
            while True:
                member = input('\rEnter Member(Press Enter key to quit): ')
                if member == '':
                    break
                elif member in tasks[task]:
                    print('input error: member already exists')
                elif member not in players:
                    print('input error: player not exists')
                else:
                    tasks[task].append(member)
                
        amount = int(input('\rEnter Amount: '))
        while input('Is Correct?(Press y to Yes or n to No): ') not in ['Y', 'y','']:
            print('Retry\r')
            amount = int(input('\rEnter Amount: '))
        split = amount/len(tasks[task])
        for member in tasks[task]:
            players[member] += split


    for task, members in tasks.items():
        print(task,': ',members)

    bill = "Bill"
    text = bill.center(width,'=')
    print('\n',text)
    for player in players:
        print(f"{player}: {players[player]:.0f}")
if __name__=="__main__":
    main()