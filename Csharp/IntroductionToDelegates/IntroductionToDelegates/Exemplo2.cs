using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace IntroductionToDelegates
{
    class Exemplo2
    {
        delegate void operacaoDelegate();
        private operacaoDelegate ligaMaquina; // instância do delegate
        Extrusora ext = new Extrusora();
        Solda solda = new Solda();
        Pintura pintura = new Pintura();

        public Exemplo2()
        {
            Console.WriteLine("Ligar e desligar as máquinas controladas pelo sistema." );
            ligaMaquina += ext.Ligar;
            //ligaMaquina = new operacaoDelegate(ext.Ligar);
        }
    }


    class Extrusora
    {
        public void Ligar() { Console.WriteLine("Extrusora ligada."); }
        public void Desligar() { Console.WriteLine("Extrusora desligada."); }
    }

    class Solda() 
    {
        public void Ligar() { }
        public void Desligar() { }
    }

    class Pintura() 
    {
        public void Ligar() { }
        public void Desligar() { }
    }
}
