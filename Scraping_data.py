import re
import time
import urllib.request
import urllib.parse
import sys , os
import string
from datetime import datetime
import Global_var
import requests
import html
import wx
from Insert_On_Database import create_filename
app = wx.App()


# def Translate_close(text_without_translate):
#     String2 = ""
#     try:
#         String2 = str(text_without_translate)
#         url = "https://translate.google.com/m?hl=en&sl=auto&tl=en&ie=UTF-8&prev=_m&q=" + str(String2) + ""
#         response1 = requests.get(str(url))
#         response2 = response1.url
#         user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
#         headers = {'User-Agent': user_agent , }
#         request = urllib.request.Request(response2, None , headers)  # The assembled request
#         time.sleep(1.2)
#         response = urllib.request.urlopen(request)
#         htmldata: str = response.read().decode('utf-8')
#         trans_data = re.search(r'(?<=dir="ltr" class="t0">).*?(?=</div>)', htmldata).group(0).strip()
#         trans_data = html.unescape(str(trans_data)).strip()
#         return trans_data
#     except:
#         return String2


def Scrap_data(get_htmlSource, href, browser,Hidden_Script,get_htmlsource_For_XML_DATA):
    SegField = []
    for data in range(45):
        SegField.append('')
    a = True
    while a == True:
        try:
            # =============================================== Email ID ===================================================
            Email_ID = ''
            try:
                for Email_ID in browser.find_elements_by_xpath('//*[@content="leaf:ContactEmail"]'):
                    Email_ID = Email_ID.get_attribute('innerText').strip()
            except:pass

            if Email_ID == '':
                for Email_ID in browser.find_elements_by_xpath('//*[@content="leaf:contactEMail"]'):
                    Email_ID = Email_ID.get_attribute('innerText').strip()

            if Email_ID == '':
                for Email_ID in browser.find_elements_by_xpath('//*[@id="PurchaseInfo_ContactEmail"]'):
                    Email_ID = Email_ID.get_attribute('innerText').strip()

            if Email_ID == '':
                for Email_ID in browser.find_elements_by_xpath('//*[@id="Requester_RepresenterEmail"]'):
                    Email_ID = Email_ID.get_attribute('innerText').strip()

            if Email_ID == '':
                for Email_ID in browser.find_elements_by_xpath('//*[@id="DynamicControlOrganizatorInfo_OrgEmail"]'):
                    Email_ID = Email_ID.get_attribute('innerText').strip()

            if Email_ID == '':
                for Email_ID in browser.find_elements_by_xpath('//*[@id="OrganizatorInfo_OrgEmail"]'):
                    Email_ID = Email_ID.get_attribute('innerText').strip()

            if Email_ID == '':
                for Email_ID in browser.find_elements_by_xpath('//*[@id="DynamicControlOrgInfo_OrgEMail"]'):
                    Email_ID = Email_ID.get_attribute('innerText').strip()

            if Email_ID == '':
                for Email_ID in browser.find_elements_by_xpath('//*[@id="OOS.OrganizatorInfo_contactEmail"]'):
                    Email_ID = Email_ID.get_attribute('innerText').strip()

            if Email_ID == '':
                for Email_ID in browser.find_elements_by_xpath('//*[@id="DynamicControlRequester_RepresenterEmail"]'):
                    Email_ID = Email_ID.get_attribute('innerText').strip()

            if Email_ID != '':
                SegField[1] = Email_ID
            else:
                pass

            # =============================================== Address ===================================================
            Address = ''
            for Address in browser.find_elements_by_xpath('//*[@content="leaf:factAddress"]'):
                Address = Address.get_attribute('innerText').strip()

            if Address == '':
                for Address in browser.find_elements_by_xpath('//*[@content="leaf:orgpostaddress"]'):

                    Address = Address.get_attribute('innerText').strip()
            if Address == '':
                for Address in browser.find_elements_by_xpath('//*[@id="PurchaseInfo_OrgAddressJur"]'):
                    Address = Address.get_attribute('innerText').strip()

            if Address == '':
                for Address in browser.find_elements_by_xpath('//*[@id="Requester_RequesterAddressJur"]'):
                    Address = Address.get_attribute('innerText').strip()

            if Address == '':
                for Address in browser.find_elements_by_xpath('//*[@id="DynamicControlOrganizatorInfo_OrgAddressJur"]'):
                    Address = Address.get_attribute('innerText').strip()

            if Address == '':
                for Address in browser.find_elements_by_xpath('//*[@id="DynamicControlRequester_RequesterAddressJur"]'):
                    Address = Address.get_attribute('innerText').strip()

            if Address == '':
                for Address in browser.find_elements_by_xpath('//*[@id="OrganizatorInfo_OrgAddressJur"]'):
                    Address = Address.get_attribute('innerText').strip()

            if Address == '':
                for Address in browser.find_elements_by_xpath('//*[@id="DynamicControlOrgInfo_OrgAddressFact"]'):
                    Address = Address.get_attribute('innerText').strip()

            if Address == '':
                for Address in browser.find_elements_by_xpath('//*[@id="OOS.OrganizatorInfo_postAddress"]'):
                    Address = Address.get_attribute('innerText').strip()

            if Address == '':
                for Address in browser.find_elements_by_xpath('//*[@content="leaf:deliveryplace"]'):
                    Address = Address.get_attribute('innerText').strip()

            if Address != '':
                # Address = Translate(Address)
                Address = string.capwords(str(Address))
                SegField[2] = Address.strip()
            else:
                pass

            # if Address != '':
            #     # Address = Translate(Address)
            #     Address = string.capwords(str(Address))
            #     SegField[2] = Address.strip()
            # else:
            #     pass

            # =============================================== Contact Person ===================================================
            Contact_Person = ''
            for Contact_Person in browser.find_elements_by_xpath('//*[@content="node:contactPerson"]'):
                Contact_Person = Contact_Person.get_attribute('innerText').strip()

            if Contact_Person == '':
                for Contact_Person in browser.find_elements_by_xpath('//*[@content="leaf:factAddress"]'):
                    Contact_Person = Contact_Person.get_attribute('innerText').strip()

            if Contact_Person == '':
                for Contact_Person in browser.find_elements_by_xpath('//*[@id="PurchaseInfo_ContactPerson"]'):
                    Contact_Person = Contact_Person.get_attribute('innerText').strip()

            if Contact_Person == '':
                for Contact_Person in browser.find_elements_by_xpath('//*[@id="Requester_RepresenterName"]'):
                    Contact_Person = Contact_Person.get_attribute('innerText').strip()

            if Contact_Person == '':
                for Contact_Person in browser.find_elements_by_xpath('//*[@id="DynamicControlRequester_RepresenterName"]'):
                    Contact_Person = Contact_Person.get_attribute('innerText').strip()

            if Contact_Person == '':
                for Contact_Person in browser.find_elements_by_xpath('//*[@id="DynamicControlOrganizatorInfo_OrgContactPerson"]'):
                    Contact_Person = Contact_Person.get_attribute('innerText').strip()

            if Contact_Person == '':
                for Contact_Person in browser.find_elements_by_xpath('//*[@id="OrganizatorInfo_OrgContactPerson"]'):
                    Contact_Person = Contact_Person.get_attribute('innerText').strip()

            if Contact_Person == '':
                for Contact_Person in browser.find_elements_by_xpath('//*[@content="node:contactPersonInfo"]'):
                    Contact_Person = Contact_Person.get_attribute('innerText').strip()

            if Contact_Person != '':
                # Contact_Person = Translate(Contact_Person)
                Contact_Person = string.capwords(str(Contact_Person))
                SegField[2] = SegField[2].strip() + '<br>\n''Контактное лицо: ' + Contact_Person
            else:
                SegField[2] = SegField[2].strip()
            # =============================================== Phone ===================================================
            Phone = ''
            for Phone in browser.find_elements_by_xpath('//*[@content="leaf:contactPhone"]'):
                Phone = Phone.get_attribute('innerText').strip()

            if Phone == '':
                for Phone in browser.find_elements_by_xpath('//*[@id="PurchaseInfo_ContactPhone"]'):
                    Phone = Phone.get_attribute('innerText').strip()

            if Phone == '':
                for Phone in browser.find_elements_by_xpath('//*[@id="Requester_RepresenterPhone"]'):
                    Phone = Phone.get_attribute('innerText').strip()

            if Phone == '':
                for Phone in browser.find_elements_by_xpath('//*[@id="DynamicControlOrganizatorInfo_OrgPhone"]'):
                    Phone = Phone.get_attribute('innerText').strip()

            if Phone == '':
                for Phone in browser.find_elements_by_xpath('//*[@id="DynamicControlRequester_RepresenterPhone"]'):
                    Phone = Phone.get_attribute('innerText').strip()

            if Phone == '':
                for Phone in browser.find_elements_by_xpath('//*[@id="OrganizatorInfo_OrgPhone"]'):
                    Phone = Phone.get_attribute('innerText').strip()

            if Phone == '':
                for Phone in browser.find_elements_by_xpath('//*[@id="DynamicControlOrgInfo_OrgPhone"]'):
                    Phone = Phone.get_attribute('innerText').strip()

            if Phone == '':
                for Phone in browser.find_elements_by_xpath('//*[@id="OOS.OrganizatorInfo_contactPhone"]'):
                    Phone = Phone.get_attribute('innerText').strip()

            if Phone != '':
                SegField[2] = SegField[2].strip()+'<br>\n''Телефон: ' + Phone
            else:
                SegField[2] = SegField[2].strip()

            # =============================================== Fax ===================================================
            Fax = ''
            for Fax in browser.find_elements_by_xpath('//*[@content="leaf:contactPhone"] '):
                Fax = Fax.get_attribute('innerText').strip()

            if Fax == '':
                for Fax in browser.find_elements_by_xpath('//*[@id="PurchaseInfo_ContactPhone"] '):
                    Fax = Fax.get_attribute('innerText').strip()

            if Fax != '':
                SegField[2] = SegField[2].strip()+'<br>\n''факс: ' + Fax.strip()
            else:
                SegField[2] = SegField[2].strip()

            # =============================================== Country ===================================================

            SegField[7] = "RU"

            # =============================================== Purchaser ===================================================
            Purchaser = ''
            for Purchaser in browser.find_elements_by_xpath('//*[@content="leaf:orgname"]'):
                Purchaser = Purchaser.get_attribute('innerText').strip()

            if Purchaser == '':
                for Purchaser in browser.find_elements_by_xpath('//*[@id="PurchaseInfo_OrgName"]'):
                    Purchaser = Purchaser.get_attribute('innerText').strip()

            if Purchaser == '':
                for Purchaser in browser.find_elements_by_xpath('//*[@id="Requester_RequesterFullName"]'):
                    Purchaser = Purchaser.get_attribute('innerText').strip()

            if Purchaser == '':
                for Purchaser in browser.find_elements_by_xpath('//*[@id="DynamicControlOrganizatorInfo_OrgName"]'):
                    Purchaser = Purchaser.get_attribute('innerText').strip()

            if Purchaser == '':
                for Purchaser in browser.find_elements_by_xpath('//*[@id="DynamicControlRequester_RequesterName"]'):
                    Purchaser = Purchaser.get_attribute('innerText').strip()

            if Purchaser == '':
                for Purchaser in browser.find_elements_by_xpath('//*[@id="OrganizatorInfo_OrgName"]'):
                    Purchaser = Purchaser.get_attribute('innerText').strip()

            if Purchaser == '':
                for Purchaser in browser.find_elements_by_xpath('//*[@id="DynamicControlOrgInfo_OrgName"]'):
                    Purchaser = Purchaser.get_attribute('innerText').strip()

            if Purchaser == '':
                for Purchaser in browser.find_elements_by_xpath('//*[@id="OOS.OrganizatorInfo_fullName"]'):
                    Purchaser = Purchaser.get_attribute('innerText').strip()

            if Purchaser == '':
                for Purchaser in browser.find_elements_by_xpath('//*[@content="leaf:orgname"]'):
                    Purchaser = Purchaser.get_attribute('innerText').strip()

            if Purchaser != '':
                # Purchaser = Translate(Purchaser)
                SegField[12] = Purchaser.upper().strip().replace('"', '')
            else:
                pass
            if SegField[12] != '':
                # =============================================== Tender No ===================================================
                Tender_No = ''
                for Tender_No in browser.find_elements_by_xpath('//*[@content="leaf:purchCode"]'):
                    Tender_No = Tender_No.get_attribute('innerText').strip()
                    break

                if Tender_No == '':
                    for Tender_No in browser.find_elements_by_xpath('//*[@id="PurchaseInfo_PurchaseCode"]'):
                        Tender_No = Tender_No.get_attribute('innerText').strip()
                        break

                if Tender_No == '':
                    for Tender_No in browser.find_elements_by_xpath('//*[@id="Purchase_PurchaseCode"]'):
                        Tender_No = Tender_No.get_attribute('innerText').strip()
                        break

                if Tender_No == '':
                    for Tender_No in browser.find_elements_by_xpath('//*[@id="DynamicControlPurchaseInfo_PurchaseCode"]'):
                        Tender_No = Tender_No.get_attribute('innerText').strip()
                        break

                if Tender_No == '':
                    for Tender_No in browser.find_elements_by_xpath('//*[@id="PurchaseInfo_PurchaseCode"]'):
                        Tender_No = Tender_No.get_attribute('innerText').strip()
                        break

                if Tender_No == '':
                    for Tender_No in browser.find_elements_by_xpath('//*[@id="PurchaseInfoView_PurchaseCode"]'):
                        Tender_No = Tender_No.get_attribute('innerText').strip()
                        break

                if Tender_No == '':
                    for Tender_No in browser.find_elements_by_xpath('//*[@id="PurchaseInfo_PurchaseUTPCode"]'):
                        Tender_No = Tender_No.get_attribute('innerText').strip()
                        break
                if Tender_No != '':
                    SegField[13] = Tender_No.strip()
                else:
                    pass

                # =============================================== Notice_type ===================================================
                SegField[14] = '2'
                # =============================================== Ind_classification ===================================================
                SegField[16] = '1'
                # =============================================== MFA ===================================================
                SegField[17] = '0'

                # =============================================== Tender Details ===================================================
                Name_of_procedure = ''
                for Name_of_procedure in browser.find_elements_by_xpath('//*[@content="leaf:purchname"]'):
                    Name_of_procedure = Name_of_procedure.get_attribute('innerText').strip()

                if Name_of_procedure == '':
                    for Name_of_procedure in browser.find_elements_by_xpath('//*[@id="PurchaseInfo_PurchaseName"]'):
                        Name_of_procedure = Name_of_procedure.get_attribute('innerText').strip()

                if Name_of_procedure == '':
                    for Name_of_procedure in browser.find_elements_by_xpath('//*[@id="Purchase_PurchaseName"]'):
                        Name_of_procedure = Name_of_procedure.get_attribute('innerText').strip()

                if Name_of_procedure == '':
                    for Name_of_procedure in browser.find_elements_by_xpath('//*[@id="DynamicControlPurchaseInfo_PurchaseName"]'):
                        Name_of_procedure = Name_of_procedure.get_attribute('innerText').strip()

                if Name_of_procedure == '':
                    for Name_of_procedure in browser.find_elements_by_xpath('//*[@id="PurchaseInfoView_PurchaseName"]'):
                        Name_of_procedure = Name_of_procedure.get_attribute('innerText').strip()

                if Name_of_procedure != '':
                    # Name_of_procedure = Translate(Name_of_procedure)
                    Name_of_procedure = string.capwords(str(Name_of_procedure))
                else:
                    pass
                # ======================================================================================================================
                purch_Type_Name = ''
                for purch_Type_Name in browser.find_elements_by_xpath('//*[@content="leaf:purchTypeName"]'):
                    purch_Type_Name = purch_Type_Name.get_attribute('innerText').strip()

                if purch_Type_Name != '':
                    # purch_Type_Name = Translate(purch_Type_Name)
                    purch_Type_Name = string.capwords(str(purch_Type_Name))
                else:
                    pass
                # ======================================================================================================================

                Type_of_procedure = ''
                for Type_of_procedure in browser.find_elements_by_xpath('//*[@id="PurchaseInfo_PurchaseTypeName"]'):
                    Type_of_procedure = Type_of_procedure.get_attribute('innerText').strip()

                if Type_of_procedure == '':
                    for Type_of_procedure in browser.find_elements_by_xpath('//*[@id="Purchase_PurchaseTypeName"]'):
                        Type_of_procedure = Type_of_procedure.get_attribute('innerText').strip()

                if Type_of_procedure == '':
                    for Type_of_procedure in browser.find_elements_by_xpath('//*[@id="DynamicControlPurchaseInfo_PurchaseTypeName"]'):
                        Type_of_procedure = Type_of_procedure.get_attribute('innerText').strip()

                if Type_of_procedure == '':
                    for Type_of_procedure in browser.find_elements_by_xpath('//*[@id="PurchaseInfoView_PurchaseTypeName"]'):
                        Type_of_procedure = Type_of_procedure.get_attribute('innerText').strip()

                if Type_of_procedure != '':
                    # Type_of_procedure = Translate(Type_of_procedure)
                    Type_of_procedure = string.capwords(str(Type_of_procedure))
                else:
                    pass
                # ======================================================================================================================
                Industry = ''
                for Industry in browser.find_elements_by_xpath('//*[@content="leaf:purchbranchname"]'):
                    Industry = Industry.get_attribute('innerText').strip()

                if Industry != '':
                    # Industry = Translate(Industry)
                    Industry = string.capwords(str(Industry))
                else:
                    pass
                # ======================================================================================================================

                Order_nomenclature = ''
                for Order_nomenclature in browser.find_elements_by_xpath('//*[@content="leaf:purchokdpname"]'):
                    Order_nomenclature = Order_nomenclature.get_attribute('innerText').strip()

                if Order_nomenclature != '':
                    # Order_nomenclature = Translate(Order_nomenclature)
                    Order_nomenclature = string.capwords(str(Order_nomenclature))
                else:
                    pass
                # ======================================================================================================================

                contract_price = ''
                for contract_price in browser.find_elements_by_xpath('//*[@content="leaf:purchAmount"]'):
                    contract_price = contract_price.get_attribute('innerText').strip()

                if contract_price == '':
                    for contract_price in browser.find_elements_by_xpath('//*[@id="BidsSMBO_BidPrice"]'):
                        contract_price = contract_price.get_attribute('innerText').strip()

                if contract_price == '':
                    for contract_price in browser.find_elements_by_xpath('//*[@id="DynamicControlBidInfo_BidAmount"]'):
                        contract_price = contract_price.get_attribute('innerText').strip()

                if contract_price == '':
                    for contract_price in browser.find_elements_by_xpath('//*[@id="BidInfo_BidAmount"]'):
                        contract_price = contract_price.get_attribute('innerText').strip()

                if contract_price == '':
                    for contract_price in browser.find_elements_by_xpath('//*[@id="PurchaseInfoView_PurchaseAmount"]'):
                        contract_price = contract_price.get_attribute('innerText').strip()

                if contract_price != '':
                    # contract_price = Translate(contract_price)
                    SegField[20] = contract_price.strip().replace(' ','').replace(',','')
                    SegField[21] = 'RUB'
                else:
                    pass
                # ======================================================================================================================

                BidCurrency = ''
                for BidCurrency in browser.find_elements_by_xpath('//*[@content="leaf:custpurchamount"]'):
                    BidCurrency = BidCurrency.get_attribute('innerText').strip()

                if BidCurrency == '':
                    for BidCurrency in browser.find_elements_by_xpath('//*[@id="BidsSMBO_BidCurrencyRUB"]'):
                        BidCurrency = BidCurrency.get_attribute('innerText').strip()

                if BidCurrency != '':
                    # BidCurrency = Translate(BidCurrency)
                    BidCurrency = string.capwords(str(BidCurrency))
                else:
                    pass
                # ======================================================================================================================

                ENI = ''
                for ENI in browser.find_elements_by_xpath('//*[@id="PurchaseInfo_PurchaseIntegratorCode"]'):
                    ENI = ENI.get_attribute('innerText').strip()

                if ENI == '':
                    for ENI in browser.find_elements_by_xpath('//*[@id="PurchaseInfo_PurchaseOOSregistrationNumber"]'):
                        ENI = ENI.get_attribute('innerText').strip()

                if ENI != '':
                    # ENI = Translate(ENI)
                    ENI = string.capwords(str(ENI))
                else:
                    pass
                Procurement_Items = ''
                tr_count = 0
                for item_name in browser.find_elements_by_xpath('//*[@id="PurchaseObjectPanel"]/tr/td[1]'):
                    if tr_count == 2:
                        item_name = item_name.get_attribute('innerText').strip()
                        Procurement_Items += item_name + ', '
                    else:
                        tr_count += 1
                if Procurement_Items != '':
                    Procurement_Items = Procurement_Items.rstrip(', ').strip()
                Tender_Details = 'Объекты закупки: '+Procurement_Items+'<br>\nТип процедуры: ' + str(Type_of_procedure) + '<br>\n''Начальная (максимальная) цена контракта: ' + str(contract_price) + '<br>\n''Начальная (максимальная) цена контракта с заказчиком: ' + str(BidCurrency) + '<br>\n''Номер процедуры UIS: ' + str(ENI)
                SegField[18] = Tender_Details

                # ====================================================== Title ================================================================

                if Name_of_procedure != '':
                    # Name_of_procedure = Translate(Name_of_procedure)
                    Name_of_procedure = string.capwords(str(Name_of_procedure))
                    SegField[19] = str(Name_of_procedure).strip()
                # ====================================================== submission Date ================================================================
                submission_Date = ''
                for submission_Date in browser.find_elements_by_xpath('//*[@content="leaf:requestdate"]'):
                    submission_Date = submission_Date.get_attribute('innerText').strip()

                if submission_Date == '':
                    for submission_Date in browser.find_elements_by_xpath('//*[@id="TenderInfo_ApplSubmissionStopDate"]'):
                        submission_Date = submission_Date.get_attribute('innerText').strip()

                if submission_Date == '':
                    for submission_Date in browser.find_elements_by_xpath('//*[@id="PurchasePlan_RequestStopDate"]'):
                        submission_Date = submission_Date.get_attribute('innerText').strip()

                if submission_Date == '':
                    for submission_Date in browser.find_elements_by_xpath('//*[@id="DynamicControlTenderInfo_RequestStopDate"] '):
                        submission_Date = submission_Date.get_attribute('innerText').strip()

                if submission_Date == '':
                    for submission_Date in browser.find_elements_by_xpath('//*[@id="DynamicControlRequestInfo_RequestStopDate"]'):
                        submission_Date = submission_Date.get_attribute('innerText').strip()

                if submission_Date == '':
                    for submission_Date in browser.find_elements_by_xpath('//*[@id="DynamicControlTerms_RequestStopDate"]'):
                        submission_Date = submission_Date.get_attribute('innerText').strip()

                if submission_Date == '':
                    for submission_Date in browser.find_elements_by_xpath('//*[@id="TenderInfo_RequestStopDate"]'):
                        submission_Date = submission_Date.get_attribute('innerText').strip()

                if submission_Date == '':
                    for submission_Date in browser.find_elements_by_xpath('//*[@id="Date"]'):
                        submission_Date = submission_Date.get_attribute('innerText').strip()

                if submission_Date != '':
                    submission_Date = submission_Date.partition(' ')[0].strip()
                    datetime_object = datetime.strptime(submission_Date, '%d.%m.%Y')
                    mydate = datetime_object.strftime("%Y-%m-%d")
                    SegField[24] = mydate
                else:
                    pass

                SegField[28] = href

                SegField[31] = 'sberbank_ast.ru'

                SegField[27] = "0"
                SegField[22] = "0"
                SegField[26] = "0.0"

                SegField[42] = SegField[7]
                SegField[43] = ""

                OKPD_CODE = ''
                for okpd in browser.find_elements_by_xpath('//*[@content="leaf:code"]'):
                    OKPD_CODE = okpd.get_attribute('innerText').strip()
                    break
                OKPD_MAIN = ''
                if OKPD_CODE != '':
                    OKPD2 = OKPD_CODE.split('.')
                    for i in range(len(OKPD2)):
                        if(i < 3):
                            OKPD_MAIN += OKPD2[i] + '.'
                    OKPD_MAIN = OKPD_MAIN.rstrip('.')
                    SegField[29] = OKPD_MAIN

                for SegIndex in range(len(SegField)):
                    print(SegIndex, end=' ')
                    print(SegField[SegIndex])
                    SegField[SegIndex] = html.unescape(str(SegField[SegIndex]))
                    SegField[SegIndex] = str(SegField[SegIndex]).replace("'", "''")
                a = False
                if len(SegField[19]) >= 200:
                    SegField[19] = str(SegField[19])[:200]+'...'
                if len(SegField[18]) >= 1500:
                    SegField[18] = str(SegField[18])[:1500]+'...'

                if str(SegField[29]) != '':
                    check_date(get_htmlSource, SegField, Hidden_Script,get_htmlsource_For_XML_DATA)
                else:
                    print('\n OKPD NOT FOUND \n')
                    a = False
            else:
                a = False
                print('Purchaser Not Found')
                Global_var.Purchaser_NOT_Found += 1
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print("Error ON : ", sys._getframe().f_code.co_name + "--> " + str(e), "\n", exc_type, "\n", fname, "\n",
                  exc_tb.tb_lineno)
            a = True
            time.sleep(5)


def check_date(get_htmlSource, SegField,Hidden_Script,get_htmlsource_For_XML_DATA):
    a = 0
    while a == 0:
        tender_date = str(SegField[24])
        nowdate = datetime.now()
        date2 = nowdate.strftime("%Y-%m-%d")
        try:
            if tender_date != '':
                deadline = time.strptime(tender_date , "%Y-%m-%d")
                currentdate = time.strptime(date2 , "%Y-%m-%d")
                if deadline > currentdate:
                    from Insert_On_Database import insert_in_Local,create_filename
                    insert_in_Local(get_htmlSource, SegField, Hidden_Script, get_htmlsource_For_XML_DATA)
                    a = 1
                else:
                    print("Tender Expired")
                    Global_var.expired += 1
                    a = 1
            else:
                print("Deadline was not given")
                Global_var.deadline_Not_given += 1
                a = 1
        except Exception as e:
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            exc_type , exc_obj , exc_tb = sys.exc_info()
            print("Error ON : " , sys._getframe().f_code.co_name + "--> " + str(e) , "\n" , exc_type , "\n" , fname , "\n" , exc_tb.tb_lineno)
            a = 0