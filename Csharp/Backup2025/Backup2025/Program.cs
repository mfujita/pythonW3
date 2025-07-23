// See https://aka.ms/new-console-template for more information
using Backup2025;
using System.Diagnostics;

//Console.WriteLine("Backup 2025");

List<string> directoryToBackup = new List<string>()
{
    "C:\\estudos",
    "C:\\faculdades"
};

//List<string> excludedDirectories = new List<string>()
//{
//    ".vs",
//    "FileContentIndex",
//    "packages"
//};

Stopwatch stopwatch = new Stopwatch();
stopwatch.Start();
MyBackup myBackup = new MyBackup(directoryToBackup);
myBackup.ListingEachDirectory();
myBackup.CreatePathExternalHd();
myBackup.CreateDirectoriesExternalHd();
Console.WriteLine();
myBackup.ListingEachDirectoryToGetFiles();
myBackup.DoBackup();
stopwatch.Stop();
TimeSpan ts = stopwatch.Elapsed;
string elapsedTime = String.Format("{0:00}h {1:00}m {2:00}s.{3:00}ms", ts.Hours, ts.Minutes, ts.Seconds, ts.Milliseconds / 10);
Console.WriteLine("Time: " + elapsedTime);
