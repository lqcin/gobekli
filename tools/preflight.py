from pathlib import Path
import re,sys
MAP=Path('fy_gobeklitepe.map')
s=MAP.read_text(encoding='ascii')
coord=re.compile(r'\(\s*(-?\d+(?:\.\d+)?)\s+(-?\d+(?:\.\d+)?)\s+(-?\d+(?:\.\d+)?)\s*\)')
def wb(s):
 st=s.find('{');d=0
 for i,ch in enumerate(s[st:],st):
  if ch=='{':d+=1
  elif ch=='}':
   d-=1
   if d==0:return s[st:i+1]
w=wb(s);blocks=[];d=0;st=None
for i,ch in enumerate(w):
 if ch=='{':
  d+=1
  if d==2:st=i
 elif ch=='}':
  if d==2 and st is not None:blocks.append(w[st:i+1]);st=None
  d-=1
a=[]
for b in blocks:
 pts=[tuple(map(float,m.groups())) for m in coord.finditer(b)]
 xs=[p[0] for p in pts];ys=[p[1] for p in pts];zs=[p[2] for p in pts]
 a.append((min(xs),max(xs),min(ys),max(ys),min(zs),max(zs),b))
def ov(a0,a1,b0,b1):return min(a1,b1)-max(a0,b0)>1e-6
sp=[]
for cls in ('info_player_start','info_player_deathmatch'):
 pat=re.compile(r'\{\s*"classname" "'+cls+r'"\s*"origin" "([^"]+)"',re.S)
 for m in pat.finditer(s):sp.append((cls,tuple(map(float,m.group(1).split()))))
hits=[]
for cls,(x,y,z) in sp:
 h=(x-16,x+16,y-16,y+16,z-36,z+36)
 for i,(x0,x1,y0,y1,z0,z1,b) in enumerate(a):
  if ov(h[0],h[1],x0,x1) and ov(h[2],h[3],y0,y1) and ov(h[4],h[5],z0,z1):hits.append((cls,(x,y,z),i))
errors=[]
if len([1 for c,_ in sp if c=='info_player_start'])!=12:errors.append('CT spawn != 12')
if len([1 for c,_ in sp if c=='info_player_deathmatch'])!=12:errors.append('T spawn != 12')
if s.count('"classname" "armoury_entity"')!=40:errors.append('weapon count != 40')
if s.count('"classname" "func_buyzone"')!=2:errors.append('buyzone count != 2')
if '"skyname" "snow"' not in s:errors.append('snow sky missing')
if hits:errors.append('spawn-solid collision: '+repr(hits[:5]))
if s.count(' CLIP [')<40:errors.append('clip system too small')
if 'GT_STONE_L' not in s or 'GT_STONE_R' not in s:errors.append('left/right wall texture split missing')
if 'GT_FLOOR_L' not in s or 'GT_FLOOR_R' not in s:errors.append('left/right floor texture split missing')
# platform/steps exact final heights
wanted=[(-548,48),(-510,82),(548,48),(510,82),(-470,112),(470,112),(-420,64),(420,64)]
for cx,top in wanted:
 found=False
 for x0,x1,y0,y1,z0,z1,b in a:
  cc=(x0+x1)/2
  if abs(cc-cx)<0.6 and abs((y0+y1)/2)<1 and abs(z0)<0.1 and abs(z1-top)<0.2:
   found=True;break
 if not found:errors.append(f'platform step missing x={cx}, top={top}')
# rear step lateral extension + front-step width check
wide=[(-548,440),(-510,440),(548,440),(510,440),(-420,440),(420,440)]
for cx,minw in wide:
 found=False
 for x0,x1,y0,y1,z0,z1,b in a:
  cc=(x0+x1)/2
  if abs(cc-cx)<0.6 and (y1-y0)>=minw-0.5:
   found=True;break
 if not found:errors.append(f'wide platform step missing x={cx}, width={minw}')
# reject low perimeter lips
for i,(x0,x1,y0,y1,z0,z1,b) in enumerate(a):
 cx=(x0+x1)/2;cy=(y0+y1)/2
 if (abs(cx)>300 or abs(cy)>300) and -20<=z0<=5 and 0<z1<=20 and z1-z0<=20:
  errors.append(f'low perimeter lip brush {i}: {(x0,x1,y0,y1,z0,z1)}');break
if errors:
 print('PREFLIGHT FAILED');[print(' -',e) for e in errors];sys.exit(1)
print('PREFLIGHT OK')
print('map: fy_gobeklitepe')
print('spawns: 12 CT + 12 T')
print('weapons: 20 CT + 20 T')
print('platform steps: rear 48 / 82 / platform 112 / front 64')
print('direction textures: LEFT + RIGHT')
print('clip faces:',s.count(' CLIP ['))
