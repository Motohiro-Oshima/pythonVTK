#reading data test from sprayCloud_**.vtp
#https://qiita.com/hiro_kuramoto/items/f1bb4af055dfe7e9fd7e

import numpy as np
#import vtkmodules.all as vtk
import vtk
from vtk.util.numpy_support import vtk_to_numpy

reader = vtk.vtkXMLPolyDataReader()
reader.SetFileName("sprayCloud_1.vtp")
reader.Update()
data = reader.GetOutput()
#all properties of read vtk file
#print('reader.GetOutput()=\n',data)
#print(type(data))



#---------------points----------------
points=data.GetPoints()
#print('data.GetPoints()=\n',points)
npts=points.GetNumberOfPoints()
#print('points.GetNumberOfPoints()=',npts)
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

  Number Of Arrays: 30
  Array 0 name = active
  Array 1 name = origId
  Array 2 name = origProcId
  Array 3 name = typeId
  Array 4 name = Cp
  Array 5 name = KHindex
  Array 6 name = T
  Array 7 name = YC7H16(l)
  Array 8 name = age
  Array 9 name = d
  Array 10 name = d0
  Array 11 name = dTarget
  Array 12 name = injector
  Array 13 name = liquidCore
  Array 14 name = mass0
  Array 15 name = ms
  Array 16 name = mu
  Array 17 name = nParticle
  Array 18 name = rho
  Array 19 name = sigma
  Array 20 name = tMom
  Array 21 name = tTurb
  Array 22 name = tc
  Array 23 name = user
  Array 24 name = y
  Array 25 name = yDot
  Array 26 name = U
  Array 27 name = UCorrect
  Array 28 name = UTurb
  Array 29 name = position0
"""

#d
g_abs_array9=g_pointdata.GetAbstractArray(9)
#print("d",g_abs_array9)
p_hexa9=vtk_to_numpy(g_abs_array9)
#print('point data shape:',p_hexa9.shape)
print("d",p_hexa9)

#nParticle
g_abs_array17=g_pointdata.GetAbstractArray(17)
#print("nParticle",g_abs_array17)
p_hexa17=vtk_to_numpy(g_abs_array17)
print("nParticle",p_hexa17)

#liquidCore
g_abs_array13=g_pointdata.GetAbstractArray(13)
#print("liquidCore",g_abs_array13)
p_hexa13=vtk_to_numpy(g_abs_array13)
print("liquidCore",p_hexa13)

#T
g_abs_array6=g_pointdata.GetAbstractArray(6)
#print("T",g_abs_array6)
p_hexa6=vtk_to_numpy(g_abs_array6)
print("T",p_hexa6)

##仮に10個目のdの粒子の場所と粒径はこのようになる．
#print(hexa1[10,:],p_hexa[10])

#num_particles=p_hexa.shape[0]
#print(type(num_particles))
