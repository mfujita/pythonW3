using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
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
        private string letter = "E";

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

        public void CreatePathExternalHd()
        {
            foreach (var item in allDirectories)
            {
                if (item.StartsWith(@"C:\faculdades\"))
                {
                    listDirectoriesExternalHd.Add(item.Replace(@"C:\faculdades\", $@"{letter}:\faculdades\"));
                    //Console.WriteLine(item.Replace(@"C:\faculdades\etec", @"E:\faculdades\etec"));
                }
                else if (item.StartsWith(@"C:\estudos\"))
                {
                    //string nameOfSubdirectory = item.Replace(@"C:\estudos", "");
                    listDirectoriesExternalHd.Add(item.Replace(@"C:\estudos", $@"{letter}:\estudos"));
                    //Console.WriteLine(item.Replace(@"C:\estudos", @"E:\estudos"));
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
                else
                {
                    Console.WriteLine("Exists " + item);
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

        public void DoBackup()
        {
            foreach (var item in allFiles)
            {
                if (item.StartsWith(@"C:\faculdades"))
                {
                    string filenameInBackup = item.Replace(@"C:\faculdades", $@"{letter}:\faculdades");
                    if (!File.Exists(filenameInBackup))
                    {
                        File.Copy(item, filenameInBackup);
                        Console.WriteLine("  Copied " + item + " => " + filenameInBackup);
                    }
                        
                    else if (File.GetLastWriteTime(item) > File.GetLastWriteTime(filenameInBackup))
                    {
                        int pos = filenameInBackup.IndexOf('/');
                        string nome = filenameInBackup.Substring(pos + 1);
                        Console.WriteLine("Replaced " + nome + " " + File.GetLastWriteTime(item) + "|" + File.GetLastWriteTime(filenameInBackup));
                        File.Copy(item, filenameInBackup, true);
                    }
                }
                else if (item.StartsWith(@"C:\estudos"))
                {
                    string filenameInBackup = item.Replace(@"C:\estudos", $@"{letter}:\estudos");
                    if (!File.Exists(filenameInBackup))
                    {
                        File.Copy(item, filenameInBackup);
                        Console.WriteLine("  Copied " + item + " => " + filenameInBackup);
                    }                        
                    else if (File.GetLastWriteTime(item) > File.GetLastWriteTime(filenameInBackup))
                    {
                        File.Copy(item, filenameInBackup, true);
                        Console.WriteLine("Replaced " + File.GetLastWriteTime(item) + "|" + File.GetLastWriteTime(filenameInBackup));
                    }
                }
            }
        }
    }
}
