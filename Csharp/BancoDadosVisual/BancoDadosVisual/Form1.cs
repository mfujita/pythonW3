using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace BancoDadosVisual
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnConectar_Click(object sender, EventArgs e)
        {
            //BancoDados bd = new BancoDados();
            //MessageBox.Show(bd.ConectaBanco());
            string stringConexao = "server=127.0.0.1;uid=root;pwd=1!2@3#4$;database=mydatabase";
            MySqlConnection conn = new MySqlConnection(stringConexao);

            try
            {
                conn.Open();
            }
            catch (MySqlException ex)
            {
                MessageBox.Show("Erro de conexão");
            }

            string sql = "SELECT * FROM cadastropessoas";
            MySqlCommand cmd = new MySqlCommand(sql, conn);
            MySqlDataReader reader = cmd.ExecuteReader();
            if (reader.HasRows)
            {
                while (reader.Read())
                {
                    txt_Saida.Text += reader.GetString(0) + " " + reader.GetInt32(1) + " " + reader.GetInt32(2) + Environment.NewLine;
                }
            }
            else
            {
                MessageBox.Show("Sem dados");
            }
            reader.Close();
            conn.Close();
        }

        private void btn_salvar_Click(object sender, EventArgs e)
        {
            string stringConexao = "server=127.0.0.1;uid=root;pwd=1!2@3#4$;database=mydatabase";
            MySqlConnection conn = new MySqlConnection(stringConexao);

            try
            {
                conn.Open();
            }
            catch (MySqlException ex)
            {
                MessageBox.Show("Erro de conexão");
            }

            string sql = "INSERT INTO cadastropessoas (nome, nota1) VALUES (@nome,@nota1);";
            MySqlCommand cmd = new MySqlCommand(sql, conn);
            cmd.Parameters.AddWithValue("@nome", txt_nome.Text);
            cmd.Parameters.AddWithValue("@nota1", txt_nota1.Text);
            int tamanho = cmd.ExecuteNonQuery();
            MessageBox.Show(tamanho + " registros armazenados.");
            conn.Close();
        }
    }
}
