/*
translate([0, 0, 0.20]) {
cube([0.25, 0.25, 0.40], true);
}
translate([0, 0, 0.40]) {
cylinder($fn=100, 0.20, 0.125, 0.125);
}
*/
/*
difference() {
translate([0, 0.15, 0.00]) {
cube([0.20, 0.30, 0.20], true);
}
translate([0, 0, -0.1]) {
cylinder($fn=100, 0.20, 0.125, 0.125);
}
}
translate([0, 0.30, -0.1]) {
cylinder($fn=100, 0.20, 0.125, 0.125);
}
*/

/*

difference () {
translate([0, 0.15, 0.00]) {
cube([0.15, 0.30, 0.15], true);
}
translate([0, 0, -0.1]) {
cylinder($fn=100, 0.20, 0.125, 0.125);
}
translate([0, 0.30, -0.1]) {
cylinder($fn=100, 0.20, 0.1, 0.1);
}
}

difference () {
translate([0, 0.30, -0.1]) {
cylinder($fn=100, 0.20, 0.1, 0.1);
}

translate([0, 0.30, -0.1]) {
cylinder($fn=100, 0.20, 0.05, 0.05);
}
}
*/

translate([0, 0, -0.25]) {
cylinder($fn=100, 0.5, 0.05, 0.05);
}