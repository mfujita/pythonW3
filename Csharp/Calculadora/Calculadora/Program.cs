using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Calculadora
{
    public class OperacoesMatematicas
    {
        public double Somar(double a, double b)
        {
            return (a + b);
        }

        public double Subtrair(double a, double b)
        {
            return (a - b);
        }

        public double Multiplicar(double a, double b)
        {
            return (a * b);
        }

        public double Dividir(double a, double b)
        {
            return (a / b);
        }

        public static void Main(string[] args)
        {
            OperacoesMatematicas om = new OperacoesMatematicas();
            Console.WriteLine(om.Somar(2.2,5.5));
            Console.WriteLine(om.Subtrair(2.2, 5.5));
            Console.WriteLine(om.Multiplicar(2.2,5.5));
            Console.WriteLine(om.Dividir(2.2, 5.5));
        }
    }
}
