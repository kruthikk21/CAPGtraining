using System;

class BankAccount
{
    public int Balance { get; private set; }

    public BankAccount(int initialBalance)
    {
        Balance = initialBalance;
    }

    public void GetBalance()
    {
        Console.WriteLine($"Balance is {Balance}");
    }

    public void Deposit()
    {
        Console.WriteLine("Enter the amount to deposit:");
        if (int.TryParse(Console.ReadLine(), out int amount) && amount > 0)
        {
            Balance += amount;
            Console.WriteLine("Amount deposited successfully.");
        }
        else
        {
            Console.WriteLine("Invalid input.");
        }
    }

    public void Withdraw()
    {
        Console.WriteLine("Enter the amount to withdraw:");
        if (int.TryParse(Console.ReadLine(), out int amount) && amount > 0)
        {
            if (amount > Balance)
            {
                Console.WriteLine("Insufficient funds.");
            }
            else
            {
                Balance -= amount;
                Console.WriteLine("Amount withdrawn successfully.");
            }
        }
        else
        {
            Console.WriteLine("Invalid input.");
        }
    }

    public class Program2
    {
        public static void Main(string[] args)
        {
            BankAccount account = new BankAccount(500);
            account.Deposit();
            account.Withdraw();
            account.GetBalance();
        }
    }
}
