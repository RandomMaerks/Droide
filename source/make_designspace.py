import os
from fontTools.designspaceLib import DesignSpaceDocument, AxisDescriptor, SourceDescriptor, InstanceDescriptor, RuleDescriptor

root = os.getcwd()
doc = DesignSpaceDocument()

familyName = "Droide"

#------
# axes
#------

a2 = AxisDescriptor()
a2.maximum = 1
a2.minimum = 0
a2.default = 0
a2.name = "Anthro"
a2.tag = "ANTH"
doc.addAxis(a2)

#---------
# masters
#---------

s0 = SourceDescriptor()
s0.path = "DroideFutur-Light.ufo"
s0.familyName = familyName
s0.styleName = "Futur Light"
s0.location = dict(Anthro=1)
s0.copyLib = True
s0.copyInfo = True
s0.copyGroups = True
s0.copyFeatures = True
doc.addSource(s0)

s1 = SourceDescriptor()
s1.path = "DroideAnthro-Light.ufo"
s1.familyName = familyName
s1.styleName = "Anthro Light"
s1.location = dict(Anthro=0)
doc.addSource(s1)

#-----------
# instances
#-----------

i0 = InstanceDescriptor()
i0.name = 'DroideAnthro-Light'
i0.familyName = familyName
i0.styleName = "Anthro Light"
i0.path = os.path.join(root, "instances", "DroideAnthro-Light.ufo")
i0.location = dict(Anthro=0)
i0.kerning = True
i0.info = True
i0.styleMapFamilyName = "Droide Anthro Light"
i0.styleMapStyleName = "regular"
doc.addInstance(i0)

i1 = InstanceDescriptor()
i1.name = 'DroideTransit-Light'
i1.familyName = familyName
i1.styleName = "Transit Light"
i1.path = os.path.join(root, "instances", "DroideTransit-Light.ufo")
i1.location = dict(Anthro=0.5)
i1.kerning = True
i1.info = True
i1.styleMapFamilyName = "Droide Transit Light"
i1.styleMapStyleName = "regular"
doc.addInstance(i1)

i2 = InstanceDescriptor()
i2.name = 'DroideFutur-Light'
i2.familyName = familyName
i2.styleName = "Futur Light"
i2.path = os.path.join(root, "instances", "DroideFutur-Light.ufo")
i2.location = dict(Anthro=1)
i2.kerning = True
i2.info = True
i2.styleMapFamilyName = "Droide Futur Light"
i2.styleMapStyleName = "regular"
doc.addInstance(i2)


#--------
# saving
#--------

path = "Droide.designspace"
doc.write(path)
