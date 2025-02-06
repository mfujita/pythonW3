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
            SetupPanel();
            SetupLabels();
        }

        private void SetupPanel()
        {
            panel1.Size = new Size(this.Width * 95 / 100, this.Height * 90 / 100);
            panel1.Location = new Point((Screen.PrimaryScreen.WorkingArea.Width - panel1.Width) / 2, (Screen.PrimaryScreen.WorkingArea.Height - panel1.Height) / 2);
            panel1.Paint += new PaintEventHandler(Panel1_Paint);
        }

        private void Panel1_Paint(object sender, PaintEventArgs e)
        {
            int largura = panel1.Width;
            using(Graphics g = e.Graphics)
            {
                Pen caneta = new Pen(Color.Black, 2);
                for (int i = 0; i < 15; i++)
                {
                    Point p1 = new Point(panel1.Left, panel1.Top + i* 50);
                    Point p2 = new Point(largura - 62, panel1.Top + i* 50);
                    g.DrawLine(caneta, p1, p2);
                }

                for (int i = 0; i <= 6; i++)
                {
                    Point p1 = new Point(panel1.Left + i * 240, panel1.Top);
                    Point p2 = new Point(panel1.Left + i * 240, panel1.Bottom-85);
                    g.DrawLine(caneta, p1, p2);
                }
            }
        }

        private void SetupLabels()
        {
            // Textos dos labels

            for (int i = 1; i < 5; i++)
            {
                Label label = new Label();
                label.Location = new Point(panel1.Left + 250 * i + 20, panel1.Top + 10);
                panel1.Controls.Add(label);

                if (i == 0) { label.Text = "Segunda"; }
                else if (i == 1) { label.Text = "Terça"; }
                else if (i == 2) { label.Text = "Quarta"; }
                else if (i == 3) { label.Text = "Quinta"; }
                else if (i == 4) { label.Text = "Sexta"; }
            }


            for (int i = 0; i < 14; i++)
            {
                Label label = new Label();
                label.Location = new Point(panel1.Left + 20, panel1.Top + i*50 + 10);
                panel1.Controls.Add(label);

                if (i == 0) { label.Text = "Horário"; }
                else if (i == 1) { label.Text = "07:30"; }
                else if (i == 2) { label.Text = "08:20"; }
                else if (i == 3) { label.Text = "09:10"; }
                else if (i == 4) { label.Text = "10:20"; }
                else if (i == 5) { label.Text = "11:10"; }
                else if (i == 6) { label.Text = "12:00"; }
                else if (i == 7) { label.Text = ""; }
                else if (i == 8) { label.Text = "13:10"; }
                else if (i == 9) { label.Text = "14:00"; }
                else if (i == 10) { label.Text = "14:50"; }
                else if (i == 11) { label.Text = "16:00"; }
                else if (i == 12) { label.Text = "16:50"; }
                else if (i == 13) { label.Text = "17:40"; }
            }
        }
    }
}
