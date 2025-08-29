import os
import time

players: dict = {} #{개별 인원 : 원별 지불해야 할 금액}
tasks: dict = {} #{지불해야할 건 : 총 금액}
amounts: dict = {} #추후 지불해야 할 건과 그에 따른 금액을 출력하거나 수정할 때 사용될 금액 리스트
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

    if not players:
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

        if not tasks[task]:
            print(f"Warning: No members were added to task '{task}'. This task will be removed.")        
            del tasks[task]
            continue
        
        while True:
            try:
                amount = int(input('\rEnter Amount: '))
                correct = input('Is Correct? (Y/n): ')
                if correct.lower() in ['y','']:
                    break
            except ValueError:
                print('input error: amount must be integer')
        amounts[task] = amount
        split = amount/len(tasks[task])
        for member in tasks[task]:
            players[member] += split


    for task, members in tasks.items():
        print(task,': ',members,', ',amounts[task],'원')

    bill = "Bill"
    text = bill.center(width,'=')
    print('\n',text)
    for player in players:
        print(f"{player}: {players[player]:.0f}")
if __name__=="__main__":
    main()