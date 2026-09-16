import re,sys,zlib
def stream_of(b,data=None):
    m=re.search(rb'stream\r?\n(.*?)endstream',b,re.S)
    if not m: return None
    raw=m.group(1)
    if b'/FlateDecode' in b:
        try: return zlib.decompressobj().decompress(raw)
        except Exception: return None
    return raw
def load(path):
    data=open(path,'rb').read()
    objs={}
    for m in re.finditer(rb'(\d+)\s+(\d+)\s+obj(.*?)endobj', data, re.S):
        objs[int(m.group(1))]=m.group(3)
    for n in [n for n,b in objs.items() if b'/ObjStm' in b]:
        b=objs[n]; s=stream_of(b)
        if not s: continue
        N=int(re.search(rb'/N\s+(\d+)',b).group(1)); first=int(re.search(rb'/First\s+(\d+)',b).group(1))
        hdr=s[:first].split()
        for i in range(N):
            num=int(hdr[2*i]); off=int(hdr[2*i+1])
            end=int(hdr[2*i+3])+first if i+1<N else len(s)
            objs[num]=s[first+off:end]
    return objs
def parse_cmap(s):
    mp={}
    for m in re.finditer(rb'beginbfchar(.*?)endbfchar',s,re.S):
        for a,b2 in re.findall(rb'<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>',m.group(1)):
            mp[int(a,16)]=''.join(chr(int(b2[i:i+4],16)) for i in range(0,len(b2),4))
    for m in re.finditer(rb'beginbfrange(.*?)endbfrange',s,re.S):
        for lo,hi,dst in re.findall(rb'<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>',m.group(1)):
            lo,hi,d=int(lo,16),int(hi,16),int(dst,16)
            for i in range(lo,hi+1): mp[i]=chr(d+i-lo)
    return mp
def extract(path):
    objs=load(path)
    cmaps={}
    for n,b in objs.items():
        m=re.search(rb'/ToUnicode\s+(\d+)\s+0\s+R',b)
        if m:
            s=stream_of(objs.get(int(m.group(1)),b''))
            if s: cmaps[n]=parse_cmap(s)
    res={}
    for n,b in objs.items():
        for nm,num in re.findall(rb'/([A-Za-z0-9_+.]+)\s+(\d+)\s+0\s+R',b):
            try:
                num=int(num)
                if num in cmaps: res[nm.decode('latin1')]=num
            except: pass
    out=[]
    for n,b in objs.items():
        s=stream_of(b)
        if not s or b'BT' not in s: continue
        cur=None
        for m in re.finditer(rb'/([A-Za-z0-9_+.]+)\s+[\d.]+\s+Tf|<([0-9A-Fa-f\s]+)>\s*Tj|\[(.*?)\]\s*TJ|(T\*|Td|TD|ET)', s, re.S):
            if m.group(1) is not None:
                cur=res.get(m.group(1).decode('latin1')); continue
            if m.group(4) is not None:
                out.append('\n'); continue
            txt=m.group(0)
            mp=cmaps.get(cur,{})
            buf=''
            for h in re.findall(rb'<([0-9A-Fa-f\s]+)>',txt):
                h=re.sub(rb'\s',b'',h)
                for i in range(0,len(h)-3,4):
                    buf+=mp.get(int(h[i:i+4],16),'')
            if buf: out.append(buf)
    t=''.join(out)
    t=re.sub(r'\n{2,}','\n',t)
    return t
if __name__=='__main__':
    print(extract(sys.argv[1]))
