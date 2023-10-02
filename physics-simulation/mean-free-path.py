#Air molecules' mean free path
from visual import*
from random import random
from visual.graph import*

N=50
L=((24.4E-3/6E23*N))**(1/3.0)/2
m,size=4E-3/6E23,310E-12
L_size=L-size
k,T=1.38E-23,298.0
t,dt=0,0.5E-13
vrms=(3*k*T/m)**0.5
atoms=[]
p_x1=[] #1 for negative
p_x2=[]
p_y1=[]
p_y2=[]
p_z1=[]
p_z2=[]
free_path=list(repeat(0,N))
total_path=[]

deltav=100.
vdist=gdisplay(x=800,y=0,ymax=N*deltav/1000.,width=500,height=300,xtitle='v',ytitle='dN')
theory=gcurve(color=color.cyan)
dv=10.
for v in arange(0.,3001.+dv,dv):
    theory.plot(pos=(v,(deltav/dv)*N*4.*pi*((m/(2.*pi*k*T))**1.5)*exp((-0.5*m*v**2)/(k*T))*v**2*dv))
observation=ghistogram(bins=arange(0.,3000.,deltav),accumulate=1,average=1,color=color.red)

scene=display(width=800,height=800,background=(0.2,0.2,0))
container=box(length=2*L,height=2*L,width=2*L,opacity=0.2,color=color.yellow)
for i in range(N):
    position=vector(-L_size+2*L_size*random(),-L_size+2*L_size*random(),-L_size+2*L_size*random())
    if i==N-1:
        atom=sphere(pos=position,radius=size,color=color.yellow,make_trail=True,retain=600)
    else:
        atom=sphere(pos=position,radius=size,color=(random(),random(),random()))
    ra,rb=pi*random(),2*pi*random()
    atom.m,atom.v=m,vector(vrms*sin(ra)*cos(rb),vrms*sin(ra)*cos(rb),vrms*sin(ra)*cos(rb))
    atoms.append(atom)

def vcollision(a1,a2):
    v1prime=a1.v-2*a2.m/(a1.m+a2.m)*(a1.pos-a2.pos)*dot(a1.v-a2.v,a1.pos-a2.pos)/abs(a1.pos-a2.pos)**2
    v2prime=a2.v-2*a1.m/(a1.m+a2.m)*(a2.pos-a1.pos)*dot(a2.v-a1.v,a2.pos-a1.pos)/abs(a2.pos-a1.pos)**2
    return v1prime,v2prime

while True:
    t+=dt
    rate(1000)
    v=[]
    for i in range(N):
        atoms[i].pos+=atoms[i].v*dt
        v.append(mag(atoms[i].v))
        free_path[i]+=abs(atoms[i].v*dt)
    observation.plot(data=v)

    for i in range(N):
        for j in range(N):
            if i!=j and abs(atoms[i].pos-atoms[j].pos)<=2*size:
                atoms[i].v,atoms[j].v=vcollision(atoms[i],atoms[j])
                total_path.append(free_path[i]+free_path[j])
                free_path[i],free_path[j]=0,0

    for i in range(N):
        if atoms[i].pos.x<=-L_size:
            atoms[i].v.x=-atoms[i].v.x
            p_x1.append(2*m*abs(atoms[i].v.x)/(dt*(2*L)**2))
        if atoms[i].pos.x>=L_size:
            atoms[i].v.x=-atoms[i].v.x
            p_x2.append(2*m*abs(atoms[i].v.x)/(dt*(2*L)**2))
        if atoms[i].pos.y<=-L_size:
            atoms[i].v.y=-atoms[i].v.y
            p_y1.append(2*m*abs(atoms[i].v.y)/(dt*(2*L)**2))
        if atoms[i].pos.y>=L_size:
            atoms[i].v.y=-atoms[i].v.y
            p_y2.append(2*m*abs(atoms[i].v.y)/(dt*(2*L)**2))
        if atoms[i].pos.z<=-L_size:
            atoms[i].v.z=-atoms[i].v.z
            p_z1.append(2*m*abs(atoms[i].v.z)/(dt*(2*L)**2))
        if atoms[i].pos.z>=L_size:
            atoms[i].v.z=-atoms[i].v.z
            p_z2.append(2*m*abs(atoms[i].v.x)/(dt*(2*L)**2))

    if t>=1000*dt:
        print 'x1 pressure:'+str(sum(p_x1)/len(p_x1))
        print 'x2 pressure:'+str(sum(p_x2)/len(p_x2))
        print 'y1 pressure:'+str(sum(p_y1)/len(p_y1))
        print 'y2 pressure:'+str(sum(p_y2)/len(p_y2))
        print 'z1 pressure:'+str(sum(p_z1)/len(p_z1))
        print 'z2 pressure:'+str(sum(p_z2)/len(p_z2))
        print 'mean free path:'+str(sum(total_path)/len(total_path))
        #Theoretical value of mean free path :1.4E-8
        total_path=[]
        t=0           
