import pyautogui, time, threading
from configs import bot_configs

def getCollectorAreaData(collector_name):
    img_name = bot_configs["collecting_data"][collector_name]["img_name"]
    confidence = bot_configs["collecting_data"][collector_name]["confidence"]
    element = list(pyautogui.locateAllOnScreen('./assets/'+ img_name,confidence=confidence))
    return len(element), element

def getTotalNumberOfAvailableStack():
    count = list(pyautogui.locateAllOnScreen('./assets/empty_stack_area.png',confidence=0.99))
    return len(count)

def isCraftBarAreaExist():
    if pyautogui.locateCenterOnScreen(image='./assets/craft_bar_area.png',confidence=0.9):
        return True
    return False


# ─── REUSEABLE ──────────────────────────────────────────────────────────────────
def doCraftProcess(element_data,extra_x=0,extra_y=0):
    pyautogui.moveTo(element_data.left+extra_x,element_data.top+extra_y)
    pyautogui.click()
    time.sleep(1.5)
    if isCraftBarAreaExist():
        #IF REDIRECTED TO CRAFTBAR
        available_stack_count = getTotalNumberOfAvailableStack()
        print('available stack = ' + str(available_stack_count))
        if available_stack_count:
            for _ in range(available_stack_count):
                pyautogui.moveTo(1600,400) #place holder
                pyautogui.click()
                time.sleep(0.7)
    else:
        pyautogui.click()
        time.sleep(1.5)
        if isCraftBarAreaExist():
            #IF REDIRECTED TO CRAFTBAR
            available_stack_count = getTotalNumberOfAvailableStack()
            print('available stack = ' + str(available_stack_count))
            if available_stack_count:
                for _ in range(available_stack_count):
                    pyautogui.moveTo(1600,400)
                    pyautogui.click()
                    time.sleep(0.7)
    pyautogui.press('esc') # exit after
    time.sleep(1) # wait a bit
# ────────────────────────────────────────────────────────────────────────────────


def startCollecting(collector_name):
    total_element_count , elements = getCollectorAreaData(collector_name)
    print(f'[DEBUG]: Total {collector_name} == {total_element_count}')
    if(total_element_count):
        if 'chained' not in bot_configs["collecting_data"][collector_name]:
            for element in elements:
                doCraftProcess(element)
        else:
            print(f'[DEBUG]: Collecting {collector_name} -> with single click [chained-case]')
            pyautogui.moveTo(elements[0].left,elements[0].top)
            pyautogui.click()

def startCraftingProcessInSequence():
    startCollecting('lumberjack')
    startCollecting('smith')
    startCollecting('sugar')
    startCollecting('jelly')
    startCollecting('jammery')
    startCollecting('jellystar')
    threading.Timer(5,startCraftingProcessInSequence).start() # threading start after all operation above is done

startCraftingProcessInSequence()