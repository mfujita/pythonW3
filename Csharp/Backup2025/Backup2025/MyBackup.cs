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
                if (item.StartsWith(@"C:\faculdades\etec\"))
                {
                    listDirectoriesExternalHd.Add(item.Replace(@"C:\faculdades\etec", @"E:\faculdades\etec"));
                    //Console.WriteLine(item.Replace(@"C:\faculdades\etec", @"E:\faculdades\etec"));
                }
                else if (item.StartsWith(@"C:\estudos\"))
                {
                    //string nameOfSubdirectory = item.Replace(@"C:\estudos", "");
                    listDirectoriesExternalHd.Add(item.Replace(@"C:\estudos", @"E:\estudos"));
                    //Console.WriteLine(item.Replace(@"C:\estudos", @"E:\estudos"));
                }
            }
        }

        public void CreateDirectoriesExternalHd()
        {
            foreach (var item in listDirectoriesExternalHd)
            {
                if (!File.Exists(item))
                {

                    //Console.WriteLine("CREATING DIRECTORY " + item);
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
                if (item.StartsWith(@"C:\faculdades\etec"))
                {
                    string filenameInBackup = item.Replace(@"C:\faculdades\etec", @"E:\faculdades\etec");
                    if (!File.Exists(filenameInBackup))
                        Console.WriteLine("    Copia " + item + " => " + filenameInBackup);
                }
                else if (item.StartsWith(@"C:\estudos"))
                {
                    string filenameInBackup = item.Replace(@"C:\estudos", @"E:\estudos");
                    if (!File.Exists(filenameInBackup))
                        Console.WriteLine("    Copia " + item + " => " + filenameInBackup);
                }
            }
        }
    }
}
