from transitions.extensions import GraphMachine

from utils import send_text_message
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod
import requests
import numpy as np
class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
        # self.machine.get_graph().draw("123.png", prog= 'dot')
        
        

    def is_going_to_game_info(self, event):
        text = event.message.text
        return text.lower() == "show game information"
    
    def on_enter_game_info(self, event):
        response = requests.get(pleague)
        soup = BeautifulSoup(response.text, "html.parser")
        result = soup.find_all("h6",limit=60)
        date = soup.find_all("span",class_="text-light fs14",limit=60)
        place = soup.find_all("span",class_="text-light fs12",limit=60)
        # game1 = date[0].getText() + "\n" + place[0].getText() + "\n" + result[1].getText() + result[2].getText() + result[3].getText();
        # game2 = date[1].getText() + "\n" + place[1].getText() + "\n" + result[4].getText() + result[5].getText() + result[6].getText();
        # game3 = date[2].getText() + "\n" + place[2].getText() + "\n" + result[7].getText() + result[8].getText() + result[9].getText();
        # game4 = date[3].getText() + "\n" + place[3].getText() + "\n" + result[10].getText() + result[11].getText() + result[12].getText();
        # game5 = date[4].getText() + "\n" + place[4].getText() + "\n" + result[13].getText() + result[14].getText() + result[15].getText();
        # game6 = date[5].getText() + "\n" + place[5].getText() + "\n" + result[16].getText() + result[17].getText() + result[18].getText();
        # game7 = date[6].getText() + "\n" + place[6].getText() + "\n" + result[19].getText() + result[20].getText() + result[21].getText();
        # game8 = date[7].getText() + "\n" + place[7].getText() + "\n" + result[22].getText() + result[23].getText() + result[24].getText();
        # game9 = date[8].getText() + "\n" + place[8].getText() + "\n" + result[25].getText() + result[26].getText() + result[27].getText();
        # game10 = date[9].getText() + "\n" + place[9].getText() + "\n" + result[28].getText() + result[29].getText() + result[30].getText();
        # game11 = date[10].getText() + "\n" + place[10].getText() + "\n" + result[31].getText() + result[32].getText() + result[33].getText();
        # game12 = date[11].getText() + "\n" + place[11].getText() + "\n" + result[34].getText() + result[35].getText() + result[36].getText();
        # game13 = date[12].getText() + "\n" + place[12].getText() + "\n" + result[37].getText() + result[38].getText() + result[39].getText();
        # game14 = date[13].getText() + "\n" + place[13].getText() + "\n" + result[40].getText() + result[41].getText() + result[42].getText();
        # game15 = date[14].getText() + "\n" + place[14].getText() + "\n" + result[43].getText() + result[44].getText() + result[45].getText();
        # game16 = date[15].getText() + "\n" + place[15].getText() + "\n" + result[46].getText() + result[47].getText() + result[48].getText();
        #ggg = game1 + "\n\n"+game2+"\n\n"+game3+"\n\n"+game4+"\n\n"+game5+"\n\n"+game6+"\n\n"+game7+"\n\n"+game8+"\n\n"+game9+"\n\n"+game10+"\n\n"+game11+"\n\n"+game12+"\n\n"+game13+"\n\n"+game14+"\n\n"+game15+"\n\n"+game16
        print(date[1].getText())
        print(place[1].getText()) 
        reply_token = event.reply_token
        send_text_message(reply_token, ggg) #一次印完
        #self.go_back()
        
    def is_going_to_statsleaderinfo(self, event):
        text = event.message.text
        return text.lower() == "show stats leader"
    
    def on_enter_stats_leader_info(self, event):
        print("I'm entering stats leader")
        reply_token = event.reply_token
        send_text_message(reply_token, "please enter the stats you want to know\n(point/rebound/assist)") #一次印完
        #self.go_back()
    
    def is_going_to_teams_info(self, event):
        text = event.message.text
        return text.lower() == "show team information"
    
    def on_enter_teams_info(self,event):
        print("I'm entering teams information")
        reply_token = event.reply_token
        send_text_message(reply_token, "please enter the team you want to know") #一次印完
        #self.go_back()
    def is_going_to_kings(self,event):
        text = event.message.text
        return text.lower() == "kings"
    
    def on_enter_kings(self, event):
        print("show kings information")
        response = requests.get(team_stats)
        soup = BeautifulSoup(response.text, "html.parser")
        result = soup.find_all("tr",limit=60)
        st = "[" + result[0].th.getText()+"]:  "+result[1].th.getText() + "\n********************************\n"
        title_st = result[0].select("th")
        stats_st = result[1].select("td")
        for q in range(1,21):
            st = st + "\n[" + title_st[q].getText()+"]:  "+stats_st[q-1].getText()+"\n********************************\n" 
        reply_token = event.reply_token
        send_text_message(reply_token, st) #一次印完
        self.go_back_teams()
        
    def is_going_to_braves(self,event):
        text = event.message.text
        return text.lower() == "braves"
    
    def on_enter_braves(self, event):
        print("show braves information")
        response = requests.get(team_stats)
        soup = BeautifulSoup(response.text, "html.parser")
        result = soup.find_all("tr",limit=60)
        st = "[" + result[0].th.getText()+"]:  "+result[3].th.getText()+"\n********************************\n"
        title_st = result[0].select("th")
        stats_st = result[3].select("td")
        for q in range(1,21):
            st = st + "\n[" + title_st[q].getText()+"]:  "+stats_st[q-1].getText() +"\n********************************\n"
        reply_token = event.reply_token
        send_text_message(reply_token, st) #一次印完
        self.go_back_teams()
        
    def is_going_to_lioneers(self,event):
        text = event.message.text
        return text.lower() == "lioneers"
    def on_enter_lioneers(self, event):
        print("show lioneers information")
        response = requests.get(team_stats)
        soup = BeautifulSoup(response.text, "html.parser")
        result = soup.find_all("tr",limit=60)
        st = "[" + result[0].th.getText()+"]:  "+result[2].th.getText()+"\n********************************\n"
        title_st = result[0].select("th")
        stats_st = result[2].select("td")
        for q in range(1,21):
            st = st + "\n[" + title_st[q].getText()+"]:  "+stats_st[q-1].getText() + "\n********************************\n"
        reply_token = event.reply_token
        send_text_message(reply_token, st) #一次印完
        self.go_back_teams()
    def is_going_to_pilots(self,event):
        text = event.message.text
        return text.lower() == "pilots"
    def on_enter_pilots(self, event):
        print("show pilots information")
        response = requests.get(team_stats)
        soup = BeautifulSoup(response.text, "html.parser")
        result = soup.find_all("tr",limit=60)
        st = "[" + result[0].th.getText()+"]:  "+result[6].th.getText()+"\n********************************\n"
        title_st = result[0].select("th")
        stats_st = result[6].select("td")
        for q in range(1,21):
            st = st + "\n[" + title_st[q].getText()+"]:  "+stats_st[q-1].getText() +"\n********************************\n"
        reply_token = event.reply_token
        send_text_message(reply_token, st) #一次印完
        self.go_back_teams()
    def is_going_to_dreamers(self,event):
        text = event.message.text
        return text.lower() == "dreamers"
    def on_enter_dreamers(self, event):
        print("show dreamers information")
        response = requests.get(team_stats)
        soup = BeautifulSoup(response.text, "html.parser")
        result = soup.find_all("tr",limit=60)
        st = "[" + result[0].th.getText()+"]:  "+result[4].th.getText()+"\n********************************\n"
        title_st = result[0].select("th")
        stats_st = result[4].select("td")
        for q in range(1,21):
            st = st + "\n[" + title_st[q].getText()+"]:  "+stats_st[q-1].getText() +"\n********************************\n"
        reply_token = event.reply_token
        send_text_message(reply_token, st) #一次印完
        self.go_back_teams()
    def is_going_to_steelers(self,event):
        text = event.message.text
        return text.lower() == "steelers"
    def on_enter_steelers(self, event):
        print("show steelers information")
        response = requests.get(team_stats)
        soup = BeautifulSoup(response.text, "html.parser")
        result = soup.find_all("tr",limit=60)
        st = "[" + result[0].th.getText()+"]:  "+result[5].th.getText()+"\n********************************\n"
        title_st = result[0].select("th")
        stats_st = result[5].select("td")
        for q in range(1,21):
            st = st + "\n[" + title_st[q].getText()+"]:  "+stats_st[q-1].getText() + "\n********************************\n"
        reply_token = event.reply_token
        send_text_message(reply_token, st) #一次印完
        self.go_back_teams()
    def is_going_to_rank_info(self, event):
        text = event.message.text
        return text.lower() == "show rank information"

    def on_enter_rank_info(self, event):
        print("I'm entering rank information")
        response = requests.get(pleague)
        soup = BeautifulSoup(response.text, "html.parser")
        result = soup.find_all("tr",limit=7)
        #print(result[1])
        zero = "     "
        first = ""
        sec = ""
        third = ""
        forth = ""
        fifth = ""
        sixth = ""
        title_st = result[0].select("th")
        stats_st1 = result[1].select("td")
        stats_st2 = result[2].select("td")
        stats_st3 = result[3].select("td")
        stats_st4 = result[4].select("td")
        stats_st5 = result[5].select("td")
        stats_st6 = result[6].select("td")
        for q in range(1,7):
            if len(title_st[q].getText().split()[0]) == 2 and q==1:
                t_add0 = title_st[q].getText().split()[0] + "                     "
            else:
                t_add0 = title_st[q].getText().split()[0]
            
            if len(stats_st1[q-1].getText()) == 4 and q == 1:
                t_add1 = stats_st1[q-1].getText() + "                    "
            elif len(stats_st1[q-1].getText()) == 7 and q == 1:
                t_add1 = stats_st1[q-1].getText() + "        "
            elif len(stats_st1[q-1].getText()) == 6 and q == 1:
                t_add1 = stats_st1[q-1].getText() + "            "
            elif len(stats_st1[q-1].getText()) == 5 and q == 1:
                t_add1 = stats_st1[q-1].getText() + "                "
            elif len(stats_st1[q-1].getText()) == 9 and q == 1:
                t_add1 = stats_st1[q-1].getText()
            else :
                t_add1 = stats_st1[q-1].getText()
            
            
            if len(stats_st2[q-1].getText()) == 4 and q == 1:
                t_add2 = stats_st2[q-1].getText() + "                    "
            elif len(stats_st2[q-1].getText()) == 7 and q == 1:
                t_add2 = stats_st2[q-1].getText() + "        "
            elif len(stats_st2[q-1].getText()) == 6 and q == 1:
                t_add2 = stats_st2[q-1].getText() + "            "
            elif len(stats_st2[q-1].getText()) == 5 and q == 1:
                t_add2 = stats_st2[q-1].getText() + "                "
            elif len(stats_st2[q-1].getText()) == 9 and q == 1:
                t_add2 = stats_st2[q-1].getText()
            else :
                t_add2 = stats_st2[q-1].getText()
                
            if len(stats_st3[q-1].getText()) == 4 and q == 1:
                t_add3 = stats_st3[q-1].getText() + "                    "
            elif len(stats_st3[q-1].getText()) == 7 and q == 1:
                t_add3 = stats_st3[q-1].getText() + "        "
            elif len(stats_st3[q-1].getText()) == 6 and q == 1:
                t_add3 = stats_st3[q-1].getText() + "            "
            elif len(stats_st3[q-1].getText()) == 5 and q == 1:
                t_add3 = stats_st3[q-1].getText() + "                "
            elif len(stats_st3[q-1].getText()) == 9 and q == 1:
                t_add3 = stats_st3[q-1].getText()
            else :
                t_add3 = stats_st3[q-1].getText()
                
            if len(stats_st4[q-1].getText()) == 4 and q == 1:
                t_add4 = stats_st4[q-1].getText() + "                    "
            elif len(stats_st4[q-1].getText()) == 7 and q == 1:
                t_add4 = stats_st4[q-1].getText() + "        "
            elif len(stats_st4[q-1].getText()) == 6 and q == 1:
                t_add4 = stats_st4[q-1].getText() + "            "
            elif len(stats_st4[q-1].getText()) == 5 and q == 1:
                t_add4 = stats_st4[q-1].getText() + "                "
            elif len(stats_st4[q-1].getText()) == 9 and q == 1:
                t_add4 = stats_st4[q-1].getText()
            else :
                t_add4 = stats_st4[q-1].getText()
                
            if len(stats_st5[q-1].getText()) == 4 and q == 1:
                t_add5 = stats_st5[q-1].getText() + "                    "
            elif len(stats_st5[q-1].getText()) == 7 and q == 1:
                t_add5 = stats_st5[q-1].getText() + "        "
            elif len(stats_st5[q-1].getText()) == 6 and q == 1:
                t_add5 = stats_st5[q-1].getText() + "            "
            elif len(stats_st5[q-1].getText()) == 5 and q == 1:
                t_add5 = stats_st5[q-1].getText() + "                "
            elif len(stats_st5[q-1].getText()) == 9 and q == 1:
                t_add5 = stats_st5[q-1].getText()
            else :
                t_add5 = stats_st5[q-1].getText()
                
            if len(stats_st6[q-1].getText()) == 4 and q == 1:
                t_add6 = stats_st6[q-1].getText() + "                    "
            elif len(stats_st6[q-1].getText()) == 7 and q == 1:
                t_add6 = stats_st6[q-1].getText() + "        "
            elif len(stats_st6[q-1].getText()) == 6 and q == 1:
                t_add6 = stats_st6[q-1].getText() + "            "
            elif len(stats_st6[q-1].getText()) == 5 and q == 1:
                t_add6 = stats_st6[q-1].getText() + "                "
            elif len(stats_st6[q-1].getText()) == 9 and q == 1:
                t_add6 = stats_st6[q-1].getText()
            else :
                t_add6 = stats_st6[q-1].getText()
            if q==1:    
                zero = zero + t_add0 + "      "
                first = first + t_add1 + "   "
                sec = sec + t_add2 + "   "
                third = third + t_add3 + "   "
                forth = forth + t_add4 + "   "
                fifth = fifth + t_add5 + "   "
                sixth = sixth + t_add6 + "   "
            elif q==5:
                zero = zero + t_add0 + "        "
                first = first + t_add1 + "       "
                sec = sec + t_add2 + "         "
                third = third + t_add3 + "         "
                forth = forth + t_add4 + "         "
                fifth = fifth + t_add5 + "         "
                sixth = sixth + t_add6 + "          "
            else:
                zero = zero + t_add0 + "      "
                first = first + t_add1 + "         "
                sec = sec + t_add2 + "         "
                third = third + t_add3 + "         "
                forth = forth + t_add4 + "         "
                fifth = fifth + t_add5 + "         "
                sixth = sixth + t_add6 + "         "
        st = "                        Please use horizontal mode to watch!!!\n**************************************************************\n" + zero+ "\n**************************************************************\n" + "1. "+first + "\n**************************************************************\n" +"2. "+ sec + "\n**************************************************************\n" +"3. "+ third + "\n**************************************************************\n" +"4. "+ forth + "\n**************************************************************\n" +"5. "+ fifth + "\n**************************************************************\n" +"6. "+ sixth
        reply_token = event.reply_token
        send_text_message(reply_token, st) #一次印完
        #self.go_back()
        
    def is_going_to_choose_player(self, event):
        text = event.message.text
        return text.lower() == "show player information"
    
    def on_enter_choose_player(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "enter the player you want to know") #一次印完
        
    def is_going_to_player_info(self, event):
        global player  
        player = event.message.text
        if len(player)>0 and len(player)<6:
            return 1
        else:
            return 0
    
    def on_enter_player_info(self, event):
        global player 
        flag = 0
        st = "[名字]:  "+player+"\n********************************\n"
        response = requests.get(player_stats)
        soup = BeautifulSoup(response.text, "html.parser")
        result = soup.find_all("tr",limit=300)
        reply_token = event.reply_token
        for q in range(1,300):
            if result[q].select_one("th").a.getText() == player:
                #st = st + result[q].select_one("th").a.getText()+"\n"
                # print(result[q].select_one("th").a.getText())
                playerinfo = result[q].select("td")
                st = st + "[背號]:  "+ playerinfo[0].getText()+"\n********************************\n"
                st = st + "[球隊]:  "+playerinfo[1].getText()+"\n********************************\n"
                st = st + "[出賽次數]:  "+playerinfo[2].getText()+"\n********************************\n"
                st = st + "[時間(分)]:  "+playerinfo[3].getText()+"\n********************************\n"
                st = st + "[兩分命中]:  "+playerinfo[4].getText()+"\n********************************\n"
                st = st + "[兩分出手]:  "+playerinfo[5].getText()+"\n********************************\n"
                st = st + "[兩分%]:  "+playerinfo[6].getText()+"\n********************************\n"
                st = st + "[三分命中]:  "+playerinfo[7].getText()+"\n********************************\n"
                st = st + "[三分出手]:  "+playerinfo[8].getText()+"\n********************************\n"
                st = st + "[三分%]:  "+playerinfo[9].getText()+"\n********************************\n"
                st = st + "[罰球命中]:  "+playerinfo[10].getText()+"\n********************************\n"
                st = st + "[罰球出手]:  "+playerinfo[11].getText()+"\n********************************\n"
                st = st + "[罰球%]:  "+playerinfo[12].getText()+"\n********************************\n"
                st = st + "[得分]:  "+playerinfo[13].getText()+"\n********************************\n"
                st = st + "[進攻籃板]:  "+playerinfo[14].getText()+"\n********************************\n"
                st = st + "[防守籃板]:  "+playerinfo[15].getText()+"\n********************************\n"
                st = st + "[籃板]:  "+playerinfo[16].getText()+"\n********************************\n"
                st = st + "[助攻]:  "+playerinfo[17].getText()+"\n********************************\n"
                st = st + "[抄截]:  "+playerinfo[18].getText()+"\n********************************\n"
                st = st + "[阻攻]:  "+playerinfo[19].getText()+"\n********************************\n"
                st = st + "[失誤]:  "+playerinfo[20].getText()+"\n********************************\n"
                st = st + "[犯規]:  "+playerinfo[21].getText()+"\n********************************"
                reply_token = event.reply_token
                send_text_message(reply_token,st) #一次印完
                self.go_back_player()
                #flag = 1
                #break
                # return
            #reply_token = event.reply_token
            # if flag == 1:
            #     send_text_message(reply_token,st)
            # else:
            #     send_text_message(reply_token,"the player not exist in P League") #一次印完
            # self.go_back_player()
            
    
    
    # def is_going_to_gameinfodate(self, event):
    #     text = event.message.text
    #     return text.lower() == "show game information (date)"
    
    # def on_enter_gameinfodate(self, event):
    #     #print("I'm entering state1")
    #     #爬蟲
    #     reply_token = event.reply_token
    #     send_text_message(reply_token, "\n12/20") #一次印完
    #     #self.go_back()
    
    def is_going_to_point_leader(self, event):
        text = event.message.text
        return text.lower() == "point"
    
    def on_enter_point_leader(self, event):
        print("show point leader\n")
        response = requests.get(pleague)
        soup = BeautifulSoup(response.text, "html.parser")
        result = soup.find_all("td","font-weight-bold",limit=15)
        st = "" 
        num = [result[6].find_next_siblings("td"),result[7].find_next_siblings("td"),result[8].find_next_siblings("td"),result[9].find_next_siblings("td"),result[10].find_next_siblings("td"),result[11].find_next_siblings("td"),result[12].find_next_siblings("td"),result[13].find_next_siblings("td")] 
        for q in range(6,14):
            if len(result[q].a.getText())==2:
                t_add = result[q].a.getText()+"     "
            elif len(result[q].a.getText())==3:
                t_add = result[q].a.getText()+" "
            st = st  + str(q-5) + ". " + t_add + "   " + num[q-6][1].getText() + "\n********************************\n"
        #st = result[6].a.getText() + "   " + num1[1].getText() + "\n" + result[7].a.getText() + "   " + num2[1].getText() + "\n" +  result[8].a.getText() + "   " + num3[1].getText() + "\n" + result[9].a.getText() + "   " + num4[1].getText() + "\n" + result[10].a.getText() + "   " + num5[1].getText() + "\n" + result[11].a.getText() +"   " + num6[1].getText() + "\n" + result[12].a.getText() +"   " + num7[1].getText() + "\n" + result[13].a.getText() + "   " + num8[1].getText()
        reply_token = event.reply_token
        send_text_message(reply_token,st) #一次印完
        self.go_back()
    
    def is_going_to_assist_leader(self, event):
        text = event.message.text
        return text.lower() == "assist"
    
    def on_enter_assist_leader(self, event):
        print("show assist leader")
        response = requests.get(pleague)
        soup = BeautifulSoup(response.text, "html.parser")
        result = soup.find_all("td","font-weight-bold",limit=30) 
        num1 = result[22].find_next_siblings("td")
        num2 = result[23].find_next_siblings("td")
        num3 = result[24].find_next_siblings("td")
        num4 = result[25].find_next_siblings("td")
        num5 = result[26].find_next_siblings("td")
        num6 = result[27].find_next_siblings("td")
        num7 = result[28].find_next_siblings("td")
        num8 = result[29].find_next_siblings("td")
        st =""
        num = [result[22].find_next_siblings("td"),result[23].find_next_siblings("td"),result[24].find_next_siblings("td"),result[25].find_next_siblings("td"),result[26].find_next_siblings("td"),result[27].find_next_siblings("td"),result[28].find_next_siblings("td"),result[29].find_next_siblings("td")]
        for q in range(22,30):
            if len(result[q].a.getText())==2:
                t_add = result[q].a.getText()+"     "
            elif len(result[q].a.getText())==3:
                t_add = result[q].a.getText()+" "
            st = st  + str(q-21) + ". " + t_add + "   " + num[q-22][1].getText() + "\n********************************\n"      
        #st = result[22].a.getText() + "   " + num1[1].getText() + "\n" + result[23].a.getText() + "   " +  num2[1].getText() + "\n" +  result[24].a.getText() + "   " + num3[1].getText() + "\n" + result[25].a.getText() + "   " + num4[1].getText() + "\n" + result[26].a.getText() + "   " + num5[1].getText() + "\n" + result[27].a.getText() +"   " + num6[1].getText() + "\n" + result[28].a.getText() +"   " + num7[1].getText() + "\n" + result[29].a.getText() + "   " + num8[1].getText()
        reply_token = event.reply_token
        send_text_message(reply_token,st) #一次印完
        self.go_back()
    
    def is_going_to_rebound_leader(self, event):
        text = event.message.text
        return text.lower() == "rebound"
    
    def on_enter_rebound_leader(self, event):
        print("show rebound leader\n")
        response = requests.get(pleague)
        soup = BeautifulSoup(response.text, "html.parser")
        st = ""
        result = soup.find_all("td","font-weight-bold",limit=30)
        num1 = result[14].find_next_siblings("td")
        num2 = result[15].find_next_siblings("td")
        num3 = result[16].find_next_siblings("td")
        num4 = result[17].find_next_siblings("td")
        num5 = result[18].find_next_siblings("td")
        num6 = result[19].find_next_siblings("td")
        num7 = result[20].find_next_siblings("td")
        num8 = result[21].find_next_siblings("td")
        num = [result[14].find_next_siblings("td"),result[15].find_next_siblings("td"),result[16].find_next_siblings("td"),result[17].find_next_siblings("td"),result[18].find_next_siblings("td"),result[19].find_next_siblings("td"),result[20].find_next_siblings("td"),result[21].find_next_siblings("td")] 
        for q in range(14,22):
            if len(result[q].a.getText())==2:
                t_add = result[q].a.getText()+"     "
            elif len(result[q].a.getText())==3:
                t_add = result[q].a.getText()+" "
            st = st  +str(q-13) + ". " + t_add + "   " + num[q-14][1].getText() + "\n********************************\n"
        #st = result[14].a.getText() + "   " + num1[1].getText() + "\n" + result[15].a.getText() + "   " + num2[1].getText() + "\n" +  result[16].a.getText() + "   " + num3[1].getText() + "\n" + result[17].a.getText() + "   " + num4[1].getText() + "\n" + result[18].a.getText() + "   " + num5[1].getText() + "\n" + result[19].a.getText() +"   " + num6[1].getText() + "\n" + result[20].a.getText() +"   " + num7[1].getText() + "\n" + result[21].a.getText() + "   " + num8[1].getText()
        reply_token = event.reply_token
        send_text_message(reply_token,st) #一次印完
        self.go_back()
    
    def back_to_menu(self, event):
        text = event.message.text
        return text.lower() == "back to menu"
    # def on_exit_state1(self):
    #     print("Leaving state1")


pleague = "https://pleagueofficial.com/"
team_stats = "https://pleagueofficial.com/stat-team/2021-22/6#record"
player_stats = "https://pleagueofficial.com/stat-player/2021-22/6#record"