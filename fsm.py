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
        send_image_url(sender_id, "https://i.imgur.com/TD6h7i9.png")
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
        
    def is_going_to_TaipeiRepresentative1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '1'
        return False

    def on_enter_TaipeiRepresentative1(self, event):
        print("I'm entering TaipeiRepresentative1")

        sender_id = event['sender']['id']
        send_image_url(sender_id, candidate('http://vote.2018.nat.gov.tw/pc/zh_TW/T1/s63000010000000000.html'))
        self.go_back()

    def is_going_to_TaipeiRepresentative2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '2'
        return False

    def on_enter_TaipeiRepresentative2(self, event):
        print("I'm entering TaipeiRepresentative")

        sender_id = event['sender']['id']
        send_image_url(sender_id, candidate('http://vote.2018.nat.gov.tw/pc/zh_TW/T1/s63000020000000000.html'))
        self.go_back()

    def is_going_to_TaipeiRepresentative3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '3'
        return False

    def on_enter_TaipeiRepresentative3(self, event):
        print("I'm entering TaipeiRepresentative")

        sender_id = event['sender']['id']
        send_image_url(sender_id, candidate('http://vote.2018.nat.gov.tw/pc/zh_TW/T1/s63000030000000000.html'))
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
        send_image_url(sender_id, candidate('http://vote.2018.nat.gov.tw/pc/zh_TW/T1/s64000010000000000.html'))
        self.go_back()

    def is_going_to_KaohsiungRepresentative2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '2'
        return False

    def on_enter_KaohsiungRepresentative2(self, event):
        print("I'm entering KaohsiungRepresentative")

        sender_id = event['sender']['id']
        send_image_url(sender_id, candidate('http://vote.2018.nat.gov.tw/pc/zh_TW/T1/s64000020000000000.html'))
        self.go_back()

    def is_going_to_KaohsiungRepresentative3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '3'
        return False

    def on_enter_KaohsiungRepresentative3(self, event):
        print("I'm entering KaohsiungRepresentative")

        sender_id = event['sender']['id']
        send_image_url(sender_id, candidate('http://vote.2018.nat.gov.tw/pc/zh_TW/T1/s64000030000000000.html'))
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
            return text.lower() == '台北市'
        return False


    def on_enter_TaipeiMayor(self, event):
        print("I'm entering TaipeiMayor")

        sender_id = event['sender']['id']
        send_image_url(sender_id, candidate('http://vote.2018.nat.gov.tw/pc/zh_TW/TC/s63000000000000000.html'))
        self.go_back()

    def on_exit_TaipeiMayor(self):
        print('Leaving TaipeiMayor')



    

    def is_going_to_KaohsiungMayor(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '高雄市'
        return False    


    def on_enter_KaohsiungMayor(self, event):
        print("I'm entering KaohsiungMayor")

        sender_id = event['sender']['id']
        send_image_url(sender_id, candidate('http://vote.2018.nat.gov.tw/pc/zh_TW/TC/s64000000000000000.html'))
        self.go_back()

    def on_exit_KaohsiungMayor(self):
        print('Leaving KaohsiungMayor')



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
        send_image_url(sender_id,opinionPoll('14','agree','是否同意'+'\n'+'以民法婚姻章保障同性別二人建立婚姻關係'))
        #send_image_url(sender_id, "https://i.imgur.com/TD6h7i9.png")
        self.go_back()

    def is_going_to_Referendum14Oppose(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '反對'
        return False



    def on_enter_Referendum14Oppose(self, event):
        print("I'm entering Referendum14")

        sender_id = event['sender']['id']
        send_image_url(sender_id,opinionPoll('14','oppose','是否同意'+'\n'+'以民法婚姻章保障同性別二人建立婚姻關係'))
        self.go_back()
        
    

    


      