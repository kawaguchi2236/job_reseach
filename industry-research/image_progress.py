from pathlib import Path
import json, sys, shutil, struct

ROOT = Path(__file__).resolve().parent

def refresh():
    all_jobs = []
    summary = ['# 画像生成 全体進捗', '', '生成方式：内蔵 imagegen。各原稿の全文を使用し、高精細出力を追加指定。実際の解像度は各表に記録。', '', '|業界|保存済|全点数|進捗|', '|---|---:|---:|---|']
    for p in sorted(ROOT.glob('*/images/manifest.json')):
        jobs = json.loads(p.read_text())
        all_jobs += jobs
        done = sum(bool(j['output']) for j in jobs)
        summary.append(f'|{p.parent.parent.name}|{done}|{len(jobs)}|[詳細]({p.parent.parent.name}/images/PROGRESS.md)|')
        rows = ['# 画像生成の進捗', '', f'保存済：{done} / {len(jobs)} 点', '', '原稿：../18_image-prompts.md。使用した全文プロンプトは prompts/、画像は generated/ に保存。', '生成済と品質確認済を区別する。要確認の画像は注記を参照。', '', '|画像|使用スライド|状態|実寸px|備考|', '|---|---|---|---|---|']
        for j in jobs:
            ident = f"[{j['id']}](generated/{Path(j['output']).name})" if j['output'] else j['id']
            dims = '×'.join(map(str, j.get('dimensions', [])))
            rows.append(f"|{ident}|{j['slide']}|{j['status']}|{dims}|{j['note']}|")
        (p.parent/'PROGRESS.md').write_text('\n'.join(rows)+'\n')
    (ROOT/'IMAGE_GENERATION_PROGRESS.md').write_text('\n'.join(summary)+'\n')
    (ROOT/'image-generation-jobs.json').write_text(json.dumps(all_jobs, ensure_ascii=False, indent=2))

if len(sys.argv) > 1:
    industry, ident, status = sys.argv[1:4]
    p = ROOT/industry/'images/manifest.json'
    jobs = json.loads(p.read_text())
    job = next(j for j in jobs if j['id'] == ident)
    job['status'] = status
    if len(sys.argv) > 4:
        source = Path(sys.argv[4])
        dest = p.parent/'generated'/f'{ident}.png'
        if dest.exists():
            raise RuntimeError(f'Already exists: {dest}')
        shutil.copy2(source, dest)
        job['output'] = str(dest.relative_to(ROOT.parent))
        job['dimensions'] = list(struct.unpack('>II', dest.read_bytes()[16:24]))
    if len(sys.argv) > 5:
        job['note'] = sys.argv[5]
    p.write_text(json.dumps(jobs, ensure_ascii=False, indent=2))
refresh()
