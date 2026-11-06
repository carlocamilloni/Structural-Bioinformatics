# Optimises a complex with GFN2-xTB and then r2SCAN-3c (the salt bridge in water, CPCM). Usage: python optimise_complexes.py name
import os, subprocess, sys, time
O='/content/orca_6_1_1_linux_x86-64_shared_openmpi418_nodmrg/orca'; os.environ['OMP_NUM_THREADS']='1'
name=sys.argv[1]
L=open(name+'.xyz').read().splitlines(); n=int(L[0]); head=L[1]
qA=int(head.split('qA=')[1].split()[0]); qB=int(head.split('qB=')[1].split()[0]); q=qA+qB
solv_x = ' ALPB(water)' if name=='acetate_methylguanidinium' else ''
solv_d = ' CPCM(water)' if name=='acetate_methylguanidinium' else ''
os.makedirs(name, exist_ok=True); os.chdir(name)
coords='\n'.join(L[2:2+n])
def run(tag, kw, xyz):
    open(tag+'.inp','w').write(f'{kw}\n%geom\n  MaxIter 300\nend\n* xyz {q} 1\n{xyz}\n*\n'); t=time.time()
    subprocess.run([O, tag+'.inp'], stdout=open(tag+'.out','w'), stderr=subprocess.STDOUT)
    txt=open(tag+'.out').read()
    print(name, tag, 'OK' if 'TERMINATED NORMALLY' in txt else 'FAIL', 'converged' if 'HURRAY' in txt else 'NOT converged', round(time.time()-t),'s', flush=True)
    return '\n'.join(open(tag+'.xyz').read().splitlines()[2:2+n])
c1=run('xtb', '! Native-GFN2-XTB Opt'+solv_x, coords)
c2=run('r2scan', '! r2SCAN-3c Opt TightSCF'+solv_d, c1)
open('../'+name+'_opt.xyz','w').write(f'{n}\n{head}\n{c2}\n')
