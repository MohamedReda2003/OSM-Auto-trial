import subprocess
subprocess.check_call([ "pip", "install", "playwright"])
subprocess.check_call([ "playwright", "install", "chromium"])
subprocess.check_call([ "playwright", "install-deps"]) 


from playwright.sync_api import Playwright, sync_playwright, expect
import time 
import sys 
num=60
num1 =60
num2 =60
print("for osm coins . . .")

def run(playwright: Playwright) -> None:
    global num1
    global num2 
    global num
    f= time.localtime()
    currenttime = time.strftime("%H:%M:%S", f)
    print(currenttime)
    #try:
    
   
    browser = playwright.chromium.launch(args=["--fast-execution"])
    context = browser.new_context()
  
        # Open new page
    try:
        page = context.new_page()
        # Go to https://en.onlinesoccermanager.com/PrivacyNotice?nextUrl=%2FLogin
        page.goto("https://en.onlinesoccermanager.com/PrivacyNotice?nextUrl=%2FLogin",timeout=500000)
        #page.wait_for_load_state('load')
        # Click button:has-text("Allow")
        page.wait_for_load_state("networkidle")
        page.wait_for_url("https://en.onlinesoccermanager.com/PrivacyNotice?nextUrl=%2FLogin")
        # page.wait_for_timeout(10000)
        page.wait_for_load_state("networkidle")
        page.wait_for_selector("button:has-text(\"Allow\")").click()
        page.wait_for_url("https://en.onlinesoccermanager.com/Register?nextUrl=/Login")
        # Click text=Log in
        page.locator("text=Log in").click()
        page.wait_for_url("https://en.onlinesoccermanager.com/Login")
        # Click [placeholder="Manager name"]
        page.locator("[placeholder=\"Manager name\"]").click()
        # Fill [placeholder="Manager name"]
        page.locator("[placeholder=\"Manager name\"]").fill("Username")
        # Click [placeholder="Password"]
        page.locator("[placeholder=\"Password\"]").click()
        # Fill [placeholder="Password"]
        page.locator("[placeholder=\"Password\"]").fill("password")
        # Click #login
        page.locator("#login").click()
  
        
        page.wait_for_timeout(10000)
        page.wait_for_load_state("networkidle")
        page.is_visible('//html/body/div[3]/div[2]/div/div[4]/div[1]/div[3]')
        coins=page.wait_for_selector("//*[@id='balances']/div[1]/div[1]/div/span",timeout=100000)
        print(coins.inner_text())
        
        first= coins.inner_text()
        
        co=coins.inner_text()
        for i in range(5):
            page.wait_for_load_state("networkidle")
            coins.click()
        # Click #product-category-free > .products-section-body > div > .product-body > .product-info > .image-container >> nth=0
            page.wait_for_selector('//*[@id="product-category-free"]/div[2]/div[1]/div/div[1]/div/div').click()
            
            coins_new=coins=page.locator("//*[@id='balances']/div[1]/div[1]/div/span")
            page.wait_for_load_state("networkidle")
            try:
                if page.locator('//*[@id="modal-dialog-alert"]/div[4]/div/div/div/div[2]/div/div/p'):
                    para=page.locator('//*[@id="modal-dialog-alert"]/div[4]/div/div/div/div[2]/div/div/p').inner_text()
                    if 'hour' in para:
                        num1=60
                    elif 'max' in para:
                        context.close()
                        browser.close()
                        execute()
                        
                    else :
                        num1 = ''.join(filter(lambda i: i.isdigit(), para))
                        num1 =int(num1)
                    print(f'wait for {num1} minutes ')
                    break 
            except :
                pass
            h=0      
            while int(coins_new.inner_text())==int(co):
                coins_new=coins=page.locator("//*[@id='balances']/div[1]/div[1]/div/span")
                page.wait_for_timeout(1000)
                h+=1
                # if h==100 :
                #     # page.locator('text=ok').click()
                #     page.reload()
                print(int(coins_new.inner_text()),':::::::::::::::::::::::::::::',int(co))
            # print(coins_new.inner_text())
            print('this part is finished ')
            page.reload()
            co =coins_new.inner_text()
            print('+1')
            print(coins_new.inner_text())
        page.wait_for_load_state("networkidle")
        page.goto("https://en.onlinesoccermanager.com/BusinessClub")
        # page.wait_for_timeout(10000)
        # co=coins_new.inner_text()
        print(co)
        for i in range (5):
            # print(co)
            page.wait_for_load_state("networkidle")
            print("Let's start the second part ...")
            page.wait_for_selector("text=Watch ad").click()
            
            #print('hhhhhh')
            try:
                if page.locator('//*[@id="modal-dialog-alert"]/div[4]/div/div/div/div[2]/div/div/p'):
                    para=page.locator('//*[@id="modal-dialog-alert"]/div[4]/div/div/div/div[2]/div/div/p').inner_text()
                    if 'hour' in para:
                        num2=60
                    else :
                        num2 = ''.join(filter(lambda i: i.isdigit(), para))
                        num2 =int(num2)
                    print(f'wait for {num2} minutes ')
                    print("seen")
                    break 
            except :
                print("nothing")
                pass
            print("+1")
            while int(coins_new.inner_text())==int(co):
                coins_new=coins=page.locator("//*[@id='balances']/div[1]/div[1]/div/span")
                page.wait_for_load_state("networkidle")
                print(int(coins_new.inner_text()),':::::::::::::::::::::::::::::',int(co))
            page.reload()
            co =coins_new.inner_text()
            print(f'{i} step. . . ')
            print(co)
        
        final=co
        #print('We added',final-first)
        
        print("Done this time ...")
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print(current_time)
        print("We will wait  ",min(num1,num2),' mins')
        num=min(num1,num2 )
        
        
        # ---------------------
        context.close()
        browser.close()
        
                
    
    # execute()
    except Exception as e  :
        print(e)
        context.close()
        browser.close()
        pass
    f= time.localtime()
    nowt = time.strftime("%H:%M:%S", f)
    
        
    time.sleep(5)
def execute():
    with sync_playwright() as playwright:
        try:
            run(playwright)
        except Exception as e :
            print(e)
            pass
            
def count_down(ts):
    if ts :
        print(ts)
        ts-=1
        time.sleep(1)
        count_down(ts)
    else :
        print("done")


while True :
    execute()
    count_down(num*60)
#execute()
