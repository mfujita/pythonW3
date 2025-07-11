using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace IntroductionToDelegatesDotNet
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("┌────────────────────────────────────┐");
            Console.WriteLine("| Menu de controle das máquinas      |");
            Console.WriteLine("│ 1 - Ligar Extrusora                │");
            Console.WriteLine("│ 2 - Ligar Máquina de solda         │");
            Console.WriteLine("│ 3 - Ligar Máquina de pintura       │");
            Console.WriteLine("│ 4 - Desligar Extrusora             │");
            Console.WriteLine("│ 5 - Desligar Máquina de solda      │");
            Console.WriteLine("│ 6 - Desligar Máquina de pintura    │");
            Console.WriteLine("└────────────────────────────────────┘");
            Console.Write("Suas opções separada por espaço: ");
            string entrada = Console.ReadLine();
            
            string[] valores = entrada.Split(' ');
            int[] parametros = new int[valores.Length];

            try
            {
                int option1 = Convert.ToInt32(valores[0]);
                if (option1.ToString() != "")
                    parametros[0] = option1;

                int option2 = Convert.ToInt32(valores[1]);
                if (option2.ToString() != null)
                    parametros[1] = option2;

                int option3 = Convert.ToInt32(valores[2]);
                if (option3.ToString() != null)
                    parametros[2] = option3;
            }
            catch { }

            Controladora control = new Controladora(parametros);
        }
    }
}
