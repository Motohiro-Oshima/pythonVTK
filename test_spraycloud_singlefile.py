#reading data test from sprayCloud_**.vtk

import numpy as np
#import vtkmodules.all as vtk
import vtk
from vtk.util.numpy_support import vtk_to_numpy

reader = vtk.vtkPolyDataReader()
reader.SetFileName("sprayCloud_24.vtk")
reader.Update()
data = reader.GetOutput()
#all properties of read vtk file
#print('reader.GetOutput()=\n',data)
#print(type(data))



#---------------points----------------
points=data.GetPoints()
#print('data.GetPoints()=\n',points)
npts=points.GetNumberOfPoints()
print('points.GetNumberOfPoints()=',npts)
#print('data.GetNumberOfPoints()',data.GetNumberOfPoints())
points_data=points.GetData()
#print('points_data=\n',points_data)
hexa1=vtk_to_numpy(points_data)
#print('points_shape: ',hexa1.shape)
num_points_data=vtk_to_numpy(points_data)
#print('num_points_data=\n',num_points_data)



#----------points data read--------------
g_pointdata=data.GetPointData()
#以下のvtkファイルにはどのようなpointデータが入っているのかのリストが出力される．
#解析を進める前には必ず確認する事！！！
#print('data.GetPointData()=\n',g_pointdata)
"""
#myLISA+myliquidevaporationBoilだと以下の出力になっている．
  Number Of Arrays: 29
  Array 0 name = active
  Array 1 name = origId
  Array 2 name = typeId
  Array 3 name = origProcId
  Array 4 name = tc
  Array 5 name = d
  Array 6 name = yDot
  Array 7 name = injector
  Array 8 name = KHindex
  Array 9 name = rho
  Array 10 name = d0
  Array 11 name = sigma
  Array 12 name = Cp
  Array 13 name = YIC8H18(l)
  Array 14 name = ms
  Array 15 name = user
  Array 16 name = tMom
  Array 17 name = dTarget
  Array 18 name = nParticle
  Array 19 name = age
  Array 20 name = mass0
  Array 21 name = T
  Array 22 name = tTurb
  Array 23 name = mu
  Array 24 name = y
  Array 25 name = liquidCore
  Array 26 name = UTurb
  Array 27 name = U
  Array 28 name = position0
"""
#d
g_abs_array5=g_pointdata.GetAbstractArray(5)
#print(g_abs_array5)
p_hexa5=vtk_to_numpy(g_abs_array5)
#print('point data shape:',p_hexa5.shape)

#nParticle
g_abs_array18=g_pointdata.GetAbstractArray(18)
#print(g_abs_array18)
p_hexa18=vtk_to_numpy(g_abs_array18)

#liquidCore
g_abs_array25=g_pointdata.GetAbstractArray(25)
#print(g_abs_array25)
p_hexa25=vtk_to_numpy(g_abs_array25)


##仮に10個目のdの粒子の場所と粒径はこのようになる．
#print(hexa1[10,:],p_hexa[10])

#num_particles=p_hexa.shape[0]
#print(type(num_particles))
d3=0
d2=0

for i in range (npts):
    if (p_hexa25[i] == 0.0):
#    print(i)
#    print(hexa1[i,:],p_hexa[i])
#        print(p_hexa5[i],p_hexa18[i],p_hexa25[i],hexa1[i,:])
        d3+=p_hexa18[i]*p_hexa5[i]**3
        d2+=p_hexa18[i]*p_hexa5[i]**2

d32=d3/d2
print("D32= ",d32*1e6, "micrometer")

