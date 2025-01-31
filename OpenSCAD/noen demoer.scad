x = 10;
y = 25;
z = -4;

//cylinder(r=10,h=4);
translate([x,y,z]) cylinder(h=20, r1=10,r2=5,center=true, $fn=7);

linear_extrude(30) square([4,19]);