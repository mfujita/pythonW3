using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using BankAccountNS;

namespace BankTests
{
    [TestClass]
    public class BankTests
    {
        [TestMethod]
        public void TestDebit()
        {
            //Arrange
            double saldoInicial = 110;
            double debito = 100;
            double saldoEsperado = 10;
            BankAccount conta = new BankAccount("Saldo do cliente ", saldoInicial);

            //Act
            conta.Debit(debito);

            //Assert
            double saldoAtual = conta.Balance;
            Assert.AreEqual(saldoEsperado, saldoAtual, 0.0001, "Erro na operação de bébito.");
        }
    }
}
