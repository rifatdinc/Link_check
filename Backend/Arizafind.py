#!/usr/bin/python3
from NasipList import RouterIp
import os
import datetime
import requests
import nmap3
import time
from routeros_api import Api, CreateSocketError


class ccrIp():

    def telegramApis(self, text):
        self.botToken = "1185283164:AAEs7zb-Khm7H9aHEjGMMgMyPevKxhyoPD0"
        self.chatId = "-1001255461523"
        self.send_Txt = 'https://api.telegram.org/bot' + self.botToken + \
            '/sendMessage'+'?chat_id=' + self.chatId + '&text=' + text
        results = requests.get(self.send_Txt)
        return results.json()

    def GepPo(self, ip):
        try:
            self.RouterOs = Api(ip, 'admin', 'mc4152')
            # Ilk Calisacak Komutlar Ayarlari Gerceklestiriyor. ##
            self.RouterOs.talk('/system/ntp/client/set\n=enabled=yes\n=primary-ntp=192.10.10.1')
            self.RouterOs.talk('/system/routerboard/upgrade')
            
            
            ##----- Burada Calisacak komutlar ise Datalari Aliyor.
            self.RouterName = self.RouterOs.talk('/system/routerboard/print')[0]['model']
            self.Signal = self.RouterOs.talk('/interface/wireless/registration-table/print')
            self.b = self.RouterOs.talk('/interface/wireless/print')
            self.c = self.RouterOs.talk('/ip/address/print')
            self.Interface = self.RouterOs.talk('/interface/getall')
            self.eth = self.RouterOs.talk('/interface/ethernet/monitor\n=numbers=ether1\n=once=')
            for eth0 in self.eth:
                pass
            for ipLists in self.c:
                pass
            for xss in self.b:
                tekSefer = xss
                lenght = len(tekSefer['tx-chains'])
                lenght1 = len(tekSefer['rx-chains'])
                scanList = tekSefer['scan-list']
                lent = len(scanList)

            for sinyal in self.Signal:
                sinyal1 = sinyal['signal-strength-ch0']
                sinyal2 = sinyal['signal-strength-ch1']
                sinyal3 = sinyal['tx-signal-strength-ch0']
                sinyal4 = sinyal['tx-signal-strength-ch1']
                if sinyal1 > '-74' or sinyal2 > '-74':
                    self.telegramApis(self.Ppoes['name'] + " " + ipLists['address'][:-3] + " " +
                                      'Sinyal Yuksek Rx'f'{sinyal1}.'f'{sinyal2}')
                elif sinyal3 > '-74' or sinyal4 > '-74':
                    self.telegramApis(self.Ppoes['name'] + " " + ipLists['address'][:-3] + " " +
                                      'Sinyal Yuksek Tx'f'{sinyal3}.'f'{sinyal4}')

            for self.Linkdown in self.Interface:
                self.Linkdowns = self.Linkdown['link-downs']
                self.IntLink = int(self.Linkdowns)

                if self.IntLink > 100:
                    self.telegramApis(self.Ppoes['name'] + " " + ipLists['address'][:-3] + "  " + self.Linkdown['name'] +
                                      " "+self.Linkdowns+" Cok Kopmus" + " "+"SINYALLERRRRR" + sinyal1+" "+sinyal2+" "+sinyal3+" "+sinyal4)

            if not self.RouterName == 'RouterBOARD 931-2nD':

                if not lenght > 1:
                    self.telegramApis(
                        self.Ppoes['name'] + " " + ipLists['address'][:-3] + " Tx Chains Isaretli Degildir.")
                if not lenght1 > 1:
                    self.telegramApis(
                        self.Ppoes['name'] + " " + ipLists['address'][:-3] + " Rx Chains Isaretli Degildir.")
                # if not tekSefer['country'] == 'no_country_set':
                #     self.telegramApis(self.Ppoes['name'] + " " + ipLists['address'][:-3] +
                #     ' Cihaz No Country Set Degildir Farkli Ulkedir.')
                # if not tekSefer['band'] == '5ghz-a/n' and tekSefer['band'] != '2ghz-b/g/n' and tekSefer['band'] != '2ghz-onlyn':
                #     self.telegramApis(self.Ppoes['name'] + " " + ipLists['address'][:-3] +
                #     ' Cihazin Band Ayari "5ghz-a/n yada 2ghz N protokolunde degildir.')
                if not tekSefer['channel-width'] == '20/40mhz-Ce' and tekSefer['channel-width'] != '20/40mhz-XX' and tekSefer['channel-width'] != '20/40mhz-eC':
                    self.telegramApis(
                        self.Ppoes['name'] + " " + ipLists['address'][:-3] + ' Cihazin Kanal Ayari "20 mHz dir".')
                if lent < 5:
                    makeScanlist = [('/system/scheduler/add', '=name=SabitFrekansDuzeltme',
                                     '=start-date='f'{month}/{dday}/{year}', '=start-time='f'{oneHour}', '=on-event=/interface wireless set scan-list=4900-6100 numbers=0')]
                    self.RouterOs.talk(makeScanlist)
                    self.telegramApis(
                        self.Ppoes['name'] + " " + ipLists['address'][:-3] + " Sabit Frekansta Zamanlayici Olusturuldu.")
                if not tekSefer['wireless-protocol'] == 'nv2-nstreme-802.11':
                    self.telegramApis(self.Ppoes['name'] + " " + ipLists['address'][:-3] +
                                      " Wireless Protokolu 'nv2-nstreme-802.11' Degildir.")
                if not tekSefer['frequency-mode'] == 'superchannel':
                    self.telegramApis(self.Ppoes['name'] + " " + ipLists['address'][:-3] +
                                      " Cihaz Super Channel Frekans Modunda Degildir.")
                if eth0['rate'] == "10Mbps":
                    self.telegramApis(
                        self.Ppoes['name'] + " " + ipLists['address'][:-3] + " CIHAZ 10 MBPS CALISIYOR ")
            else:
                print('Cihaz hAp mini')

            self.RouterOs.close()

        except Exception as err:
            print(err)

    def getPpoes(self, NasIp):
        nmap = nmap3.NmapHostDiscovery()

        self.router = Api(address=NasIp, user='admin',
                          password='0rtaca@2002@Bozagac', verbose=True)
        self.userIp = self.router.talk('/ppp/active/print')
        self.identy = self.router.talk('/system/identity/print')
        for self.isim in self.identy:
            pass
        for self.Ppoes in self.userIp:
            nmap = nmap3.NmapHostDiscovery()
            ip = self.Ppoes['address']
            result = nmap.nmap_portscan_only(ip, args="-p 8728")
            b = result[ip]['ports']
            for cl in b:
                if cl['state'] == 'open':
                    self.GepPo(ip)
        self.router.close()

    def getVersn(self):
        #  RouterIp Import Edip Ccr'larin iplerini aldim.
        self.NassIpList = RouterIp()
        for ix in self.NassIpList:
            xs = ix
            sd = xs[0]
            routerIp = sd.decode()
            try:
                self.getPpoes(routerIp)

            except Exception as err:
                print('NEler Oluyor', err)
                pass
                # s = str(err)
                # self.telegramApis(""+self.Ppoes['name'] + " " + repr(s)+" ""Cihazin Sifresi Yanlis yada Api Port Kapali Cihaz Hangi Nasda: "+" ")
