from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import Global_var
import sys, os
import ctypes
import pymysql.cursors
import wx
import re
app = wx.App()


def Local_connection_links():
    a = 0
    while a == 0:
        try:
            connection = pymysql.connect(host='185.142.34.92',user='ams',password='TgdRKAGedt%h',db='tenders_db',charset='utf8',cursorclass=pymysql.cursors.DictCursor)
            return connection
        except pymysql.connect  as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print("Error ON : ", sys._getframe().f_code.co_name + "--> " + str(e), "\n", exc_type, "\n", fname,
                  "\n", exc_tb.tb_lineno)
            a = 0
            time.sleep(10)


def Collect_Link():
    mydb_Local = Local_connection_links()
    mycursorLocal = mydb_Local.cursor()
    a = 0
    while a == 0:
        try:
            Links_List = []
            mydb_Local = Local_connection_links()
            mycursorLocal = mydb_Local.cursor()  # SELECT * FROM `Tenders_Russia`.`sberbank_temptbl` ORDER BY id DESC LIMIT 0, 500
            # mycursorLocal.execute("SELECT `doc_links` FROM `sberbank_temptbl` ORDER BY id DESC LIMIT "+str(Global_var.Number_Of_Links2)+", "+str(Global_var.Number_Of_Links)+"")
            mycursorLocal.execute("SELECT `doc_links` FROM `sberbank_temptbl` ORDER BY id DESC")
            rows = mycursorLocal.fetchall()
            mydb_Local.close()
            mycursorLocal.close()
            for row in rows:
                links = "%s" % (row["doc_links"])
                if links not in Links_List:
                    Links_List.append(links)
            time.sleep(2)
            print("Number OF Link Get From Database: ", len(Links_List))
            Nav_Links(Links_List)
            a = 1
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print("Error ON : ", sys._getframe().f_code.co_name + "--> " + str(e), "\n", exc_type, "\n", fname, "\n",
                  exc_tb.tb_lineno)
            mydb_Local.close()
            mycursorLocal.close()
            a = 0
            time.sleep(10)


def Nav_Links(Links_List):
    chrome_options = Options()
    chrome_options.add_extension('C:\\BrowsecVPN.crx')
    browser = webdriver.Chrome(executable_path=str(f"C:\\chromedriver.exe"),chrome_options=chrome_options)
    browser.maximize_window()
    # browser.get("""https://chrome.google.com/webstore/detail/browsec-vpn-free-and-unli/omghfjlpggmjjaagoclmmobgdodcjboh?hl=en" ping="/url?sa=t&amp;source=web&amp;rct=j&amp;url=https://chrome.google.com/webstore/detail/browsec-vpn-free-and-unli/omghfjlpggmjjaagoclmmobgdodcjboh%3Fhl%3Den&amp;ved=2ahUKEwivq8rjlcHmAhVtxzgGHZ-JBMgQFjAAegQIAhAB""")
    wx.MessageBox(' -_-  Add Extension and Select Proxy Between 10 SEC -_- ', 'Info', wx.OK | wx.ICON_WARNING)
    time.sleep(15)  # WAIT UNTIL CHANGE THE MANUAL VPN SETtING
    
    time.sleep(2)
    for href in Links_List:
        loop = 0
        while loop == 0:
            try:
                # browser.refresh()
                browser.get(href)
                get_htmlsource_For_XML_DATA = ''
                Hidden_Script = ''
                get_htmlsource = ''
                for get_htmlsource_For_Script in browser.find_elements_by_xpath('/html'):
                    get_htmlsource_For_Script = get_htmlsource_For_Script.get_attribute('outerHTML')
                    List_OF_Scripts = re.findall(r"(?<=<script).*?(?=</script>)", str(get_htmlsource_For_Script))
                    for scrip in List_OF_Scripts:
                        scrip = scrip.replace('src="/', 'src="http://utp.sberbank-ast.ru/')
                        Hidden_Script += '<script'+scrip+'</script>'+'\n'
                    break
                for get_htmlsource_For_XML_DATA in browser.find_elements_by_id('docForm'):
                    get_htmlsource_For_XML_DATA = get_htmlsource_For_XML_DATA.get_attribute('outerHTML')
                    get_htmlsource_For_XML_DATA = get_htmlsource_For_XML_DATA.replace('action="/', 'action="http://utp.sberbank-ast.ru/')
                    break
                for get_htmlsource in browser.find_elements_by_xpath('//*[@class="master_open_content"]/div[1]'):
                    get_htmlsource = get_htmlsource.get_attribute('outerHTML').replace('src="/img', 'src="http://utp.sberbank-ast.ru/img').replace('src="/Content', 'src="http://utp.sberbank-ast.ru/Content')\
                        .replace('<select content="leaf:RequestPart" id="BidsSMBO_RequestPart" name="BidsSMBO_RequestPart" class="" style="" disabled="disabled"><option value=""></option><option value="1">Часть 1</option><option value="2">Часть 2</option><option value="3">Ценовое предложение</option></select>', '').replace('<select content="leaf:BidMainCustomer" id="BidsSMBO_BidMainCustomer" name="BidsSMBO_BidMainCustomer" class="" style="" disabled="disabled"><option value=""></option><option value="1">да</option></select>', '')
                    from Scraping_data import Scrap_data
                    Global_var.Total += 1
                    Scrap_data(get_htmlsource,href,browser,Hidden_Script,get_htmlsource_For_XML_DATA)
                    break
                DeleteLink_From_Database(href)
                loop = 1
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print("Error ON : ", sys._getframe().f_code.co_name + "--> " + str(e), "\n", exc_type, "\n", fname, "\n",
                      exc_tb.tb_lineno)
                loop = 0
    ctypes.windll.user32.MessageBoxW(0, "Total: " + str(Global_var.Total) + "\n""Duplicate: " + str(
        Global_var.duplicate) + "\n""Expired: " + str(Global_var.expired) + "\n""Inserted: " + str(
        Global_var.inserted) + "\n""Deadline Not given: " + str(
        Global_var.deadline_Not_given) + "\n""QC Tenders: " + str(Global_var.QC_Tender)+ "\n""Link Delete From Table: " + str(Global_var.Delete_Link) + "\n""Purchaser NOT Found: " + str(Global_var.Purchaser_NOT_Found) + "",
                                     "sberbank_ast.ru", 1)
    Global_var.Process_End()
    browser.close()
    sys.exit()


def DeleteLink_From_Database(href):
    mydb_Local = Local_connection_links()
    mycursorLocal = mydb_Local.cursor()
    a5 = 0
    while a5 == 0:
        try:
            mycursorLocal.execute("DELETE FROM `sberbank_temptbl` WHERE `doc_links` = '"+str(href)+"'")
            mydb_Local.commit()
            Global_var.Delete_Link += 1
            print("Link Delete From Table")
            print(" Total: " + str(Global_var.Total) + " Duplicate: " + str(Global_var.duplicate) + " Expired: " + str(Global_var.expired) + " Inserted: " + str(Global_var.inserted) + " Deadline Not given: " + str(Global_var.deadline_Not_given) + " QC Tenders: " + str(Global_var.QC_Tender) + " Link Delete From Table: " + str(Global_var.Delete_Link) + "\n""Purchaser NOT Found: " + str(Global_var.Purchaser_NOT_Found),"\n")
            a5 = 1
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print("Error ON : ", sys._getframe().f_code.co_name + "--> " + str(e), "\n", exc_type, "\n", fname, "\n",exc_tb.tb_lineno)
            a5 = 0


Collect_Link()
