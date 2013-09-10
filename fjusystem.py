# encoding: utf-8
import getpass
import sys
import telnetlib
import time

def big5(str):
    return str.decode('utf-8', 'ignore').encode('big5', 'ignore')

def up(num):
    for i in range(num):
        tn.write("i")
def down(num):
    for i in range(num):
        tn.write("m")
def right(num):
    for i in range(num):
        tn.write("k")

print big5("輔仁大學搶課系統-by YunChen")
print big5("Facebook:https://www.facebook.com/Alex.YunChen")
print big5("純粹做好玩給自己用來搶課而已，沒UI、懶的Debug...ps:所以輸入錯誤會卡住")
print big5("【請先輸入您的選課帳號及密碼再進行下一步】")
print "\r"

HOST = "signcourse.fju.edu.tw"
user = raw_input("User: ")
password = getpass.getpass()
print "\r"
print big5("[進]中文   [進]全英聽 [日]服飾銷 [日]化學   [研]音樂   [研]織品   [研]資工 \n"+
           "[進]歷史   [進]全自科 [日]餐旅   [日]資工   [研]應美   [研]餐旅   [研]生科 \n"+
           "[進]哲學   [進]全人藝 [日]兒家   [日]生科   [研]景觀   [研]兒家   [研]應工 \n"+
           "[進]企管   [進]全社科 [日]服飾設 [日]物理   [研]音樂組 [研]食科   [研]電機 \n"+
           "[進]金融國 [進]軍訓   [日]食科   [日]光電   [研]演奏組 [研]營養   [研]非營利 \n"+
           "[進]大傳   [日]音樂   [日]營養   [日]電通組 [研]中文   [研]傳研   [研]心理 \n"+
           "[進]運管   [日]應美   [日]影傳   [日]天主教 [研]歷史   [研]法律   [研]社會 \n"+
           "[進]商管   [日]景觀   [日]新傳   [日]心理   [研]哲學   [研]財法   [研]社工 \n"+
           "[進]文創   [日]中文   [日]廣告   [日]社會   [研]長照   [研]體育   [研]經濟 \n"+
           "[進]軟創   [日]歷史   [日]法律   [日]社工   [研]護理   [研]圖資   [研]宗教 \n"+
           "[進]圖資   [日]哲學   [日]財法   [日]經濟   [研]公衛   [研]教育   [研]院外語 \n"+
           "[進]英文   [日]護理   [日]學士後 [日]宗教   [研]臨心   [研]企管   [研]學程 \n"+
           "[進]日文   [日]公衛   [日]圖資   [日]院外語 [研]基礎醫 [研]金融   [技]護理二 \n"+
           "[進]數學   [日]醫學   [日]體育學 [日]院理工 [研]語言   [研]國際經 \n"+
           "[進]餐管   [日]臨心   [日]競技   [日]進階英 [研]翻譯   [研]社企 \n"+
           "[進]經濟   [日]職治   [日]運管   [日]教學程 [研]比研   [研]會計 \n"+
           "[進]法律   [日]呼吸治 [日]企管   [日]學程   [研]英文   [研]資管 \n"+
           "[進]會計   [日]英文   [日]金融國 [日]體育   [研]法文   [研]應統 \n"+
           "[進]統資   [日]法文   [日]會計   [日]全國文 [研]西文   [研]商學 \n"+
           "[進]應美   [日]西文   [日]資管   [日]全外語 [研]日文   [研]科管 \n"+
           "[進]宗教   [日]日文   [日]統資   [日]全自科 [研]德語   [研]國創 \n"+
           "[進]體育   [日]義大利 [日]系晶組 [日]全人藝 [研]食營   [研]物理 \n"+
           "[進]全國文 [日]德語   [日]純數   [日]全社科 [研]品牌時 [研]化學 \n"+
           "[進]全外語 [日]織品設 [日]應數   [日]軍訓   [研]博館   [研]數學 \n")
