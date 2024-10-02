namespace BancoDadosVisual
{
    partial class Form1
    {
        /// <summary>
        /// Variável de designer necessária.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Limpar os recursos que estão sendo usados.
        /// </summary>
        /// <param name="disposing">true se for necessário descartar os recursos gerenciados; caso contrário, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Código gerado pelo Windows Form Designer

        /// <summary>
        /// Método necessário para suporte ao Designer - não modifique 
        /// o conteúdo deste método com o editor de código.
        /// </summary>
        private void InitializeComponent()
        {
            this.txt_Saida = new System.Windows.Forms.TextBox();
            this.btnConectar = new System.Windows.Forms.Button();
            this.tabControl1 = new System.Windows.Forms.TabControl();
            this.tabInserir = new System.Windows.Forms.TabPage();
            this.tabSelecionar = new System.Windows.Forms.TabPage();
            this.tabAtualizar = new System.Windows.Forms.TabPage();
            this.tabDeletar = new System.Windows.Forms.TabPage();
            this.lbl_nota1 = new System.Windows.Forms.Label();
            this.lbl_Nome = new System.Windows.Forms.Label();
            this.txt_nota1 = new System.Windows.Forms.TextBox();
            this.txt_nome = new System.Windows.Forms.TextBox();
            this.btn_salvar = new System.Windows.Forms.Button();
            this.tabControl1.SuspendLayout();
            this.tabInserir.SuspendLayout();
            this.tabSelecionar.SuspendLayout();
            this.SuspendLayout();
            // 
            // txt_Saida
            // 
            this.txt_Saida.Location = new System.Drawing.Point(16, 19);
            this.txt_Saida.Multiline = true;
            this.txt_Saida.Name = "txt_Saida";
            this.txt_Saida.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.txt_Saida.Size = new System.Drawing.Size(900, 260);
            this.txt_Saida.TabIndex = 0;
            // 
            // btnConectar
            // 
            this.btnConectar.Location = new System.Drawing.Point(929, 19);
            this.btnConectar.Name = "btnConectar";
            this.btnConectar.Size = new System.Drawing.Size(110, 40);
            this.btnConectar.TabIndex = 1;
            this.btnConectar.Text = "Conectar";
            this.btnConectar.UseVisualStyleBackColor = true;
            this.btnConectar.Click += new System.EventHandler(this.btnConectar_Click);
            // 
            // tabControl1
            // 
            this.tabControl1.Controls.Add(this.tabInserir);
            this.tabControl1.Controls.Add(this.tabSelecionar);
            this.tabControl1.Controls.Add(this.tabAtualizar);
            this.tabControl1.Controls.Add(this.tabDeletar);
            this.tabControl1.Location = new System.Drawing.Point(12, 12);
            this.tabControl1.Name = "tabControl1";
            this.tabControl1.SelectedIndex = 0;
            this.tabControl1.Size = new System.Drawing.Size(1058, 336);
            this.tabControl1.TabIndex = 2;
            // 
            // tabInserir
            // 
            this.tabInserir.Controls.Add(this.btn_salvar);
            this.tabInserir.Controls.Add(this.lbl_nota1);
            this.tabInserir.Controls.Add(this.lbl_Nome);
            this.tabInserir.Controls.Add(this.txt_nota1);
            this.tabInserir.Controls.Add(this.txt_nome);
            this.tabInserir.Location = new System.Drawing.Point(4, 31);
            this.tabInserir.Name = "tabInserir";
            this.tabInserir.Padding = new System.Windows.Forms.Padding(3);
            this.tabInserir.Size = new System.Drawing.Size(1050, 301);
            this.tabInserir.TabIndex = 0;
            this.tabInserir.Text = "Inserir";
            this.tabInserir.UseVisualStyleBackColor = true;
            // 
            // tabSelecionar
            // 
            this.tabSelecionar.Controls.Add(this.txt_Saida);
            this.tabSelecionar.Controls.Add(this.btnConectar);
            this.tabSelecionar.Location = new System.Drawing.Point(4, 31);
            this.tabSelecionar.Name = "tabSelecionar";
            this.tabSelecionar.Padding = new System.Windows.Forms.Padding(3);
            this.tabSelecionar.Size = new System.Drawing.Size(1050, 301);
            this.tabSelecionar.TabIndex = 1;
            this.tabSelecionar.Text = "Selecionar";
            this.tabSelecionar.UseVisualStyleBackColor = true;
            // 
            // tabAtualizar
            // 
            this.tabAtualizar.Location = new System.Drawing.Point(4, 31);
            this.tabAtualizar.Name = "tabAtualizar";
            this.tabAtualizar.Size = new System.Drawing.Size(839, 301);
            this.tabAtualizar.TabIndex = 2;
            this.tabAtualizar.Text = "Atualizar";
            this.tabAtualizar.UseVisualStyleBackColor = true;
            // 
            // tabDeletar
            // 
            this.tabDeletar.Location = new System.Drawing.Point(4, 31);
            this.tabDeletar.Name = "tabDeletar";
            this.tabDeletar.Size = new System.Drawing.Size(839, 301);
            this.tabDeletar.TabIndex = 3;
            this.tabDeletar.Text = "Deletar";
            this.tabDeletar.UseVisualStyleBackColor = true;
            // 
            // lbl_nota1
            // 
            this.lbl_nota1.AutoSize = true;
            this.lbl_nota1.Location = new System.Drawing.Point(21, 93);
            this.lbl_nota1.Name = "lbl_nota1";
            this.lbl_nota1.Size = new System.Drawing.Size(59, 24);
            this.lbl_nota1.TabIndex = 12;
            this.lbl_nota1.Text = "Nota1";
            // 
            // lbl_Nome
            // 
            this.lbl_Nome.AutoSize = true;
            this.lbl_Nome.Location = new System.Drawing.Point(21, 27);
            this.lbl_Nome.Name = "lbl_Nome";
            this.lbl_Nome.Size = new System.Drawing.Size(62, 24);
            this.lbl_Nome.TabIndex = 11;
            this.lbl_Nome.Text = "Nome";
            // 
            // txt_nota1
            // 
            this.txt_nota1.Location = new System.Drawing.Point(121, 90);
            this.txt_nota1.Name = "txt_nota1";
            this.txt_nota1.Size = new System.Drawing.Size(404, 28);
            this.txt_nota1.TabIndex = 9;
            // 
            // txt_nome
            // 
            this.txt_nome.Location = new System.Drawing.Point(121, 28);
            this.txt_nome.Name = "txt_nome";
            this.txt_nome.Size = new System.Drawing.Size(404, 28);
            this.txt_nome.TabIndex = 8;
            // 
            // btn_salvar
            // 
            this.btn_salvar.Location = new System.Drawing.Point(228, 161);
            this.btn_salvar.Name = "btn_salvar";
            this.btn_salvar.Size = new System.Drawing.Size(93, 36);
            this.btn_salvar.TabIndex = 14;
            this.btn_salvar.Text = "Salvar";
            this.btn_salvar.UseVisualStyleBackColor = true;
            this.btn_salvar.Click += new System.EventHandler(this.btn_salvar_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(10F, 22F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1082, 384);
            this.Controls.Add(this.tabControl1);
            this.Font = new System.Drawing.Font("Microsoft Sans Serif", 12.22642F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Margin = new System.Windows.Forms.Padding(5);
            this.Name = "Form1";
            this.Text = "Form1";
            this.tabControl1.ResumeLayout(false);
            this.tabInserir.ResumeLayout(false);
            this.tabInserir.PerformLayout();
            this.tabSelecionar.ResumeLayout(false);
            this.tabSelecionar.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.TextBox txt_Saida;
        private System.Windows.Forms.Button btnConectar;
        private System.Windows.Forms.TabControl tabControl1;
        private System.Windows.Forms.TabPage tabInserir;
        private System.Windows.Forms.TabPage tabSelecionar;
        private System.Windows.Forms.TabPage tabAtualizar;
        private System.Windows.Forms.TabPage tabDeletar;
        private System.Windows.Forms.Button btn_salvar;
        private System.Windows.Forms.Label lbl_nota1;
        private System.Windows.Forms.Label lbl_Nome;
        private System.Windows.Forms.TextBox txt_nota1;
        private System.Windows.Forms.TextBox txt_nome;
    }
}

