

import random

lotto_num = range(1,46)

for i in range(5):
    print(random.sample(lotto_num,6))
#여기까지 코드 작성을 마쳤다면 커밋을 실시하자.
#tkinter 버튼으로 로또번호 생성하기
#이제 버튼을 누르면 로또번호 생성이 진행되도록 main.py 의 코드를 아래와 같이 수정하자.
import tkinter
import tkinter.font
import random
lotto_num = range(1,46)

def buttonClick():
    label = tkinter.Label(window, text=str(random.sample(lotto_num,6)))
    label.pack()

 #print(random.sample(lotto_num,6))
    
    
window=tkinter.Tk()
window.title("lotto")
window.geometry("400x200")
window.resizable(False, False)

button = tkinter.Button(window, overrelief="solid",text="번호확인", width=15, command=buttonClick, repeatdelay=1000, repeatinterval=100)
button.pack()

    
    
    
window.mainloop()



































    