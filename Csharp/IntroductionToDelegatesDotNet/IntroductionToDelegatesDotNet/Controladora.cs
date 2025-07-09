using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace IntroductionToDelegatesDotNet
{
    class Controladora
    {
        delegate void ligaMaquinaDelegate();
        private ligaMaquinaDelegate controladora;

        public Controladora(params int[] menu)
        {
            Extrusora ext = new Extrusora();
            Solda solda = new Solda();
            Pintura pintura = new Pintura();
            for (int i = 0; i < menu.Length; i++)
            {
                if (menu[i] == 1)
                    controladora += ext.Ligar;
                if (menu[i] == 2)
                    controladora += solda.Ligar;
                if (menu[i] == 3)
                    controladora += pintura.Ligar;
                if (menu[i] == 4)
                    controladora += ext.Desligar;
                if (menu[i] == 5)
                    controladora += solda.Desligar;
                if (menu[i] == 6)
                    controladora += pintura.Desligar;
                
            }
            controladora();
        }
    }

    class Extrusora
    {
        public void Ligar()
        {
            Console.WriteLine("Extrusora ligada");
        }

        public void Desligar()
        {
            Console.WriteLine("Extrusora desligada.");
        }
    }

    class Solda
    {
        public void Ligar()
        {
            Console.WriteLine("Máquina de solda ligada");
        }

        public void Desligar()
        {
            Console.WriteLine("Máquina de solda desligada.");
        }
    }

    class Pintura
    {
        public void Ligar()
        {
            Console.WriteLine("Máquina de pintura ligada");
        }

        public void Desligar()
        {
            Console.WriteLine("Máquina de pintura desligada.");
        }
    }
}
