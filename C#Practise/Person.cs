using System;

class Person
{
    public string name { get; set; }
    public int Id { get; set; }

    public void display()
    {
        Console.WriteLine($" my name is {name} and id is {Id}\n");
    }
}

class Employee : Person
{
    public string Job_title { get; set; }

    public void display1()
    {
        Console.WriteLine($" my job role is {Job_title}\n");
    }
}

class Program
{
    static void Main(string[] args)
    {
        var obj = new Employee { name = "Kruthik", Id = 6206, Job_title = "developer" };
        obj.display();
        obj.display1();
    }
}