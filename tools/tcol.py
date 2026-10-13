import sys;U=sys.argv[1];T=sys.argv[2]
from playwright.sync_api import sync_playwright
A='/workspace/coronary-specs/app/'
with sync_playwright() as p:
  b=p.chromium.launch(executable_path='/usr/bin/google-chrome');errs=[]
  for vp,n in [({'width':1300,'height':900},'desk'),({'width':390,'height':844},'mob')]:
    pg=b.new_context(viewport=vp).new_page();pg.on('pageerror',lambda e:errs.append(str(e)));pg.on('console',lambda m:m.type=='error' and errs.append(m.text))
    pg.goto(U+'#c=DES');pg.wait_for_timeout(2500)
    hd=pg.eval_on_selector_all('th.hp .vend','e=>e.map(x=>x.innerText.replace(/\\s+/g," "))');print(n,'headers',hd)
    for v in ['cmp','stk','dsk']:
      pg.select_option('#vw',v);pg.wait_for_timeout(300);pg.screenshot(path=A+f'{T}-cols-{v}-{n}.png')
    pg.select_option('#vw','cmp');pg.select_option('#cat','Guidewire');pg.wait_for_timeout(400)
    pg.click('.pk input[data-i="3"]');pg.wait_for_timeout(300)
    print(n,'Other groups',pg.locator('.pk input[data-i="3"] ~ .list .grp').count(),'items',pg.locator('.pk input[data-i="3"] ~ .list [data-m]').count())
    pg.screenshot(path=A+f'{T}-other-dropdown-{n}.png');pg.keyboard.press('Escape')
    pg.fill('#gq','shockwave');pg.wait_for_timeout(400);pg.screenshot(path=A+f'{T}-search-{n}.png')
    pg.locator('#gl [data-k]').first.dispatch_event('mousedown');pg.wait_for_timeout(500)
    print(n,'after search cat',pg.input_value('#cat'),'col3',pg.input_value('.pk input[data-i="3"]'))
    pg.locator('.fam').first.click();pg.wait_for_timeout(300);print(n,'family open',pg.is_visible('#fd'));pg.screenshot(path=A+f'{T}-family-{n}.png');pg.keyboard.press('Escape')
    pg.check('#diff');pg.wait_for_timeout(300);pg.uncheck('#diff')
    pg.locator('tr.sh').first.click();pg.wait_for_timeout(200);print(n,'collapsed',pg.locator('tbody.col').count())
  print('errors',errs)
