using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace HorarioAulasETEC
{
    public partial class Form1 : Form
    {
        ComboBox combo;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.Location = new Point(0, 0);
            this.WindowState = FormWindowState.Maximized;
            this.Text = "Gerador de horários de aulas em HTML v2.0";
            SetupPanel();
            SetupLabels();
            LoadCombobox();
            CreateButton();
        }

        private void SetupPanel()
        {
            panel1.Size = new Size(this.Width * 95 / 100, this.Height * 85 / 100);
            panel1.Location = new Point((Screen.PrimaryScreen.WorkingArea.Width - panel1.Width) / 2, 20);
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
                    Point p2 = new Point(panel1.Left + i * 240, panel1.Bottom-40);
                    g.DrawLine(caneta, p1, p2);
                }
            }
        }

        private void SetupLabels()
        {
            for (int i = 0; i < 5; i++)
            {
                Label label = new Label();
                label.Location = new Point(panel1.Left + 250 * (i+1) + 20, panel1.Top + 10);
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

        private void LoadCombobox()
        {
            int largura = Screen.PrimaryScreen.WorkingArea.Width * 12 / 100;
            for (int i = 1; i < 6; i++)
            {
                for (int j = 1; j < 14; j++)
                {
                    if (j == 7)
                        continue;
                    else
                    {
                        combo = new ComboBox();
                        combo.Size = new Size(largura, 50);
                        combo.Location = new Point(53 + i * 240, 30 + j * 50);
                        combo.DropDownStyle = ComboBoxStyle.DropDownList;
                        combo.Tag = "c" + i + "_" + j;
                        combo.Items.AddRange(new string[] { "", "APS", "DS", "IP", "IoT", "PAM 1", "PAM 2", "PTI", "PW2", "QTS", "SE", "TCC", "TPA" });
                        panel1.Controls.Add(combo);
                    }
                }
            }
        }

        private void CreateButton()
        {
            Button button = new Button();
            button.Size = new Size(200, 40);
            button.Location = new Point((panel1.Width - button.Width) / 2, 770);
            button.ForeColor = Color.Blue;
            button.Text = "Gerar horário";
            this.Controls.Add(button);
            button.Click += Button_Click;
        }

        private void Button_Click(object sender, EventArgs e)
        {
            FileStream fs = new FileStream("horario.html", FileMode.Create);
            StreamWriter sw = new StreamWriter(fs);
            sw.WriteLine("<!DOCTYPE html>");
            sw.WriteLine("<html lang=\"pt-br\">");
            sw.WriteLine("<head>");
            sw.WriteLine("    <meta charset=\"UTF-8\">");
            sw.WriteLine("    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">");
            sw.WriteLine("    <title>Horário de aulas</title>");
            sw.WriteLine("    <style>");
            sw.WriteLine("        body { font-family: Verdana; font-size: 1.2rem; }");
            sw.WriteLine("        table { width: 90%; margin: auto; margin-top: 15px;}");
            sw.WriteLine("        td { text-align: center; padding: 2px;}");
            sw.WriteLine("    </style>");
            sw.WriteLine("</head>");
            sw.WriteLine("<body>");
            sw.WriteLine("<table border=\"1\">");
            sw.WriteLine("    <tr><th>Horário</th> <th>Segunda</th> <th>Terça</th> <th>Quarta</th> <th>Quinta</th> <th>Sexta</th></tr>");
            sw.WriteLine("    <tr><td>07:30</td> <td>"+GetTextFromComboboxTag("c1_1")+"</td> <td>"  + GetTextFromComboboxTag("c2_1")  + "</td> <td>"+GetTextFromComboboxTag("c3_1") +"</td> <td>"+GetTextFromComboboxTag("c4_1") +"</td> <td>"+GetTextFromComboboxTag("c5_1") +"</td></tr>");
            sw.WriteLine("    <tr><td>08:20</td> <td>"+GetTextFromComboboxTag("c1_2")+"</td> <td>"  + GetTextFromComboboxTag("c2_2")  + "</td> <td>"+GetTextFromComboboxTag("c3_2") +"</td> <td>"+GetTextFromComboboxTag("c4_2") +"</td> <td>"+GetTextFromComboboxTag("c5_2") +"</td></tr>");
            sw.WriteLine("    <tr><td>09:10</td> <td>"+GetTextFromComboboxTag("c1_3")+"</td> <td>"  + GetTextFromComboboxTag("c2_3")  + "</td> <td>"+GetTextFromComboboxTag("c3_3") +"</td> <td>"+GetTextFromComboboxTag("c4_3") +"</td> <td>"+GetTextFromComboboxTag("c5_3") +"</td></tr>");
            sw.WriteLine("    <tr><td>10:20</td> <td>"+GetTextFromComboboxTag("c1_4")+"</td> <td>"  + GetTextFromComboboxTag("c2_4")  + "</td> <td>"+GetTextFromComboboxTag("c3_4") +"</td> <td>"+GetTextFromComboboxTag("c4_4") +"</td> <td>"+GetTextFromComboboxTag("c5_4") +"</td></tr>");
            sw.WriteLine("    <tr><td>11:10</td> <td>"+GetTextFromComboboxTag("c1_5")+"</td> <td>"  + GetTextFromComboboxTag("c2_5")  + "</td> <td>"+GetTextFromComboboxTag("c3_5") +"</td> <td>"+GetTextFromComboboxTag("c4_5") +"</td> <td>"+GetTextFromComboboxTag("c5_5") +"</td></tr>");
            sw.WriteLine("    <tr><td>12:00</td> <td>"+GetTextFromComboboxTag("c1_6")+"</td> <td>"  + GetTextFromComboboxTag("c2_6")  + "</td> <td>"+GetTextFromComboboxTag("c3_6") +"</td> <td>"+GetTextFromComboboxTag("c4_6") +"</td> <td>"+GetTextFromComboboxTag("c5_6") +"</td></tr>");
            sw.WriteLine("    <tr><td colspan=\"6\">Almoço</td></tr>");
            sw.WriteLine("    <tr><td>13:10</td> <td>"+GetTextFromComboboxTag("c1_8") +"</td> <td>" + GetTextFromComboboxTag("c2_8")  + "</td> <td>"+GetTextFromComboboxTag("c3_8") +"</td> <td>"+GetTextFromComboboxTag("c4_8") +"</td> <td>"+GetTextFromComboboxTag("c5_8") +"</td></tr>");
            sw.WriteLine("    <tr><td>14:00</td> <td>"+GetTextFromComboboxTag("c1_9") +"</td> <td>" + GetTextFromComboboxTag("c2_9")  + "</td> <td>"+GetTextFromComboboxTag("c3_9") +"</td> <td>"+GetTextFromComboboxTag("c4_9") +"</td> <td>"+GetTextFromComboboxTag("c5_9") +"</td></tr>");
            sw.WriteLine("    <tr><td>14:50</td> <td>"+GetTextFromComboboxTag("c1_10")+"</td> <td>" + GetTextFromComboboxTag("c2_10") + "</td> <td>"+GetTextFromComboboxTag("c3_10")+"</td> <td>"+GetTextFromComboboxTag("c4_10")+"</td> <td>"+GetTextFromComboboxTag("c5_10")+"</td></tr>");
            sw.WriteLine("    <tr><td>16:00</td> <td>"+GetTextFromComboboxTag("c1_11")+"</td> <td>" + GetTextFromComboboxTag("c2_11") + "</td> <td>"+GetTextFromComboboxTag("c3_11")+"</td> <td>"+GetTextFromComboboxTag("c4_11")+"</td> <td>"+GetTextFromComboboxTag("c5_11")+"</td></tr>");
            sw.WriteLine("    <tr><td>16:50</td> <td>"+GetTextFromComboboxTag("c1_12")+"</td> <td>" + GetTextFromComboboxTag("c2_12") + "</td> <td>"+GetTextFromComboboxTag("c3_12")+"</td> <td>"+GetTextFromComboboxTag("c4_12")+"</td> <td>"+GetTextFromComboboxTag("c5_12")+"</td></tr>");
            sw.WriteLine("    <tr><td>17:40</td> <td>"+GetTextFromComboboxTag("c1_13")+ "</td> <td>"+ GetTextFromComboboxTag("c2_13") + "</td> <td>"+GetTextFromComboboxTag("c3_13")+"</td> <td>"+GetTextFromComboboxTag("c4_13")+"</td> <td>"+GetTextFromComboboxTag("c5_13")+"</td></tr>");
            sw.WriteLine("</table>");
            sw.WriteLine("</body>");
            sw.WriteLine("</html>");
            sw.Close();
            fs.Close();
            MessageBox.Show("Grade de horários das aulas gerada com sucesso!");
        }

        private string GetTextFromComboboxTag(string id)
        {
            string horario = "";
            foreach (Control item in panel1.Controls)
            {
                if (item is ComboBox)
                {
                    if (item.Tag.ToString().Equals(id))
                    {
                        horario = item.Text;
                    }
                }
            }
            return horario;
        }
    }
}
