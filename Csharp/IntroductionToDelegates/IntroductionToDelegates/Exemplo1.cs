using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace IntroductionToDelegates
{
    class Exemplo1
    {
        delegate double operacaoDelegate(double a, double b);

        public Exemplo1()
        {
            double n1, n2;
            operacaoDelegate operacao;

            Console.Write("Digite dois números separados por espaço (use vírgula para parte decimal): ");
            string? inputData = Console.ReadLine();
            n1 = Convert.ToDouble(inputData.Split(' ')[0]);
            n2 = Convert.ToDouble(inputData.Split(' ')[1]);

            Console.Write("Digite M para operação de multiplicação e D para operação de divisão: ");
            string? option = Console.ReadLine();
            if (option.Equals("M"))
                operacao = new operacaoDelegate(Multiplicacao);
            else
                operacao = new operacaoDelegate(Divisao);
            Console.WriteLine("Resultado: {0}", operacao(n1,n2));
        }

        private double Multiplicacao(double parametro1, double parametro2)
        {
            return parametro1 * parametro2;
        }

        private double Divisao(double parametro1, double parametro2)
        {
            return parametro1 / parametro2;
        }
    }
}