#


IsIs = ccrIp()
IsIs.getVersn()

# ldf = 0
# disc = 0
# sxtlite5 = 0
# lhg = 0
# sq = 0
# sq5Ac = 0
# lhgXl = 0
# other = 0
# x = datetime.datetime.now()
# month = (x.strftime("%b"))
# day = datetime.date.today() + datetime.timedelta(days=0)
# dday = (day.strftime("%d"))
# year = (x.strftime("%Y"))
# oneHour = "03:33:00"

#  self.telegramApis(self.isim['name']+" " + "Ldf Sayisi :"+str(ldf) + " " + "Disc Lite 5 Sayisi :"+str(disc) + " "+"Sxt Lte 5 Sayisi :" + str(sxtlite5)+" " +
#   "Lhg Sayisi : "+str(lhg)+" "+" Sq Lite 5 Sayisi"+str(sq)+" "+"Sq5AcSayisi"+str(sq5Ac)+" "+"Lhg 5 Xl sayisi " + str(lhgXl)+" "+"Diger Cihazlar"+str(other))

# if Name['model'] == 'RBDisc-5nD':
#                     disc += 1
#                 elif Name['model'] == 'SXT 5nD r2':
#                     sxtlite5 += 1
#                 elif Name['model'] == 'RouterBOARD LHG 5nD' or Name['model'] == 'RouterBOARD LHG 5HPnD':
#                     lhg += 1
#                 elif Name['model'] == 'RBLDF-5nD':
#                     ldf += 1
#                 elif Name['model'] == 'RouterBOARD SXTsq 5nD':
#                     sq += 1
#                 elif Name['model'] == 'RouterBOARD SXTsq G-5acD':
#                     sq5Ac += 1
#                 elif Name['model'] == 'RouterBOARD LHG 5HPnD-XL':
#                     lhgXl += 1
#                 else:
#                     other += 1
