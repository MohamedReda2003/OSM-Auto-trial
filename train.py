import subprocess
subprocess.check_call([ "pip", "install", "playwright"])
subprocess.check_call([ "playwright", "install", "chromium"])
subprocess.check_call([ "playwright", "install-deps"]) 

from playwright.sync_api import Playwright, sync_playwright, expect
import time 
import random



print("for osm training . . .")



def search_text(page,text):
    
        # page.goto("https://www.example.com",timeout=10000)
        try:
            element = page.wait_for_selector(f"//*[contains(text(), '{text}')]")
            
        except :
            element=0
        return element
        # if element:
        #     print(f"Element containing text '{text}' found")
        #     print(element.inner_text())
        # else:
        #     print(f"Element containing text '{text}' not found")
        



# elapsed=100



def count_down(ts):
    if ts :
        print(ts)
        ts-=1
        time.sleep(1)
        count_down(ts)
    else :
        print("done")






def run(playwright: Playwright) -> None:
    # global elapsed
    
    
    browser = playwright.chromium.launch()
    context = browser.new_context()
  
        # Open new page
    try:
        page = context.new_page()
        # Go to https://en.onlinesoccermanager.com/PrivacyNotice?nextUrl=%2FLogin
        page.goto("https://en.onlinesoccermanager.com/PrivacyNotice?nextUrl=%2FLogin")
        # page.wait_for_load_state('load')
        # Click button:has-text("Allow")
        page.wait_for_url("https://en.onlinesoccermanager.com/PrivacyNotice?nextUrl=%2FLogin")
        # page.wait_for_timeout(10000)
        page.wait_for_selector("button:has-text(\"Allow\")").click()
        page.wait_for_url("https://en.onlinesoccermanager.com/Register?nextUrl=/Login")
        # Click text=Log in
        page.locator("text=Log in").click()
        page.wait_for_url("https://en.onlinesoccermanager.com/Login")
        # Click [placeholder="Manager name"]
        page.locator("[placeholder=\"Manager name\"]").click()
        # Fill [placeholder="Manager name"]
        page.locator("[placeholder=\"Manager name\"]").fill("mohamedredazhar")
        # Click [placeholder="Password"]
        page.locator("[placeholder=\"Password\"]").click()
        # Fill [placeholder="Password"]
        page.locator("[placeholder=\"Password\"]").fill("he3eyetR#2003")
        # Click #login
        page.locator("#login").click()
  
        page.wait_for_timeout(10000)
        # page.wait_for_load_state("networkidle")
        # page.wait_for_selector()
        page.goto('https://en.onlinesoccermanager.com/Dashboard')
        # page.wait_for_load_state("networkidle")
        ll=page.wait_for_selector("text=Moghreb Tétouan").click()
        page.wait_for_load_state("networkidle")
        page.goto("https://en.onlinesoccermanager.com/Training")
        try:
            duration=page.wait_for_selector('//*[@id="cached-html-wrapper-training"]/div[2]/div/div[1]/div/div/div/div[2]/div/div/div[3]/h1[2]').inner_text()
            print(duration)
            try:
                h=duration.split('h')[0]
                b=duration.split('h')[1]
                print(int(h))
            except :
                h=0
                b=duration
                pass
            try:
                mins=b.split('m')[0]
                print(int(mins))
                g=b.split('m')[1]
            except :
                mins=0
                g=b
                pass
            try:
                secs=g[:-1]
                print(int(secs)) 
            except :
                secs=0
                pass
            elapsed=int(secs)+int(mins)*60+int(h)*60*60
            print(f"we'll wait {elapsed} s")
        except:
            
            elements =search_text(page,"Complete")
            while elements:
                elements =search_text(page,"Complete")
                if elements !=0:
                    elements.click()
            
   
            print('training completed')
            page.goto('https://en.onlinesoccermanager.com/Dashboard')
            page.goto('https://en.onlinesoccermanager.com/Training')
            try:
               goalkeepers=['Saber']
               trained=random.choice(goalkeepers)
               page.locator("text=Goalkeeping coach Select a player Start >> button").click()
               # Click text=Donnarumma
               page.locator(f"text={trained}").click()
               print(trained)
            except :
               try:
                   remainersgoalkeepers=[value for value in goalkeepers if value != trained]
                   trained=random.choice(remainersgoalkeepers)
                   page.locator("text=Attacking coach Select a player Start >> button").click()
                   # Click text=Messi
                   page.locator(f"text={trained}").click()
                   print(trained)
                   
               except Exception as e :
                   print(e)
                   print('no Goalkeeper')
                   pass
           # Click text=Defending coach Select a player Start >> button
            try:
               defs=['C. Richards','Flamingo','J. Sands','Turitsov','Lamrabat']
               tdefs=random.choice(defs)
               page.locator("text=Defending coach Select a player Start >> button").click()
               # Click text=Hakimi
               page.locator(f"text={tdefs}").click()
               print(tdefs)
            except :
                try:
                    remainersdefs=[value for value in defs if value != tdefs]
                    page.locator("text=Attacking coach Select a player Start >> button").click()
                    
                    tdefs=random.choice(remainersdefs)
                    page.locator(f"text={tdefs}").click()
                    print(tdefs)
                    
                except Exception as e :
                   print(e)
                   print('no defender')
                   pass
           # Click text=Midfielder coach Select a player Start >> button
            try:
               mids=['El Hassnaoui','McArthur','Krouch','Radouani']
               trmids=random.choice(mids)
               page.locator("text=Midfielder coach Select a player Start >> button").click()
               # Click text=Gavi
               page.locator(f"text={trmids}").click()
               print(trmids)
            except :
                try:
                    remainersmids=[value for value in mids if value != trmids]
                    page.locator("text=Attacking coach Select a player Start >> button").click()
                    # Click text=Messi
                    trmids=random.choice(remainersmids)
                    page.locator(f"text={trmids}").click()
                    print(trmids)
                    
                except Exception as e :
                   print(e)
                   print('no Midfielder')
                   pass 
               
           # Click button:has-text("Start")
            try :
               attack=['Kamal','Robson','A. Ayew','Scheidler']
               trattack=random.choice(attack)
               page.locator("text=Attacking coach Select a player Start >> button").click()
               # Click text=Messi
               page.locator(f"text={trattack}").click()
               print(trattack)
            except :
                try :
                    remainersattackers=[value for value in attack if value != trattack]
                    page.locator("text=Attacking coach Select a player Start >> button").click()
                    trattack=random.choice(remainersattackers)
                    page.locator(f"text={trattack}").click()
                    print(trattack)
                except Exception as e :
                   print(e)
                   print('no Attacker')
                   pass
            duration=page.wait_for_selector('//*[@id="cached-html-wrapper-training"]/div[2]/div/div[1]/div/div/div/div[2]/div/div/div[3]/h1[2]').inner_text()
            print(duration)
            try:
                h=duration.split('h')[0]
                b=duration.split('h')[1]
                print(int(h))
            except :
                h=0
                b=duration
                pass
            try:
                mins=b.split('m')[0]
                print(int(mins))
                g=b.split('m')[1]
            except :
                mins=0
                g=b
                pass
            try:
                secs=g[:-1]
                print(int(secs)) 
            except :
                secs=0
                pass
            print(int(secs))            
            elapsed=int(secs)+int(mins)*60+int(h)*60*60
            print(f"we'll wait {elapsed} s")
            
        # ---------------------
        context.close()
        browser.close()
        # return elapsed
                
    
    # execute()
    except Exception as e:
        print(e)
        context.close()
        browser.close()
        elapsed=200
        pass
    return elapsed
    # time.sleep(5)




# playwright = sync_playwright()



# st.title('OSM TRAINING TRACKING ...')

# if st.button('Automate OSM training'):
with sync_playwright() as playwright:
    while True:  
        elapsed=run(playwright)
        elapsed-=30

        count_down(elapsed)
