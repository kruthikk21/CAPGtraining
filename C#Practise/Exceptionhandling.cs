using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

    class Exceptionhandling
    {
        static void Main() {
            try
            {
                int a = 10;
                int b = 0;
                int c = a / b;
            }
            
            catch (DivideByZeroException e)
            {
                Console.WriteLine("Divide by zero exception caught: " + e);
            }
            catch (ArithmeticException e)
            {
                Console.WriteLine("Arithmetic exception caught: " + e);
            }
            catch (Exception e)
            {
                Console.WriteLine("Exception caught: " + e);
            }
            finally
            {
                Console.WriteLine("Finally block executed");
            }

        }
    }

