from chess import Board,Move
from tkinter import Tk,Button,Text,INSERT
from math import floor
from threading import Thread
from contextlib import redirect_stdout
from io import StringIO
ch={'P':0,'N':48,'B':32,'R':32,'Q':65,'K':0}
uni={'P':'♟','N':'♞','B':'♝','R':'♜','Q':'♛','K':'♚','p':'♙','n':'♘','b':'♗','r':'♖','q':'♕','k':'♔'}
dic={'P':850,'N':3300,'B':4000,'R':5000,'Q':9500,'K':0}
di={'P':(0,0,0,0,0,0,0,0,-50,-50,25,50,50,-50,-250,-250,-40,-40,20,40,40,-40,-200,-200,-30,-30,15,30,30,-30,-150,-150,-20,-20,10,20,20,-20,-100,-100,-10,-10,5,10,10,-10,-50,-50,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),'N':(-50,-50,-50,-50,-50,-50,-50,-50,-50,0,0,0,0,0,0,-50,-50,0,75,75,75,75,50,-50,-50,0,75,200,200,150,100,-50,-50,0,75,200,200,100,50,-50,-50,0,75,75,75,75,50,-50,-50,0,0,0,0,0,0,-50,-50,-50,-50,-50,-50,-50,-50,-50),'B':(-50,-50,-50,-50,-50,-50,-50,-50,-50,0,0,0,0,0,0,-50,-50,0,75,75,75,75,0,-50,-50,0,75,150,150,75,0,-50,-50,0,75,150,150,75,0,-50,-50,0,75,75,75,75,0,-50,-50,0,0,0,0,0,0,-50,-50,-50,-50,-50,-50,-50,-50,-50),'R':(0,40,80,100,100,100,75,40,0,40,80,100,100,100,75,40,0,40,80,100,100,100,75,40,0,40,80,100,100,100,75,40,0,40,80,100,100,100,75,40,0,40,80,100,100,100,75,40,0,40,80,100,100,100,75,40,0,40,80,100,100,100,75,40),'Q':(0,0,0,0,0,0,0,0,0,60,60,60,60,60,60,0,0,60,120,120,120,120,60,0,0,60,120,180,180,120,60,0,0,60,120,180,180,120,60,0,0,60,120,120,120,120,60,0,0,60,60,60,60,60,60,0,0,0,0,0,0,0,0,0),'K':(-100,-75,-125,-175,-175,-125,-75,-100,-75,-50,-100,-150,-150,-100,-50,-75,-50,-25,-75,-125,-125,-75,-25,-50,-25,0,-50,-100,-100,-50,0,-25,0,25,-25,-75,-75,-25,25,0,25,50,0,-50,-50,0,50,25,75,100,50,0,0,50,100,75,100,125,75,25,25,75,125,100),'k':(-180,-120,-90,-60,-60,-90,-120,-180,-120,-60,-30,0,0,-30,-60,-120,-90,-30,0,30,30,0,-30,-90,-60,0,30,60,60,30,0,-60,-60,0,30,60,60,30,0,-60,-90,-30,0,30,30,0,-30,-90,-120,-60,-30,0,0,-30,-60,-120,-180,-120,-90,-60,-60,-90,-120,-180)}
r=0
n=0
board=Board()
tot=StringIO()
root=Tk()
root.title('smart chess')
def alt(x)->str:
	alv=str(x).replace(' ','').replace('\n','').replace('.',' ')
	for i in uni:
		alv=alv.replace(i,uni[i])
	return alv
def g(i:int)->None:
	with redirect_stdout(tot):
		print("abcdefgh"[i-8*floor(i/8)]+str(8-floor(i/8)))
def f(x:str)->None:
	root=Tk()
	root.title('smart chess')
	for i in range(64):
		Button(root,text=x[i],width=4,command=lambda i=i:g(i),font=("David",24)).grid(row=floor(i/8),column=i-8*floor(i/8))
	Button(root,text='send',command=lambda:exit(),width=4,font=('David',24)).grid(row=9,column=4)
	root.mainloop()
t=Thread(target=f,args=[alt(board)])
t.setDaemon(True)
t.start()
board.push(Move.from_uci('0000'))
def el(z:list,bi:list)->None:
	for j in list(board.legal_moves):
		board.push(j)
		q=board.is_checkmate()*(-1000000)
		bb=str(board)
		bbb=[sum([((2*(x==x.capitalize())-1)*dic[x.capitalize()]+di[x.capitalize()][int(31.5*((2*(x==x.capitalize())-1)+1)-(2*(x==x.capitalize())-1)*i)])*(bb.replace(' ','').replace('\n','')[i]==x) for i in range(64)]) for x in ['P','p','R','r','N','n','B','b','Q','q','K','k']]
		z+=[len(list(board.legal_moves))*5+sum(bbb)+q+r+check+(n==1)*100+(sum(bi)==0)*1500+('R' in bb[8:16])*1000]
		board.pop()
def er(x,logic=1)->None:#if endgame di['K']=di['k']
	global n
	global check
	c=str(x)
	for i in list(x.legal_moves):
		x.push(i)
		z=[10**6]*x.is_checkmate()
		n+=(c.replace(' ','').replace('\n','')['abcdefgh'.index(str(x.peek())[0])+(8-int(str(x.peek())[1]))*8]=='N')+(n==1)/2
		ind=0
		r=0
		for j in alt(x):
			if j=='♖' and '♙' not in [alt(x)[i] for i in [ind%8+8*i for i in range(8)]]:r+=375 if '♟' not in [alt(x)[i] for i in [ind%8+8*i for i in range(8)]] else 125
			ind+=1
		check=x.is_check()*sum([(str(c).replace(' ','').replace('\n','')['abcdefgh'.index(str(x.peek())[0])+(8-int(str(x.peek())[1]))*8]==i)*ch[i] for i in 'PNBRQK'])
		bi=[str(x).replace(' ','').replace('\n','')['abcdefgh'.index(str(x.uci(j))[0])+(8-int(str(x.uci(j))[1]))*8]=='B' for j in list(x.pseudo_legal_moves)]
		el(z,bi)
		x.pop()
		yield min(z)
while board.result()[0]=='*':
	while True:
		while t.is_alive():
			none=None
		F=tot.getvalue().split('\n')[-3]+tot.getvalue().split('\n')[-2]
		tot=StringIO()
		if F+'q' in [str(i) for i in list(board.legal_moves)]:
			F+='0'
		if F in [str(i) for i in list(board.legal_moves)]:
			board.push(Move.from_uci(F))
			break
		else:
			t=Thread(target=f,args=[alt(board)])
			t.setDaemon(True)
			t.start()
	if board.result()[0]=='*':
		moves=list(er(board))
		board.push(list(board.legal_moves)[moves.index(max(moves))])
		t=Thread(target=f,args=[alt(board)])
		t.setDaemon(True)
		t.start()
root=Tk()
root.title('smart chess')
te=Text(root)
te.insert(INSERT,board.result())
te.pack()
root.mainloop()
