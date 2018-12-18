from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import send_image_url
from utils import send_button_message
from gp import candidate
from gp import opinionPoll



class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    

    def is_going_to_state1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '市長'
        return False

    def on_enter_state1(self, event):
        print("I'm entering state1")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "請選擇欲查詢的縣市")
        #self.go_back()

    # def on_exit_state1(self):
    #     print('Leaving state1')    





    def is_going_to_state2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '議員'
        return False

    def on_enter_state2(self, event):
        print("I'm entering state2")

        sender_id = event['sender']['id']
        #send_text_message(sender_id, "I'm entering state2")
        #print(candidate('http://vote.2018.nat.gov.tw/pc/zh_TW/T1/s63000030000000000.html'))
        #send_image_url(sender_id, "https://i.imgur.com/TD6h7i9.png")
        responese = send_text_message(sender_id, "請選擇欲查詢的縣市")
        #send_image_url(sender_id, candidate('http://vote.2018.nat.gov.tw/pc/zh_TW/T1/s63000030000000000.html'))
        

    def is_going_to_TaipeiRepresentative(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '台北市'
        return False

    def on_enter_TaipeiRepresentative(self, event):
        print("I'm entering TaipeiRepresentative")



        
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "請選擇欲查詢的選區")
        #send_button_message(sender_id, "請選擇欲查詢的選區", button)

        
    def is_going_to_TaipeiRepresentative1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '1'
        return False

    def on_enter_TaipeiRepresentative1(self, event):
        print("I'm entering TaipeiRepresentative1")

        sender_id = event['sender']['id']
        send_image_url(sender_id, candidate('http://vote.2018.nat.gov.tw/pc/zh_TW/T1/s63000010000000000.html','台北市士林北投區議員候選人得票數'))
        self.go_back()

    def is_going_to_TaipeiRepresentative2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '2'
        return False

    def on_enter_TaipeiRepresentative2(self, event):
        print("I'm entering TaipeiRepresentative")

        sender_id = event['sender']['id']
        send_image_url(sender_id, candidate('http://vote.2018.nat.gov.tw/pc/zh_TW/T1/s63000020000000000.html','台北市南港內湖區議員候選人得票數'))
        self.go_back()

    def is_going_to_TaipeiRepresentative3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '3'
        return False

    def on_enter_TaipeiRepresentative3(self, event):
        print("I'm entering TaipeiRepresentative")

        sender_id = event['sender']['id']
        send_image_url(sender_id, candidate('http://vote.2018.nat.gov.tw/pc/zh_TW/T1/s63000030000000000.html','台北市松山信義區議員候選人得票數'))
        self.go_back()        



    



    def is_going_to_KaohsiungRepresentative(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '高雄市'
        return False 

    def on_enter_KaohsiungRepresentative(self, event):
        print("I'm entering KaohsiungRepresentative")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "請選擇欲查詢的選區")


    def is_going_to_KaohsiungRepresentative1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '1'
        return False

    def on_enter_KaohsiungRepresentative1(self, event):
        print("I'm entering KaohsiungRepresentative1")

        sender_id = event['sender']['id']
        send_image_url(sender_id, candidate('http://vote.2018.nat.gov.tw/pc/zh_TW/T1/s64000010000000000.html','高雄市旗美六地區議員候選人得票數'))
        self.go_back()

    def is_going_to_KaohsiungRepresentative2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '2'
        return False

    def on_enter_KaohsiungRepresentative2(self, event):
        print("I'm entering KaohsiungRepresentative")

        sender_id = event['sender']['id']
        send_image_url(sender_id, candidate('http://vote.2018.nat.gov.tw/pc/zh_TW/T1/s64000020000000000.html','高雄市路竹地區議員候選人得票數'))
        self.go_back()

    def is_going_to_KaohsiungRepresentative3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '3'
        return False

    def on_enter_KaohsiungRepresentative3(self, event):
        print("I'm entering KaohsiungRepresentative")

        sender_id = event['sender']['id']
        send_image_url(sender_id, candidate('http://vote.2018.nat.gov.tw/pc/zh_TW/T1/s64000030000000000.html','高雄市岡山地區候選人得票數'))
        self.go_back()       




    def is_going_to_state3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '公投白話文'
        return False



    def on_enter_state3(self, event):
        print("I'm entering state3")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "請選擇欲參考的白話文")
        
       

    


    def is_going_to_TaipeiMayor(self, event):
        if event.get("message"):
            text = event['message']['text']
            global city
            city = text
            return text.lower() == '台北市' or text.lower() == '基隆市' or text.lower() == '新北市' or text.lower() == '桃園市' or text.lower() == '新竹市' or text.lower() == '新竹縣' or text.lower() == '苗栗縣' or text.lower() == '台中市' or text.lower() == '彰化縣' or text.lower() == '南投縣' or text.lower() == '雲林縣' or text.lower() == '嘉義市' or text.lower() == '嘉義縣' or text.lower() == '台南市' or text.lower() == '高雄市' or text.lower() == '屏東縣' or text.lower() == '台東縣' or text.lower() == '花蓮縣' or text.lower() == '宜蘭縣' or text.lower() == '澎湖縣' or text.lower() == '金門縣' or text.lower() == '連江縣'
        return False


    def on_enter_TaipeiMayor(self, event):
        print("I'm entering TaipeiMayor")
        global city

        if city == '基隆市':
            toChoose = 's10017000000000000.html'
        if city == '台北市':
            toChoose = 's63000000000000000.html'
        if city == '新北市':
            toChoose = 's65000000000000000.html'
        if city == '桃園市':
            toChoose = 's68000000000000000.html'
        if city == '新竹市':
            toChoose = 's10018000000000000.html'
        if city == '新竹縣':
            toChoose = 's10004000000000000.html'
        if city == '苗栗縣':
            toChoose = 's10005000000000000.html'
        if city == '台中市':
            toChoose = 's66000000000000000.html'
        if city == '彰化縣':
            toChoose = 's10007000000000000.html'
        if city == '南投縣':
            toChoose = 's10008000000000000.html'
        if city == '雲林縣':
            toChoose = 's10009000000000000.html'
        if city == '嘉義市':
            toChoose = 's10020000000000000.html'
        if city == '嘉義縣':
            toChoose = 's10010000000000000.html'
        if city == '台南市':
            toChoose = 's67000000000000000.html'
        if city == '高雄市':
            toChoose = 's64000000000000000.html'
        if city == '屏東縣':
            toChoose = 's10013000000000000.html'
        if city == '台東縣':
            toChoose = 's10014000000000000.html'
        if city == '花蓮縣':
            toChoose = 's10015000000000000.html'
        if city == '宜蘭縣':
            toChoose = 's10002000000000000.html'
        if city == '澎湖縣':
            toChoose = 's10016000000000000.html'
        if city == '金門縣':
            toChoose = 's09020000000000000.html'
        if city == '連江縣':
            toChoose = 's09007000000000000.html'
        
        
        ur = 'http://vote.2018.nat.gov.tw/pc/zh_TW/TC/' + toChoose

        tp = city + '市長候選人得票數'


        sender_id = event['sender']['id']
        send_image_url(sender_id, candidate(ur,tp))
        self.go_back()

    def on_exit_TaipeiMayor(self):
        print('Leaving TaipeiMayor')



    

    


    def is_going_to_Referendum14(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '14'
        return False



    def on_enter_Referendum14(self, event):
        print("I'm entering Referendum14")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "如果同意")
        send_text_message(sender_id, "將於民法婚姻章擴充配偶定義以規範同性婚姻，公投通過將保障同性婚姻納入民法，權利義務與現行一夫一妻相同。")
        send_text_message(sender_id, "如果反對")
        send_text_message(sender_id, "同志婚姻將有可能以專法形式呈現。")


    def is_going_to_Referendum14Agree(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '同意'
        return False



    def on_enter_Referendum14Agree(self, event):
        print("I'm entering Referendum14")

        sender_id = event['sender']['id']
        send_image_url(sender_id,opinionPoll('14','agree','是否同意'+'\n'+'以民法婚姻章保障同性別二人建立婚姻関係'))
        
        self.go_back()

    def is_going_to_Referendum14Oppose(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '反對'
        return False



    def on_enter_Referendum14Oppose(self, event):
        print("I'm entering Referendum14")

        sender_id = event['sender']['id']
        send_image_url(sender_id,opinionPoll('14','oppose','是否同意'+'\n'+'以民法婚姻章保障同性別二人建立婚姻関係'))
        self.go_back()
        
    ############################################
    def is_going_to_Referendum15(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '15'
        return False



    def on_enter_Referendum15(self, event):
        print("I'm entering Referendum15")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "如果同意")
        send_text_message(sender_id, "主張性別教育應確實包含情感教育、性教育、尊重同志教育。公投案若通過，將使以上三者由「細則」提升到「法律」")
        send_text_message(sender_id, "如果反對")
        send_text_message(sender_id, "維持現狀，仍以性平法細則呈現")


    def is_going_to_Referendum15Agree(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '同意'
        return False



    def on_enter_Referendum15Agree(self, event):
        print("I'm entering Referendum15")

        sender_id = event['sender']['id']
        send_image_url(sender_id,opinionPoll('15','agree','是否同意，以『性別平等教育法』'+'\n'+'明定在國民教育各階段實施性別平等教育'+'\n'+'且應涵蓋情感教育.性教育.同志教育等課程'))
        
        self.go_back()

    def is_going_to_Referendum15Oppose(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '反對'
        return False



    def on_enter_Referendum15Oppose(self, event):
        print("I'm entering Referendum15")

        sender_id = event['sender']['id']
        send_image_url(sender_id,opinionPoll('15','oppose','是否同意，以『性別平等教育法』'+'\n'+'明定在國民教育各階段實施性別平等教育'+'\n'+'且應涵蓋情感教育.性教育.同志教育等課程'))
        self.go_back()
    


      