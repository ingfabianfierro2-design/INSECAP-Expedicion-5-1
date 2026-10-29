import sys,qrcode
from pathlib import Path
from urllib.parse import urlsplit
from PIL import Image,ImageDraw,ImageFont
if len(sys.argv)!=2 or not sys.argv[1].startswith('https://'):
 raise SystemExit('Uso: python GENERAR_QR.py https://USUARIO.github.io/REPOSITORIO/')
url=sys.argv[1].rstrip('/')+'/'
folder=Path('QR_INSECAP_25');folder.mkdir(exist_ok=True)
for prefix,country in [('COL','COLOMBIA'),('VEN','VENEZUELA'),('PER','PERÚ'),('BOL','BOLIVIA'),('CHI','CHILE')]:
 for st in range(1,6):
  code=f'{prefix}-{st:02d}'; link=url+'?code='+code
  qr=qrcode.make(link).convert('RGB');qr.save(folder/(code+'.png'))
  im=Image.new('RGB',(520,650),'white');im.paste(qr.resize((450,450)),(35,75));d=ImageDraw.Draw(im);d.text((35,25),f'{country} / ESTACIÓN {st}',fill='black');d.text((180,540),code,fill='black');d.text((28,585),'Abre la app instalada si estás sin señal',fill='black');im.save(folder/(code+'_TARJETA.png'))
print('Listo: 25 QR y 25 tarjetas en',folder)
