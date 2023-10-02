from visual import*
import numpy as np
#scale 100 times bigger(use meter instead of centimeter)

#create array for big loop's 50 little segments' ds vector 
ds_length=24*pi/50
dtheta=2*pi/50
Bloop_ds=np.empty((0,3),float)
Bloop_r=np.empty((0,3),float)
for i in range(0,50):
    v1=(-sin(i*dtheta),cos(i*dtheta),0)
    v2=norm(v1)*ds_length
    Bloop_ds=np.append(Bloop_ds,[[v2.x,v2.y,v2.z]],axis=0)

#create array for big loop's 50 little segments' r vector
for i in range(0,50):
    v3=(cos(i*dtheta),sin(i*dtheta),0)
    v4=norm(v3)*12
    Bloop_r=np.append(Bloop_r,[[v4.x,v4.y,v4.z]],axis=0)

#calculate magnetic flux of the small loop by adding up partition rings
#list of variables I create and their data type
m=1 #partition number
m_area=0
m_position=0
B_point=vector(0,0,0)
B_ring=0
B_total=0
#calculation
while m<=25:
    m_position=vector(m*0.24,0,30) #0.24=6/25
    m_area=pi*(m*0.24)**2-pi*((m-1)*0.24)**2
    for i in range(0,50): #Biot-Savart law (outcome should be a vector
        B_point+=10**-7*cross(Bloop_ds[i],(m_position-Bloop_r[i]))/mag(m_position-Bloop_r[i])**3

    B_ring=B_point.z*m_area #flux=A dot B
    B_total+=B_ring
    m+=1
    B_point=vector(0,0,0)

print 'M_sl=',B_total

#smae thing to M_ls
#create array for small loop's 50 little segments' ds vector 
ds_length=12*pi/50
dtheta=2*pi/50
Sloop_ds=np.empty((0,3),float)
Sloop_r=np.empty((0,3),float)
for i in range(0,50):
    v1=(-sin(i*dtheta),cos(i*dtheta),0)
    v2=norm(v1)*ds_length
    Sloop_ds=np.append(Sloop_ds,[[v2.x,v2.y,v2.z]],axis=0)

#create array for small loop's 50 little segments' r vector
for i in range(0,50):
    v3=vector(6*cos(i*dtheta),6*sin(i*dtheta),30)
    Sloop_r=np.append(Sloop_r,[[v3.x,v3.y,v3.z]],axis=0)

#calculate magnetic flux of the big loop by adding up partition rings
#list of variables I create and their data type
m=1 #partition number
m_area=0
m_position=0
B_point=vector(0,0,0)
B_ring=0
B_total=0
#calculation
while m<=50:
    m_position=vector(m*0.24,0,0) #0.24=12/50
    m_area=pi*(m*0.24)**2-pi*((m-1)*0.24)**2
    for i in range(0,50): #Biot-Savart law (outcome should be a vector
        B_point+=10**-7*cross(Sloop_ds[i],(m_position-Sloop_r[i]))/mag(m_position-Sloop_r[i])**3

    B_ring=B_point.z*m_area #flux=A dot B
    B_total+=B_ring
    m+=1
    B_point=vector(0,0,0)

print 'M_ls=',B_total
print 'they are very close!!!'
