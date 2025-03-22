#pgzero

WIDTH=650
HEIGHT=400
TITLE='Escape to Reality'
FPS=60

lery=Actor('lery',(50,350))
arkaplan=Actor('arkaplan')
sol=Actor('sol')
sag=Actor('sag')
dusman = Actor('dusman', (600, 350))
kaybettin = Actor("kaybettin")
platform_lst = [Actor ('platform', (250, 320))]
platform_lst.append( Actor ('basamak',(370, 200)))
platform_lst.append(Actor ('yer',(500, 200)))z_onay
platform_lst.append(Actor ('taban',(290, 300)))
platform_lst.append(Actor ('cimen',(320, 280)))
platform_lst.append(Actor ('toprak',(350, 250)))
kapi = Actor('kapi',(550,150))
kazandin = Actor('kazandin')
law = Actor('law',(450,389))
lew = Actor('lew',(550,389))
yer_c = 6
z_onay = True
mod = "oyun"
def draw():
    arkaplan.draw()
    if mod == "oyun":
        lery.draw()
        dusman.draw()
        kapi.draw()
        law.draw()
        lew.draw()
        for platform in platform_lst:
            platform.draw()
    if mod == "kaybettin":
        kaybettin.draw()
    if mod == 'kazandin':
        kazandin.draw()
    if mod == 'bitti':
        kaybettin.draw()
    if mod == 'oldun':
        kaybettin.draw()
def carp():
    for platform in  platform_lst:
        if lery.colliderect(platform) and lery.y < platform.y-15:
            lery.y = platform.y - 40
            return True
    return False
def update(dt):
    global mod, z_onay
    if mod == "oyun":
        if keyboard.left and lery.x > 20:
            lery.x = lery.x - 5
            lery.image = 'sol'
        elif keyboard.right and lery.x < 610:
            lery.x =lery.x + 5
            lery.image = 'sag'
        else:
            lery.image = 'lery'
       
        dusman.x = dusman.x - 5
        if lery.colliderect(dusman):
            mod = "kaybettin"
        if lery .colliderect (kapi):
            mod = 'kazandin'
        if lery.colliderect(law):
            mod = "bitti"
        if lery.colliderect(lew):
            mod = "oldun"
        if not carp():
            z_onay = True
            
        else:
            z_onay = True
        
        if lery.y < 350 and not carp():
            lery.y += yer_c
            z_onay = False
def on_key_down(key):
     if keyboard.up and (z_onay):
            lery.y -= 100
            
