import sys, numpy as np
from PIL import Image, ImageEnhance
def brighten(path, target=118, maxg=0.62, hi=246):
    im=Image.open(path).convert('RGB'); a=np.asarray(im).astype(np.float32)/255
    lum=0.299*a[...,0]+0.587*a[...,1]+0.114*a[...,2]
    med=float(np.median(lum))*255
    if med>=target-3: return med,med
    g=max(np.log(target/255)/np.log(med/255), maxg)
    y=np.power(np.clip(a,1e-4,1),g)*255
    knee=hi-20; o=y>knee; y[o]=knee+(hi-knee)*(1-np.exp(-(y[o]-knee)/(hi-knee)))
    out=Image.fromarray(np.clip(y,0,255).astype(np.uint8))
    out=ImageEnhance.Contrast(out).enhance(1.04); out=ImageEnhance.Color(out).enhance(1.03)
    out.save(path,'WEBP',quality=88,method=6)
    b=np.asarray(out.convert('L')); return med,float(np.median(b))
for p in sys.argv[1:]:
    t=96 if 'carseat' in p else 118
    print(p, '%.0f → %.0f'%brighten(p,target=t))
