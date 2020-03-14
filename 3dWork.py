#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = color(BlackPaint)(cylinder(r=1/4, h=5))
b = color(BlackPaint)(sphere(1.5))
c = color(Blue)(sphere(1.5))
d = (b) + rotate([0, 54, 0])(a) + translate([4,0,3])((b)) + translate([8,0,0])(b) + translate([8,0,0])(rotate([0, -54, 0])(a)) + translate([1,0,-2])(rotate([0, -144, 0])(a)) + translate([5.5,0,-3.5])(c) + translate([1,0,-3.5])(rotate([0, 90, 0])(a)) + translate([0,0,-3.5])(b)  
print(scad_render(d))

