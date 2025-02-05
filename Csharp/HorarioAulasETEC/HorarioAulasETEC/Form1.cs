using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace HorarioAulasETEC
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.Location = new Point(0, 0);
            this.WindowState = FormWindowState.Maximized;
            tableLayoutPanel1.CellBorderStyle = TableLayoutPanelCellBorderStyle.Single;
            tableLayoutPanel1.Width = this.Width * 95 / 100;

            SetupLayout();

            // Textos dos labels
            lblDia1.Text = "Segunda";
            lblDia2.Text = "Terça";
            lblDia3.Text = "Quarta";
            lblDia4.Text = "Quinta";
            lblDia5.Text = "Sexta";

            lblhor1.Text = "Horário";
            lblhor2.Text = "07:30";
            lblhor3.Text = "08:20";
            lblhor4.Text = "09:10";
            lblhor5.Text = "10:00";
            lblhor6.Text = "10:20";
            lblhor7.Text = "11:10";
            lblhor8.Text = "12:00";
            lblhor9.Text = "12:50";
            lblhor10.Text = "13:10";
            lblhor11.Text = "14:00";
            lblhor12.Text = "14:50";
            lblhor13.Text = "15:40";
            lblhor14.Text = "16:00";
            lblhor15.Text = "16:50";
            lblhor16.Text = "17:40";
            LoadCombobox();
        }

        private void SetupLayout()
        {
            tableLayoutPanel1.Height = this.Height * 80/100;
            for (int i = 0; i < tableLayoutPanel1.RowCount; i++)
            {
                tableLayoutPanel1.RowStyles[i].SizeType = SizeType.Percent;
                tableLayoutPanel1.RowStyles[i].Height = 6.25F;
            }

            tableLayoutPanel1.ColumnStyles[0].SizeType = SizeType.Percent;
            tableLayoutPanel1.ColumnStyles[0].Width = 10F;
            for (int i = 1; i < tableLayoutPanel1.ColumnCount; i++)
            {
                tableLayoutPanel1.ColumnStyles[i].SizeType = SizeType.Percent;
                tableLayoutPanel1.ColumnStyles[i].Width = 18F;
            }
        }

        private void LoadCombobox()
        {
            for (int i = 1; i < tableLayoutPanel1.RowCount; i++)
            {
                for (int j = 1; j < tableLayoutPanel1.ColumnCount; j++)
                {
                    Control celula = tableLayoutPanel1.GetControlFromPosition(i, j);
                    if (celula == null)
                    {
                        ComboBox combo = new ComboBox();
                        tableLayoutPanel1.Controls.Add(combo);
                        combo.DropDownStyle = ComboBoxStyle.DropDownList;
                        ColumnStyle larguraColuna = tableLayoutPanel1.ColumnStyles[1];
                        combo.Width = 300;
                        combo.Items.AddRange(new string[] { "Sist. Embarcados", "Projeto Tecnologia", "PAM 2", "TPA", "TCC", "Prog Web 2", "Desenv. Sistemas", "QTS", "APS", "IP" });
                    }
                }
            }
        }
    }
}
