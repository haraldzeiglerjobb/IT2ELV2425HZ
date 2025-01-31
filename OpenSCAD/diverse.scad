linear_extrude(number = 2, center = false, convexity = 2, twist = 180, slices = 5, scale = 1, $fn  = 9) circle(r = 20, $fn = 7);

translate([10, 30]) hull() {
    cube(5); 
    translate([15,40]) sphere(7);
}

translate([-10, -30,0]) minkowski() {
    cube(5); 
    translate([-15,-40]) sphere(7);
}

translate([-10,30,0]) union(){
   cube(10, center  =true); 
    sphere(7, center = true);
}

translate([10,30,0]) intersection(){
   cube(10, center  =true); 
    sphere(7, center = true);
}

translate([10,-30,0]) difference(){
   cube(10, center  =true); 
    sphere(7, center = true);
}