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

    def is_going_to_tutorial(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() != '市長' and text.lower() != '議員' and text.lower() != '公投白話文'
        return False

    def on_enter_tutorial(self, event):
        print("I'm entering tutorial")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "歡迎使用選舉哪回事Chat Bot!")
        responese = send_text_message(sender_id, "你可以輸入「市長」查看各縣市市長得票情形")
        responese = send_text_message(sender_id, "也可以輸入「議員」查看各縣市議員得票情形")
        responese = send_text_message(sender_id, "覺得公投題目看不懂也可以輸入「公投白話文」為您解惑")
        self.go_back()

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
            global number
            number = text
            return text.lower() == '7' or text.lower() == '8' or text.lower() == '9' or text.lower() == '10' or text.lower() == '11' or text.lower() == '12' or text.lower() == '13' or text.lower() == '14' or text.lower() == '15' or text.lower() == '16' 
        return False



    def on_enter_Referendum14(self, event):
        print("I'm entering Referendum14")

        sender_id = event['sender']['id']
        global number
        if number == '7':
            send_text_message(sender_id, "如果同意")
            send_text_message(sender_id, "每年必須調降1%火力發電比例")
            send_text_message(sender_id, "如果反對")
            send_text_message(sender_id, "維持現狀，並從2017年的84.4%降至2025年80%")
        if number == '8':
            send_text_message(sender_id, "如果同意")
            send_text_message(sender_id, "不再新建、擴建燃煤電廠或機組")
            send_text_message(sender_id, "如果反對")
            send_text_message(sender_id, "持續新建、擴建")
        if number == '9':
            send_text_message(sender_id, "如果同意")
            send_text_message(sender_id, "維持現有食安標準，禁止日本核災地區食品進口")
            send_text_message(sender_id, "如果反對")
            send_text_message(sender_id, "未來將有可能開放核食")
        if number == '10':
            send_text_message(sender_id, "如果同意")
            send_text_message(sender_id, "主張婚姻限定在一男一女，明確定義婚姻是一男一女")
            send_text_message(sender_id, "如果反對")
            send_text_message(sender_id, "立法者可以選擇修改民法婚姻章或是另立專法，以保障同性者可以結婚")
        if number == '11':
            send_text_message(sender_id, "如果同意")
            send_text_message(sender_id, "刪除性平法細則「同志教育」字樣，國中小將避談同志的性平教育")
            send_text_message(sender_id, "如果反對")
            send_text_message(sender_id, "維持現狀，保留尊重同志內容")
        if number == '12':
            send_text_message(sender_id, "如果同意")
            send_text_message(sender_id, "將於民法婚姻章擴充配偶定義以規範同性婚姻，公投通過將保障同性婚姻納入民法，權利義務與現行一夫一妻相同。")
            send_text_message(sender_id, "如果反對")
            send_text_message(sender_id, "同志婚姻將有可能以專法形式呈現。")
        if number == '13':
            send_text_message(sender_id, "如果同意")
            send_text_message(sender_id, "主張以民法外的方式，規範同性結合的權利義務。(立同婚專法)")
            send_text_message(sender_id, "如果反對")
            send_text_message(sender_id, "同志婚姻將於民法中進行修改")
        if number == '14':
            send_text_message(sender_id, "如果同意")
            send_text_message(sender_id, "將於民法婚姻章擴充配偶定義以規範同性婚姻，公投通過將保障同性婚姻納入民法，權利義務與現行一夫一妻相同。")
            send_text_message(sender_id, "如果反對")
            send_text_message(sender_id, "同志婚姻將有可能以專法形式呈現。")
        if number == '15':
            send_text_message(sender_id, "如果同意")
            send_text_message(sender_id, "主張性別教育應確實包含情感教育、性教育、尊重同志教育。公投案若通過，將使以上三者由「細則」提升到「法律」")
            send_text_message(sender_id, "如果反對")
            send_text_message(sender_id, "維持現狀，仍以性平法細則呈現")
        if number == '16':
            send_text_message(sender_id, "如果同意")
            send_text_message(sender_id, "保留核電，以作為轉型過度的基礎電力。")
            send_text_message(sender_id, "如果反對")
            send_text_message(sender_id, "維持現狀，於2025年全面廢止核能發電。")


    def is_going_to_Referendum14Agree(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '同意'
        return False



    def on_enter_Referendum14Agree(self, event):
        print("I'm entering Referendum14")
        global number
        if number == '7':
            top = '是否同意'+'\n'+'以平均每年至少降低1%之方式'+'\n'+'逐年降低火力發電廠發電量'
        if number == '9':
            top = '是否同意'+'\n'+'政府維持禁止開放'+'\n'+'日本福島311核災相関地區農產品及食品進口'
        if number == '8':
            top = '是否同意'+'\n'+'確立停止新建、擴建'+'\n'+'任何燃煤發電廠或發電機組(包括深澳電廠擴建)之能源政策'
        if number == '10':
            top = '是否同意'+'\n'+'民法婚姻規定應限定在一男一女的結合'
        if number == '11':
            top = '是否同意'+'\n'+'在國民教育階段內(國中及國小)'+'\n'+'教育部及各級學校不應對學生實施性別平等教育法施行細則所定之同志教育'
        if number == '12':
            top = '是否同意'+'\n'+'以民法婚姻規定以外之其他形式'+'\n'+'來保障同性別二人經營永久共同生活的權益'
        if number == '13':
            top = '是否同意'+'\n'+' 以「台灣」(taiwan)為全名'+'\n'+'申請參加所有國際運動賽事及2020年東京奧運'
        if number == '14':
            top = '是否同意'+'\n'+'以民法婚姻章保障同性別二人建立婚姻関係'
        if number == '15':
            top = '是否同意，以『性別平等教育法』'+'\n'+'明定在國民教育各階段實施性別平等教育'+'\n'+'且應涵蓋情感教育.性教育.同志教育等課程'
        if number == '16':
            top = '是否同意'+'\n'+'廢除電業法「核能發電設備'+'\n'+'應於中華民國114年以前全部停止運轉」之條文?'

        sender_id = event['sender']['id']
        send_image_url(sender_id,opinionPoll(number,'agree',top))
        
        self.go_back()

    def is_going_to_Referendum14Oppose(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '反對'
        return False



    def on_enter_Referendum14Oppose(self, event):
        print("I'm entering Referendum14")

        global number
        if number == '7':
            top = '是否同意'+'\n'+'以平均每年至少降低1%之方式'+'\n'+'逐年降低火力發電廠發電量'
        if number == '9':
            top = '是否同意'+'\n'+'政府維持禁止開放'+'\n'+'日本福島311核災相関地區農產品及食品進口'
        if number == '8':
            top = '是否同意'+'\n'+'確立停止新建、擴建'+'\n'+'任何燃煤發電廠或發電機組(包括深澳電廠擴建)之能源政策'
        if number == '10':
            top = '是否同意'+'\n'+'民法婚姻規定應限定在一男一女的結合'
        if number == '11':
            top = '是否同意'+'\n'+'在國民教育階段內(國中及國小)'+'\n'+'教育部及各級學校不應對學生實施性別平等教育法施行細則所定之同志教育'
        if number == '12':
            top = '是否同意'+'\n'+'以民法婚姻規定以外之其他形式'+'\n'+'來保障同性別二人經營永久共同生活的權益'
        if number == '13':
            top = '是否同意'+'\n'+' 以「台灣」(taiwan)為全名'+'\n'+'申請參加所有國際運動賽事及2020年東京奧運'
        if number == '14':
            top = '是否同意'+'\n'+'以民法婚姻章保障同性別二人建立婚姻関係'
        if number == '15':
            top = '是否同意，以『性別平等教育法』'+'\n'+'明定在國民教育各階段實施性別平等教育'+'\n'+'且應涵蓋情感教育.性教育.同志教育等課程'
        if number == '16':
            top = '是否同意'+'\n'+'廢除電業法「核能發電設備'+'\n'+'應於中華民國114年以前全部停止運轉」之條文?'

        sender_id = event['sender']['id']
        send_image_url(sender_id,opinionPoll(number,'oppose',top))
        self.go_back()
        

    


    