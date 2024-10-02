using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BancoDadosVisual
{
    internal class BancoDados
    {
        public string ConectaBanco()
        {
            string stringConexao = "server=127.0.0.1;uid=root;pwd=1!2@3#4$;database=mydatabase";
            string status = "";

            try
            {
                MySqlConnection conn = new MySqlConnection(stringConexao);
                conn.Open();
                status = "ok";
            }
            catch (MySqlException ex)
            {
                status = ex.Message;
            }
            return status;
        }
    }
}
