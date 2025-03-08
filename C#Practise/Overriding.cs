using System;
class Shape
{
    public virtual void display()
    {
        Console.WriteLine("shape class\n");
    }
}
class Circle : Shape
{
    public override void display()
    {
        Console.WriteLine("Circle classs");

    }
}
class Rectangle : Shape
{
    public override void display()
    {
        Console.WriteLine("Rectangle class\n");
    }
}
//public class program
//{
//    public static void Main(string[] args)
//    {
//        Circle obj = new Circle();
//        obj.display();
//        Rectangle obj2 = new Rectangle();
//        obj2.display();
//    }
//}
