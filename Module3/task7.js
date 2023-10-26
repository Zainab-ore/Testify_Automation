//Task seven
const side1= 10;
const side2=10;
const side3=20;

//if zi sides are all equal in lenhgt
if(side1==side2&&side1==side3&&side2==side3)
{
    console.log("Equilateral triangle")
}
//else if only two sides are equal
else if (side1==side2&&side2==side1||side2==side3)
{
    console.log("Isoscelese triangle")
}
else //else when they are not equal
{
    console.log("scelene triangle")
}