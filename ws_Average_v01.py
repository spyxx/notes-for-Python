#    Script:     ws_Average
#    Version:    1.0
#    Author:     Wesley Schneider
#    Website:    http://www.wanimation.com
#	 E-mail:	 contact@wanimation.com
#    Descr:		Select first object, second object and Middle object. Press Do It!

#    Requires:   put in the script folder
print '-----------------------------------------start--------------------------------------'
import maya.cmds as cmds

#End Var
def quanti():
	s = cmds.ls( sl=True )

	rotplus1=cmds.shadingNode ('plusMinusAverage',au=1)
	transplus2=cmds.shadingNode ('plusMinusAverage',au=1)
	scaleplus3=cmds.shadingNode ('plusMinusAverage',au=1)
	
	cmds.setAttr (rotplus1+'.operation', 3);
	cmds.setAttr (transplus2+'.operation', 3);
	cmds.setAttr (scaleplus3+'.operation', 3);

	cmds.connectAttr(s[0]+'.rotate',rotplus1+ '.input3D[0]',f=1 )
	cmds.connectAttr(s[1]+'.rotate',rotplus1+ '.input3D[1]',f=1 )
	cmds.connectAttr(rotplus1 + '.output3D', s[2]+'.rotate', f=1)
	
	cmds.connectAttr(s[0]+'.translate',transplus2+ '.input3D[0]',f=1 )
	cmds.connectAttr(s[1]+'.translate',transplus2+ '.input3D[1]',f=1 )
	cmds.connectAttr(transplus2+ '.output3D', s[2]+'.translate', f=1)
	
	cmds.connectAttr(s[0]+'.scale',scaleplus3+ '.input3D[0]',f=1 )
	cmds.connectAttr(s[1]+'.scale',scaleplus3+ '.input3D[1]',f=1 )
	cmds.connectAttr(scaleplus3+ '.output3D', s[2]+'.scale', f=1)
	

if cmds.window('ws_average', exists=True):
	cmds.deleteUI ("ws_average")
windowaverage = cmds.window("ws_average", s=True,w=300,h=340,ret=True)
cmds.columnLayout( adjustableColumn=True )

cmds.text(l='AVERAGE', fn='boldLabelFont')
cmds.frameLayout( label='help', cll=True)
cmds.frameLayout( label='', labelAlign='top', borderStyle='in' )
cmds.columnLayout()

cmds.text( l= '1- select First Object')
cmds.text( l= '2- select Last Object')
cmds.text( l= '3- select Middle Object')


cmds.setParent( '..' )
cmds.setParent( '..' )
cmds.setParent( '..' )
cmds.button(l='Do it!',c='quanti()')
#------
cmds.separator(st='doubleDash')
cmds.text(l='Wesley Schneider - 2010')
cmds.text(l='www.wanimation.com', fn='boldLabelFont')
#------

cmds.showWindow( windowaverage )