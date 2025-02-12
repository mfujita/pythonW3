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
        List<string> listSegunda;
        List<string> listTerca;
        List<string> listQuarta;
        List<string> listQuinta;
        List<string> listSexta;

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
                        combo.Items.AddRange(new string[] { "", "APS", "DS", "IP", "PAM1", "PAM2", "PTI", "PW2", "QTS", "SE IoT", "TCC", "TPA" });
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

        private void StoreInList()
        {
            listSegunda = new List<string>();
            listTerca = new List<string>();
            listQuarta = new List<string>();
            listQuinta = new List<string>();
            listSexta = new List<string>();

            listSegunda.Add(GetTextFromComboboxTag("c1_1"));
            listSegunda.Add(GetTextFromComboboxTag("c1_2"));
            listSegunda.Add(GetTextFromComboboxTag("c1_3"));
            listSegunda.Add(GetTextFromComboboxTag("c1_4"));
            listSegunda.Add(GetTextFromComboboxTag("c1_5"));
            listSegunda.Add(GetTextFromComboboxTag("c1_6"));
            listSegunda.Add(GetTextFromComboboxTag("c1_7"));
            listSegunda.Add(GetTextFromComboboxTag("c1_8"));
            listSegunda.Add(GetTextFromComboboxTag("c1_9"));
            listSegunda.Add(GetTextFromComboboxTag("c1_10"));
            listSegunda.Add(GetTextFromComboboxTag("c1_11"));
            listSegunda.Add(GetTextFromComboboxTag("c1_12"));
            listSegunda.Add(GetTextFromComboboxTag("c1_13"));

            listTerca.Add(GetTextFromComboboxTag("c2_1"));
            listTerca.Add(GetTextFromComboboxTag("c2_2"));
            listTerca.Add(GetTextFromComboboxTag("c2_3"));
            listTerca.Add(GetTextFromComboboxTag("c2_4"));
            listTerca.Add(GetTextFromComboboxTag("c2_5"));
            listTerca.Add(GetTextFromComboboxTag("c2_6"));
            listTerca.Add(GetTextFromComboboxTag("c2_7"));
            listTerca.Add(GetTextFromComboboxTag("c2_8"));
            listTerca.Add(GetTextFromComboboxTag("c2_9"));
            listTerca.Add(GetTextFromComboboxTag("c2_10"));
            listTerca.Add(GetTextFromComboboxTag("c2_11"));
            listTerca.Add(GetTextFromComboboxTag("c2_12"));
            listTerca.Add(GetTextFromComboboxTag("c2_13"));

            listQuarta.Add(GetTextFromComboboxTag("c3_1"));
            listQuarta.Add(GetTextFromComboboxTag("c3_2"));
            listQuarta.Add(GetTextFromComboboxTag("c3_3"));
            listQuarta.Add(GetTextFromComboboxTag("c3_4"));
            listQuarta.Add(GetTextFromComboboxTag("c3_5"));
            listQuarta.Add(GetTextFromComboboxTag("c3_6"));
            listQuarta.Add(GetTextFromComboboxTag("c3_7"));
            listQuarta.Add(GetTextFromComboboxTag("c3_8"));
            listQuarta.Add(GetTextFromComboboxTag("c3_9"));
            listQuarta.Add(GetTextFromComboboxTag("c3_10"));
            listQuarta.Add(GetTextFromComboboxTag("c3_11"));
            listQuarta.Add(GetTextFromComboboxTag("c3_12"));
            listQuarta.Add(GetTextFromComboboxTag("c3_13"));

            listQuinta.Add(GetTextFromComboboxTag("c4_1"));
            listQuinta.Add(GetTextFromComboboxTag("c4_2"));
            listQuinta.Add(GetTextFromComboboxTag("c4_3"));
            listQuinta.Add(GetTextFromComboboxTag("c4_4"));
            listQuinta.Add(GetTextFromComboboxTag("c4_5"));
            listQuinta.Add(GetTextFromComboboxTag("c4_6"));
            listQuinta.Add(GetTextFromComboboxTag("c4_7"));
            listQuinta.Add(GetTextFromComboboxTag("c4_8"));
            listQuinta.Add(GetTextFromComboboxTag("c4_9"));
            listQuinta.Add(GetTextFromComboboxTag("c4_10"));
            listQuinta.Add(GetTextFromComboboxTag("c4_11"));
            listQuinta.Add(GetTextFromComboboxTag("c4_12"));
            listQuinta.Add(GetTextFromComboboxTag("c4_13"));

            listSexta.Add(GetTextFromComboboxTag("c5_1"));
            listSexta.Add(GetTextFromComboboxTag("c5_2"));
            listSexta.Add(GetTextFromComboboxTag("c5_3"));
            listSexta.Add(GetTextFromComboboxTag("c5_4"));
            listSexta.Add(GetTextFromComboboxTag("c5_5"));
            listSexta.Add(GetTextFromComboboxTag("c5_6"));
            listSexta.Add(GetTextFromComboboxTag("c5_7"));
            listSexta.Add(GetTextFromComboboxTag("c5_8"));
            listSexta.Add(GetTextFromComboboxTag("c5_9"));
            listSexta.Add(GetTextFromComboboxTag("c5_10"));
            listSexta.Add(GetTextFromComboboxTag("c5_11"));
            listSexta.Add(GetTextFromComboboxTag("c5_12"));
            listSexta.Add(GetTextFromComboboxTag("c5_13"));
        }

        private int GetTextSize(List<string> listDay)
        {
            int textSize = 0;
            foreach (var item in listDay)
            {
                if (item.Count() > textSize)
                    textSize = item.Count();
            }
            return textSize;
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

            if (horario.Equals("APS")) { horario = "Análise e Projeto de Sistemas"; }
            else if (horario.Equals("DS")) { horario = "Desenvolvimento de Sistemas"; }
            else if (horario.Equals("IP")) { horario = "Internet, Protocolos e Segurança de Sistemas da Informação"; }
            else if (horario.Equals("PAM1")) { horario = "Programação de Aplicativos Mobile 1"; }
            else if (horario.Equals("PAM2")) { horario = "Programação de Aplicativos Mobile 2"; }
            else if (horario.Equals("PTI")) { horario = "Projetos de Tecnologia de Informação e Comunicação"; }
            else if (horario.Equals("PW2")) { horario = "Programação Web 2"; }
            else if (horario.Equals("QTS")) { horario = "Qualidade e Teste de Software"; }
            else if (horario.Equals("SE IoT")) { horario = "Sistemas Embarcados e IoT"; }
            else if (horario.Equals("TCC")) { horario = "Planejamento e Desenvolvimento do TCC"; }
            else if (horario.Equals("TPA")) { horario = "Técnicas de Programação e Algoritmos"; }
            return horario;
        }

        private void Button_Click(object sender, EventArgs e)
        {
            StoreInList();
            int sizeMonday = GetTextSize(listSegunda);
            int sizeTuesday = GetTextSize(listTerca);
            int sizeWednesday = GetTextSize(listQuarta);
            int sizeThursday = GetTextSize(listQuinta);
            int sizeFriday = GetTextSize(listSexta);

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
            sw.WriteLine("    <tr><th>Horário</th> <th>{0," + sizeMonday + "}</th> <th>{1," + sizeTuesday + "}</th> <th>{2," + sizeWednesday + "}</th> <th>{3," + sizeThursday + "}</th> <th>{4," + sizeFriday +"}</th></tr>", "Segunda", "Terça", "Quarta", "Quinta", "Sexta");
            sw.WriteLine("    <tr><td>  07:30</td> <td>{0," + sizeMonday + "}</td> <td>{1," + sizeTuesday + "}</td> <td>{2," + sizeWednesday + "}</td> <td>{3," + sizeThursday + "}</td> <td>{4," + sizeFriday +"}</td></tr>", GetTextFromComboboxTag("c1_1"),  GetTextFromComboboxTag("c2_1"),  GetTextFromComboboxTag("c3_1"),  GetTextFromComboboxTag("c4_1"),  GetTextFromComboboxTag("c5_1"));
            sw.WriteLine("    <tr><td>  08:20</td> <td>{0," + sizeMonday + "}</td> <td>{1," + sizeTuesday + "}</td> <td>{2," + sizeWednesday + "}</td> <td>{3," + sizeThursday + "}</td> <td>{4," + sizeFriday +"}</td></tr>", GetTextFromComboboxTag("c1_2"),  GetTextFromComboboxTag("c2_2"),  GetTextFromComboboxTag("c3_2"),  GetTextFromComboboxTag("c4_2"),  GetTextFromComboboxTag("c5_2"));
            sw.WriteLine("    <tr><td>  09:10</td> <td>{0," + sizeMonday + "}</td> <td>{1," + sizeTuesday + "}</td> <td>{2," + sizeWednesday + "}</td> <td>{3," + sizeThursday + "}</td> <td>{4," + sizeFriday +"}</td></tr>", GetTextFromComboboxTag("c1_3"),  GetTextFromComboboxTag("c2_3"),  GetTextFromComboboxTag("c3_3"),  GetTextFromComboboxTag("c4_3"),  GetTextFromComboboxTag("c5_3"));
            sw.WriteLine("    <tr><td>  10:20</td> <td>{0," + sizeMonday + "}</td> <td>{1," + sizeTuesday + "}</td> <td>{2," + sizeWednesday + "}</td> <td>{3," + sizeThursday + "}</td> <td>{4," + sizeFriday +"}</td></tr>", GetTextFromComboboxTag("c1_4"),  GetTextFromComboboxTag("c2_4"),  GetTextFromComboboxTag("c3_4"),  GetTextFromComboboxTag("c4_4"),  GetTextFromComboboxTag("c5_4"));
            sw.WriteLine("    <tr><td>  11:10</td> <td>{0," + sizeMonday + "}</td> <td>{1," + sizeTuesday + "}</td> <td>{2," + sizeWednesday + "}</td> <td>{3," + sizeThursday + "}</td> <td>{4," + sizeFriday +"}</td></tr>", GetTextFromComboboxTag("c1_5"),  GetTextFromComboboxTag("c2_5"),  GetTextFromComboboxTag("c3_5"),  GetTextFromComboboxTag("c4_5"),  GetTextFromComboboxTag("c5_5"));
            sw.WriteLine("    <tr><td>  12:00</td> <td>{0," + sizeMonday + "}</td> <td>{1," + sizeTuesday + "}</td> <td>{2," + sizeWednesday + "}</td> <td>{3," + sizeThursday + "}</td> <td>{4," + sizeFriday +"}</td></tr>", GetTextFromComboboxTag("c1_6"),  GetTextFromComboboxTag("c2_6"),  GetTextFromComboboxTag("c3_6"),  GetTextFromComboboxTag("c4_6"),  GetTextFromComboboxTag("c5_6"));
            sw.WriteLine("    <tr><td colspan=\"6\">Almoço</td></tr>") ;
            sw.WriteLine("    <tr><td>  13:10</td> <td>{0," + sizeMonday + "}</td> <td>{1," + sizeTuesday + "}</td> <td>{2," + sizeWednesday + "}</td> <td>{3," + sizeThursday + "}</td> <td>{4," + sizeFriday +"}</td></tr>", GetTextFromComboboxTag("c1_8"),  GetTextFromComboboxTag("c2_8"),  GetTextFromComboboxTag("c3_8"),  GetTextFromComboboxTag("c4_8"),  GetTextFromComboboxTag("c5_8"));
            sw.WriteLine("    <tr><td>  14:00</td> <td>{0," + sizeMonday + "}</td> <td>{1," + sizeTuesday + "}</td> <td>{2," + sizeWednesday + "}</td> <td>{3," + sizeThursday + "}</td> <td>{4," + sizeFriday +"}</td></tr>", GetTextFromComboboxTag("c1_9"),  GetTextFromComboboxTag("c2_9"),  GetTextFromComboboxTag("c3_9"),  GetTextFromComboboxTag("c4_9"),  GetTextFromComboboxTag("c5_9"));
            sw.WriteLine("    <tr><td>  14:50</td> <td>{0," + sizeMonday + "}</td> <td>{1," + sizeTuesday + "}</td> <td>{2," + sizeWednesday + "}</td> <td>{3," + sizeThursday + "}</td> <td>{4," + sizeFriday +"}</td></tr>", GetTextFromComboboxTag("c1_10"), GetTextFromComboboxTag("c2_10"), GetTextFromComboboxTag("c3_10"), GetTextFromComboboxTag("c4_10"), GetTextFromComboboxTag("c5_10"));
            sw.WriteLine("    <tr><td>  16:00</td> <td>{0," + sizeMonday + "}</td> <td>{1," + sizeTuesday + "}</td> <td>{2," + sizeWednesday + "}</td> <td>{3," + sizeThursday + "}</td> <td>{4," + sizeFriday +"}</td></tr>", GetTextFromComboboxTag("c1_11"), GetTextFromComboboxTag("c2_11"), GetTextFromComboboxTag("c3_11"), GetTextFromComboboxTag("c4_11"), GetTextFromComboboxTag("c5_11"));
            sw.WriteLine("    <tr><td>  16:50</td> <td>{0," + sizeMonday + "}</td> <td>{1," + sizeTuesday + "}</td> <td>{2," + sizeWednesday + "}</td> <td>{3," + sizeThursday + "}</td> <td>{4," + sizeFriday +"}</td></tr>", GetTextFromComboboxTag("c1_12"), GetTextFromComboboxTag("c2_12"), GetTextFromComboboxTag("c3_12"), GetTextFromComboboxTag("c4_12"), GetTextFromComboboxTag("c5_12"));
            sw.WriteLine("    <tr><td>  17:40</td> <td>{0," + sizeMonday + "}</td> <td>{1," + sizeTuesday + "}</td> <td>{2," + sizeWednesday + "}</td> <td>{3," + sizeThursday + "}</td> <td>{4," + sizeFriday +"}</td></tr>", GetTextFromComboboxTag("c1_13"), GetTextFromComboboxTag("c2_13"), GetTextFromComboboxTag("c3_13"), GetTextFromComboboxTag("c4_13"), GetTextFromComboboxTag("c5_13"));
            sw.WriteLine("</table>");
            sw.WriteLine("</body>");
            sw.WriteLine("</html>");
            sw.Close();
            fs.Close();
            MessageBox.Show("Grade de horários das aulas gerada com sucesso!");
        }
    }
}
