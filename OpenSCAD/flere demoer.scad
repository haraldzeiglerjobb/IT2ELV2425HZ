//cube(10);
//cube([10,20,3]);//Denne kuben er x = 10, y = 20, z  =3
/*
Laaaaang kommentar
Over flere linjer
*/
 
//translate([30,0,0]) rotate([10,0,0]) cylinder(10,5,0,$fn=3);
 
 
a1 = 6;
dim1 = 10;
 
/*translate([40,40,0]) {
    sphere(r=a1,$fn = 50);
    cube(dim1,center = true);
}*/
 
//union
/*union() sphere(r=a1,$fn = 50); cube(dim1,center = true);
*/
//difference
/*difference() {
    cube(dim1,center = true); 
    sphere(r=a1,$fn = 50);
}*/
 
/*difference() {    
    sphere(r=a1,$fn = 50);
    cube(dim1,center = true); 
}*/
 
/*intersection() {    
    sphere(r=a1,$fn = 50);
    cube(dim1,center = true); 
}*/
 
/*intersection() {    
    cube(dim1,center = true); 
       sphere(r=a1,$fn = 50);
}*/
 
/*minkowski() {
    cube(dim1,center = true); 
    translate([20,0,0]) sphere(r=a1,$fn = 50);
}*/
 
/*hull() {
    cube(dim1,center = true); 
    translate([20,0,0]) sphere(r=a1,$fn = 50);
}*/
 
 
module name_of_module(input1=10, input2=10) {
hull() {
    cube(dim1,center = true); 
    translate([20,0,0]) sphere(r=a1,$fn = 50);
    }   
}
 
name_of_module();
 
//function()