import sys;U=sys.argv[1];T=sys.argv[2]
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
  b=p.chromium.launch(executable_path='/usr/bin/google-chrome');errs=[]
  for vp,n in [({'width':1300,'height':900},'desk'),({'width':390,'height':844},'mob')]:
    pg=b.new_context(viewport=vp).new_page();pg.on('pageerror',lambda e:errs.append(str(e)));pg.on('console',lambda m:m.type=='error' and errs.append(m.text))
    pg.goto(U+'#c=DES');pg.wait_for_timeout(2500)
    for v in ['cmp','stk','dsk']:
      pg.select_option('#vw',v);pg.wait_for_timeout(300)
      pg.locator('.pk .x[data-i="3"]').dispatch_event('click');pg.wait_for_timeout(300)
      mfs=pg.eval_on_selector('.pk select.mf[data-i="3"]','s=>[...s.options].map(o=>o.value).filter(Boolean)')
      pg.select_option('.pk select.mf[data-i="3"]',mfs[0]);pg.wait_for_timeout(300)
      pg.click('.pk input[data-i="3"]');pg.wait_for_timeout(300)
      items=pg.locator('.pk input[data-i="3"] ~ .list > div').count();dis=pg.locator('.pk input[data-i="3"] ~ .list > .dis').count()
      pg.screenshot(path=f'/workspace/coronary-specs/app/{T}-hdrpicker-open-{v}-{n}.png')
      en=pg.locator('.pk input[data-i="3"] ~ .list > div[data-m]')
      if en.count(): en.first.dispatch_event('mousedown');pg.wait_for_timeout(400)
      vals=[pg.input_value(f'.pk input[data-i="{i}"]') for i in range(4)];f=[x for x in vals if x]
      pg.click('#gd summary');pg.wait_for_timeout(200);gd=pg.locator('#gd li').count();pg.screenshot(path=f'/workspace/coronary-specs/app/{T}-guides-{v}-{n}.png');pg.keyboard.press('Escape')
      print(n,v,'mfr',mfs[0],'list',items,'disabled',dis,'filled',len(f),'dupes',len(f)-len(set(f)),'guides',gd)
      pg.screenshot(path=f'/workspace/coronary-specs/app/{T}-hdrpicker-{v}-{n}.png')
  print('errors',errs)