print "\r"
print big5("【請輸入您想選課的系所 例如:日 資工】")
course = raw_input(big5("請輸入系所:"))
print "\r"
print big5("【請輸入您想搶是該系所的第幾門課 例如:2】")
print big5("【可先上telnet://signcourse.fju.edu.tw 進入你想選課的系所*由上往下數*】")
print big5("【因帳號無法重覆登入，填入課堂順序前記得先將telnet的程序先關閉】")
number = int(raw_input(big5("請輸入課堂順序:")))
print "\r"
while True:
    print big5("開始連線到: ") + HOST +"..."
    tn = telnetlib.Telnet(HOST)
    print big5("已成功連線到: ") + HOST
    print big5("開始登入學生系統[selcou]...")
    tn.read_until("login",10)  
    tn.write("selcou" + "\r")
    tn.read_until("Password",10) 
    tn.write("\r")
    print big5("已成功連線學生系統")

    print big5("快速略過系統公告")
    tn.read_until(big5("系統公告："),10)
    tn.write("\r")
    tn.read_until(big5("注意！"),10)
    tn.write("\r")
    tn.read_until(big5("畫面操作注意事項："),10)
    tn.write("\r")

    decide = True
    key = ""
    print big5("開始擷取驗證密碼...")
    while decide:    
        string = tn.read_very_eager()
        if big5("簽名密碼：") in string:
            key_start = string.find(big5("簽名密碼："))+20
            key = string[key_start : key_start+4]
            print big5("本次登入的驗證碼為: ") + key
            decide = False
    print big5("輸入驗證碼...")
    tn.write(key + "\r")
    print big5("驗證成功")

    print big5("開始登入個人選課帳號...")
    tn.read_until("===",10)
    tn.write(user + "\r")
    tn.write(password + "\r") 
    print big5("登入成功")

    print big5("載入加選科目介面...")
    tn.read_until(big5("輔大網路選課資訊系統"),10)
    tn.write("\r")
    tn.read_until(big5("(進)中文"),10)
    tn.write("\r")
    decide = True
    data = ""
    while decide:    
        string = tn.read_very_eager()
        if big5("確定選修或必修後才真正選到該門課") in string:
            data_start = string.find(big5("("))
            data = string[data_start : data_start+9]        
            decide = False
    tn.write("q")
    tn.write("\r")
    tn.read_until(big5("(進)中文"),10)
    if data == big5("(進)中文 "):
        pass
    elif data == big5("(進)歷史 "):
        up(1)
    elif data == big5("(進)哲學 "):
        up(2)
    elif data == big5("(進)企管 "):
        up(3)
    elif data == big5("(進)金融國"):
        up(4)
    elif data == big5("(進)大傳 "):
        up(5)
    elif data == big5("(進)運管 "):
        up(6)
    elif data == big5("(進)商管 "):
        up(7)
    elif data == big5("(進)文創 "):
        up(8)
    elif data == big5("(進)軟創 "):
        up(9)
    elif data == big5("(進)圖資 "):
        up(10)
    elif data == big5("(進)英文 "):
        up(11)
    elif data == big5("(進)日文 "):
        up(12)
    elif data == big5("(進)數學 "):
        up(13)
    elif data == big5("(進)餐管 "):
        up(14)
    elif data == big5("(進)經濟 "):
        up(15)
    elif data == big5("(進)法律 "):
        up(16)
    elif data == big5("(進)會計 "):
        up(17)
    elif data == big5("(進)統資 "):
        up(18)
    elif data == big5("(進)應美 "):
        up(19)
    elif data == big5("(進)宗教 "):
        up(20)
    elif data == big5("(進)體育 "):
        up(21)
    elif data == big5("(進)全國文"):
        up(22)
    elif data == big5("(進)全外語"):
        up(23)
    elif data == big5("(進)全英聽"):
        right(6)
    elif data == big5("(進)全自科"):
        up(1)
        right(6)
    elif data == big5("(進)全人藝"):
        up(2)
        right(6)
    elif data == big5("(進)全社科"):
        up(3)
        right(6)
    elif data == big5("(進)軍訓 "):
        up(4)
        right(6)
    elif data == big5("(日)音樂 "):
        up(5)
        right(6)
    elif data == big5("(日)應美 "):
        up(6)
        right(6)
    elif data == big5("(日)景觀 "):
        up(7)
        right(6)
    elif data == big5("(日)中文 "):
        up(8)
        right(6)
    elif data == big5("(日)歷史 "):
        up(9)
        right(6)
    elif data == big5("(日)哲學 "):
        up(10)
        right(6)
    elif data == big5("(日)護理 "):
        up(11)
        right(6)
    elif data == big5("(日)公衛 "):
        up(12)
        right(6)
    elif data == big5("(日)醫學 "):
        up(13)
        right(6)
    elif data == big5("(日)臨心 "):
        up(14)
        right(6)
    elif data == big5("(日)職治 "):
        up(15)
        right(6)
    elif data == big5("(日)呼吸治"):
        up(16)
        right(6)
    elif data == big5("(日)英文 "):
        up(17)
        right(6)
    elif data == big5("(日)法文 "):
        up(18)
        right(6)
    elif data == big5("(日)西文 "):
        up(19)
        right(6)
    elif data == big5("(日)日文 "):
        up(20)
        right(6)
    elif data == big5("(日)義大利"):
        up(21)
        right(6)
    elif data == big5("(日)德語 "):
        up(22)
        right(6)
    elif data == big5("(日)織品設"):
        up(23)
        right(6)
    elif data == big5("(日)服飾銷"):
        right(5)
    elif data == big5("(日)餐旅 "):
        up(1)
        right(5)
    elif data == big5("(日)兒家 "):
        up(2)
        right(5)
    elif data == big5("(日)服飾設"):
        up(3)
        right(5)
    elif data == big5("(日)食科 "):
        up(4)
        right(5)
    elif data == big5("(日)營養 "):
        up(5)
        right(5)
    elif data == big5("(日)影傳 "):
        up(6)
        right(5)
    elif data == big5("(日)新傳 "):
        up(7)
        right(5)
    elif data == big5("(日)廣告 "):
        up(8)
        right(5)
    elif data == big5("(日)法律 "):
        up(9)
        right(5)
    elif data == big5("(日)財法 "):
        up(10)
        right(5)
    elif data == big5("(日)學士後"):
        up(11)
        right(5)
    elif data == big5("(日)圖資 "):
        up(12)
        right(5)
    elif data == big5("(日)體育學"):
        up(13)
        right(5)
    elif data == big5("(日)競技 "):
        up(14)
        right(5)
    elif data == big5("(日)運管 "):
        up(15)
        right(5)
    elif data == big5("(日)企管 "):
        up(16)
        right(5)
    elif data == big5("(日)金融國"):
        up(17)
        right(5)
    elif data == big5("(日)會計 "):
        up(18)
        right(5)
    elif data == big5("(日)資管 "):
        up(19)
        right(5)
    elif data == big5("(日)統資 "):
        up(20)
        right(5)
    elif data == big5("(日)系晶組"):
        up(21)
        right(5)
    elif data == big5("(日)純數 "):
        up(22)
        right(5)
    elif data == big5("(日)應數 "):
        up(23)
        right(5)
    elif data == big5("(日)化學 "):
        right(4)
    elif data == big5("(日)資工 "):
        up(1)
        right(4)
    elif data == big5("(日)生科 "):
        up(2)
        right(4)
    elif data == big5("(日)物理 "):
        up(3)
        right(4)
    elif data == big5("(日)光電 "):
        up(4)
        right(4)
    elif data == big5("(日)電通組"):
        up(5)
        right(4)
    elif data == big5("(日)天主教"):
        up(6)
        right(4)
    elif data == big5("(日)心理 "):
        up(7)
        right(4)
    elif data == big5("(日)社會 "):
        up(8)
        right(4)
    elif data == big5("(日)社工 "):
        up(9)
        right(4)
    elif data == big5("(日)經濟 "):
        up(10)
        right(4)
    elif data == big5("(日)宗教 "):
        up(11)
        right(4)
    elif data == big5("(日)院外語"):
        up(12)
        right(4)
    elif data == big5("(日)院理工"):
        up(13)
        right(4)
    elif data == big5("(日)進階英"):
        up(14)
        right(4)
    elif data == big5("(日)教學程"):
        up(15)
        right(4)
    elif data == big5("(日)學程 "):
        up(16)
        right(4)
    elif data == big5("(日)體育 "):
        up(17)
        right(4)
    elif data == big5("(日)全國文"):
        up(18)
        right(4)
    elif data == big5("(日)全外語"):
        up(19)
        right(4)
    elif data == big5("(日)全自科"):
        up(20)
        right(4)
    elif data == big5("(日)全人藝"):
        up(21)
        right(4)
    elif data == big5("(日)全社科"):
        up(22)
        right(4)
    elif data == big5("(日)軍訓 "):
        up(23)
        right(4)
    elif data == big5("(研)音樂 "):
        right(3)
    elif data == big5("(研)應美 "):
        up(1)
        right(3)
    elif data == big5("(研)景觀 "):
        up(2)
        right(3)
    elif data == big5("(研)音樂組"):
        up(3)
        right(3)
    elif data == big5("(研)演奏組"):
        up(4)
        right(3)
    elif data == big5("(研)中文 "):
        up(5)
        right(3)
    elif data == big5("(研)歷史 "):
        up(6)
        right(3)
    elif data == big5("(研)哲學 "):
        up(7)
        right(3)
    elif data == big5("(研)長照 "):
        up(8)
        right(3)
    elif data == big5("(研)護理 "):
        up(9)
        right(3)
    elif data == big5("(研)公衛 "):
        up(10)
        right(3)
    elif data == big5("(研)臨心 "):
        up(11)
        right(3)
    elif data == big5("(研)基礎醫"):
        up(12)
        right(3)
    elif data == big5("(研)語言 "):
        up(13)
        right(3)
    elif data == big5("(研)翻譯 "):
        up(14)
        right(3)
    elif data == big5("(研)比研 "):
        up(15)
        right(3)
    elif data == big5("(研)英文 "):
        up(16)
        right(3)
    elif data == big5("(研)法文 "):
        up(17)
        right(3)
    elif data == big5("(研)西文 "):
        up(18)
        right(3)
    elif data == big5("(研)日文 "):
        up(19)
        right(3)
    elif data == big5("(研)德語 "):
        up(20)
        right(3)
    elif data == big5("(研)食營 "):
        up(21)
        right(3)
    elif data == big5("(研)品牌時"):
        up(22)
        right(3)
    elif data == big5("(研)博館 "):
        up(23)
        right(3)
    elif data == big5("(研)織品 "):
        right(2)
    elif data == big5("(研)餐旅 "):
        up(1)
        right(2)
    elif data == big5("(研)兒家 "):
        up(2)
        right(2)
    elif data == big5("(研)食科 "):
        up(3)
        right(2)
    elif data == big5("(研)營養 "):
        up(4)
        right(2)
    elif data == big5("(研)傳研 "):
        up(5)
        right(2)
    elif data == big5("(研)法律 "):
        up(6)
        right(2)
    elif data == big5("(研)財法 "):
        up(7)
        right(2)
    elif data == big5("(研)體育 "):
        up(8)
        right(2)
    elif data == big5("(研)圖資 "):
        up(9)
        right(2)
    elif data == big5("(研)教育 "):
        up(10)
        right(2)
    elif data == big5("(研)企管 "):
        up(11)
        right(2)
    elif data == big5("(研)金融 "):
        up(12)
        right(2)
    elif data == big5("(研)國際經"):
        up(13)
        right(2)
    elif data == big5("(研)社企 "):
        up(14)
        right(2)
    elif data == big5("(研)會計 "):
        up(15)
        right(2)
    elif data == big5("(研)資管 "):
        up(16)
        right(2)
    elif data == big5("(研)應統 "):
        up(17)
        right(2)
    elif data == big5("(研)商學 "):
        up(18)
        right(2)
    elif data == big5("(研)科管 "):
        up(19)
        right(2)
    elif data == big5("(研)國創 "):
        up(20)
        right(2)
    elif data == big5("(研)物理 "):
        up(21)
        right(2)
    elif data == big5("(研)化學 "):
        up(22)
        right(2)
    elif data == big5("(研)數學 "):
        up(23)
        right(2)
    elif data == big5("(研)資工 "):
        right(1)
    elif data == big5("(研)生科 "):
        up(1)
        right(1)
    elif data == big5("(研)應工 "):
        up(2)
        right(1)
    elif data == big5("(研)電機 "):
        up(3)
        right(1)
    elif data == big5("(研)非營利"):
        up(4)
        right(1)
    elif data == big5("(研)心理 "):
        up(5)
        right(1)
    elif data == big5("(研)社會 "):
        up(6)
        right(1)
    elif data == big5("(研)社工 "):
        up(7)
        right(1)
    elif data == big5("(研)經濟 "):
        up(8)
        right(1)
    elif data == big5("(研)宗教 "):
        up(9)
        right(1)
    elif data == big5("(研)院外語"):
        up(10)
        right(1)
    elif data == big5("(研)學程 "):
        up(11)
        right(1)
    else:
        up(12)
        right(1)

    if course == big5("進 中文"):    
        tn.write("\r")
    elif course == big5("進 歷史"):
        down(1)
        tn.write("\r")
    elif course == big5("進 哲學"):
        down(2)
        tn.write("\r")
    elif course == big5("進 企管"):
        down(3)
        tn.write("\r")
    elif course == big5("進 金融國"):
        down(4)
        tn.write("\r")
    elif course == big5("進 大傳"):
        down(5)
        tn.write("\r")
    elif course == big5("進 運管"):
        down(6)
        tn.write("\r")
    elif course == big5("進 商管"):
        down(7)
        tn.write("\r")
    elif course == big5("進 文創"):
        down(8)
        tn.write("\r")
    elif course == big5("進 軟創"):
        down(9)
        tn.write("\r")
    elif course == big5("進 圖資"):
        down(10)
        tn.write("\r")
    elif course == big5("進 英文"):
        down(11)
        tn.write("\r")
    elif course == big5("進 日文"):
        down(12)
        tn.write("\r")
    elif course == big5("進 數學"):
        down(13)
        tn.write("\r")
    elif course == big5("進 餐管"):
        down(14)
        tn.write("\r")
    elif course == big5("進 經濟"):
        down(15)
        tn.write("\r")
    elif course == big5("進 法律"):
        down(16)
        tn.write("\r")
    elif course == big5("進 會計"):
        down(17)
        tn.write("\r")
    elif course == big5("進 統資"):
        down(18)
        tn.write("\r")
    elif course == big5("進 應美"):
        down(19)
        tn.write("\r")
    elif course == big5("進 宗教"):
        down(20)
        tn.write("\r")
    elif course == big5("進 體育"):
        down(21)
        tn.write("\r")
    elif course == big5("進 全國文"):
        down(22)
        tn.write("\r")
    elif course == big5("進 全外語"):
        down(23)
        tn.write("\r")
    elif course == big5("進 全英聽"):
        right(1)
        tn.write("\r")
    elif course == big5("進 全自科"):
        right(1)
        down(1)
        tn.write("\r")
    elif course == big5("進 全人藝"):
        right(1)
        down(2)
        tn.write("\r")
    elif course == big5("進 全社科"):
        right(1)
        down(3)
        tn.write("\r")
    elif course == big5("進 軍訓"):
        right(1)
        down(4)
        tn.write("\r")
    elif course == big5("日 音樂"):
        right(1)
        down(5)
        tn.write("\r")
    elif course == big5("日 應美"):
        right(1)
        down(6)
        tn.write("\r")
    elif course == big5("日 景觀"):
        right(1)
        down(7)
        tn.write("\r")
    elif course == big5("日 中文"):
        right(1)
        down(8)
        tn.write("\r")
    elif course == big5("日 歷史"):
        right(1)
        down(9)
        tn.write("\r")
    elif course == big5("日 哲學"):
        right(1)
        down(10)
        tn.write("\r")
    elif course == big5("日 護理"):
        right(1)
        down(11)
        tn.write("\r")
    elif course == big5("日 公衛"):
        right(1)
        down(12)
        tn.write("\r")
    elif course == big5("日 醫學"):
        right(1)
        down(13)
        tn.write("\r")
    elif course == big5("日 臨心"):
        right(1)
        down(14)
        tn.write("\r")
    elif course == big5("日 職治"):
        right(1)
        down(15)
        tn.write("\r")
    elif course == big5("日 呼吸治"):
        right(1)
        down(16)
        tn.write("\r")
    elif course == big5("日 英文"):
        right(1)
        down(17)
        tn.write("\r")
    elif course == big5("日 法文"):
        right(1)
        down(18)
        tn.write("\r")
    elif course == big5("日 西文"):
        right(1)
        down(19)
        tn.write("\r")
    elif course == big5("日 日文"):
        right(1)
        down(20)
        tn.write("\r")
    elif course == big5("日 義大利"):
        right(1)
        down(21)
        tn.write("\r")
    elif course == big5("日 德語"):
        right(1)
        down(22)
        tn.write("\r")
    elif course == big5("日 織品設"):
        right(1)
        down(23)
        tn.write("\r")
    elif course == big5("日 服飾銷"):
        right(2)
        tn.write("\r")
    elif course == big5("日 餐旅"):
        right(2)
        down(1)
        tn.write("\r")
    elif course == big5("日 兒家"):
        right(2)
        down(2)
        tn.write("\r")
    elif course == big5("日 服飾設"):
        right(2)
        down(3)
        tn.write("\r")
    elif course == big5("日 食科"):
        right(2)
        down(4)
        tn.write("\r")
    elif course == big5("日 營養"):
        right(2)
        down(5)
        tn.write("\r")
    elif course == big5("日 影傳"):
        right(2)
        down(6)
        tn.write("\r")
    elif course == big5("日 新傳"):
        right(2)
        down(7)
        tn.write("\r")
    elif course == big5("日 廣告"):
        right(2)
        down(8)
        tn.write("\r")
    elif course == big5("日 法律"):
        right(2)
        down(9)
        tn.write("\r")
    elif course == big5("日 財法"):
        right(2)
        down(10)
        tn.write("\r")
    elif course == big5("日 學士後"):
        right(2)
        down(11)
        tn.write("\r")
    elif course == big5("日 圖資"):
        right(2)
        down(12)
        tn.write("\r")
    elif course == big5("日 體育學"):
        right(2)
        down(13)
        tn.write("\r")
    elif course == big5("日 競技"):
        right(2)
        down(14)
        tn.write("\r")
    elif course == big5("日 運管"):
        right(2)
        down(15)
        tn.write("\r")
    elif course == big5("日 企管"):
        right(2)
        down(16)
        tn.write("\r")
    elif course == big5("日 金融國"):
        right(2)
        down(17)
        tn.write("\r")
    elif course == big5("日 會計"):
        right(2)
        down(18)
        tn.write("\r")
    elif course == big5("日 資管"):
        right(2)
        down(19)
        tn.write("\r")
    elif course == big5("日 統資"):
        right(2)
        down(20)
        tn.write("\r")
    elif course == big5("日 系晶組"):
        right(2)
        down(21)
        tn.write("\r")
    elif course == big5("日 純數"):
        right(2)
        down(22)
        tn.write("\r")
    elif course == big5("日 應數"):
        right(2)
        down(23)
        tn.write("\r")
    elif course == big5("日 化學"):
        right(3)
        tn.write("\r")
    elif course == big5("日 資工"):
        right(3)
        down(1)
        tn.write("\r")
    elif course == big5("日 生科"):
        right(3)
        down(2)
        tn.write("\r")
    elif course == big5("日 物理"):
        right(3)
        down(3)
        tn.write("\r")
    elif course == big5("日 光電"):
        right(3)
        down(4)
        tn.write("\r")
    elif course == big5("日 電通組"):
        right(3)
        down(5)
        tn.write("\r")
    elif course == big5("日 天主教"):
        right(3)
        down(6)
        tn.write("\r")
    elif course == big5("日 心理"):
        right(3)
        down(7)
        tn.write("\r")
    elif course == big5("日 社會"):
        right(3)
        down(8)
        tn.write("\r")
    elif course == big5("日 社工"):
        right(3)
        down(9)
        tn.write("\r")
    elif course == big5("日 經濟"):
        right(3)
        down(10)
        tn.write("\r")
    elif course == big5("日 宗教"):
        right(3)
        down(11)
        tn.write("\r")
    elif course == big5("日 院外語"):
        right(3)
        down(12)
        tn.write("\r")
    elif course == big5("日 院理工"):
        right(3)
        down(13)
        tn.write("\r")
    elif course == big5("日 進階英"):
        right(3)
        down(14)
        tn.write("\r")
    elif course == big5("日 教學程"):
        right(3)
        down(15)
        tn.write("\r")
    elif course == big5("日 學程"):
        right(3)
        down(16)
        tn.write("\r")
    elif course == big5("日 體育"):
        right(3)
        down(17)
        tn.write("\r")
    elif course == big5("日 全國文"):
        right(3)
        down(18)
        tn.write("\r")
    elif course == big5("日 全外語"):
        right(3)
        down(19)
        tn.write("\r")
    elif course == big5("日 全自科"):
        right(3)
        down(20)
        tn.write("\r")
    elif course == big5("日 全人藝"):
        right(3)
        down(21)
        tn.write("\r")
    elif course == big5("日 全社科"):
        right(3)
        down(22)
        tn.write("\r")
    elif course == big5("日 軍訓"):
        right(3)
        down(23)
        tn.write("\r")
    elif course == big5("研 音樂"):
        right(4)
        tn.write("\r")
    elif course == big5("研 應美"):
        right(4)
        down(1)
        tn.write("\r")
    elif course == big5("研 景觀"):
        right(4)
        down(2)
        tn.write("\r")
    elif course == big5("研 音樂組"):
        right(4)
        down(3)
        tn.write("\r")
    elif course == big5("研 演奏組"):
        right(4)
        down(4)
        tn.write("\r")
    elif course == big5("研 中文"):
        right(4)
        down(5)
        tn.write("\r")
    elif course == big5("研 歷史"):
        right(4)
        down(6)
        tn.write("\r")
    elif course == big5("研 哲學"):
        right(4)
        down(7)
        tn.write("\r")
    elif course == big5("研 長照"):
        right(4)
        down(8)
        tn.write("\r")
    elif course == big5("研 護理"):
        right(4)
        down(9)
        tn.write("\r")
    elif course == big5("研 公衛"):
        right(4)
        down(10)
        tn.write("\r")
    elif course == big5("研 臨心"):
        right(4)
        down(11)
        tn.write("\r")
    elif course == big5("研 基礎醫"):
        right(4)
        down(12)
        tn.write("\r")
    elif course == big5("研 語言"):
        right(4)
        down(13)
        tn.write("\r")
    elif course == big5("研 翻譯"):
        right(4)
        down(14)
        tn.write("\r")
    elif course == big5("研 比研"):
        right(4)
        down(15)
        tn.write("\r")
    elif course == big5("研 英文"):
        right(4)
        down(16)
        tn.write("\r")
    elif course == big5("研 法文"):
        right(4)
        down(17)
        tn.write("\r")
    elif course == big5("研 西文"):
        right(4)
        down(18)
        tn.write("\r")
    elif course == big5("研 日文"):
        right(4)
        down(19)
        tn.write("\r")
    elif course == big5("研 德語"):
        right(4)
        down(20)
        tn.write("\r")
    elif course == big5("研 食營"):
        right(4)
        down(21)
        tn.write("\r")
    elif course == big5("研 品牌時"):
        right(4)
        down(22)
        tn.write("\r")
    elif course == big5("研 博館"):
        right(4)
        down(23)
        tn.write("\r")
    elif course == big5("研 織品"):
        right(5)
        tn.write("\r")
    elif course == big5("研 餐旅"):
        right(5)
        down(1)
        tn.write("\r")
    elif course == big5("研 兒家"):
        right(5)
        down(2)
        tn.write("\r")
    elif course == big5("研 食科"):
        right(5)
        down(3)
        tn.write("\r")
    elif course == big5("研 營養"):
        right(5)
        down(4)
        tn.write("\r")
    elif course == big5("研 傳研"):
        right(5)
        down(5)
        tn.write("\r")
    elif course == big5("研 法律"):
        right(5)
        down(6)
        tn.write("\r")
    elif course == big5("研 財法"):
        right(5)
        down(7)
        tn.write("\r")
    elif course == big5("研 體育"):
        right(5)
        down(8)
        tn.write("\r")
    elif course == big5("研 圖資"):
        right(5)
        down(9)
        tn.write("\r")
    elif course == big5("研 教育"):
        right(5)
        down(10)
        tn.write("\r")
    elif course == big5("研 企管"):
        right(5)
        down(11)
        tn.write("\r")
    elif course == big5("研 金融"):
        right(5)
        down(12)
        tn.write("\r")
    elif course == big5("研 國際經"):
        right(5)
        down(13)
        tn.write("\r")
    elif course == big5("研 社企"):
        right(5)
        down(14)
        tn.write("\r")
    elif course == big5("研 會計"):
        right(5)
        down(15)
        tn.write("\r")
    elif course == big5("研 資管"):
        right(5)
        down(16)
        tn.write("\r")
    elif course == big5("研 應統"):
        right(5)
        down(17)
        tn.write("\r")
    elif course == big5("研 商學"):
        right(5)
        down(18)
        tn.write("\r")
    elif course == big5("研 科管"):
        right(5)
        down(19)
        tn.write("\r")
    elif course == big5("研 國創"):
        right(5)
        down(20)
        tn.write("\r")
    elif course == big5("研 物理"):
        right(5)
        down(21)
        tn.write("\r")
    elif course == big5("研 化學"):
        right(5)
        down(22)
        tn.write("\r")
    elif course == big5("研 數學"):
        right(5)
        down(23)
        tn.write("\r")
    elif course == big5("研 資工"):
        right(6)
        tn.write("\r")
    elif course == big5("研 生科"):
        right(6)
        down(1)
        tn.write("\r")
    elif course == big5("研 應工"):
        right(6)
        down(2)
        tn.write("\r")
    elif course == big5("研 電機"):
        right(6)
        down(3)
        tn.write("\r")
    elif course == big5("研 非營利"):
        right(6)
        down(4)
        tn.write("\r")
    elif course == big5("研 心理"):
        right(6)
        down(5)
        tn.write("\r")
    elif course == big5("研 社會"):
        right(6)
        down(6)
        tn.write("\r")
    elif course == big5("研 社工"):
        right(6)
        down(7)
        tn.write("\r")
    elif course == big5("研 經濟"):
        right(6)
        down(8)
        tn.write("\r")
    elif course == big5("研 宗教"):
        right(6)
        down(9)
        tn.write("\r")
    elif course == big5("研 院外語"):
        right(6)
        down(10)
        tn.write("\r")
    elif course == big5("研 學程"):
        right(6)
        down(11)
        tn.write("\r")
    else:
        right(6)
        down(12)
        tn.write("\r")

    print big5("載入課堂介面...")
    tn.read_until(big5("確定選修或必修後才真正選到該門課"),10)
    print big5("載入成功")
    downnum = number -1
    if number == 1 or number == 0:
        pass
    else:
        down(downnum)
    ttime = 0
    while True:
        if ttime == 1000:
            break
        tn.write("\r")
        time.sleep(0.5)
        ttime = ttime + 1
        string = tn.read_very_eager()
        if big5("重覆！") in string:
            print big5("已成功搶到課堂 or 已擁有此課程")
            break
        else:
            print big5("未選入此課程，繼續重新嘗試")
            tn.write("\r")
    if ttime == 1000:
        continue
    else:
        print big5("Bye")
        break
