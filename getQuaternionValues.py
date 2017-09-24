import maya.OpenMaya as OpenMaya

#make  a object of type MObject
obj=OpenMaya.MObject()

#make a object of type MSelectionList
selList=OpenMaya.MSelectionList()

#add something to it
#you could retrieve this form function or the user selection
selList.add("pSphere1")

#fill in the MObject
selList.getDependNode(0,obj)

#check if its a transform
if (obj.hasFn(OpenMaya.MFn.kTransform)):
  #then we can add it to transfrom Fn
  #Fn is basically the collection of functions for given objects
  xform=OpenMaya.MFnTransform(obj)
  #now the api requires pointer types
  x = OpenMaya.MScriptUtil().asDoublePtr()
  y = OpenMaya.MScriptUtil().asDoublePtr()
  z = OpenMaya.MScriptUtil().asDoublePtr()
  w = OpenMaya.MScriptUtil().asDoublePtr()
  #we are ready to ask the values
  xform.getRotationQuaternion(x,y,z,w)
  #convert them back to normal python floats
  x = OpenMaya.MScriptUtil().getDouble(x)
  y = OpenMaya.MScriptUtil().getDouble(y)
  z = OpenMaya.MScriptUtil().getDouble(z)
  w = OpenMaya.MScriptUtil().getDouble(w)
  #and print it out
  print ("QuatRotation is: "+str(x)+" "+str(y)+" "+str(z)+" "+str(w))