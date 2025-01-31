//2d shapes

//circle(r = 10);

//square([10,20]);

p1 = [10,-10];
p2 = [20,20];
p3 = [-10,0];

//polygon([p1,p2,p3]);

//linear_extrude(20) circle(10, $fn = 5);

//linear_extrude(10, twist = 45, slices = 100, scale = [1.0, 2.0]) circle(10,$fn=5);

//linear_extrude(10, twist = 45, slices = 100, scale = [1.0, 1.0],center=false) translate([10,10,0])circle(10, $fn=4);

linear_extrude(10, scale = [0,0]) square([10,10]);