import re,sys,zlib
from pdftext import load,stream_of,parse_cmap

def build(path):
    objs=load(path)
    cmaps={}; simple=set()
    for n,b in objs.items():
        if b'/Font' not in b and b'/BaseFont' not in b: continue
        m=re.search(rb'/ToUnicode\s+(\d+)\s+0\s+R',b)
        if m:
            s=stream_of(objs.get(int(m.group(1)),b''))
            if s: cmaps[n]=parse_cmap(s)
        elif b'/Subtype' in b and (b'/TrueType' in b or b'/Type1' in b):
            simple.add(n)
    return objs,cmaps,simple

def pages(path):
    objs,cmaps,simple=build(path)
    # page objects in order
    pgs=[n for n,b in objs.items() if re.search(rb'/Type\s*/Page\b',b)]
    out=[]
    for pn in pgs:
        b=objs[pn]
        # resources font map
        fm={}
        rs=re.search(rb'/Resources\s+(\d+)\s+0\s+R',b)
        rb_=objs.get(int(rs.group(1)),b'') if rs else b
        fo=re.search(rb'/Font\s*(?:(\d+)\s+0\s+R|<<(.*?)>>)',rb_,re.S)
        fdict=b''
        if fo:
            fdict=objs.get(int(fo.group(1)),b'') if fo.group(1) else fo.group(2)
        for nm,num in re.findall(rb'/([A-Za-z0-9_+.\-]+)\s+(\d+)\s+0\s+R',fdict):
            fm[nm.decode('latin1')]=int(num)
        # contents
        cs=re.findall(rb'/Contents\s+(?:(\d+)\s+0\s+R|\[(.*?)\])',b,re.S)
        ids=[]
        for a,arr in cs:
            if a: ids.append(int(a))
            else: ids+= [int(x) for x in re.findall(rb'(\d+)\s+0\s+R',arr)]
        data=b''.join((stream_of(objs.get(i,b'')) or b'') for i in ids)
        items=[]; cur=None; x=y=0.0
        for m in re.finditer(rb'/([A-Za-z0-9_+.\-]+)\s+[\d.\-]+\s+Tf|([\d.\-]+)\s+([\d.\-]+)\s+([\d.\-]+)\s+([\d.\-]+)\s+([\d.\-]+)\s+([\d.\-]+)\s+Tm|([\d.\-]+)\s+([\d.\-]+)\s+T[dD]|\[(.*?)\]\s*TJ|(\((?:[^()\\]|\\.)*\)|<[0-9A-Fa-f\s]+>)\s*Tj',data,re.S):
            if m.group(1):
                cur=fm.get(m.group(1).decode('latin1')); continue
            if m.group(2):
                x=float(m.group(6)); y=float(m.group(7)); continue
            if m.group(8):
                x+=float(m.group(8)); y+=float(m.group(9)); continue
            txt=m.group(10) or m.group(11)
            mp=cmaps.get(cur)
            buf=''
            if mp is not None:
                for h in re.findall(rb'<([0-9A-Fa-f\s]+)>',txt):
                    h=re.sub(rb'\s',b'',h)
                    for i in range(0,len(h)-3,4):
                        buf+=mp.get(int(h[i:i+4],16),'')
            else:
                for lit in re.findall(rb'\(((?:[^()\\]|\\.)*)\)',txt):
                    lit=re.sub(rb'\\([()\\])',rb'\1',lit)
                    buf+=lit.decode('latin1')
            if buf: items.append((round(y,1),round(x,1),buf))
        # group rows
        rows={}
        for yy,xx,t in items: rows.setdefault(yy,[]).append((xx,t))
        lines=[]
        for yy in sorted(rows,reverse=True):
            lines.append(' '.join(t for _,t in sorted(rows[yy])))
        out.append('\n'.join(lines))
    return out
if __name__=='__main__':
    ps=pages(sys.argv[1])
    for i,p in enumerate(ps):
        print(f'===== PAGE {i+1} =====')
        print(p)
