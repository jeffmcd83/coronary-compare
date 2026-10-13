import sys
from playwright.sync_api import sync_playwright
U=sys.argv[1];T=sys.argv[2];A='/workspace/coronary-specs/app/'
with sync_playwright() as p:
  b=p.chromium.launch(executable_path='/usr/bin/google-chrome');errs=[]
  for vp,n in [({'width':1300,'height':900},'desk'),({'width':390,'height':844},'mob')]:
    pg=b.new_context(viewport=vp).new_page();pg.on('pageerror',lambda e:errs.append(str(e)));pg.on('console',lambda m:m.type=='error' and errs.append(m.text))
    lab=lambda: pg.locator('th.a',has_text='Reprocessed').count()
    pg.goto(U+'#c=DES');pg.wait_for_timeout(2000);r1=lab()
    pg.goto(U+'#c=Imaging%20%26%20physiology&m=Eagle%20Eye%20Platinum%20RX~NES%20Reprocessed%20Eagle%20Eye%20Platinum%20RX~~');pg.reload();pg.wait_for_timeout(2000);r2=lab()
    pg.screenshot(path=A+f'{T}-reproc-shown-{n}.png')
    pg.click('.pk .x[data-i="1"]');pg.wait_for_timeout(500);r3=lab();pg.check('#diff');pg.wait_for_timeout(300);r4=lab();pg.uncheck('#diff')
    pg.goto(U+'#c=DES');pg.reload();pg.wait_for_timeout(2000)
    for v in ['cmp','stk','dsk']:
      pg.select_option('#vw',v);pg.wait_for_timeout(300)
      pg.click('.pk .x[data-i="1"]');pg.wait_for_timeout(400)
      cols=pg.locator('thead th').count();slots=pg.locator('thead th.slot').count();pg.screenshot(path=A+f'{T}-slot-removed-{v}-{n}.png')
      for i in range(4): pg.locator(f'.pk .x[data-i="{i}"]').dispatch_event('click');pg.wait_for_timeout(150)
      pg.wait_for_timeout(400);ca=pg.locator('thead th').count();rows=pg.locator('tbody tr').count();pg.screenshot(path=A+f'{T}-all-empty-{v}-{n}.png')
      print(n,v,'cols',cols,'slots',slots,'| all-empty cols',ca,'rows',rows)
      pg.goto(U+'#c=DES&m=');pg.evaluate('location.hash="c=DES"');pg.reload();pg.wait_for_timeout(1500)
    print(n,'reproc label: DES',r1,'with reprocessed',r2,'after removing reprocessed',r3,'diff mode',r4)
  print('errors',errs)
