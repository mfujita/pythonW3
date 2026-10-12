using System;
using System.Collections;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Threading.Tasks;

namespace Backup2025
{ 
    class MyBackup
    {
        private List<string> allDirectories;
        private List<string> allFiles;
        private List<string> listFromMain;
        private List<string> listDirectoriesExternalHd;
        private string letter = "D";

        public void DefineDriveLetter()
        {
            DriveInfo[] drives = DriveInfo.GetDrives();
            foreach (var item in drives)
            {
                if (!item.ToString().Contains("c"))
                {
                    letter = item.ToString().Substring(0,1);
                }
            }
        }

        public MyBackup(List<string> lista)
        {
            allDirectories = new List<string>();
            allFiles = new List<string>();
            listDirectoriesExternalHd = new List<string>();
            listFromMain = lista;
        }

        public void ListingEachDirectory()
        {
            foreach (string item in listFromMain)
            {
                CreateListDirectoriesAndSubdirectories(item);
            }
        }

        private void CreateListDirectoriesAndSubdirectories(string myDir)
        {
            string[] initialDirectory = Directory.GetDirectories(myDir);
            foreach (string subdirectory in initialDirectory)
            {
                if (!subdirectory.Contains(".vs") && !subdirectory.Contains("FileContentIndex") && 
                    !subdirectory.Contains("packages") && !subdirectory.Contains(".vscode"))
                {
                    CreateListDirectoriesAndSubdirectories(subdirectory);
                    allDirectories.Add(subdirectory);
                }
            }
        }

        public void CreatePathExternalHd(string myDirectory)
        {
            foreach (var item in allDirectories)
            {
                if (item.StartsWith(myDirectory))
                {
                    listDirectoriesExternalHd.Add(item.Replace(myDirectory, myDirectory.Replace("C:", $@"{letter}:")));
                }
            }
        }

        public void CreateDirectoriesExternalHd()
        {
            foreach (var item in listDirectoriesExternalHd)
            {
                if (!Directory.Exists(item))
                {
                    Console.WriteLine("CREATING DIRECTORY " + item);
                    Directory.CreateDirectory(item);
                }
            }
        }

        public void ListingEachDirectoryToGetFiles()
        {
            foreach (var item in allDirectories)
            {
                AddFilesToList(item);
            }
        }

        private void AddFilesToList(string dirname)
        {
            string[] filenames = Directory.GetFiles(dirname);
            foreach (var item in filenames)
            {
                allFiles.Add(item);
            }
        }

        public void DoBackup(string myDirectory)
        {
            foreach (var item in allFiles)
            {
                if (item.StartsWith(myDirectory))
                {
                    string filenameInBackup = item.Replace(myDirectory, myDirectory.Replace("C:", $@"{letter}:"));
                    if (!File.Exists(filenameInBackup))
                    {
                        File.Copy(item, filenameInBackup);
                        Console.WriteLine("  Copied " + item + " => " + filenameInBackup);
                    }

                    FileInfo arqOrigem = new FileInfo(item);
                    FileInfo arqDestino = new FileInfo(filenameInBackup);
                    if (arqOrigem.LastWriteTime > arqDestino.LastWriteTime)
                    {
                        int pos = filenameInBackup.IndexOf('/');
                        string nome = filenameInBackup.Substring(pos + 1);
                        Console.WriteLine("Replaced " + nome + " " + File.GetLastWriteTime(item) + "|" + File.GetLastWriteTime(filenameInBackup));
                        File.Copy(item, filenameInBackup, true);
                    }
                }
            }
        }

        // Comparar o que existe no backup, mas não no computador para apagar os arquivos do backup que não existem no computador.
        public void ShowFilesInBackupNotInComputer(string externalHD)
        {
            if (externalHD.StartsWith(@"C:\estudos"))
            {
                List<string> dir = new List<string> { "batch", "csharp", "dart", "data_science", "dsa", "dsaCodes", "duolingo", "grancursos", "hashtag", "hiragana", "html", "js", "ptic", "python", "qualidade e testes de softwares", "toda a matematica", "w3schoolsDart" };
                int index = 0;
                foreach (string dirName in dir)
                {
                    string fileInBackup = externalHD.Replace("C:", $@"{letter}:");
                    string[] directories = Directory.GetDirectories(fileInBackup + "\\" + dir[index]);
                    foreach (var directory in directories)
                    {
                        foreach (var files in Directory.GetFiles(directory))
                        {
                            string fileInComputer = files.Replace($@"{letter}:", "C:");
                            if (!File.Exists(fileInComputer))
                            {
                                Console.WriteLine(fileInComputer);
                            }
                        }
                    }
                    index++;
                }
            }
            else if (externalHD.StartsWith(@"C:\faculdade"))
            {
                string[] directories = Directory.GetDirectories(externalHD.Replace("C:", $@"{letter}:"));
                foreach (var directory in directories)
                {
                    foreach (var files in Directory.GetFiles(directory))
                    {
                        string fileInComputer = files.Replace($@"{letter}:", "C:");
                        if (!File.Exists(fileInComputer))
                        {
                            Console.WriteLine(fileInComputer);
                        }
                    }
                }
            }
        }
    }
}
