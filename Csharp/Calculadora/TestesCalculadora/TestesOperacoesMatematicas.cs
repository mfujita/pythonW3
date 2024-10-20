using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using Calculadora;

namespace TestesCalculadora
{
    [TestClass]
    public class TestesOperacoesMatematicas
    {
        [TestMethod]
        public void TesteSomar()
        {
            double a = 2.2;
            double b = 5.5;
            double esperado = 7.7;

            OperacoesMatematicas om = new OperacoesMatematicas();
            double resultado = om.Somar(a, b);

            Assert.AreEqual(esperado, resultado,0.0001, "Soma");
        }

        [TestMethod]
        public void TesteSubtrair()
        {
            double a = 2.2;
            double b = 5.5;
            double esperado = -3.3;

            OperacoesMatematicas om = new OperacoesMatematicas();
            double resultado = om.Subtrair(a, b);

            Assert.AreEqual(esperado, resultado, 0, "Subtração");
        }

        [TestMethod]
        public void TesteMultiplicar()
        {
            double a = 2.2;
            double b = 5.5;
            double esperado = 12.10;

            OperacoesMatematicas om = new OperacoesMatematicas();
            double resultado = om.Multiplicar(a, b);

            Assert.AreEqual(esperado, resultado, 0.001, "Multiplcação");
        }

        [TestMethod]
        public void TesteDividir()
        {
            double a = 2.2;
            double b = 5.5;
            double esperado = 0.4;

            OperacoesMatematicas om = new OperacoesMatematicas();
            double resultado = om.Dividir(a, b);

            Assert.AreEqual(esperado, resultado, 0, "Divisão");
        }
    }
}
