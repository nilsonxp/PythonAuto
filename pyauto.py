import pyautogui as p

# p.screenshot('tela.jpg')

# p.screenshot('telacalc.jpg',region=(1998,383,(2398-1998),(1046-383)))

print(p.locateOnScreen('cal_btn_4.jpg'))
print(p.locateCenterOnScreen('cal_btn_4.jpg'))
local4 = p.locateCenterOnScreen('cal_btn_4.jpg')
p.click(local4)