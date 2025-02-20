from f_path.main import Path

P = Path

txt = P.join(P.cwd(), 'test.txt')
txt2 = P.join(P.cwd(), 'test2.txt')
txt3 = P.join(P.cwd(), 'test3.txt')
if P.e(txt):
    P.rm(txt)
if P.e(txt2):
    P.rm(txt2)

P.touch(txt)
P.file.write('dasdada', txt)
P.link(txt, txt2)
P.mv(txt, txt3)
P.chmod(txt3, '755')
